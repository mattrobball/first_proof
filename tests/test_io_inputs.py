from __future__ import annotations

from pathlib import Path

import pytest

from pipeline.io import (
    InputValidationError,
    _extract_question_from_paper,
    ensure_problem_files,
    load_problem_inputs,
)


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


# ---------------------------------------------------------------------------
# _extract_question_from_paper
# ---------------------------------------------------------------------------

_SAMPLE_PAPER = """\
## 2 The questions

**Question 1.** This is the first question.
It spans multiple lines.

**Question 2.** This is question two.
Also multi-line.

**Question 3.** Third question here.

## 3 Related work

Some unrelated text.
"""


def test_extract_question_found() -> None:
    text = _extract_question_from_paper(_SAMPLE_PAPER, 2)
    assert text is not None
    assert text.startswith("**Question 2.**")
    assert "question two" in text
    # Should not include question 3 or section 3
    assert "Question 3" not in text
    assert "Related work" not in text


def test_extract_question_last_before_section() -> None:
    text = _extract_question_from_paper(_SAMPLE_PAPER, 3)
    assert text is not None
    assert text.startswith("**Question 3.**")
    assert "Related work" not in text


def test_extract_question_not_found() -> None:
    text = _extract_question_from_paper(_SAMPLE_PAPER, 99)
    assert text is None


# ---------------------------------------------------------------------------
# ensure_problem_files
# ---------------------------------------------------------------------------


def test_ensure_creates_directory(tmp_path: Path) -> None:
    problem_dir = tmp_path / "7"
    assert not problem_dir.exists()
    ensure_problem_files(problem_dir)
    assert problem_dir.is_dir()


def test_ensure_generates_question_from_paper(tmp_path: Path) -> None:
    _write(tmp_path / "first_proof.md", _SAMPLE_PAPER)
    problem_dir = tmp_path / "2"

    ensure_problem_files(problem_dir, repo_root=tmp_path)

    question_path = problem_dir / "QUESTION.md"
    assert question_path.exists()
    content = question_path.read_text(encoding="utf-8")
    assert "Question 2" in content
    assert "question two" in content


def test_ensure_creates_background_stub(tmp_path: Path) -> None:
    problem_dir = tmp_path / "2"
    ensure_problem_files(problem_dir)
    bg = problem_dir / "BACKGROUND.md"
    assert bg.exists()
    assert "Background" in bg.read_text(encoding="utf-8")


def test_ensure_does_not_overwrite_existing(tmp_path: Path) -> None:
    _write(tmp_path / "first_proof.md", _SAMPLE_PAPER)
    problem_dir = tmp_path / "2"
    problem_dir.mkdir()
    _write(problem_dir / "QUESTION.md", "My custom question")
    _write(problem_dir / "BACKGROUND.md", "My custom background")

    ensure_problem_files(problem_dir, repo_root=tmp_path)

    assert (problem_dir / "QUESTION.md").read_text() == "My custom question"
    assert (problem_dir / "BACKGROUND.md").read_text() == "My custom background"


def test_ensure_non_numeric_dir_skips_extraction(tmp_path: Path) -> None:
    _write(tmp_path / "first_proof.md", _SAMPLE_PAPER)
    problem_dir = tmp_path / "my_problem"

    ensure_problem_files(problem_dir, repo_root=tmp_path)

    # Directory created, but no QUESTION.md (can't map name to number)
    assert problem_dir.is_dir()
    assert not (problem_dir / "QUESTION.md").exists()
