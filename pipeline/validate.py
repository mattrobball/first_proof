from __future__ import annotations

import json
import re

from .models import EditorDispatch, EditorVerdict, ReviewerIssue, ReviewerResult, Severity

REQUIRED_HEADINGS: dict[str, list[str]] = {
    "researcher": [
        "## Relevant Theorems",
        "## Key Definitions",
        "## Proof Strategies",
        "## Gaps and Concerns",
    ],
    "mentor": [
        "## Definitions",
        "## Formal Statement",
        "## Assumptions",
        "## Notation",
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
VALID_EDITOR_VERDICTS: set[str] = {"accept", "right_track", "wrong_track"}


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


def _extract_json_block(text: str, label: str) -> dict:
    """Extract and parse a fenced JSON block from *text*."""
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise OutputValidationError(f"{label} output missing fenced JSON payload")
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise OutputValidationError(f"{label} JSON payload is invalid") from exc


def parse_reviewer_output(
    text: str, reviewer_name: str = "", perspective_name: str = ""
) -> ReviewerResult:
    payload = _extract_json_block(text, "Reviewer")

    issues_raw = payload.get("issues")
    if not isinstance(issues_raw, list):
        raise OutputValidationError("Reviewer issues must be a list")

    residual = payload.get("residual_concerns", [])
    if not isinstance(residual, list) or not all(isinstance(x, str) for x in residual):
        raise OutputValidationError("Reviewer residual_concerns must be a list of strings")

    issues: list[ReviewerIssue] = []
    for idx, issue_obj in enumerate(issues_raw, start=1):
        if not isinstance(issue_obj, dict):
            raise OutputValidationError(f"Reviewer issue #{idx} must be an object")

        severity = issue_obj.get("severity")
        location = issue_obj.get("location")
        reason = issue_obj.get("reason")
        required_fix = issue_obj.get("required_fix")
        suggestion = issue_obj.get("suggestion")

        if severity not in VALID_SEVERITIES:
            raise OutputValidationError(
                f"Reviewer issue #{idx} severity must be one of {sorted(VALID_SEVERITIES)}"
            )
        if not isinstance(location, str) or not location.strip():
            raise OutputValidationError(f"Reviewer issue #{idx} location must be non-empty")
        if not isinstance(reason, str) or not reason.strip():
            raise OutputValidationError(f"Reviewer issue #{idx} reason must be non-empty")
        if not isinstance(required_fix, str) or not required_fix.strip():
            raise OutputValidationError(
                f"Reviewer issue #{idx} required_fix must be non-empty"
            )
        if not isinstance(suggestion, str) or not suggestion.strip():
            raise OutputValidationError(
                f"Reviewer issue #{idx} suggestion must be non-empty"
            )

        typed_severity: Severity = severity
        issues.append(
            ReviewerIssue(
                severity=typed_severity,
                location=location.strip(),
                reason=reason.strip(),
                required_fix=required_fix.strip(),
                suggestion=suggestion.strip(),
            )
        )

    return ReviewerResult(
        reviewer_name=reviewer_name,
        perspective_name=perspective_name,
        issues=issues,
        residual_concerns=residual,
    )


def parse_editor_dispatch_output(
    text: str,
    available_perspectives: list[str],
    available_pool_names: list[str],
) -> EditorDispatch:
    payload = _extract_json_block(text, "Editor dispatch")

    assignments = payload.get("assignments")
    if not isinstance(assignments, dict):
        raise OutputValidationError("Editor dispatch assignments must be an object")

    reasoning = payload.get("reasoning", "")
    if not isinstance(reasoning, str):
        raise OutputValidationError("Editor dispatch reasoning must be a string")

    # Validate every perspective is assigned
    for perspective in available_perspectives:
        if perspective not in assignments:
            raise OutputValidationError(
                f"Editor dispatch missing assignment for perspective: '{perspective}'"
            )

    # Validate every assigned pool name exists
    for perspective, pool_name in assignments.items():
        if not isinstance(pool_name, str):
            raise OutputValidationError(
                f"Editor dispatch assignment for '{perspective}' must be a string"
            )
        if pool_name not in available_pool_names:
            raise OutputValidationError(
                f"Editor dispatch assigned unknown pool name '{pool_name}' "
                f"to perspective '{perspective}'. "
                f"Available: {sorted(available_pool_names)}"
            )

    return EditorDispatch(assignments=assignments, reasoning=reasoning)


def parse_editor_decision_output(
    text: str,
) -> tuple[EditorVerdict, str, str]:
    payload = _extract_json_block(text, "Editor decision")

    verdict = payload.get("verdict")
    if verdict not in VALID_EDITOR_VERDICTS:
        raise OutputValidationError(
            f"Editor decision verdict must be one of {sorted(VALID_EDITOR_VERDICTS)}"
        )

    summary = payload.get("summary", "")
    if not isinstance(summary, str):
        raise OutputValidationError("Editor decision summary must be a string")

    feedback = payload.get("feedback", "")
    if not isinstance(feedback, str):
        raise OutputValidationError("Editor decision feedback must be a string")

    if verdict == "accept" and feedback:
        raise OutputValidationError(
            "Editor decision with 'accept' verdict must have empty feedback"
        )
    if verdict != "accept" and not feedback.strip():
        raise OutputValidationError(
            f"Editor decision with '{verdict}' verdict must have non-empty feedback"
        )

    typed_verdict: EditorVerdict = verdict
    return typed_verdict, summary, feedback
