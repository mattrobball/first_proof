from __future__ import annotations

from dataclasses import dataclass, field

from .models import ReviewerPerspective

DEFAULT_REVIEWER_PERSPECTIVES: list[ReviewerPerspective] = [
    ReviewerPerspective(
        name="Correctness & Completeness",
        description=(
            "Focus on the validity of logical inferences, correct application "
            "of proof techniques, soundness of deductions, mathematical gaps, "
            "missing lemmas, unstated assumptions, and incomplete case analysis. "
            "Ensure every claim is justified and no steps are hand-waved."
        ),
    ),
    ReviewerPerspective(
        name="Clarity & Rigor",
        description=(
            "Focus on precision of notation, consistency of definitions, "
            "quality of exposition, and adherence to the stated rigor target. "
            "Ensure the proof would be acceptable for peer review at the "
            "specified rigor level."
        ),
    ),
    ReviewerPerspective(
        name="Reference Validity",
        description=(
            "Verify all citations, referenced theorems, and external results. "
            "Ensure every invoked theorem or lemma is correctly stated, its "
            "hypotheses are satisfied in context, and no phantom references "
            "are used. Flag any appeal to results not established or cited."
        ),
    ),
]


@dataclass(frozen=True)
class PipelineConfig:
    max_loops: int = 5
    rigor: str = "graduate"
    backend: str = "codex"
    model: str | None = None
    seed: int | None = None
    config_path: str | None = None
    reviewer_perspectives: tuple[ReviewerPerspective, ...] = tuple(DEFAULT_REVIEWER_PERSPECTIVES)

    def validate(self) -> None:
        if self.max_loops < 1:
            raise ValueError("max_loops must be at least 1")
        if not self.rigor.strip():
            raise ValueError("rigor must be non-empty")
        if not self.reviewer_perspectives:
            raise ValueError("reviewer_perspectives must be non-empty")
