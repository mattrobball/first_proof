from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from .config import PipelineConfig
from .models import LoopRecord, PipelineRunResult, ProblemInputs


class InputValidationError(ValueError):
    pass


def _read_required_markdown(path: Path) -> str:
    if not path.exists():
        raise InputValidationError(f"Missing required file: {path}")
    if not path.is_file():
        raise InputValidationError(f"Expected a file at: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise InputValidationError(f"Required file is empty: {path}")
    return text


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_problem_inputs(problem_dir: Path) -> ProblemInputs:
    if not problem_dir.exists():
        raise InputValidationError(f"Problem directory does not exist: {problem_dir}")
    if not problem_dir.is_dir():
        raise InputValidationError(f"Problem path is not a directory: {problem_dir}")

    question_path = problem_dir / "QUESTION.md"
    background_path = problem_dir / "BACKGROUND.md"
    question_text = _read_required_markdown(question_path)
    background_text = _read_required_markdown(background_path)
    problem_id = problem_dir.name

    return ProblemInputs(
        problem_id=problem_id,
        question_text=question_text,
        background_text=background_text,
        question_hash=sha256_text(question_text),
        background_hash=sha256_text(background_text),
    )


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def format_timestamp(ts: datetime) -> str:
    return ts.astimezone(timezone.utc).strftime("%Y%m%d-%H%M%S")


def ensure_output_dir(problem_dir: Path, out_dir_name: str) -> Path:
    out_dir = problem_dir / out_dir_name
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def build_transcript(
    problem_inputs: ProblemInputs,
    config: PipelineConfig,
    loops: list[LoopRecord],
    started_at: str,
    finished_at: str,
    final_verdict: str,
) -> str:
    lines: list[str] = []
    lines.append("# Proof Pipeline Transcript")
    lines.append("")
    lines.append(f"- Problem: `{problem_inputs.problem_id}`")
    lines.append(f"- Started (UTC): `{started_at}`")
    lines.append(f"- Finished (UTC): `{finished_at}`")
    lines.append(f"- Max loops: `{config.max_loops}`")
    lines.append(f"- Executed loops: `{len(loops)}`")
    lines.append(f"- Rigor: `{config.rigor}`")
    lines.append(f"- Final verdict: `{final_verdict}`")
    lines.append("")

    for loop in loops:
        lines.append(f"## Loop {loop.loop_index}")
        lines.append("")
        lines.append("### Statement Agent")
        lines.append("")
        lines.append(loop.statement_text.rstrip())
        lines.append("")
        lines.append("### Sketch Agent")
        lines.append("")
        lines.append(loop.sketch_text.rstrip())
        lines.append("")
        lines.append("### Prover Agent")
        lines.append("")
        lines.append(loop.prover_text.rstrip())
        lines.append("")
        lines.append("### Critic Agent")
        lines.append("")
        lines.append(loop.critic_text.rstrip())
        lines.append("")

    lines.append("## Final Status")
    lines.append("")
    lines.append(f"Pipeline finished with verdict: `{final_verdict}`.")
    lines.append("")
    return "\n".join(lines)


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def write_meta(
    path: Path,
    run_result: PipelineRunResult,
    input_hashes: dict[str, str],
) -> None:
    payload = run_result.to_meta_dict()
    payload["input_hashes"] = input_hashes
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
