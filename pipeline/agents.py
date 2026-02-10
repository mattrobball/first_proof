from __future__ import annotations

from functools import lru_cache
from pathlib import Path

ROLE_TO_TEMPLATE = {
    "statement": "statement.md",
    "sketch": "sketch.md",
    "prover": "prover.md",
    "editor_dispatch": "editor_dispatch.md",
    "editor_decision": "editor_decision.md",
    "reviewer": "reviewer.md",
}


class PromptTemplateError(ValueError):
    pass


def template_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "prompts"


@lru_cache(maxsize=8)
def load_template(role: str) -> str:
    filename = ROLE_TO_TEMPLATE.get(role)
    if not filename:
        raise PromptTemplateError(f"Unsupported role: {role}")
    path = template_dir() / filename
    if not path.exists():
        raise PromptTemplateError(f"Missing prompt template: {path}")
    return path.read_text(encoding="utf-8")


def render_prompt(role: str, context: dict[str, str]) -> str:
    template = load_template(role)
    try:
        return template.format(**context)
    except KeyError as exc:
        missing = str(exc).strip("'")
        raise PromptTemplateError(
            f"Prompt rendering failed for role '{role}', missing key: {missing}"
        ) from exc
