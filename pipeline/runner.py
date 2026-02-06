from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .agents import render_prompt
from .backends import AgentBackend, build_backend
from .config import PipelineConfig
from .io import (
    InputValidationError,
    build_transcript,
    ensure_output_dir,
    format_timestamp,
    load_problem_inputs,
    utc_now,
    write_meta,
    write_text,
)
from .models import CriticIssue, LoopRecord, PipelineRunResult
from .validate import OutputValidationError, ensure_required_sections, parse_critic_output


def _issues_to_markdown(issues: list[CriticIssue]) -> str:
    if not issues:
        return "None."
    lines = []
    for idx, issue in enumerate(issues, start=1):
        lines.append(
            f"{idx}. [{issue.severity}] {issue.location}: {issue.reason} "
            f"(required fix: {issue.required_fix})"
        )
    return "\n".join(lines)


def _format_loop_for_context(loop: LoopRecord) -> str:
    return (
        f"## Loop {loop.loop_index}\n"
        "### Statement\n"
        f"{loop.statement_text.strip()}\n"
        "### Sketch\n"
        f"{loop.sketch_text.strip()}\n"
        "### Prover\n"
        f"{loop.prover_text.strip()}\n"
        "### Critic\n"
        f"{loop.critic_text.strip()}\n"
    )


def _build_context(
    problem_id: str,
    question_text: str,
    background_text: str,
    rigor: str,
    loop_index: int,
    max_loops: int,
    prior_transcript: str,
    critic_issues: list[CriticIssue],
) -> dict[str, str]:
    return {
        "problem_id": problem_id,
        "question_text": question_text,
        "background_text": background_text,
        "rigor": rigor,
        "loop_index": str(loop_index),
        "max_loops": str(max_loops),
        "prior_transcript": prior_transcript.strip() or "None.",
        "critic_issues_markdown": _issues_to_markdown(critic_issues),
    }


def _aggregate_issue_counts(loops: list[LoopRecord]) -> dict[str, int]:
    counts: dict[str, int] = {"critical": 0, "major": 0, "minor": 0}
    for loop in loops:
        for issue in loop.critic_result.issues:
            counts[issue.severity] += 1
    return counts


def run_pipeline(
    problem_dir: Path,
    config: PipelineConfig,
    backend: AgentBackend,
) -> PipelineRunResult:
    config.validate()
    problem_inputs = load_problem_inputs(problem_dir)
    started_dt = utc_now()
    started_at = started_dt.isoformat()

    loops: list[LoopRecord] = []
    prior_transcript = ""
    critic_issues: list[CriticIssue] = []

    for loop_index in range(1, config.max_loops + 1):
        base_context = _build_context(
            problem_id=problem_inputs.problem_id,
            question_text=problem_inputs.question_text,
            background_text=problem_inputs.background_text,
            rigor=config.rigor,
            loop_index=loop_index,
            max_loops=config.max_loops,
            prior_transcript=prior_transcript,
            critic_issues=critic_issues,
        )

        statement_prompt = render_prompt("statement", base_context)
        statement_text = backend.generate("statement", statement_prompt, base_context)
        ensure_required_sections("statement", statement_text)

        sketch_context = dict(base_context)
        sketch_context["statement_output"] = statement_text
        sketch_prompt = render_prompt("sketch", sketch_context)
        sketch_text = backend.generate("sketch", sketch_prompt, sketch_context)
        ensure_required_sections("sketch", sketch_text)

        prover_context = dict(sketch_context)
        prover_context["sketch_output"] = sketch_text
        prover_prompt = render_prompt("prover", prover_context)
        prover_text = backend.generate("prover", prover_prompt, prover_context)
        ensure_required_sections("prover", prover_text)

        critic_context = dict(prover_context)
        critic_context["prover_output"] = prover_text
        critic_prompt = render_prompt("critic", critic_context)
        critic_text = backend.generate("critic", critic_prompt, critic_context)
        critic_result = parse_critic_output(critic_text)

        loop = LoopRecord(
            loop_index=loop_index,
            statement_text=statement_text,
            sketch_text=sketch_text,
            prover_text=prover_text,
            critic_text=critic_text,
            critic_result=critic_result,
        )
        loops.append(loop)
        prior_transcript += "\n" + _format_loop_for_context(loop)

        if critic_result.verdict == "PASS":
            break
        critic_issues = critic_result.issues

    finished_dt = utc_now()
    finished_at = finished_dt.isoformat()
    timestamp = format_timestamp(started_dt)
    out_dir = ensure_output_dir(problem_dir, config.out_dir_name)
    transcript_path = out_dir / f"{timestamp}-transcript.md"
    meta_path = out_dir / f"{timestamp}-meta.json"

    final_verdict = loops[-1].critic_result.verdict
    issue_counts = _aggregate_issue_counts(loops)
    run_result = PipelineRunResult(
        problem_id=problem_inputs.problem_id,
        started_at=started_at,
        finished_at=finished_at,
        max_loops=config.max_loops,
        executed_loops=len(loops),
        final_verdict=final_verdict,
        issue_counts=issue_counts,
        loops=loops,
        transcript_path=transcript_path,
        meta_path=meta_path,
    )

    transcript_text = build_transcript(
        problem_inputs=problem_inputs,
        config=config,
        loops=loops,
        started_at=started_at,
        finished_at=finished_at,
        final_verdict=final_verdict,
    )
    write_text(transcript_path, transcript_text)
    write_meta(
        meta_path,
        run_result=run_result,
        input_hashes={
            "question_sha256": problem_inputs.question_hash,
            "background_sha256": problem_inputs.background_hash,
        },
    )
    return run_result


def _build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the multi-agent proof pipeline.")
    parser.add_argument(
        "--problem",
        required=True,
        help="Problem folder path or id (for example: 5 or ./5).",
    )
    parser.add_argument("--max-loops", type=int, default=5, help="Maximum revision loops.")
    parser.add_argument(
        "--rigor",
        default="graduate",
        help="Rigor target label included in prompts.",
    )
    parser.add_argument(
        "--out-dir",
        default="runs",
        help="Output directory name inside the problem folder.",
    )
    parser.add_argument(
        "--backend",
        default="codex",
        choices=["codex", "demo"],
        help="Agent backend implementation.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Optional model name when backend=codex. If omitted, Codex CLI profile defaults are used.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional deterministic seed for compatible backends.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate problem inputs and prompt rendering only.",
    )
    return parser


def _resolve_problem_dir(problem: str) -> Path:
    candidate = Path(problem)
    if candidate.exists():
        return candidate
    return Path.cwd() / problem


def main(argv: list[str] | None = None) -> int:
    parser = _build_argument_parser()
    args = parser.parse_args(argv)

    config = PipelineConfig(
        max_loops=args.max_loops,
        rigor=args.rigor,
        out_dir_name=args.out_dir,
        backend=args.backend,
        model=args.model,
        seed=args.seed,
    )

    problem_dir = _resolve_problem_dir(args.problem)
    try:
        config.validate()
        problem_inputs = load_problem_inputs(problem_dir)
    except (ValueError, InputValidationError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 2

    if args.dry_run:
        dry_context = _build_context(
            problem_id=problem_inputs.problem_id,
            question_text=problem_inputs.question_text,
            background_text=problem_inputs.background_text,
            rigor=config.rigor,
            loop_index=1,
            max_loops=config.max_loops,
            prior_transcript="",
            critic_issues=[],
        )
        dry_context["statement_output"] = "<dry-run statement output placeholder>"
        dry_context["sketch_output"] = "<dry-run sketch output placeholder>"
        dry_context["prover_output"] = "<dry-run prover output placeholder>"
        try:
            for role in ("statement", "sketch", "prover", "critic"):
                _ = render_prompt(role, dry_context)
        except Exception as exc:
            print(f"[error] Prompt rendering failed: {exc}", file=sys.stderr)
            return 2
        print(
            f"[ok] Dry run succeeded for problem '{problem_inputs.problem_id}' "
            f"with backend '{config.backend}'."
        )
        return 0

    try:
        backend = build_backend(
            config.backend,
            config.model,
            config.seed,
            workdir=Path.cwd(),
        )
        result = run_pipeline(problem_dir=problem_dir, config=config, backend=backend)
    except (OutputValidationError, ValueError, RuntimeError, InputValidationError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 3

    print(f"[ok] Problem: {result.problem_id}")
    print(f"[ok] Loops: {result.executed_loops}/{result.max_loops}")
    print(f"[ok] Verdict: {result.final_verdict}")
    print(f"[ok] Transcript: {result.transcript_path}")
    print(f"[ok] Meta: {result.meta_path}")
    if result.final_verdict == "PASS":
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
