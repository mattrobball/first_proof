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
class CriticPerspective:
    name: str
    description: str


@dataclass(frozen=True)
class CriticIssue:
    severity: Severity
    location: str
    reason: str
    required_fix: str
    suggestion: str

    def to_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "location": self.location,
            "reason": self.reason,
            "required_fix": self.required_fix,
            "suggestion": self.suggestion,
        }


@dataclass(frozen=True)
class CriticResult:
    critic_name: str
    verdict: Verdict
    issues: list[CriticIssue]
    residual_concerns: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "critic_name": self.critic_name,
            "verdict": self.verdict,
            "issues": [issue.to_dict() for issue in self.issues],
            "residual_concerns": self.residual_concerns,
        }


@dataclass(frozen=True)
class CouncilResult:
    """Aggregated result from all critics in the council."""

    verdicts: list[CriticResult]

    @property
    def overall_verdict(self) -> Verdict:
        if all(cr.verdict == "PASS" for cr in self.verdicts):
            return "PASS"
        return "FAIL"

    @property
    def all_issues(self) -> list[CriticIssue]:
        issues: list[CriticIssue] = []
        for cr in self.verdicts:
            issues.extend(cr.issues)
        return issues

    def to_dict(self) -> dict[str, object]:
        return {
            "overall_verdict": self.overall_verdict,
            "critics": [cr.to_dict() for cr in self.verdicts],
        }


@dataclass(frozen=True)
class LoopRecord:
    loop_index: int
    statement_text: str
    sketch_text: str
    prover_text: str
    critic_texts: dict[str, str]
    council_result: CouncilResult


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
    latex_path: Path

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
            "latex_path": str(self.latex_path),
            "loops": [
                {
                    "loop_index": loop.loop_index,
                    "council_result": loop.council_result.to_dict(),
                }
                for loop in self.loops
            ],
        }
