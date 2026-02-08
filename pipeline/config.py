from __future__ import annotations

from dataclasses import dataclass, field

from .models import CriticPerspective

DEFAULT_CRITIC_PERSPECTIVES: list[CriticPerspective] = [
    CriticPerspective(
        name="Logical Correctness",
        description=(
            "Focus on the validity of logical inferences, correct application "
            "of proof techniques, and soundness of deductions. Check for "
            "logical fallacies, circular reasoning, and invalid proof steps."
        ),
    ),
    CriticPerspective(
        name="Mathematical Completeness",
        description=(
            "Focus on mathematical gaps, missing lemmas, unstated assumptions, "
            "and incomplete case analysis. Ensure every claim is justified and "
            "no steps are hand-waved or left to the reader without warrant."
        ),
    ),
    CriticPerspective(
        name="Clarity and Rigor",
        description=(
            "Focus on precision of notation, consistency of definitions, "
            "quality of exposition, and adherence to the stated rigor target. "
            "Ensure the proof would be acceptable for peer review at the "
            "specified rigor level."
        ),
    ),
]


@dataclass(frozen=True)
class PipelineConfig:
    max_loops: int = 5
    rigor: str = "graduate"
    out_dir_name: str = "runs"
    backend: str = "codex"
    model: str | None = None
    seed: int | None = None
    config_path: str | None = None
    critic_perspectives: tuple[CriticPerspective, ...] = tuple(DEFAULT_CRITIC_PERSPECTIVES)

    def validate(self) -> None:
        if self.max_loops < 1:
            raise ValueError("max_loops must be at least 1")
        if not self.rigor.strip():
            raise ValueError("rigor must be non-empty")
        if not self.out_dir_name.strip():
            raise ValueError("out_dir_name must be non-empty")
        if not self.critic_perspectives:
            raise ValueError("critic_perspectives must be non-empty")
