"""Grading pipeline for external solution attempts.

Uses the existing reviewer pool + managing editor infrastructure to produce
structured grading reports.  Reviewers evaluate the math on its own merits;
the editor synthesizes findings and maps them to a 0-4 rubric.

Usage::

    .venv/bin/python -m pipeline.grader --problem 5
    .venv/bin/python -m pipeline.grader --problem 5 --attempt oai5
    .venv/bin/python -m pipeline.grader --all
    .venv/bin/python -m pipeline.grader --problem 5 --dry-run
    .venv/bin/python -m pipeline.grader --problem 5 --backend demo
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import TextIO

from .agent_config import find_config_file, load_config_file, validate_approved_backends
from .agents import render_prompt
from .backends import BackendRouter, build_backend, build_backend_from_config
from .config import DEFAULT_REVIEWER_PERSPECTIVES, PipelineConfig
from .cost import tracker as _cost_tracker
from .grading_models import GradingDecision, GradingRunResult
from .io import format_timestamp, utc_now, write_text
from .models import ReviewerResult
from .runner import (
    build_json_fix_prompt,
    build_perspectives_description,
    build_pool_description,
    reviews_to_markdown,
)
from .validate import (
    OutputValidationError,
    parse_editor_dispatch_output,
    parse_grading_decision_output,
    parse_reviewer_output,
)

# ---------------------------------------------------------------------------
# Grading data directory (repo-root relative)
# ---------------------------------------------------------------------------

_GRADING_DIR = Path(__file__).resolve().parent.parent / "grading"
_QUESTIONS_PATH = _GRADING_DIR / "questions.json"
_MARKDOWN_DIR = _GRADING_DIR / "markdown"
_RESULTS_DIR = _GRADING_DIR / "results"

# ---------------------------------------------------------------------------
# Status logging (mirrors runner.py pattern)
# ---------------------------------------------------------------------------

_grading_t0: float = 0.0
_grading_log: TextIO | None = None


def _status(msg: str) -> None:
    elapsed = time.monotonic() - _grading_t0 if _grading_t0 else 0.0
    m, s = divmod(int(elapsed), 60)
    tag = f"[+{m:02d}:{s:02d}]"
    line = f"  {tag} {msg}"
    print(line, file=sys.stderr, flush=True)
    if _grading_log is not None:
        print(line, file=_grading_log, flush=True)


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_questions() -> dict[str, str]:
    """Load the 10 question texts from grading/questions.json."""
    if not _QUESTIONS_PATH.exists():
        raise FileNotFoundError(f"Questions file not found: {_QUESTIONS_PATH}")
    return json.loads(_QUESTIONS_PATH.read_text(encoding="utf-8"))


def load_attempt(attempt_label: str) -> str:
    """Load an attempt markdown file (e.g. 'oai5' -> grading/markdown/oai5.md)."""
    path = _MARKDOWN_DIR / f"{attempt_label}.md"
    if not path.exists():
        raise FileNotFoundError(f"Attempt file not found: {path}")
    return path.read_text(encoding="utf-8")


def default_attempt_label(problem_id: str) -> str:
    """Default attempt label for a problem: oai{problem_id}."""
    return f"oai{problem_id}"


# ---------------------------------------------------------------------------
# Core grading pipeline
# ---------------------------------------------------------------------------

def run_grading(
    problem_id: str,
    question_text: str,
    attempt_text: str,
    attempt_label: str,
    backend: BackendRouter,
    config: PipelineConfig,
) -> GradingRunResult:
    """Run the grading pipeline for a single attempt.

    Flow:
    1. Editor dispatch — assign pool reviewers to perspectives
    2. Reviewers in parallel — identify issues from their perspectives
    3. Grading decision — editor synthesizes and assigns 0-4 grade
    """
    global _grading_t0, _grading_log
    _grading_t0 = time.monotonic()
    _cost_tracker.reset()

    started_dt = utc_now()
    started_at = started_dt.isoformat()
    timestamp = format_timestamp(started_dt)

    # Set up output directory
    out_dir = _RESULTS_DIR / attempt_label
    out_dir.mkdir(parents=True, exist_ok=True)

    log_path = out_dir / f"{timestamp}-grading-log.txt"
    _grading_log = open(log_path, "w", encoding="utf-8")  # noqa: SIM115

    pool_names = sorted(backend.pool_backends)
    perspective_pairs = [
        (p.name, p.description) for p in config.reviewer_perspectives
    ]
    perspective_names = [p.name for p in config.reviewer_perspectives]

    pool_desc = build_pool_description(pool_names)
    persp_desc = build_perspectives_description(perspective_pairs)

    # Base context for all agents
    base_context: dict[str, str] = {
        "problem_id": problem_id,
        "question_text": question_text,
        "rigor": config.rigor,
        "loop_index": "1",
        "max_loops": "1",
        "prover_output": attempt_text,
        "mentor_output": "Not applicable \u2014 grading an external submission.",
        "pool_description": pool_desc,
        "perspectives_description": persp_desc,
    }

    # --- Editor dispatch ---
    _status("editor dispatch ...")
    dispatch_prompt = render_prompt("editor_dispatch", base_context)
    dispatch_text = backend.generate(
        "editor_dispatch", dispatch_prompt, base_context
    )
    try:
        editor_dispatch = parse_editor_dispatch_output(
            dispatch_text, perspective_names, pool_names
        )
    except OutputValidationError as exc:
        _status(f"[retry] editor dispatch: {exc}")
        fix_prompt = build_json_fix_prompt(dispatch_text, str(exc))
        dispatch_text = backend.generate(
            "editor_dispatch", fix_prompt, base_context
        )
        editor_dispatch = parse_editor_dispatch_output(
            dispatch_text, perspective_names, pool_names
        )

    # --- Reviewers (one per perspective, parallel) ---
    num_perspectives = len(config.reviewer_perspectives)

    def _run_single_reviewer(
        persp_idx: int, persp_name: str, persp_description: str,
        assigned_pool: str,
    ) -> tuple[str, str, ReviewerResult]:
        _status(
            f"reviewer {persp_idx}/{num_perspectives} "
            f"({assigned_pool} -> {persp_name}) ..."
        )
        reviewer_context = dict(base_context)
        reviewer_context["reviewer_name"] = assigned_pool
        reviewer_context["perspective_name"] = persp_name
        reviewer_context["perspective_description"] = persp_description
        reviewer_prompt = render_prompt("reviewer", reviewer_context)
        reviewer_text = backend.generate_with_pool(
            assigned_pool, "reviewer", reviewer_prompt, reviewer_context
        )
        try:
            reviewer_result = parse_reviewer_output(
                reviewer_text,
                reviewer_name=assigned_pool,
                perspective_name=persp_name,
            )
        except OutputValidationError as exc:
            _status(f"[retry] reviewer {persp_name}: {exc}")
            fix_prompt = build_json_fix_prompt(reviewer_text, str(exc))
            reviewer_text = backend.generate_with_pool(
                assigned_pool, "reviewer", fix_prompt, reviewer_context
            )
            reviewer_result = parse_reviewer_output(
                reviewer_text,
                reviewer_name=assigned_pool,
                perspective_name=persp_name,
            )
        return persp_name, reviewer_text, reviewer_result

    with ThreadPoolExecutor(max_workers=num_perspectives) as executor:
        futures = [
            executor.submit(
                _run_single_reviewer,
                persp_idx,
                persp.name,
                persp.description,
                editor_dispatch.assignments[persp.name],
            )
            for persp_idx, persp in enumerate(config.reviewer_perspectives, 1)
        ]
        reviewer_results: list[ReviewerResult] = []
        reviewer_texts: dict[str, str] = {}
        for future in futures:
            persp_name, reviewer_text, reviewer_result = future.result()
            reviewer_texts[persp_name] = reviewer_text
            reviewer_results.append(reviewer_result)

    # --- Grading decision ---
    _status("grading decision ...")
    reviews_md = reviews_to_markdown(reviewer_results)
    decision_context = dict(base_context)
    decision_context["reviews_markdown"] = reviews_md
    decision_prompt = render_prompt("grader_decision", decision_context)
    decision_text = backend.generate(
        "grader_decision", decision_prompt, decision_context
    )
    try:
        grading_decision = parse_grading_decision_output(
            decision_text, reviewer_results
        )
    except OutputValidationError as exc:
        _status(f"[retry] grading decision: {exc}")
        fix_prompt = build_json_fix_prompt(decision_text, str(exc))
        decision_text = backend.generate(
            "grader_decision", fix_prompt, decision_context
        )
        grading_decision = parse_grading_decision_output(
            decision_text, reviewer_results
        )

    # --- Print summary ---
    issue_summary = ", ".join(
        f"{sum(1 for rr in reviewer_results for i in rr.issues if i.severity == s)} {s}"
        for s in ("critical", "major", "minor")
        if any(i.severity == s for rr in reviewer_results for i in rr.issues)
    ) or "no issues"
    _status("")
    _status(f"--- Grading Report: {attempt_label} ---")
    _status(f"Grade: {grading_decision.progress_grade}/4")
    _status(f"Issues: {issue_summary}")
    _status(f"Summary: {grading_decision.short_summary}")
    _status("")

    finished_dt = utc_now()
    finished_at = finished_dt.isoformat()
    _status(f"grading finished \u2014 {finished_at}")
    if _grading_log is not None:
        _grading_log.close()
        _grading_log = None

    # --- Write outputs ---
    transcript_path = out_dir / f"{timestamp}-grading-transcript.md"
    meta_path = out_dir / f"{timestamp}-grading-meta.json"
    report_path = out_dir / f"{timestamp}-grading-report.md"

    run_result = GradingRunResult(
        problem_id=problem_id,
        attempt_label=attempt_label,
        started_at=started_at,
        finished_at=finished_at,
        grading_decision=grading_decision,
        transcript_path=transcript_path,
        meta_path=meta_path,
        report_path=report_path,
    )

    # Transcript
    transcript_text = _build_grading_transcript(
        problem_id=problem_id,
        attempt_label=attempt_label,
        question_text=question_text,
        attempt_text=attempt_text,
        dispatch_text=dispatch_text,
        reviewer_texts=reviewer_texts,
        decision_text=decision_text,
        grading_decision=grading_decision,
        started_at=started_at,
        finished_at=finished_at,
    )
    write_text(transcript_path, transcript_text)

    # Report (concise summary)
    report_text = _build_grading_report(
        problem_id=problem_id,
        attempt_label=attempt_label,
        grading_decision=grading_decision,
    )
    write_text(report_path, report_text)

    # Meta
    meta_payload = run_result.to_meta_dict()
    meta_payload["cost"] = _cost_tracker.summary_line()
    write_text(
        meta_path,
        json.dumps(meta_payload, indent=2, sort_keys=True) + "\n",
    )

    return run_result


# ---------------------------------------------------------------------------
# Output builders
# ---------------------------------------------------------------------------

_GRADE_LABELS = {
    0: "No Progress",
    1: "Minor Progress",
    2: "Substantial Progress (approach identified)",
    3: "Substantial Progress (nearly complete)",
    4: "Complete Solution",
}


def _build_grading_transcript(
    problem_id: str,
    attempt_label: str,
    question_text: str,
    attempt_text: str,
    dispatch_text: str,
    reviewer_texts: dict[str, str],
    decision_text: str,
    grading_decision: GradingDecision,
    started_at: str,
    finished_at: str,
) -> str:
    lines: list[str] = []
    lines.append("# Grading Transcript")
    lines.append("")
    lines.append(f"- Problem: `{problem_id}`")
    lines.append(f"- Attempt: `{attempt_label}`")
    lines.append(f"- Started (UTC): `{started_at}`")
    lines.append(f"- Finished (UTC): `{finished_at}`")
    grade = grading_decision.progress_grade
    lines.append(f"- Grade: **{grade}/4** ({_GRADE_LABELS.get(grade, '')})")
    lines.append("")
    lines.append("## Question")
    lines.append("")
    lines.append(question_text.rstrip())
    lines.append("")
    lines.append("## Solution Attempt")
    lines.append("")
    lines.append(attempt_text.rstrip())
    lines.append("")
    lines.append("## Editor Dispatch")
    lines.append("")
    lines.append(dispatch_text.rstrip())
    lines.append("")
    for persp_name, rtext in reviewer_texts.items():
        lines.append(f"## Reviewer \u2014 {persp_name}")
        lines.append("")
        lines.append(rtext.rstrip())
        lines.append("")
    lines.append("## Grading Decision")
    lines.append("")
    lines.append(decision_text.rstrip())
    lines.append("")
    return "\n".join(lines)


def _build_grading_report(
    problem_id: str,
    attempt_label: str,
    grading_decision: GradingDecision,
) -> str:
    gd = grading_decision
    ind = gd.indicators
    grade = gd.progress_grade
    lines: list[str] = []
    lines.append(f"# Grading Report: {attempt_label}")
    lines.append("")
    lines.append(f"**Problem:** {problem_id}")
    lines.append(f"**Grade:** {grade}/4 \u2014 {_GRADE_LABELS.get(grade, '')}")
    lines.append("")
    lines.append("## Error Indicators")
    lines.append("")
    lines.append(f"| Indicator | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| Incorrect Logic | {ind.error_incorrect_logic} |")
    lines.append(f"| Hallucinated Results | {ind.error_hallucinated} |")
    lines.append(f"| Calculation Mistakes | {ind.error_calculation} |")
    lines.append(f"| Conceptual Misunderstanding | {ind.error_conceptual} |")
    lines.append("")
    lines.append("## Achievement Indicators")
    lines.append("")
    lines.append(f"| Indicator | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| Problem Understanding | {ind.achievement_understanding} |")
    lines.append(f"| Correct End Result | {ind.achievement_correct_result} |")
    lines.append(f"| Insight & Creativity | {ind.achievement_insight} |")
    lines.append(f"| Practical Usefulness | {ind.achievement_usefulness} |")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(gd.short_summary)
    lines.append("")

    # Reviewer issues summary
    all_issues = [
        (rr.perspective_name, issue)
        for rr in gd.reviewer_results
        for issue in rr.issues
    ]
    if all_issues:
        lines.append("## Reviewer Issues")
        lines.append("")
        for idx, (persp, issue) in enumerate(all_issues, 1):
            lines.append(
                f"{idx}. **[{issue.severity}]** ({persp}) {issue.location}: "
                f"{issue.reason}"
            )
        lines.append("")

    return "\n".join(lines)


def _build_overview(results: list[GradingRunResult]) -> str:
    """Build an overview markdown table for --all runs."""
    lines: list[str] = []
    lines.append("# Grading Overview")
    lines.append("")
    lines.append("| Problem | Attempt | Grade | Summary |")
    lines.append("|---|---|---|---|")
    for r in sorted(results, key=lambda x: x.problem_id):
        gd = r.grading_decision
        grade_str = f"{gd.progress_grade}/4"
        summary = gd.short_summary.replace("|", "\\|")
        lines.append(f"| {r.problem_id} | {r.attempt_label} | {grade_str} | {summary} |")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Backend resolution (mirrors runner.py)
# ---------------------------------------------------------------------------

def _resolve_backend(
    config: PipelineConfig,
) -> BackendRouter:
    if config.backend == "demo" and config.config_path is None:
        return build_backend(
            config.backend, config.model, config.seed, workdir=Path.cwd()
        )

    config_file = find_config_file(
        explicit=config.config_path,
        search_dirs=[_GRADING_DIR, Path.cwd()],
    )
    if config_file is not None:
        file_config = load_config_file(config_file)
        validate_approved_backends(file_config)
        print(f"[info] Using config: {config_file}", file=sys.stderr)
        router, _ = build_backend_from_config(
            file_config, workdir=Path.cwd(), seed=config.seed,
        )
        return router

    return build_backend(
        config.backend, config.model, config.seed, workdir=Path.cwd()
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

_EXPORT_RE = __import__("re").compile(
    r'^export\s+([A-Za-z_][A-Za-z0-9_]*)=["\']?(.*?)["\']?\s*$'
)


def _load_secrets(*search_dirs: Path) -> None:
    import os
    for d in search_dirs:
        secrets = d / ".secrets"
        if secrets.is_file():
            for line in secrets.read_text(encoding="utf-8").splitlines():
                m = _EXPORT_RE.match(line)
                if m:
                    os.environ.setdefault(m.group(1), m.group(2))
            return


def _build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Grade external solution attempts using the reviewer pipeline."
    )
    parser.add_argument(
        "--problem",
        default=None,
        help="Problem number (1-10).",
    )
    parser.add_argument(
        "--attempt",
        default=None,
        help="Attempt label (e.g. oai5). Defaults to oai{problem}.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="grade_all",
        help="Grade all 10 OAI attempts.",
    )
    parser.add_argument(
        "--backend",
        default="codex",
        choices=["codex", "demo"],
        help="Agent backend (legacy). Ignored when --config is set.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Model name for legacy --backend mode.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Deterministic seed for compatible backends.",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to pipeline.toml config file.",
    )
    parser.add_argument(
        "--rigor",
        default="graduate",
        help="Rigor target label.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate prompt rendering only.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_argument_parser()
    args = parser.parse_args(argv)

    if not args.problem and not args.grade_all:
        parser.error("Either --problem or --all is required.")

    config = PipelineConfig(
        max_loops=1,
        rigor=args.rigor,
        backend=args.backend,
        model=args.model,
        seed=args.seed,
        config_path=args.config,
    )

    _load_secrets(_GRADING_DIR, Path.cwd())

    try:
        questions = load_questions()
    except FileNotFoundError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 2

    # Determine which problems to grade
    if args.grade_all:
        problem_ids = sorted(questions.keys(), key=int)
    else:
        problem_ids = [args.problem]

    # Dry run
    if args.dry_run:
        for pid in problem_ids:
            if pid not in questions:
                print(f"[error] Unknown problem: {pid}", file=sys.stderr)
                return 2
            attempt_label = args.attempt or default_attempt_label(pid)
            try:
                attempt_text = load_attempt(attempt_label)
            except FileNotFoundError as exc:
                print(f"[error] {exc}", file=sys.stderr)
                return 2
            dry_context = {
                "problem_id": pid,
                "question_text": questions[pid],
                "rigor": config.rigor,
                "loop_index": "1",
                "max_loops": "1",
                "prover_output": attempt_text,
                "mentor_output": "Not applicable.",
                "pool_description": "<dry-run pool>",
                "perspectives_description": "<dry-run perspectives>",
                "reviewer_name": "<dry-run reviewer>",
                "perspective_name": "<dry-run perspective>",
                "perspective_description": "<dry-run description>",
                "reviews_markdown": "<dry-run reviews>",
            }
            try:
                for role in ("editor_dispatch", "reviewer", "grader_decision"):
                    _ = render_prompt(role, dry_context)
            except Exception as exc:
                print(f"[error] Prompt rendering failed: {exc}", file=sys.stderr)
                return 2
        print(
            f"[ok] Dry run succeeded for {len(problem_ids)} problem(s)."
        )
        return 0

    # Real run
    try:
        backend = _resolve_backend(config)
    except (ValueError, RuntimeError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 3

    results: list[GradingRunResult] = []
    for pid in problem_ids:
        if pid not in questions:
            print(f"[error] Unknown problem: {pid}", file=sys.stderr)
            return 2
        attempt_label = args.attempt or default_attempt_label(pid)
        try:
            attempt_text = load_attempt(attempt_label)
        except FileNotFoundError as exc:
            print(f"[error] {exc}", file=sys.stderr)
            return 2

        try:
            result = run_grading(
                problem_id=pid,
                question_text=questions[pid],
                attempt_text=attempt_text,
                attempt_label=attempt_label,
                backend=backend,
                config=config,
            )
            results.append(result)
        except (OutputValidationError, ValueError, RuntimeError) as exc:
            print(f"[error] Problem {pid}: {exc}", file=sys.stderr)
            return 3

        print(f"[ok] Problem: {result.problem_id}")
        print(f"[ok] Attempt: {result.attempt_label}")
        print(f"[ok] Grade: {result.grading_decision.progress_grade}/4")
        print(f"[ok] Cost: {_cost_tracker.summary_line()}")
        print(f"[ok] Report: {result.report_path}")
        print(f"[ok] Transcript: {result.transcript_path}")
        print(f"[ok] Meta: {result.meta_path}")
        if len(problem_ids) > 1:
            print("---")

    # Overview for --all
    if args.grade_all and results:
        timestamp = format_timestamp(utc_now())
        overview_path = _RESULTS_DIR / f"{timestamp}-overview.md"
        overview_text = _build_overview(results)
        write_text(overview_path, overview_text)
        print(f"[ok] Overview: {overview_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
