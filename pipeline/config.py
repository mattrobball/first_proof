from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PipelineConfig:
    max_loops: int = 5
    rigor: str = "graduate"
    out_dir_name: str = "runs"
    backend: str = "codex"
    model: str | None = None
    seed: int | None = None

    def validate(self) -> None:
        if self.max_loops < 1:
            raise ValueError("max_loops must be at least 1")
        if not self.rigor.strip():
            raise ValueError("rigor must be non-empty")
        if not self.out_dir_name.strip():
            raise ValueError("out_dir_name must be non-empty")
