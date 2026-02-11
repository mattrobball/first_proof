"""HTTP API backends for LLM providers.

Each backend accepts a prompt string and returns the model's text response.
Supported providers:

  * **anthropic** – Anthropic Messages API (Claude family).
  * **openai** – OpenAI Chat Completions API (GPT family).
  * **gemini** – Google Generative Language API (Gemini family).
  * **openai_compat** – Any provider exposing an OpenAI-compatible
    ``/v1/chat/completions`` endpoint (vLLM, Ollama, LM Studio, etc.).

All networking uses :mod:`urllib.request` from the standard library so there
are no third-party dependencies.
"""

from __future__ import annotations

import http.client
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass

from .agent_config import AgentModelConfig, _PROVIDER_DEFAULTS

_MAX_RETRIES = 3
_RETRY_BASE_DELAY = 2.0  # seconds; doubles each attempt
_DEFAULT_TIMEOUT = 120  # seconds per HTTP request


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _post_json(
    url: str,
    headers: dict[str, str],
    body: dict,
) -> dict:
    """Send a JSON POST request and return the parsed response.

    Retries up to ``_MAX_RETRIES`` times on transient errors (HTTP 5xx,
    429 rate-limit, ``RemoteDisconnected``, ``ConnectionResetError``, etc.)
    with exponential backoff.
    """
    data = json.dumps(body).encode()
    last_exc: Exception | None = None
    for attempt in range(_MAX_RETRIES):
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=_DEFAULT_TIMEOUT) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:
            error_body = ""
            try:
                error_body = exc.read().decode()[:2000]
            except Exception:
                pass
            if exc.code >= 500 or exc.code == 429:
                last_exc = RuntimeError(
                    f"API request failed ({exc.code}): {error_body}"
                )
            else:
                raise RuntimeError(
                    f"API request failed ({exc.code}): {error_body}"
                ) from exc
        except urllib.error.URLError as exc:
            # URLError wraps socket-level errors; retry on transient ones
            if isinstance(exc.reason, (ConnectionResetError, http.client.RemoteDisconnected,
                                       TimeoutError, OSError)):
                last_exc = exc
            else:
                raise RuntimeError(f"Network error: {exc.reason}") from exc
        except (ConnectionError, http.client.RemoteDisconnected, OSError) as exc:
            last_exc = exc
        delay = _RETRY_BASE_DELAY * (2 ** attempt)
        print(
            f"  [retry] transient error (attempt {attempt + 1}/{_MAX_RETRIES}): "
            f"{last_exc!r} — retrying in {delay:.0f}s",
            file=sys.stderr, flush=True,
        )
        time.sleep(delay)
    raise RuntimeError(f"Request failed after {_MAX_RETRIES} retries: {last_exc}") from last_exc


# ---------------------------------------------------------------------------
# Anthropic Messages API
# ---------------------------------------------------------------------------

@dataclass
class AnthropicBackend:
    """Calls the Anthropic Messages API."""

    cfg: AgentModelConfig

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        url = f"{self.cfg.resolved_api_base()}/v1/messages"
        headers = {
            "x-api-key": self.cfg.resolved_api_key(),
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }
        body: dict = {
            "model": self.cfg.model,
            "max_tokens": self.cfg.max_tokens or 16384,
            "messages": [{"role": "user", "content": prompt}],
        }
        if self.cfg.temperature is not None:
            body["temperature"] = self.cfg.temperature

        resp = _post_json(url, headers, body)

        content_blocks = resp.get("content", [])
        texts = [b["text"] for b in content_blocks if b.get("type") == "text"]
        if not texts:
            raise RuntimeError(
                f"Anthropic API returned no text for role '{role}'"
            )
        return "\n".join(texts)


# ---------------------------------------------------------------------------
# OpenAI Chat Completions API (also covers openai_compat)
# ---------------------------------------------------------------------------

@dataclass
class OpenAIBackend:
    """Calls an OpenAI-compatible Chat Completions endpoint."""

    cfg: AgentModelConfig

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        base = self.cfg.resolved_api_base()
        url = f"{base}/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.cfg.resolved_api_key()}",
            "Content-Type": "application/json",
        }
        body: dict = {
            "model": self.cfg.model,
            "messages": [{"role": "user", "content": prompt}],
        }
        if self.cfg.max_tokens:
            body["max_tokens"] = self.cfg.max_tokens
        if self.cfg.temperature is not None:
            body["temperature"] = self.cfg.temperature

        resp = _post_json(url, headers, body)

        choices = resp.get("choices", [])
        if not choices:
            raise RuntimeError(
                f"OpenAI API returned no choices for role '{role}'"
            )
        text = choices[0].get("message", {}).get("content", "")
        if not text:
            raise RuntimeError(
                f"OpenAI API returned empty content for role '{role}'"
            )
        return text


# ---------------------------------------------------------------------------
# Google Gemini API
# ---------------------------------------------------------------------------

def gemini_list_models(api_key: str) -> list[str]:
    """Return model IDs visible to *api_key* (health-check / auth test)."""
    url = (
        f"{_PROVIDER_DEFAULTS['gemini']['api_base']}"
        f"/v1beta/models?key={api_key}&pageSize=1000"
    )
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        error_body = ""
        try:
            error_body = exc.read().decode()[:2000]
        except Exception:
            pass
        raise RuntimeError(
            f"Gemini list-models failed ({exc.code}): {error_body}"
        ) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc
    return [m["name"] for m in data.get("models", [])]


@dataclass
class GeminiBackend:
    """Calls the Google Generative Language API (Gemini)."""

    cfg: AgentModelConfig

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        api_key = self.cfg.resolved_api_key()
        base = self.cfg.resolved_api_base()
        model = self.cfg.model
        url = (
            f"{base}/v1beta/models/{model}:generateContent"
            f"?key={api_key}"
        )
        headers = {"Content-Type": "application/json"}
        body: dict = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {},
        }
        gen_cfg = body["generationConfig"]
        if self.cfg.max_tokens:
            gen_cfg["maxOutputTokens"] = self.cfg.max_tokens
        if self.cfg.temperature is not None:
            gen_cfg["temperature"] = self.cfg.temperature
        if self.cfg.reasoning_effort:
            gen_cfg["thinkingConfig"] = {
                "thinkingLevel": self.cfg.reasoning_effort,
            }

        resp = _post_json(url, headers, body)

        candidates = resp.get("candidates", [])
        if not candidates:
            raise RuntimeError(
                f"Gemini API returned no candidates for role '{role}'"
            )
        parts = candidates[0].get("content", {}).get("parts", [])
        texts = [p["text"] for p in parts if "text" in p]
        if not texts:
            raise RuntimeError(
                f"Gemini API returned no text for role '{role}'"
            )
        return "\n".join(texts)


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

def build_api_backend(cfg: AgentModelConfig) -> AnthropicBackend | OpenAIBackend | GeminiBackend:
    """Construct the correct API backend for *cfg.provider*."""
    provider = cfg.provider.lower()
    if provider == "anthropic":
        return AnthropicBackend(cfg)
    if provider in {"openai", "openai_compat"}:
        return OpenAIBackend(cfg)
    if provider == "gemini":
        return GeminiBackend(cfg)
    raise ValueError(
        f"Unsupported API provider: '{cfg.provider}'. "
        f"Supported: anthropic, openai, gemini, openai_compat"
    )
