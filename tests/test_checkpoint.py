from __future__ import annotations

import json
from pathlib import Path

from pipeline.backends import BackendRouter
from pipeline.checkpoint import (
    CheckpointData,
    load_checkpoint,
    validate_checkpoint_inputs,
    write_checkpoint,
)
from pipeline.config import PipelineConfig
from pipeline.models import (
    EditorDecision,
    EditorDispatch,
    LoopRecord,
    ReviewerIssue,
    ReviewerResult,
)
from pipeline.runner import run_pipeline

# Re-use the test helpers from test_runner
from tests.test_runner import (
    EditorAwareBackend,
    _editor_decision_accept,
    _editor_decision_right_track,
    _make_router,
    _prepare_problem_dir,
    _reviewer_fail,
)


def _sample_loop(loop_index: int = 1) -> LoopRecord:
    issue = ReviewerIssue(
        severity="major",
        location="Lemma 1",
        reason="Gap in reasoning",
        required_fix="Add justification",
        suggestion="Use induction",
    )
    rr = ReviewerResult(
        reviewer_name="pool_a",
        perspective_name="Correctness & Completeness",
        issues=[issue],
        residual_concerns=["Check edge case"],
    )
    dispatch = EditorDispatch(
        assignments={"Correctness & Completeness": "pool_a"},
        reasoning="Best match",
    )
    decision = EditorDecision(
        verdict="right_track",
        summary="Needs minor fixes.",
        feedback="Fix Lemma 1.",
        feedback_target="prover",
        reviewer_results=[rr],
    )
    return LoopRecord(
        loop_index=loop_index,
        researcher_text="## Relevant Theorems\n- T1\n",
        mentor_text="## Definitions\n- D1\n",
        prover_text="## Complete Proof\nProof.\n",
        editor_dispatch=dispatch,
        reviewer_texts={"Correctness & Completeness": "Review text."},
        editor_decision=decision,
    )


# --- Round-trip serialization tests ---


def test_loop_record_round_trip() -> None:
    loop = _sample_loop()
    d = loop.to_dict()
    restored = LoopRecord.from_dict(d)
    assert restored.loop_index == loop.loop_index
    assert restored.researcher_text == loop.researcher_text
    assert restored.mentor_text == loop.mentor_text
    assert restored.prover_text == loop.prover_text
    assert restored.reviewer_texts == loop.reviewer_texts
    assert restored.editor_dispatch.assignments == loop.editor_dispatch.assignments
    assert restored.editor_decision.verdict == loop.editor_decision.verdict
    assert len(restored.editor_decision.reviewer_results) == 1
    rr = restored.editor_decision.reviewer_results[0]
    assert rr.issues[0].severity == "major"
    assert rr.residual_concerns == ["Check edge case"]


def test_loop_record_json_round_trip() -> None:
    """Serialize to JSON string and back."""
    loop = _sample_loop()
    text = json.dumps(loop.to_dict())
    restored = LoopRecord.from_dict(json.loads(text))
    assert restored == loop


def test_checkpoint_write_and_load(tmp_path: Path) -> None:
    loop = _sample_loop()
    hashes = {"question_sha256": "abc123", "background_sha256": "def456"}
    cp_path = write_checkpoint(
        out_dir=tmp_path,
        timestamp="20260101-120000",
        problem_id="5",
        started_at="2026-01-01T12:00:00+00:00",
        max_loops=5,
        input_hashes=hashes,
        loops=[loop],
        editor_feedback="Fix Lemma 1.",
        feedback_target="prover",
    )
    assert cp_path.exists()
    assert cp_path.name == "20260101-120000-checkpoint.json"

    loaded = load_checkpoint(cp_path)
    assert loaded.problem_id == "5"
    assert loaded.started_at == "2026-01-01T12:00:00+00:00"
    assert loaded.timestamp == "20260101-120000"
    assert loaded.max_loops == 5
    assert loaded.input_hashes == hashes
    assert len(loaded.loops) == 1
    assert loaded.loops[0] == loop
    assert loaded.editor_feedback == "Fix Lemma 1."
    assert loaded.feedback_target == "prover"


def test_checkpoint_version_mismatch(tmp_path: Path) -> None:
    bad = {"version": 999, "problem_id": "5"}
    path = tmp_path / "bad-checkpoint.json"
    path.write_text(json.dumps(bad), encoding="utf-8")
    try:
        load_checkpoint(path)
        assert False, "Should have raised ValueError"
    except ValueError as exc:
        assert "version" in str(exc).lower()


# --- Hash validation tests ---


def test_validate_checkpoint_inputs_ok() -> None:
    loop = _sample_loop()
    cp = CheckpointData(
        problem_id="5",
        started_at="2026-01-01T12:00:00+00:00",
        timestamp="20260101-120000",
        max_loops=5,
        input_hashes={"question_sha256": "aaa", "background_sha256": "bbb"},
        loops=[loop],
        editor_feedback="None.",
        feedback_target="",
    )
    # Should not raise
    validate_checkpoint_inputs(cp, "aaa", "bbb")


def test_validate_checkpoint_inputs_question_changed() -> None:
    cp = CheckpointData(
        problem_id="5",
        started_at="",
        timestamp="",
        max_loops=5,
        input_hashes={"question_sha256": "aaa", "background_sha256": "bbb"},
        loops=[],
        editor_feedback="None.",
        feedback_target="",
    )
    try:
        validate_checkpoint_inputs(cp, "CHANGED", "bbb")
        assert False, "Should have raised ValueError"
    except ValueError as exc:
        assert "QUESTION.md" in str(exc)


def test_validate_checkpoint_inputs_background_changed() -> None:
    cp = CheckpointData(
        problem_id="5",
        started_at="",
        timestamp="",
        max_loops=5,
        input_hashes={"question_sha256": "aaa", "background_sha256": "bbb"},
        loops=[],
        editor_feedback="None.",
        feedback_target="",
    )
    try:
        validate_checkpoint_inputs(cp, "aaa", "CHANGED")
        assert False, "Should have raised ValueError"
    except ValueError as exc:
        assert "BACKGROUND.md" in str(exc)


# --- Resume integration tests ---


def test_pipeline_creates_checkpoint(tmp_path: Path) -> None:
    """A normal pipeline run should create a checkpoint file."""
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=5, out_dir_name="runs")
    result = run_pipeline(problem_dir, config, _make_router())

    runs_dir = problem_dir / "runs"
    checkpoints = list(runs_dir.glob("*-checkpoint.json"))
    assert len(checkpoints) == 1
    cp = load_checkpoint(checkpoints[0])
    assert len(cp.loops) == result.executed_loops


def test_resume_skips_completed_loops(tmp_path: Path) -> None:
    """Resuming should skip already-completed loops."""
    call_count = {"n": 0}

    def decision_fn(ctx):
        call_count["n"] += 1
        if call_count["n"] <= 2:
            return _editor_decision_right_track()
        return _editor_decision_accept()

    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=5, out_dir_name="runs")
    backend = EditorAwareBackend(
        reviewer_fn=lambda ctx: _reviewer_fail(),
        decision_fn=decision_fn,
    )
    router = _make_router(backend)

    # Run first: will do 3 loops (2 right_track + 1 accept)
    result1 = run_pipeline(problem_dir, config, router)
    assert result1.executed_loops == 3
    assert result1.final_verdict == "accept"

    # Now simulate a crash after loop 2 by loading the checkpoint,
    # then building a new one with only the first 2 loops
    checkpoints = list((problem_dir / "runs").glob("*-checkpoint.json"))
    full_cp = load_checkpoint(checkpoints[0])
    # Truncate to first 2 loops to simulate crash before loop 3
    partial_cp = CheckpointData(
        problem_id=full_cp.problem_id,
        started_at=full_cp.started_at,
        timestamp=full_cp.timestamp,
        max_loops=full_cp.max_loops,
        input_hashes=full_cp.input_hashes,
        loops=full_cp.loops[:2],
        editor_feedback="Fix Lemma B derivation.",
        feedback_target="prover",
    )

    # Reset decision counter so next call accepts
    call_count["n"] = 2
    result2 = run_pipeline(
        problem_dir, config, router, resume_checkpoint=partial_cp
    )
    # Should have 3 total loops: 2 restored + 1 new
    assert result2.executed_loops == 3
    assert result2.final_verdict == "accept"
    # The first two loops should be the originals
    assert result2.loops[0].loop_index == 1
    assert result2.loops[1].loop_index == 2
    assert result2.loops[2].loop_index == 3
