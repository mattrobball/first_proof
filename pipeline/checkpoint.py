"""Checkpoint / resume support for the proof pipeline."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .models import LoopRecord

_CHECKPOINT_VERSION = 1


@dataclass(frozen=True)
class CheckpointData:
    problem_id: str
    started_at: str
    timestamp: str
    max_loops: int
    input_hashes: dict[str, str]
    loops: list[LoopRecord]
    editor_feedback: str
    feedback_target: str

    def to_dict(self) -> dict[str, object]:
        return {
            "version": _CHECKPOINT_VERSION,
            "problem_id": self.problem_id,
            "started_at": self.started_at,
            "timestamp": self.timestamp,
            "max_loops": self.max_loops,
            "input_hashes": self.input_hashes,
            "loops": [loop.to_dict() for loop in self.loops],
            "editor_feedback": self.editor_feedback,
            "feedback_target": self.feedback_target,
        }


def write_checkpoint(
    out_dir: Path,
    timestamp: str,
    problem_id: str,
    started_at: str,
    max_loops: int,
    input_hashes: dict[str, str],
    loops: list[LoopRecord],
    editor_feedback: str,
    feedback_target: str,
) -> Path:
    """Write a checkpoint JSON file, overwriting any previous checkpoint."""
    data = CheckpointData(
        problem_id=problem_id,
        started_at=started_at,
        timestamp=timestamp,
        max_loops=max_loops,
        input_hashes=input_hashes,
        loops=loops,
        editor_feedback=editor_feedback,
        feedback_target=feedback_target,
    )
    path = out_dir / f"{timestamp}-checkpoint.json"
    path.write_text(
        json.dumps(data.to_dict(), indent=2) + "\n", encoding="utf-8"
    )
    return path


def load_checkpoint(path: Path) -> CheckpointData:
    """Load a checkpoint file and return a CheckpointData instance."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    version = raw.get("version", 0)
    if version != _CHECKPOINT_VERSION:
        raise ValueError(
            f"Unsupported checkpoint version {version} "
            f"(expected {_CHECKPOINT_VERSION})"
        )
    return CheckpointData(
        problem_id=str(raw["problem_id"]),
        started_at=str(raw["started_at"]),
        timestamp=str(raw["timestamp"]),
        max_loops=int(raw["max_loops"]),
        input_hashes=dict(raw["input_hashes"]),
        loops=[LoopRecord.from_dict(d) for d in raw["loops"]],
        editor_feedback=str(raw.get("editor_feedback", "None.")),
        feedback_target=str(raw.get("feedback_target", "")),
    )


def validate_checkpoint_inputs(
    checkpoint: CheckpointData, question_hash: str, background_hash: str
) -> None:
    """Raise ValueError if input files have changed since the checkpoint."""
    saved = checkpoint.input_hashes
    if saved.get("question_sha256") != question_hash:
        raise ValueError(
            "QUESTION.md has changed since the checkpoint was created"
        )
    if saved.get("background_sha256") != background_hash:
        raise ValueError(
            "BACKGROUND.md has changed since the checkpoint was created"
        )
