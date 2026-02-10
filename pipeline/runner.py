from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from .agent_config import find_config_file, load_config_file, validate_approved_backends
from .agents import render_prompt
from .backends import BackendRouter, build_backend, build_backend_from_config
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
from .models import (
    EditorDecision,
    EditorDispatch,
    EditorVerdict,
    LoopRecord,
    PipelineRunResult,
    ReviewerResult,
)
from .validate import (
    OutputValidationError,
    ensure_required_sections,
    parse_editor_decision_output,
    parse_editor_dispatch_output,
    parse_reviewer_output,
)


def _reviews_to_markdown(reviewer_results: list[ReviewerResult]) -> str:
    lines: list[str] = []
    idx = 0
    for rr in reviewer_results:
        for issue in rr.issues:
            idx += 1
            lines.append(
                f"{idx}. [{issue.severity}] ({rr.perspective_name}) {issue.location}: "
                f"{issue.reason} (required fix: {issue.required_fix}) "
                f"[suggestion: {issue.suggestion}]"
            )
    return "\n".join(lines) if lines else "None."


def _build_pool_description(pool_names: list[str]) -> str:
    if not pool_names:
        return "No reviewers available."
    lines = [f"- **{name}**" for name in pool_names]
    return "\n".join(lines)


def _build_perspectives_description(
    perspectives: list[tuple[str, str]],
) -> str:
    lines = []
    for i, (name, desc) in enumerate(perspectives, start=1):
        lines.append(f"{i}. **{name}**: {desc}")
    return "\n".join(lines)


def _format_loop_for_context(loop: LoopRecord) -> str:
    parts = [
        f"## Loop {loop.loop_index}\n"
        "### Mentor\n"
        f"{loop.mentor_text.strip()}\n"
        "### Prover\n"
        f"{loop.prover_text.strip()}\n"
    ]
    for persp_name, reviewer_text in loop.reviewer_texts.items():
        parts.append(f"### Reviewer — {persp_name}\n{reviewer_text.strip()}\n")
    decision = loop.editor_decision
    parts.append(
        f"### Editor Decision — {decision.verdict}\n"
        f"{decision.summary}\n"
    )
    return "".join(parts)


_JOKE_REVIEWER_LINES: dict[str, str] = {
    "self_citer": (
        "has submitted what appears to be an annotated bibliography of "
        "their own collected works, tangentially organized around the "
        "pretense of evaluating the proof. They cite themselves no fewer "
        "than fourteen times. They engage with the actual mathematics "
        "zero times. They have also, remarkably, suggested we add them "
        "as a co-author."
    ),
    "extension_requester": (
        "has — after a delay that I can only describe as geological — "
        "informed me that they managed to read the title and part of "
        "the abstract before being called away by a departmental "
        "retreat, two grant deadlines, a child's school play, and "
        "(I am not making this up) 'a particularly engrossing season "
        "of television.' They request six to eight additional months, "
        "contingent on the completion of their sabbatical."
    ),
}


def _exasperated_rejection(
    joke_assigned: dict[str, str],
    all_assignments: dict[str, str],
    required_reviewers: list[str],
) -> tuple[EditorVerdict, str, str]:
    """Build an exasperated editor rejection when joke reviewers are present."""
    parts = [
        "I have now read all submitted reviews. What follows is my "
        "candid assessment of the review process for this manuscript.",
    ]
    for persp, pool in sorted(joke_assigned.items()):
        line = _JOKE_REVIEWER_LINES.get(pool, "has submitted a review of dubious merit.")
        parts.append(f"The reviewer assigned to '{persp}' {line}")

    real = [
        persp for persp, pool in all_assignments.items()
        if pool not in required_reviewers
    ]
    if real:
        parts.append(
            f"The reviewer assigned to '{real[0]}' provided a genuine and "
            "substantive evaluation, which I now lack the will to act upon."
        )
    parts.append(
        "I am rejecting this manuscript effective immediately — not on "
        "its mathematical merits, which remain unexamined, but because "
        "the review process itself has become untenable."
    )
    summary = "\n\n".join(parts)

    feedback = (
        "After careful deliberation, the editorial board has determined "
        "that your submission does not meet the journal's current "
        "standards. We encourage the authors to consider alternative "
        "venues. No further correspondence will be entered into "
        "regarding this decision. We thank you for your interest in "
        "the Annals of Conditions Under Which Peer Review Actually "
        "Functions."
    )
    verdict: EditorVerdict = "reject"
    return verdict, summary, feedback


def _build_context(
    problem_id: str,
    question_text: str,
    background_text: str,
    rigor: str,
    loop_index: int,
    max_loops: int,
    prior_transcript: str,
    editor_feedback: str,
    researcher_output: str = "None.",
) -> dict[str, str]:
    return {
        "problem_id": problem_id,
        "question_text": question_text,
        "background_text": background_text,
        "rigor": rigor,
        "loop_index": str(loop_index),
        "max_loops": str(max_loops),
        "prior_transcript": prior_transcript.strip() or "None.",
        "editor_feedback": editor_feedback,
        "researcher_output": researcher_output,
    }


def _aggregate_issue_counts(loops: list[LoopRecord]) -> dict[str, int]:
    counts: dict[str, int] = {"critical": 0, "major": 0, "minor": 0}
    for loop in loops:
        for rr in loop.editor_decision.reviewer_results:
            for issue in rr.issues:
                counts[issue.severity] += 1
    return counts


def _status(msg: str) -> None:
    """Print a pipeline progress line to stderr."""
    print(f"  {msg}", file=sys.stderr, flush=True)


def run_pipeline(
    problem_dir: Path,
    config: PipelineConfig,
    backend: BackendRouter,
) -> PipelineRunResult:
    config.validate()
    problem_inputs = load_problem_inputs(problem_dir)
    started_dt = utc_now()
    started_at = started_dt.isoformat()

    loops: list[LoopRecord] = []
    prior_transcript = ""
    editor_feedback = "None."
    feedback_target = ""

    pool_names = sorted(backend.pool_backends)
    perspective_pairs = [
        (p.name, p.description) for p in config.reviewer_perspectives
    ]
    perspective_names = [p.name for p in config.reviewer_perspectives]

    pool_desc = _build_pool_description(pool_names)
    persp_desc = _build_perspectives_description(perspective_pairs)

    # --- Researcher (once, pre-loop) ---
    _status("researcher ...")
    researcher_context = {
        "problem_id": problem_inputs.problem_id,
        "question_text": problem_inputs.question_text,
        "background_text": problem_inputs.background_text,
        "rigor": config.rigor,
    }
    researcher_prompt = render_prompt("researcher", researcher_context)
    researcher_text = backend.generate("researcher", researcher_prompt, researcher_context)
    ensure_required_sections("researcher", researcher_text)
    _status("researcher done")

    for loop_index in range(1, config.max_loops + 1):
        base_context = _build_context(
            problem_id=problem_inputs.problem_id,
            question_text=problem_inputs.question_text,
            background_text=problem_inputs.background_text,
            rigor=config.rigor,
            loop_index=loop_index,
            max_loops=config.max_loops,
            prior_transcript=prior_transcript,
            editor_feedback=editor_feedback,
            researcher_output=researcher_text,
        )

        # --- Mentor (runs if first loop or wrong_track) ---
        if feedback_target != "prover":
            _status(f"[loop {loop_index}/{config.max_loops}] mentor ...")
            mentor_prompt = render_prompt("mentor", base_context)
            mentor_text = backend.generate("mentor", mentor_prompt, base_context)
            ensure_required_sections("mentor", mentor_text)
        else:
            _status(f"[loop {loop_index}/{config.max_loops}] mentor (reused — right_track)")
            # Reuse last mentor output when feedback_target is prover (right_track)
            mentor_text = loops[-1].mentor_text

        # --- Prover ---
        _status(f"[loop {loop_index}/{config.max_loops}] prover ...")
        prover_context = dict(base_context)
        prover_context["mentor_output"] = mentor_text
        prover_prompt = render_prompt("prover", prover_context)
        prover_text = backend.generate("prover", prover_prompt, prover_context)
        ensure_required_sections("prover", prover_text)

        # --- Editor dispatch ---
        _status(f"[loop {loop_index}/{config.max_loops}] editor dispatch ...")
        dispatch_context = dict(prover_context)
        dispatch_context["prover_output"] = prover_text
        dispatch_context["pool_description"] = pool_desc
        dispatch_context["perspectives_description"] = persp_desc
        dispatch_prompt = render_prompt("editor_dispatch", dispatch_context)
        dispatch_text = backend.generate(
            "editor_dispatch", dispatch_prompt, dispatch_context
        )
        editor_dispatch = parse_editor_dispatch_output(
            dispatch_text, perspective_names, pool_names
        )

        # --- Enforce required reviewers ---
        if backend.required_reviewers:
            patched = dict(editor_dispatch.assignments)
            already = {v for v in patched.values() if v in backend.required_reviewers}
            missing = [r for r in backend.required_reviewers if r not in already]
            if missing:
                # Perspectives not assigned to any required reviewer first
                overridable = [
                    p for p in perspective_names
                    if patched[p] not in backend.required_reviewers
                ]
                # Then perspectives with duplicate required-reviewer assignments
                if len(overridable) < len(missing):
                    seen: set[str] = set()
                    for p in perspective_names:
                        pool = patched[p]
                        if pool in backend.required_reviewers:
                            if pool in seen:
                                overridable.append(p)
                            seen.add(pool)
                for req in missing:
                    if overridable:
                        persp = overridable.pop(0)
                        patched[persp] = req
            if patched != editor_dispatch.assignments:
                _status(
                    f"[loop {loop_index}/{config.max_loops}] "
                    f"required reviewers enforced: "
                    + ", ".join(
                        f"{p} -> {patched[p]}"
                        for p in perspective_names
                        if patched[p] != editor_dispatch.assignments[p]
                    )
                )
                editor_dispatch = EditorDispatch(
                    assignments=patched,
                    reasoning=editor_dispatch.reasoning,
                )

        # --- Reviewers (one per perspective) ---
        reviewer_results: list[ReviewerResult] = []
        reviewer_texts: dict[str, str] = {}
        num_perspectives = len(config.reviewer_perspectives)
        for persp_idx, persp in enumerate(config.reviewer_perspectives, 1):
            assigned_pool = editor_dispatch.assignments[persp.name]
            _status(
                f"[loop {loop_index}/{config.max_loops}] "
                f"reviewer {persp_idx}/{num_perspectives} "
                f"({assigned_pool} -> {persp.name}) ..."
            )
            reviewer_context = dict(dispatch_context)
            reviewer_context["reviewer_name"] = assigned_pool
            reviewer_context["perspective_name"] = persp.name
            reviewer_context["perspective_description"] = persp.description
            reviewer_prompt = render_prompt("reviewer", reviewer_context)
            reviewer_text = backend.generate_with_pool(
                assigned_pool, "reviewer", reviewer_prompt, reviewer_context
            )
            reviewer_result = parse_reviewer_output(
                reviewer_text,
                reviewer_name=assigned_pool,
                perspective_name=persp.name,
            )
            reviewer_results.append(reviewer_result)
            reviewer_texts[persp.name] = reviewer_text

        # --- Editor decision ---
        joke_assigned = {
            persp: pool
            for persp, pool in editor_dispatch.assignments.items()
            if pool in backend.required_reviewers
        }
        if joke_assigned:
            verdict, summary, feedback = _exasperated_rejection(
                joke_assigned, editor_dispatch.assignments,
                backend.required_reviewers,
            )
            _status(
                f"[loop {loop_index}/{config.max_loops}] "
                "editor decision (exasperated) ..."
            )
        else:
            _status(f"[loop {loop_index}/{config.max_loops}] editor decision ...")
            reviews_md = _reviews_to_markdown(reviewer_results)
            decision_context = dict(dispatch_context)
            decision_context["reviews_markdown"] = reviews_md
            decision_prompt = render_prompt("editor_decision", decision_context)
            decision_text = backend.generate(
                "editor_decision", decision_prompt, decision_context
            )
            verdict, summary, feedback = parse_editor_decision_output(
                decision_text
            )

        # --- Editor summary (shown to user) ---
        issue_summary = ", ".join(
            f"{sum(1 for rr in reviewer_results for i in rr.issues if i.severity == s)} {s}"
            for s in ("critical", "major", "minor")
            if any(i.severity == s for rr in reviewer_results for i in rr.issues)
        ) or "no issues"
        _status("")
        _status(f"--- Managing Editor — Loop {loop_index}/{config.max_loops} ---")
        _status(f"Verdict: {verdict}")
        _status(f"Issues:  {issue_summary}")
        _status(f"Summary: {summary}")
        if feedback:
            _status(f"Feedback: {feedback}")
        _status("")

        if verdict in ("accept", "reject"):
            feedback_target_str = ""
        elif verdict == "right_track":
            feedback_target_str = "prover"
        else:
            feedback_target_str = "mentor"

        editor_decision = EditorDecision(
            verdict=verdict,
            summary=summary,
            feedback=feedback,
            feedback_target=feedback_target_str,
            reviewer_results=reviewer_results,
        )

        loop = LoopRecord(
            loop_index=loop_index,
            mentor_text=mentor_text,
            prover_text=prover_text,
            editor_dispatch=editor_dispatch,
            reviewer_texts=reviewer_texts,
            editor_decision=editor_decision,
        )
        loops.append(loop)
        prior_transcript += "\n" + _format_loop_for_context(loop)

        if verdict in ("accept", "reject"):
            break
        editor_feedback = feedback
        feedback_target = feedback_target_str

    finished_dt = utc_now()
    finished_at = finished_dt.isoformat()
    timestamp = format_timestamp(started_dt)
    out_dir = ensure_output_dir(problem_dir, config.out_dir_name)
    transcript_path = out_dir / f"{timestamp}-transcript.md"
    meta_path = out_dir / f"{timestamp}-meta.json"
    latex_path = out_dir / f"{timestamp}-report.tex"

    final_verdict: EditorVerdict = loops[-1].editor_decision.verdict
    issue_counts = _aggregate_issue_counts(loops)
    run_result = PipelineRunResult(
        problem_id=problem_inputs.problem_id,
        started_at=started_at,
        finished_at=finished_at,
        max_loops=config.max_loops,
        executed_loops=len(loops),
        final_verdict=final_verdict,
        issue_counts=issue_counts,
        researcher_text=researcher_text,
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
        researcher_text=researcher_text,
    )
    write_text(transcript_path, transcript_text)

    latex_text = build_latex(
        problem_inputs=problem_inputs,
        config=config,
        loops=loops,
        started_at=started_at,
        finished_at=finished_at,
        final_verdict=final_verdict,
        researcher_text=researcher_text,
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
) -> BackendRouter:
    """Build the appropriate backend: config-file router or legacy single."""
    # Explicit --backend demo bypasses config file discovery
    if config.backend == "demo" and config.config_path is None:
        return build_backend(
            config.backend, config.model, config.seed, workdir=Path.cwd()
        )

    config_file = find_config_file(
        explicit=config.config_path,
        search_dirs=[problem_dir, Path.cwd()],
    )
    if config_file is not None:
        file_config = load_config_file(config_file)
        validate_approved_backends(file_config)
        print(f"[info] Using config: {config_file}", file=sys.stderr)
        router, assignments = build_backend_from_config(
            file_config, workdir=Path.cwd(), seed=config.seed,
        )
        for role, pool_name in sorted(assignments.items()):
            cfg = file_config.reviewer_pool.get(pool_name, file_config.defaults)
            print(
                f"[info] {role} -> {pool_name} "
                f"({cfg.backend}/{cfg.provider}/{cfg.model})",
                file=sys.stderr,
            )
        return router

    # Fall back to legacy single-backend mode
    return build_backend(
        config.backend, config.model, config.seed, workdir=Path.cwd()
    )


_EXPORT_RE = re.compile(
    r'^export\s+([A-Za-z_][A-Za-z0-9_]*)=["\']?(.*?)["\']?\s*$'
)


def _load_secrets(*search_dirs: Path) -> None:
    """Load ``export KEY=value`` lines from the first ``.secrets`` file found."""
    for d in search_dirs:
        secrets = d / ".secrets"
        if secrets.is_file():
            for line in secrets.read_text(encoding="utf-8").splitlines():
                m = _EXPORT_RE.match(line)
                if m:
                    os.environ.setdefault(m.group(1), m.group(2))
            return


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
    _load_secrets(problem_dir, Path.cwd())

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
            editor_feedback="None.",
            researcher_output="<dry-run researcher output placeholder>",
        )
        dry_context["mentor_output"] = "<dry-run mentor output placeholder>"
        dry_context["prover_output"] = "<dry-run prover output placeholder>"
        dry_context["pool_description"] = "<dry-run pool description>"
        dry_context["perspectives_description"] = "<dry-run perspectives>"
        dry_context["reviewer_name"] = "<dry-run reviewer>"
        dry_context["perspective_name"] = "<dry-run perspective>"
        dry_context["perspective_description"] = "<dry-run description>"
        dry_context["reviews_markdown"] = "<dry-run reviews>"
        try:
            for role in (
                "researcher", "mentor", "prover",
                "editor_dispatch", "editor_decision", "reviewer",
            ):
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
    if result.final_verdict == "accept":
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
