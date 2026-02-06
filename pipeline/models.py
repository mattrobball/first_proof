from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

Severity = Literal["critical", "major", "minor"]
Verdict = Literal["PASS", "FAIL"]


@dataclass(frozen=True)
class ProblemInputs:
    problem_id: str
    question_text: str
    background_text: str
    question_hash: str
    background_hash: str


@dataclass(frozen=True)
class CriticIssue:
    severity: Severity
    location: str
    reason: str
    required_fix: str

    def to_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "location": self.location,
            "reason": self.reason,
            "required_fix": self.required_fix,
        }


@dataclass(frozen=True)
class CriticResult:
    verdict: Verdict
    issues: list[CriticIssue]
    residual_concerns: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "verdict": self.verdict,
            "issues": [issue.to_dict() for issue in self.issues],
            "residual_concerns": self.residual_concerns,
        }


@dataclass(frozen=True)
class LoopRecord:
    loop_index: int
    statement_text: str
    sketch_text: str
    prover_text: str
    critic_text: str
    critic_result: CriticResult


@dataclass(frozen=True)
class PipelineRunResult:
    problem_id: str
    started_at: str
    finished_at: str
    max_loops: int
    executed_loops: int
    final_verdict: Verdict
    issue_counts: dict[str, int]
    loops: list[LoopRecord]
    transcript_path: Path
    meta_path: Path

    def to_meta_dict(self) -> dict[str, object]:
        return {
            "problem_id": self.problem_id,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "max_loops": self.max_loops,
            "executed_loops": self.executed_loops,
            "final_verdict": self.final_verdict,
            "issue_counts": self.issue_counts,
            "transcript_path": str(self.transcript_path),
            "meta_path": str(self.meta_path),
            "loops": [
                {
                    "loop_index": loop.loop_index,
                    "critic_result": loop.critic_result.to_dict(),
                }
                for loop in self.loops
            ],
        }
