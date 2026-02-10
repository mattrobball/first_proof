from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

Severity = Literal["critical", "major", "minor"]
EditorVerdict = Literal["accept", "right_track", "wrong_track", "reject"]


@dataclass(frozen=True)
class ProblemInputs:
    problem_id: str
    question_text: str
    background_text: str
    question_hash: str
    background_hash: str


@dataclass(frozen=True)
class ReviewerPerspective:
    name: str
    description: str


@dataclass(frozen=True)
class ReviewerIssue:
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
class ReviewerResult:
    reviewer_name: str
    perspective_name: str
    issues: list[ReviewerIssue]
    residual_concerns: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "reviewer_name": self.reviewer_name,
            "perspective_name": self.perspective_name,
            "issues": [issue.to_dict() for issue in self.issues],
            "residual_concerns": self.residual_concerns,
        }


@dataclass(frozen=True)
class EditorDispatch:
    assignments: dict[str, str]
    reasoning: str

    def to_dict(self) -> dict[str, object]:
        return {
            "assignments": self.assignments,
            "reasoning": self.reasoning,
        }


@dataclass(frozen=True)
class EditorDecision:
    verdict: EditorVerdict
    summary: str
    feedback: str
    feedback_target: str
    reviewer_results: list[ReviewerResult]

    def to_dict(self) -> dict[str, object]:
        return {
            "verdict": self.verdict,
            "summary": self.summary,
            "feedback": self.feedback,
            "feedback_target": self.feedback_target,
            "reviewer_results": [rr.to_dict() for rr in self.reviewer_results],
        }


@dataclass(frozen=True)
class LoopRecord:
    loop_index: int
    mentor_text: str
    prover_text: str
    editor_dispatch: EditorDispatch
    reviewer_texts: dict[str, str]
    editor_decision: EditorDecision


@dataclass(frozen=True)
class PipelineRunResult:
    problem_id: str
    started_at: str
    finished_at: str
    max_loops: int
    executed_loops: int
    final_verdict: EditorVerdict
    issue_counts: dict[str, int]
    researcher_text: str
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
            "researcher_text": self.researcher_text,
            "transcript_path": str(self.transcript_path),
            "meta_path": str(self.meta_path),
            "latex_path": str(self.latex_path),
            "loops": [
                {
                    "loop_index": loop.loop_index,
                    "editor_decision": loop.editor_decision.to_dict(),
                }
                for loop in self.loops
            ],
        }
