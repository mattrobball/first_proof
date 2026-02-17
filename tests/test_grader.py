"""Tests for the grading pipeline."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from pipeline.backends import BackendRouter, DemoBackend
from pipeline.config import PipelineConfig
from pipeline.grader import (
    default_attempt_label,
    load_attempt,
    load_questions,
    run_grading,
    _build_grading_report,
    _build_overview,
)
from pipeline.grading_models import GradingDecision, GradingIndicators, GradingRunResult
from pipeline.models import ReviewerResult
from pipeline.validate import (
    OutputValidationError,
    parse_grading_decision_output,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _demo_backend() -> BackendRouter:
    demo = DemoBackend()
    return BackendRouter(
        role_backends={},
        default_backend=demo,
        pool_backends={"default_reviewer": demo},
    )


def _default_config() -> PipelineConfig:
    return PipelineConfig(max_loops=1, rigor="graduate", backend="demo")


# ---------------------------------------------------------------------------
# Unit: parse_grading_decision_output
# ---------------------------------------------------------------------------

def test_parse_grading_decision_valid() -> None:
    text = """
## Analysis
Some analysis here.

```json
{
  "progress_grade": 3,
  "error_incorrect_logic": "false",
  "error_hallucinated": "false",
  "error_calculation": "false",
  "error_conceptual": "false",
  "achievement_understanding": "true",
  "achievement_correct_result": "true",
  "achievement_insight": "true",
  "achievement_usefulness": "true",
  "short_summary": "Nearly complete proof with minor gap."
}
```
"""
    result = parse_grading_decision_output(text, [])
    assert result.progress_grade == 3
    assert result.indicators.error_incorrect_logic == "false"
    assert result.indicators.achievement_understanding == "true"
    assert result.short_summary == "Nearly complete proof with minor gap."


def test_parse_grading_decision_not_applicable() -> None:
    text = """
```json
{
  "progress_grade": 1,
  "error_incorrect_logic": "true",
  "error_hallucinated": "not_sure",
  "error_calculation": "false",
  "error_conceptual": "false",
  "achievement_understanding": "true",
  "achievement_correct_result": "not_applicable",
  "achievement_insight": "false",
  "achievement_usefulness": "false",
  "short_summary": "Minor progress with logical errors."
}
```
"""
    result = parse_grading_decision_output(text, [])
    assert result.progress_grade == 1
    assert result.indicators.achievement_correct_result == "not_applicable"


def test_parse_grading_decision_invalid_grade() -> None:
    text = """
```json
{
  "progress_grade": 5,
  "error_incorrect_logic": "false",
  "error_hallucinated": "false",
  "error_calculation": "false",
  "error_conceptual": "false",
  "achievement_understanding": "true",
  "achievement_correct_result": "true",
  "achievement_insight": "true",
  "achievement_usefulness": "true",
  "short_summary": "Bad grade."
}
```
"""
    with pytest.raises(OutputValidationError, match="progress_grade"):
        parse_grading_decision_output(text, [])


def test_parse_grading_decision_invalid_tri_state() -> None:
    text = """
```json
{
  "progress_grade": 2,
  "error_incorrect_logic": "yes",
  "error_hallucinated": "false",
  "error_calculation": "false",
  "error_conceptual": "false",
  "achievement_understanding": "true",
  "achievement_correct_result": "true",
  "achievement_insight": "true",
  "achievement_usefulness": "true",
  "short_summary": "Invalid value."
}
```
"""
    with pytest.raises(OutputValidationError, match="error_incorrect_logic"):
        parse_grading_decision_output(text, [])


def test_parse_grading_decision_empty_summary() -> None:
    text = """
```json
{
  "progress_grade": 2,
  "error_incorrect_logic": "false",
  "error_hallucinated": "false",
  "error_calculation": "false",
  "error_conceptual": "false",
  "achievement_understanding": "true",
  "achievement_correct_result": "true",
  "achievement_insight": "true",
  "achievement_usefulness": "true",
  "short_summary": ""
}
```
"""
    with pytest.raises(OutputValidationError, match="short_summary"):
        parse_grading_decision_output(text, [])


def test_parse_grading_decision_no_json() -> None:
    text = "No JSON block here."
    with pytest.raises(OutputValidationError, match="missing fenced JSON"):
        parse_grading_decision_output(text, [])


# ---------------------------------------------------------------------------
# Unit: grading_models serialization
# ---------------------------------------------------------------------------

def test_grading_decision_roundtrip() -> None:
    indicators = GradingIndicators(
        error_incorrect_logic="true",
        error_hallucinated="false",
        error_calculation="not_sure",
        error_conceptual="false",
        achievement_understanding="true",
        achievement_correct_result="not_applicable",
        achievement_insight="true",
        achievement_usefulness="false",
    )
    decision = GradingDecision(
        progress_grade=2,
        indicators=indicators,
        short_summary="Test summary.",
        reviewer_results=[],
    )
    d = decision.to_dict()
    restored = GradingDecision.from_dict(d)
    assert restored.progress_grade == 2
    assert restored.indicators.error_incorrect_logic == "true"
    assert restored.indicators.achievement_correct_result == "not_applicable"
    assert restored.short_summary == "Test summary."


# ---------------------------------------------------------------------------
# Unit: helper functions
# ---------------------------------------------------------------------------

def test_default_attempt_label() -> None:
    assert default_attempt_label("5") == "oai5"
    assert default_attempt_label("10") == "oai10"


def test_load_questions() -> None:
    questions = load_questions()
    assert len(questions) == 10
    assert "1" in questions
    assert "10" in questions


def test_load_attempt() -> None:
    text = load_attempt("oai1")
    assert len(text) > 100


def test_load_attempt_missing() -> None:
    with pytest.raises(FileNotFoundError):
        load_attempt("nonexistent_attempt")


# ---------------------------------------------------------------------------
# Integration: run_grading with DemoBackend
# ---------------------------------------------------------------------------

def test_run_grading_demo(tmp_path: Path) -> None:
    """Full grading run with the deterministic demo backend."""
    import pipeline.grader as grader_mod

    # Temporarily redirect results dir
    orig_results_dir = grader_mod._RESULTS_DIR
    grader_mod._RESULTS_DIR = tmp_path

    try:
        questions = load_questions()
        attempt_text = load_attempt("oai5")
        backend = _demo_backend()
        config = _default_config()

        result = run_grading(
            problem_id="5",
            question_text=questions["5"],
            attempt_text=attempt_text,
            attempt_label="oai5",
            backend=backend,
            config=config,
        )
    finally:
        grader_mod._RESULTS_DIR = orig_results_dir

    assert result.problem_id == "5"
    assert result.attempt_label == "oai5"
    assert result.grading_decision.progress_grade == 2
    assert result.grading_decision.indicators.error_incorrect_logic == "true"
    assert result.grading_decision.indicators.achievement_understanding == "true"
    assert result.transcript_path.exists()
    assert result.meta_path.exists()
    assert result.report_path.exists()

    # Verify meta is valid JSON
    meta = json.loads(result.meta_path.read_text())
    assert meta["problem_id"] == "5"
    assert meta["grading_decision"]["progress_grade"] == 2


# ---------------------------------------------------------------------------
# Integration: CLI dry-run
# ---------------------------------------------------------------------------

def test_cli_dry_run() -> None:
    from pipeline.grader import main
    assert main(["--problem", "5", "--dry-run"]) == 0


def test_cli_dry_run_all() -> None:
    from pipeline.grader import main
    assert main(["--all", "--dry-run"]) == 0


def test_cli_demo(tmp_path: Path) -> None:
    import pipeline.grader as grader_mod
    orig_results_dir = grader_mod._RESULTS_DIR
    grader_mod._RESULTS_DIR = tmp_path
    try:
        from pipeline.grader import main
        rc = main(["--problem", "3", "--backend", "demo"])
    finally:
        grader_mod._RESULTS_DIR = orig_results_dir
    assert rc == 0


def test_cli_no_args() -> None:
    from pipeline.grader import main
    with pytest.raises(SystemExit):
        main([])


# ---------------------------------------------------------------------------
# Unit: report/overview builders
# ---------------------------------------------------------------------------

def test_build_grading_report() -> None:
    indicators = GradingIndicators(
        error_incorrect_logic="true",
        error_hallucinated="false",
        error_calculation="false",
        error_conceptual="false",
        achievement_understanding="true",
        achievement_correct_result="not_sure",
        achievement_insight="true",
        achievement_usefulness="true",
    )
    decision = GradingDecision(
        progress_grade=2,
        indicators=indicators,
        short_summary="Test summary for report.",
        reviewer_results=[],
    )
    report = _build_grading_report("5", "oai5", decision)
    assert "# Grading Report: oai5" in report
    assert "2/4" in report
    assert "Test summary for report." in report
    assert "Incorrect Logic | true" in report


def test_build_overview() -> None:
    indicators = GradingIndicators(
        error_incorrect_logic="false",
        error_hallucinated="false",
        error_calculation="false",
        error_conceptual="false",
        achievement_understanding="true",
        achievement_correct_result="true",
        achievement_insight="true",
        achievement_usefulness="true",
    )
    decision = GradingDecision(
        progress_grade=4,
        indicators=indicators,
        short_summary="Complete solution.",
        reviewer_results=[],
    )
    result = GradingRunResult(
        problem_id="1",
        attempt_label="oai1",
        started_at="2026-01-01T00:00:00+00:00",
        finished_at="2026-01-01T00:01:00+00:00",
        grading_decision=decision,
        transcript_path=Path("/tmp/t.md"),
        meta_path=Path("/tmp/m.json"),
        report_path=Path("/tmp/r.md"),
    )
    overview = _build_overview([result])
    assert "# Grading Overview" in overview
    assert "4/4" in overview
    assert "Complete solution." in overview
