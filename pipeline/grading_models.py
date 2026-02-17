from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from .models import ReviewerResult

TriState = Literal["true", "false", "not_sure"]
TriStatePlus = Literal["true", "false", "not_sure", "not_applicable"]


@dataclass(frozen=True)
class GradingIndicators:
    error_incorrect_logic: TriState
    error_hallucinated: TriState
    error_calculation: TriState
    error_conceptual: TriState
    achievement_understanding: TriState
    achievement_correct_result: TriStatePlus
    achievement_insight: TriState
    achievement_usefulness: TriState

    def to_dict(self) -> dict[str, str]:
        return {
            "error_incorrect_logic": self.error_incorrect_logic,
            "error_hallucinated": self.error_hallucinated,
            "error_calculation": self.error_calculation,
            "error_conceptual": self.error_conceptual,
            "achievement_understanding": self.achievement_understanding,
            "achievement_correct_result": self.achievement_correct_result,
            "achievement_insight": self.achievement_insight,
            "achievement_usefulness": self.achievement_usefulness,
        }

    @classmethod
    def from_dict(cls, d: dict[str, object]) -> GradingIndicators:
        return cls(
            error_incorrect_logic=str(d["error_incorrect_logic"]),  # type: ignore[arg-type]
            error_hallucinated=str(d["error_hallucinated"]),  # type: ignore[arg-type]
            error_calculation=str(d["error_calculation"]),  # type: ignore[arg-type]
            error_conceptual=str(d["error_conceptual"]),  # type: ignore[arg-type]
            achievement_understanding=str(d["achievement_understanding"]),  # type: ignore[arg-type]
            achievement_correct_result=str(d["achievement_correct_result"]),  # type: ignore[arg-type]
            achievement_insight=str(d["achievement_insight"]),  # type: ignore[arg-type]
            achievement_usefulness=str(d["achievement_usefulness"]),  # type: ignore[arg-type]
        )


@dataclass(frozen=True)
class GradingDecision:
    progress_grade: int
    indicators: GradingIndicators
    short_summary: str
    reviewer_results: list[ReviewerResult]

    def to_dict(self) -> dict[str, object]:
        return {
            "progress_grade": self.progress_grade,
            "indicators": self.indicators.to_dict(),
            "short_summary": self.short_summary,
            "reviewer_results": [rr.to_dict() for rr in self.reviewer_results],
        }

    @classmethod
    def from_dict(cls, d: dict[str, object]) -> GradingDecision:
        return cls(
            progress_grade=int(d["progress_grade"]),  # type: ignore[arg-type]
            indicators=GradingIndicators.from_dict(d["indicators"]),  # type: ignore[arg-type]
            short_summary=str(d["short_summary"]),
            reviewer_results=[
                ReviewerResult.from_dict(rr)  # type: ignore[arg-type]
                for rr in d["reviewer_results"]  # type: ignore[union-attr]
            ],
        )


@dataclass(frozen=True)
class GradingRunResult:
    problem_id: str
    attempt_label: str
    started_at: str
    finished_at: str
    grading_decision: GradingDecision
    transcript_path: Path
    meta_path: Path
    report_path: Path

    def to_meta_dict(self) -> dict[str, object]:
        return {
            "problem_id": self.problem_id,
            "attempt_label": self.attempt_label,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "grading_decision": self.grading_decision.to_dict(),
            "transcript_path": str(self.transcript_path),
            "meta_path": str(self.meta_path),
            "report_path": str(self.report_path),
        }
