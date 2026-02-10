from __future__ import annotations

import pytest

from pipeline.validate import (
    OutputValidationError,
    parse_editor_decision_output,
    parse_editor_dispatch_output,
    parse_reviewer_output,
)


# ---------------------------------------------------------------------------
# parse_reviewer_output
# ---------------------------------------------------------------------------


def test_parse_reviewer_output_accepts_valid_no_issues() -> None:
    text = """## Review
No issues.

```json
{
  "issues": [],
  "residual_concerns": []
}
```
"""
    result = parse_reviewer_output(text, reviewer_name="claude", perspective_name="Clarity")
    assert result.issues == []
    assert result.reviewer_name == "claude"
    assert result.perspective_name == "Clarity"


def test_parse_reviewer_output_accepts_valid_with_issues() -> None:
    text = """## Review
Issues found.

```json
{
  "issues": [
    {
      "severity": "major",
      "location": "Lemma 1",
      "reason": "Missing justification.",
      "required_fix": "Add proof for Lemma 1.",
      "suggestion": "Consider using induction on the structure."
    }
  ],
  "residual_concerns": []
}
```
"""
    result = parse_reviewer_output(text, reviewer_name="gpt", perspective_name="Correctness")
    assert len(result.issues) == 1
    assert result.issues[0].suggestion == "Consider using induction on the structure."
    assert result.reviewer_name == "gpt"
    assert result.perspective_name == "Correctness"


def test_parse_reviewer_output_rejects_missing_json() -> None:
    with pytest.raises(OutputValidationError, match="JSON"):
        parse_reviewer_output("No structured output")


def test_parse_reviewer_output_rejects_missing_suggestion() -> None:
    text = """```json
{
  "issues": [
    {
      "severity": "major",
      "location": "Lemma 1",
      "reason": "Missing justification.",
      "required_fix": "Add proof."
    }
  ],
  "residual_concerns": []
}
```"""
    with pytest.raises(OutputValidationError, match="suggestion"):
        parse_reviewer_output(text)


def test_parse_reviewer_output_default_names() -> None:
    text = """```json
{
  "issues": [],
  "residual_concerns": []
}
```"""
    result = parse_reviewer_output(text)
    assert result.reviewer_name == ""
    assert result.perspective_name == ""


# ---------------------------------------------------------------------------
# parse_editor_dispatch_output
# ---------------------------------------------------------------------------


def test_parse_editor_dispatch_valid() -> None:
    text = """## Dispatch
```json
{
  "assignments": {
    "Correctness": "claude_reviewer",
    "Clarity": "gpt_reviewer"
  },
  "reasoning": "Best fit."
}
```
"""
    result = parse_editor_dispatch_output(
        text,
        available_perspectives=["Correctness", "Clarity"],
        available_pool_names=["claude_reviewer", "gpt_reviewer"],
    )
    assert result.assignments["Correctness"] == "claude_reviewer"
    assert result.assignments["Clarity"] == "gpt_reviewer"
    assert result.reasoning == "Best fit."


def test_parse_editor_dispatch_missing_perspective() -> None:
    text = """```json
{
  "assignments": {
    "Correctness": "claude_reviewer"
  },
  "reasoning": "Partial."
}
```"""
    with pytest.raises(OutputValidationError, match="Clarity"):
        parse_editor_dispatch_output(
            text,
            available_perspectives=["Correctness", "Clarity"],
            available_pool_names=["claude_reviewer"],
        )


def test_parse_editor_dispatch_unknown_pool_name() -> None:
    text = """```json
{
  "assignments": {
    "Correctness": "unknown_reviewer"
  },
  "reasoning": "Bad."
}
```"""
    with pytest.raises(OutputValidationError, match="unknown_reviewer"):
        parse_editor_dispatch_output(
            text,
            available_perspectives=["Correctness"],
            available_pool_names=["claude_reviewer"],
        )


def test_parse_editor_dispatch_missing_json() -> None:
    with pytest.raises(OutputValidationError, match="JSON"):
        parse_editor_dispatch_output("No json here", ["A"], ["b"])


# ---------------------------------------------------------------------------
# parse_editor_decision_output
# ---------------------------------------------------------------------------


def test_parse_editor_decision_accept() -> None:
    text = """```json
{
  "verdict": "accept",
  "summary": "All good.",
  "feedback": ""
}
```"""
    verdict, summary, feedback = parse_editor_decision_output(text)
    assert verdict == "accept"
    assert summary == "All good."
    assert feedback == ""


def test_parse_editor_decision_right_track() -> None:
    text = """```json
{
  "verdict": "right_track",
  "summary": "Minor issues.",
  "feedback": "Fix Lemma B."
}
```"""
    verdict, summary, feedback = parse_editor_decision_output(text)
    assert verdict == "right_track"
    assert feedback == "Fix Lemma B."


def test_parse_editor_decision_wrong_track() -> None:
    text = """```json
{
  "verdict": "wrong_track",
  "summary": "Fundamental flaw.",
  "feedback": "Redesign approach."
}
```"""
    verdict, summary, feedback = parse_editor_decision_output(text)
    assert verdict == "wrong_track"
    assert feedback == "Redesign approach."


def test_parse_editor_decision_invalid_verdict() -> None:
    text = """```json
{
  "verdict": "PASS",
  "summary": "Old format.",
  "feedback": ""
}
```"""
    with pytest.raises(OutputValidationError, match="verdict"):
        parse_editor_decision_output(text)


def test_parse_editor_decision_accept_with_feedback_rejected() -> None:
    text = """```json
{
  "verdict": "accept",
  "summary": "Good.",
  "feedback": "But also fix this."
}
```"""
    with pytest.raises(OutputValidationError, match="accept.*empty feedback"):
        parse_editor_decision_output(text)


def test_parse_editor_decision_non_accept_empty_feedback_rejected() -> None:
    text = """```json
{
  "verdict": "right_track",
  "summary": "Issues.",
  "feedback": ""
}
```"""
    with pytest.raises(OutputValidationError, match="non-empty feedback"):
        parse_editor_decision_output(text)


def test_parse_editor_decision_missing_json() -> None:
    with pytest.raises(OutputValidationError, match="JSON"):
        parse_editor_decision_output("No json")
