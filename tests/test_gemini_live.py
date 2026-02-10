"""Live integration tests for the Gemini API backend.

These tests hit the real Gemini API and are skipped when GEMINI_API_KEY
is not set.  Run explicitly with:

    GEMINI_API_KEY=... python -m pytest tests/test_gemini_live.py -v
"""

from __future__ import annotations

import os

import pytest

_KEY = os.environ.get("GEMINI_API_KEY", "")
_skip = pytest.mark.skipif(not _KEY, reason="GEMINI_API_KEY not set")


@_skip
def test_gemini_list_models() -> None:
    """API key is valid and can list models (health check)."""
    from pipeline.api_backends import gemini_list_models

    models = gemini_list_models(_KEY)
    assert isinstance(models, list)
    assert len(models) > 0
    # Our configured model should be visible
    assert any("gemini-3-pro-preview" in m for m in models)


@_skip
def test_gemini_generate_minimal() -> None:
    """Minimal generateContent call returns a non-empty text response."""
    from pipeline.agent_config import AgentModelConfig
    from pipeline.api_backends import GeminiBackend

    cfg = AgentModelConfig(
        backend="api",
        provider="gemini",
        model="gemini-3-pro-preview",
        max_tokens=256,
        timeout=60,
        reasoning_effort="low",
    )
    backend = GeminiBackend(cfg=cfg)
    text = backend.generate("test", "Reply with exactly: HELLO", {})
    assert len(text.strip()) > 0


@_skip
def test_gemini_thinking_level() -> None:
    """Verify thinkingConfig.thinkingLevel is accepted by the API."""
    from pipeline.agent_config import AgentModelConfig
    from pipeline.api_backends import GeminiBackend

    cfg = AgentModelConfig(
        backend="api",
        provider="gemini",
        model="gemini-3-pro-preview",
        max_tokens=256,
        timeout=60,
        reasoning_effort="high",
    )
    backend = GeminiBackend(cfg=cfg)
    text = backend.generate("test", "What is 2+2?", {})
    assert "4" in text
