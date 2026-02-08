from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .agent_config import find_config_file, load_config_file
from .agents import render_prompt
from .backends import AgentBackend, build_backend, build_backend_from_config
from .config import PipelineConfig
from .io import (
    InputValidationError,
    build_latex,
    build_transcript,
    ensure_output_dir,
    format_timestamp,
    load_problem_inputs,
    utc_now,
    write_meta,
    write_text,
)
from .models import CouncilResult, CriticIssue, CriticResult, LoopRecord, PipelineRunResult
from .validate import OutputValidationError, ensure_required_sections, parse_critic_output


def _issues_to_markdown(issues: list[CriticIssue], critics: list[CriticResult] | None = None) -> str:
    if critics is not None:
        lines = []
        idx = 0
        for cr in critics:
            for issue in cr.issues:
                idx += 1
                lines.append(
                    f"{idx}. [{issue.severity}] ({cr.critic_name}) {issue.location}: "
                    f"{issue.reason} (required fix: {issue.required_fix}) "
                    f"[suggestion: {issue.suggestion}]"
                )
        return "\n".join(lines) if lines else "None."

    if not issues:
        return "None."
    lines = []
    for idx, issue in enumerate(issues, start=1):
        lines.append(
            f"{idx}. [{issue.severity}] {issue.location}: {issue.reason} "
            f"(required fix: {issue.required_fix}) "
            f"[suggestion: {issue.suggestion}]"
        )
    return "\n".join(lines)


def _format_loop_for_context(loop: LoopRecord) -> str:
    parts = [
        f"## Loop {loop.loop_index}\n"
        "### Statement\n"
        f"{loop.statement_text.strip()}\n"
        "### Sketch\n"
        f"{loop.sketch_text.strip()}\n"
        "### Prover\n"
        f"{loop.prover_text.strip()}\n"
    ]
    for critic_name, critic_text in loop.critic_texts.items():
        parts.append(f"### Critic — {critic_name}\n{critic_text.strip()}\n")
    return "".join(parts)


def _build_context(
    problem_id: str,
    question_text: str,
    background_text: str,
    rigor: str,
    loop_index: int,
    max_loops: int,
    prior_transcript: str,
    critic_issues: list[CriticIssue],
    council_critics: list[CriticResult] | None = None,
) -> dict[str, str]:
    return {
        "problem_id": problem_id,
        "question_text": question_text,
        "background_text": background_text,
        "rigor": rigor,
        "loop_index": str(loop_index),
        "max_loops": str(max_loops),
        "prior_transcript": prior_transcript.strip() or "None.",
        "critic_issues_markdown": _issues_to_markdown(critic_issues, council_critics),
    }


def _aggregate_issue_counts(loops: list[LoopRecord]) -> dict[str, int]:
    counts: dict[str, int] = {"critical": 0, "major": 0, "minor": 0}
    for loop in loops:
        for issue in loop.council_result.all_issues:
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
    council_critics: list[CriticResult] | None = None

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
            council_critics=council_critics,
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

        critic_base_context = dict(prover_context)
        critic_base_context["prover_output"] = prover_text

        critic_results: list[CriticResult] = []
        critic_texts: dict[str, str] = {}

        for perspective in config.critic_perspectives:
            critic_context = dict(critic_base_context)
            critic_context["critic_perspective_name"] = perspective.name
            critic_context["critic_perspective_description"] = perspective.description
            critic_prompt = render_prompt("critic", critic_context)
            critic_text = backend.generate("critic", critic_prompt, critic_context)
            critic_result = parse_critic_output(critic_text, critic_name=perspective.name)
            critic_results.append(critic_result)
            critic_texts[perspective.name] = critic_text

        council = CouncilResult(verdicts=critic_results)

        loop = LoopRecord(
            loop_index=loop_index,
            statement_text=statement_text,
            sketch_text=sketch_text,
            prover_text=prover_text,
            critic_texts=critic_texts,
            council_result=council,
        )
        loops.append(loop)
        prior_transcript += "\n" + _format_loop_for_context(loop)

        if council.overall_verdict == "PASS":
            break
        critic_issues = council.all_issues
        council_critics = critic_results

    finished_dt = utc_now()
    finished_at = finished_dt.isoformat()
    timestamp = format_timestamp(started_dt)
    out_dir = ensure_output_dir(problem_dir, config.out_dir_name)
    transcript_path = out_dir / f"{timestamp}-transcript.md"
    meta_path = out_dir / f"{timestamp}-meta.json"
    latex_path = out_dir / f"{timestamp}-report.tex"

    final_verdict = loops[-1].council_result.overall_verdict
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
        latex_path=latex_path,
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

    latex_text = build_latex(
        problem_inputs=problem_inputs,
        config=config,
        loops=loops,
        started_at=started_at,
        finished_at=finished_at,
        final_verdict=final_verdict,
    )
    write_text(latex_path, latex_text)

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
        help="Agent backend (legacy single-backend mode). Ignored when --config is set.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Model name for legacy --backend mode. Ignored when --config is set.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional deterministic seed for compatible backends.",
    )
    parser.add_argument(
        "--config",
        default=None,
        help=(
            "Path to a pipeline.toml config file for per-agent backend/model "
            "selection. If omitted, searches for pipeline.toml in the problem "
            "directory and current working directory."
        ),
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


def _resolve_backend(
    config: PipelineConfig, problem_dir: Path
) -> AgentBackend:
    """Build the appropriate backend: config-file router or legacy single."""
    config_file = find_config_file(
        explicit=config.config_path,
        search_dirs=[problem_dir, Path.cwd()],
    )
    if config_file is not None:
        file_config = load_config_file(config_file)
        print(f"[info] Using config: {config_file}", file=sys.stderr)
        return build_backend_from_config(file_config, workdir=Path.cwd())

    # Fall back to legacy single-backend mode
    return build_backend(
        config.backend, config.model, config.seed, workdir=Path.cwd()
    )


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
        config_path=args.config,
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
        dry_context["critic_perspective_name"] = "<dry-run perspective>"
        dry_context["critic_perspective_description"] = "<dry-run description>"
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
        backend = _resolve_backend(config, problem_dir)
        result = run_pipeline(problem_dir=problem_dir, config=config, backend=backend)
    except (OutputValidationError, ValueError, RuntimeError, InputValidationError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 3

    print(f"[ok] Problem: {result.problem_id}")
    print(f"[ok] Loops: {result.executed_loops}/{result.max_loops}")
    print(f"[ok] Verdict: {result.final_verdict}")
    print(f"[ok] Transcript: {result.transcript_path}")
    print(f"[ok] LaTeX: {result.latex_path}")
    print(f"[ok] Meta: {result.meta_path}")
    if result.final_verdict == "PASS":
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
