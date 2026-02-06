from __future__ import annotations

from pathlib import Path

import pytest

from pipeline.io import InputValidationError, load_problem_inputs


def _write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def test_missing_question_fails(tmp_path: Path) -> None:
    problem_dir = tmp_path / "5"
    problem_dir.mkdir()
    _write(problem_dir / "BACKGROUND.md", "Background text")

    with pytest.raises(InputValidationError, match="QUESTION.md"):
        load_problem_inputs(problem_dir)


def test_missing_background_fails(tmp_path: Path) -> None:
    problem_dir = tmp_path / "5"
    problem_dir.mkdir()
    _write(problem_dir / "QUESTION.md", "Question text")

    with pytest.raises(InputValidationError, match="BACKGROUND.md"):
        load_problem_inputs(problem_dir)


def test_empty_required_file_fails(tmp_path: Path) -> None:
    problem_dir = tmp_path / "5"
    problem_dir.mkdir()
    _write(problem_dir / "QUESTION.md", "Question text")
    _write(problem_dir / "BACKGROUND.md", "  \n")

    with pytest.raises(InputValidationError, match="empty"):
        load_problem_inputs(problem_dir)
