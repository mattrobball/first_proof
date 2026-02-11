from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

Severity = Literal["critical", "major", "minor"]
EditorVerdict = Literal["accept", "right_track", "wrong_track"]


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

    @classmethod
    def from_dict(cls, d: dict[str, object]) -> ReviewerIssue:
        return cls(
            severity=d["severity"],  # type: ignore[arg-type]
            location=str(d["location"]),
            reason=str(d["reason"]),
            required_fix=str(d["required_fix"]),
            suggestion=str(d["suggestion"]),
        )


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

    @classmethod
    def from_dict(cls, d: dict[str, object]) -> ReviewerResult:
        return cls(
            reviewer_name=str(d["reviewer_name"]),
            perspective_name=str(d["perspective_name"]),
            issues=[ReviewerIssue.from_dict(i) for i in d["issues"]],  # type: ignore[union-attr]
            residual_concerns=list(d.get("residual_concerns") or []),  # type: ignore[arg-type]
        )


@dataclass(frozen=True)
class EditorDispatch:
    assignments: dict[str, str]
    reasoning: str

    def to_dict(self) -> dict[str, object]:
        return {
            "assignments": self.assignments,
            "reasoning": self.reasoning,
        }

    @classmethod
    def from_dict(cls, d: dict[str, object]) -> EditorDispatch:
        return cls(
            assignments=dict(d["assignments"]),  # type: ignore[arg-type]
            reasoning=str(d["reasoning"]),
        )


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

    @classmethod
    def from_dict(cls, d: dict[str, object]) -> EditorDecision:
        return cls(
            verdict=d["verdict"],  # type: ignore[arg-type]
            summary=str(d["summary"]),
            feedback=str(d["feedback"]),
            feedback_target=str(d.get("feedback_target", "")),
            reviewer_results=[
                ReviewerResult.from_dict(rr)  # type: ignore[arg-type]
                for rr in d["reviewer_results"]  # type: ignore[union-attr]
            ],
        )


@dataclass(frozen=True)
class LoopRecord:
    loop_index: int
    researcher_text: str
    mentor_text: str
    prover_text: str
    editor_dispatch: EditorDispatch
    reviewer_texts: dict[str, str]
    editor_decision: EditorDecision

    def to_dict(self) -> dict[str, object]:
        return {
            "loop_index": self.loop_index,
            "researcher_text": self.researcher_text,
            "mentor_text": self.mentor_text,
            "prover_text": self.prover_text,
            "editor_dispatch": self.editor_dispatch.to_dict(),
            "reviewer_texts": self.reviewer_texts,
            "editor_decision": self.editor_decision.to_dict(),
        }

    @classmethod
    def from_dict(cls, d: dict[str, object]) -> LoopRecord:
        return cls(
            loop_index=int(d["loop_index"]),  # type: ignore[arg-type]
            researcher_text=str(d["researcher_text"]),
            mentor_text=str(d["mentor_text"]),
            prover_text=str(d["prover_text"]),
            editor_dispatch=EditorDispatch.from_dict(d["editor_dispatch"]),  # type: ignore[arg-type]
            reviewer_texts=dict(d["reviewer_texts"]),  # type: ignore[arg-type]
            editor_decision=EditorDecision.from_dict(d["editor_decision"]),  # type: ignore[arg-type]
        )


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
