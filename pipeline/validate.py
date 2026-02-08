from __future__ import annotations

import json
import re

from .models import CriticIssue, CriticResult, Severity, Verdict

REQUIRED_HEADINGS: dict[str, list[str]] = {
    "statement": [
        "## Definitions",
        "## Formal Statement",
        "## Assumptions",
        "## Notation",
    ],
    "sketch": [
        "## High-Level Strategy",
        "## Key Lemmas",
        "## Dependency Graph",
        "## Risky Steps",
    ],
    "prover": [
        "## Complete Proof",
        "## Lemma Proofs",
        "## Gap Closure Notes",
    ],
}

VALID_SEVERITIES: set[str] = {"critical", "major", "minor"}
VALID_VERDICTS: set[str] = {"PASS", "FAIL"}


class OutputValidationError(ValueError):
    pass


def ensure_required_sections(role: str, text: str) -> None:
    headings = REQUIRED_HEADINGS.get(role)
    if not headings:
        return
    missing = [heading for heading in headings if heading not in text]
    if missing:
        role_name = role.upper()
        missing_str = ", ".join(missing)
        raise OutputValidationError(
            f"{role_name} output is missing required heading(s): {missing_str}"
        )


def parse_critic_output(text: str, critic_name: str = "") -> CriticResult:
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise OutputValidationError("Critic output missing fenced JSON payload")

    try:
        payload = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise OutputValidationError("Critic JSON payload is invalid") from exc

    verdict = payload.get("verdict")
    if verdict not in VALID_VERDICTS:
        raise OutputValidationError("Critic verdict must be PASS or FAIL")

    issues_raw = payload.get("issues")
    if not isinstance(issues_raw, list):
        raise OutputValidationError("Critic issues must be a list")

    residual = payload.get("residual_concerns", [])
    if not isinstance(residual, list) or not all(isinstance(x, str) for x in residual):
        raise OutputValidationError("Critic residual_concerns must be a list of strings")

    issues: list[CriticIssue] = []
    for idx, issue_obj in enumerate(issues_raw, start=1):
        if not isinstance(issue_obj, dict):
            raise OutputValidationError(f"Critic issue #{idx} must be an object")

        severity = issue_obj.get("severity")
        location = issue_obj.get("location")
        reason = issue_obj.get("reason")
        required_fix = issue_obj.get("required_fix")
        suggestion = issue_obj.get("suggestion")

        if severity not in VALID_SEVERITIES:
            raise OutputValidationError(
                f"Critic issue #{idx} severity must be one of {sorted(VALID_SEVERITIES)}"
            )
        if not isinstance(location, str) or not location.strip():
            raise OutputValidationError(f"Critic issue #{idx} location must be non-empty")
        if not isinstance(reason, str) or not reason.strip():
            raise OutputValidationError(f"Critic issue #{idx} reason must be non-empty")
        if not isinstance(required_fix, str) or not required_fix.strip():
            raise OutputValidationError(
                f"Critic issue #{idx} required_fix must be non-empty"
            )
        if not isinstance(suggestion, str) or not suggestion.strip():
            raise OutputValidationError(
                f"Critic issue #{idx} suggestion must be non-empty"
            )

        typed_severity: Severity = severity
        issues.append(
            CriticIssue(
                severity=typed_severity,
                location=location.strip(),
                reason=reason.strip(),
                required_fix=required_fix.strip(),
                suggestion=suggestion.strip(),
            )
        )

    typed_verdict: Verdict = verdict
    if typed_verdict == "PASS" and issues:
        raise OutputValidationError("Critic cannot return PASS with non-empty issues")
    if typed_verdict == "FAIL" and not issues:
        raise OutputValidationError("Critic cannot return FAIL with empty issues")

    return CriticResult(
        critic_name=critic_name,
        verdict=typed_verdict,
        issues=issues,
        residual_concerns=residual,
    )
