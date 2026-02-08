from __future__ import annotations

import pytest

from pipeline.validate import OutputValidationError, parse_critic_output


def test_parse_critic_output_accepts_valid_pass() -> None:
    text = """## Verdict
PASS

```json
{
  "verdict": "PASS",
  "issues": [],
  "residual_concerns": []
}
```
"""
    result = parse_critic_output(text, critic_name="Test Critic")
    assert result.verdict == "PASS"
    assert result.issues == []
    assert result.critic_name == "Test Critic"


def test_parse_critic_output_accepts_valid_fail_with_suggestion() -> None:
    text = """## Verdict
FAIL

```json
{
  "verdict": "FAIL",
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
    result = parse_critic_output(text, critic_name="Logical Correctness")
    assert result.verdict == "FAIL"
    assert len(result.issues) == 1
    assert result.issues[0].suggestion == "Consider using induction on the structure."
    assert result.critic_name == "Logical Correctness"


def test_parse_critic_output_rejects_fail_with_no_issues() -> None:
    text = """```json
{
  "verdict": "FAIL",
  "issues": [],
  "residual_concerns": []
}
```"""
    with pytest.raises(OutputValidationError, match="FAIL"):
        parse_critic_output(text)


def test_parse_critic_output_rejects_missing_json() -> None:
    with pytest.raises(OutputValidationError, match="JSON"):
        parse_critic_output("No structured output")


def test_parse_critic_output_rejects_missing_suggestion() -> None:
    text = """```json
{
  "verdict": "FAIL",
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
        parse_critic_output(text)


def test_parse_critic_output_default_critic_name() -> None:
    text = """```json
{
  "verdict": "PASS",
  "issues": [],
  "residual_concerns": []
}
```"""
    result = parse_critic_output(text)
    assert result.critic_name == ""
