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
    result = parse_critic_output(text)
    assert result.verdict == "PASS"
    assert result.issues == []


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
