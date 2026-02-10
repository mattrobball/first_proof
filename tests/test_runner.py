from __future__ import annotations

import json
from pathlib import Path

from pipeline.backends import BackendRouter, DemoBackend
from pipeline.config import PipelineConfig
from pipeline.runner import run_pipeline


def _write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _statement() -> str:
    return """## Definitions
- Def 1

## Formal Statement
Prove X.

## Assumptions
- A1

## Notation
- N1
"""


def _sketch() -> str:
    return """## High-Level Strategy
Use lemmas.

## Key Lemmas
- L1

## Dependency Graph
L1 -> theorem.

## Risky Steps
- none
"""


def _prover() -> str:
    return """## Complete Proof
Proof body.

## Lemma Proofs
Lemma body.

## Gap Closure Notes
No gaps.
"""


def _reviewer_pass() -> str:
    return """## Review
No issues.

## Structured Review
```json
{
  "issues": [],
  "residual_concerns": []
}
```
"""


def _reviewer_fail() -> str:
    return """## Review
Issues found.

## Structured Review
```json
{
  "issues": [
    {
      "severity": "major",
      "location": "Complete Proof",
      "reason": "Missing justification.",
      "required_fix": "Add details.",
      "suggestion": "Break the argument into smaller steps."
    }
  ],
  "residual_concerns": []
}
```
"""


def _editor_dispatch(context: dict[str, str]) -> str:
    """Build a dispatch response that assigns all perspectives to default_reviewer."""
    import re
    persp_desc = context.get("perspectives_description", "")
    persp_names = re.findall(r"\d+\.\s+\*\*(.+?)\*\*", persp_desc)
    assignments = {p: "default_reviewer" for p in persp_names}
    payload = json.dumps(
        {"assignments": assignments, "reasoning": "Test dispatch."},
        indent=2,
    )
    return f"## Dispatch\n```json\n{payload}\n```\n"


def _editor_decision_accept() -> str:
    payload = json.dumps(
        {"verdict": "accept", "summary": "All good.", "feedback": ""},
        indent=2,
    )
    return f"## Decision\n```json\n{payload}\n```\n"


def _editor_decision_right_track() -> str:
    payload = json.dumps(
        {
            "verdict": "right_track",
            "summary": "Needs minor fixes.",
            "feedback": "Fix Lemma B derivation.",
        },
        indent=2,
    )
    return f"## Decision\n```json\n{payload}\n```\n"


def _editor_decision_wrong_track() -> str:
    payload = json.dumps(
        {
            "verdict": "wrong_track",
            "summary": "Fundamentally flawed approach.",
            "feedback": "Redesign the proof strategy entirely.",
        },
        indent=2,
    )
    return f"## Decision\n```json\n{payload}\n```\n"


class EditorAwareBackend:
    """Test backend that handles all new roles."""

    def __init__(
        self,
        reviewer_fn=None,
        decision_fn=None,
    ):
        self._reviewer_fn = reviewer_fn or (lambda ctx: _reviewer_pass())
        self._decision_fn = decision_fn or (lambda ctx: _editor_decision_accept())

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        if role == "statement":
            return _statement()
        if role == "sketch":
            return _sketch()
        if role == "prover":
            return _prover()
        if role == "editor_dispatch":
            return _editor_dispatch(context)
        if role == "reviewer":
            return self._reviewer_fn(context)
        if role == "editor_decision":
            return self._decision_fn(context)
        raise ValueError(role)


def _make_router(backend=None) -> BackendRouter:
    b = backend or EditorAwareBackend()
    return BackendRouter(
        role_backends={},
        default_backend=b,
        pool_backends={"default_reviewer": b},
    )


def _prepare_problem_dir(tmp_path: Path) -> Path:
    problem_dir = tmp_path / "5"
    problem_dir.mkdir()
    _write(problem_dir / "QUESTION.md", "Prove X.")
    _write(problem_dir / "BACKGROUND.md", "Assume A1.")
    return problem_dir


def test_stops_early_on_accept(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=5, out_dir_name="runs")
    result = run_pipeline(problem_dir, config, _make_router())

    assert result.final_verdict == "accept"
    assert result.executed_loops == 1
    assert result.transcript_path.exists()
    assert result.meta_path.exists()
    assert result.latex_path.exists()


def test_right_track_feeds_back_to_prover(tmp_path: Path) -> None:
    """right_track should feed back to prover, reusing the previous sketch."""
    call_count = {"n": 0}

    def decision_fn(ctx):
        call_count["n"] += 1
        if call_count["n"] == 1:
            return _editor_decision_right_track()
        return _editor_decision_accept()

    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=5, out_dir_name="runs")
    backend = EditorAwareBackend(decision_fn=decision_fn)
    result = run_pipeline(problem_dir, config, _make_router(backend))

    assert result.final_verdict == "accept"
    assert result.executed_loops == 2
    # Loop 2 should reuse loop 1's sketch (right_track -> prover)
    assert result.loops[1].sketch_text == result.loops[0].sketch_text


def test_wrong_track_feeds_back_to_sketch(tmp_path: Path) -> None:
    """wrong_track should cause the sketch agent to regenerate."""
    call_count = {"n": 0}

    def decision_fn(ctx):
        call_count["n"] += 1
        if call_count["n"] == 1:
            return _editor_decision_wrong_track()
        return _editor_decision_accept()

    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=5, out_dir_name="runs")
    backend = EditorAwareBackend(decision_fn=decision_fn)
    result = run_pipeline(problem_dir, config, _make_router(backend))

    assert result.final_verdict == "accept"
    assert result.executed_loops == 2
    # Loop 1 verdict should be wrong_track
    assert result.loops[0].editor_decision.verdict == "wrong_track"
    assert result.loops[0].editor_decision.feedback_target == "sketch"


def test_stops_at_max_loops_on_right_track(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=3, out_dir_name="runs")
    backend = EditorAwareBackend(
        reviewer_fn=lambda ctx: _reviewer_fail(),
        decision_fn=lambda ctx: _editor_decision_right_track(),
    )
    result = run_pipeline(problem_dir, config, _make_router(backend))

    assert result.final_verdict == "right_track"
    assert result.executed_loops == 3


def test_transcript_and_meta_content(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=2, out_dir_name="runs")
    result = run_pipeline(problem_dir, config, _make_router())

    transcript = result.transcript_path.read_text(encoding="utf-8")
    assert "# Proof Pipeline Transcript" in transcript
    assert "## Loop 1" in transcript
    assert "Pipeline finished with verdict: `accept`." in transcript
    assert "Editor Dispatch" in transcript
    assert "Editor Decision" in transcript

    meta = json.loads(result.meta_path.read_text(encoding="utf-8"))
    assert meta["problem_id"] == "5"
    assert meta["final_verdict"] == "accept"
    assert "input_hashes" in meta


def test_editor_decision_in_meta(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=2, out_dir_name="runs")
    result = run_pipeline(problem_dir, config, _make_router())

    meta = json.loads(result.meta_path.read_text(encoding="utf-8"))
    loop_meta = meta["loops"][0]
    decision = loop_meta["editor_decision"]
    assert decision["verdict"] == "accept"
    assert isinstance(decision["reviewer_results"], list)
    assert len(decision["reviewer_results"]) == 3  # default 3 perspectives


def test_reviewer_results_recorded(tmp_path: Path) -> None:
    """Each reviewer result should have the correct perspective_name."""
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=1, out_dir_name="runs")
    backend = EditorAwareBackend(
        reviewer_fn=lambda ctx: _reviewer_fail(),
        decision_fn=lambda ctx: _editor_decision_right_track(),
    )
    result = run_pipeline(problem_dir, config, _make_router(backend))

    decision = result.loops[0].editor_decision
    perspective_names = [rr.perspective_name for rr in decision.reviewer_results]
    assert "Correctness & Completeness" in perspective_names
    assert "Clarity & Rigor" in perspective_names
    assert "Reference Validity" in perspective_names
    for rr in decision.reviewer_results:
        assert len(rr.issues) > 0
        for issue in rr.issues:
            assert issue.suggestion


def test_latex_output_generated(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=2, out_dir_name="runs")
    result = run_pipeline(problem_dir, config, _make_router())

    assert result.latex_path.exists()
    latex = result.latex_path.read_text(encoding="utf-8")
    assert r"\documentclass" in latex
    assert r"\begin{document}" in latex
    assert r"\end{document}" in latex
    assert "Proof Pipeline Report" in latex
    assert "Editor Dispatch" in latex
    assert "Editor Decision" in latex
    assert "Reviewer Feedback" in latex


def test_latex_contains_suggestions_on_fail(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=1, out_dir_name="runs")
    backend = EditorAwareBackend(
        reviewer_fn=lambda ctx: _reviewer_fail(),
        decision_fn=lambda ctx: _editor_decision_right_track(),
    )
    result = run_pipeline(problem_dir, config, _make_router(backend))

    latex = result.latex_path.read_text(encoding="utf-8")
    assert "Suggestion" in latex
    assert "Required fix" in latex


def test_demo_backend_full_run(tmp_path: Path) -> None:
    """The DemoBackend should complete a full run with the editor flow."""
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=5, out_dir_name="runs")
    demo = DemoBackend()
    router = BackendRouter(
        role_backends={},
        default_backend=demo,
        pool_backends={"default_reviewer": demo},
    )
    result = run_pipeline(problem_dir, config, router)

    assert result.final_verdict == "accept"
    assert result.executed_loops == 2
