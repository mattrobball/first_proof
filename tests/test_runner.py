from __future__ import annotations

import json
from pathlib import Path

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


def _critic_pass() -> str:
    return """## Verdict
PASS

## Structured Verdict
```json
{
  "verdict": "PASS",
  "issues": [],
  "residual_concerns": []
}
```
"""


def _critic_fail() -> str:
    return """## Verdict
FAIL

## Structured Verdict
```json
{
  "verdict": "FAIL",
  "issues": [
    {
      "severity": "major",
      "location": "Complete Proof",
      "reason": "Missing justification.",
      "required_fix": "Add details."
    }
  ],
  "residual_concerns": []
}
```
"""


class AlwaysPassBackend:
    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        if role == "statement":
            return _statement()
        if role == "sketch":
            return _sketch()
        if role == "prover":
            return _prover()
        if role == "critic":
            return _critic_pass()
        raise ValueError(role)


class AlwaysFailBackend:
    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        if role == "statement":
            return _statement()
        if role == "sketch":
            return _sketch()
        if role == "prover":
            return _prover()
        if role == "critic":
            return _critic_fail()
        raise ValueError(role)


def _prepare_problem_dir(tmp_path: Path) -> Path:
    problem_dir = tmp_path / "5"
    problem_dir.mkdir()
    _write(problem_dir / "QUESTION.md", "Prove X.")
    _write(problem_dir / "BACKGROUND.md", "Assume A1.")
    return problem_dir


def test_stops_early_on_pass(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=5, out_dir_name="runs")
    result = run_pipeline(problem_dir, config, AlwaysPassBackend())

    assert result.final_verdict == "PASS"
    assert result.executed_loops == 1
    assert result.transcript_path.exists()
    assert result.meta_path.exists()


def test_stops_at_max_loops_on_fail(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=3, out_dir_name="runs")
    result = run_pipeline(problem_dir, config, AlwaysFailBackend())

    assert result.final_verdict == "FAIL"
    assert result.executed_loops == 3


def test_transcript_and_meta_content(tmp_path: Path) -> None:
    problem_dir = _prepare_problem_dir(tmp_path)
    config = PipelineConfig(max_loops=2, out_dir_name="runs")
    result = run_pipeline(problem_dir, config, AlwaysPassBackend())

    transcript = result.transcript_path.read_text(encoding="utf-8")
    assert "# Proof Pipeline Transcript" in transcript
    assert "## Loop 1" in transcript
    assert "Pipeline finished with verdict: `PASS`." in transcript

    meta = json.loads(result.meta_path.read_text(encoding="utf-8"))
    assert meta["problem_id"] == "5"
    assert meta["final_verdict"] == "PASS"
    assert "input_hashes" in meta
