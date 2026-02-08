"""TOML-based configuration for per-agent backend and model selection.

Loads a ``pipeline.toml`` file and resolves which backend (API or CLI)
and model each agent role should use.  Settings cascade from ``[defaults]``
into per-role ``[agents.<role>]`` sections so only overrides need to be
specified.

Supported backends:
  - ``api``:  HTTP calls to provider APIs (Anthropic, OpenAI, Gemini, or
              any OpenAI-compatible endpoint via ``provider = "openai_compat"``).
  - ``cli``:  Local CLI tools (``codex``, ``claude``).
  - ``demo``: Deterministic stub for testing.

Example ``pipeline.toml``::

    [defaults]
    backend  = "api"
    provider = "anthropic"
    model    = "claude-sonnet-4-20250514"

    [agents.prover]
    provider = "openai"
    model    = "gpt-4o"

    [agents.critic]
    backend     = "cli"
    cli_command  = "claude"
"""

from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ---- provider → default env-var / base-url mapping -------------------------

_PROVIDER_DEFAULTS: dict[str, dict[str, str]] = {
    "anthropic": {
        "api_key_env": "ANTHROPIC_API_KEY",
        "api_base": "https://api.anthropic.com",
    },
    "openai": {
        "api_key_env": "OPENAI_API_KEY",
        "api_base": "https://api.openai.com",
    },
    "gemini": {
        "api_key_env": "GEMINI_API_KEY",
        "api_base": "https://generativelanguage.googleapis.com",
    },
    "openai_compat": {
        "api_key_env": "OPENAI_API_KEY",
        "api_base": "",
    },
}

_CLI_DEFAULTS: dict[str, str] = {
    "codex": "codex",
    "claude": "claude",
}


# ---- data classes -----------------------------------------------------------

@dataclass(frozen=True)
class AgentModelConfig:
    """Fully-resolved configuration for a single agent role."""

    backend: str = "api"  # "api" | "cli" | "demo"
    provider: str = "anthropic"
    model: str = ""
    api_base: str = ""
    api_key_env: str = ""
    temperature: float = 0.2
    max_tokens: int = 16384
    timeout: int = 600
    cli_command: str = ""

    def resolved_api_key(self) -> str:
        """Return the API key from the environment, or raise."""
        env_var = self.api_key_env or _PROVIDER_DEFAULTS.get(
            self.provider, {}
        ).get("api_key_env", "")
        if not env_var:
            raise ValueError(
                f"No api_key_env configured for provider '{self.provider}'"
            )
        key = os.environ.get(env_var, "")
        if not key:
            raise ValueError(
                f"Environment variable '{env_var}' is not set "
                f"(required for provider '{self.provider}')"
            )
        return key

    def resolved_api_base(self) -> str:
        """Return the API base URL, falling back to provider defaults."""
        if self.api_base:
            return self.api_base.rstrip("/")
        default = _PROVIDER_DEFAULTS.get(self.provider, {}).get("api_base", "")
        if not default:
            raise ValueError(
                f"No api_base configured and no default for provider '{self.provider}'"
            )
        return default.rstrip("/")

    def resolved_cli_command(self) -> str:
        if self.cli_command:
            return self.cli_command
        return _CLI_DEFAULTS.get(self.provider, self.provider)


@dataclass
class PipelineFileConfig:
    """Full pipeline configuration loaded from a TOML file."""

    defaults: AgentModelConfig
    agents: dict[str, AgentModelConfig]

    def resolve(self, role: str) -> AgentModelConfig:
        """Return effective config for *role*, falling back to defaults."""
        return self.agents.get(role, self.defaults)


# ---- loading helpers --------------------------------------------------------

_AGENT_CONFIG_FIELDS = {f.name for f in AgentModelConfig.__dataclass_fields__.values()}


def _raw_to_agent_config(
    defaults: dict[str, Any], overrides: dict[str, Any]
) -> AgentModelConfig:
    merged = {**defaults, **overrides}
    filtered = {k: v for k, v in merged.items() if k in _AGENT_CONFIG_FIELDS}

    # Apply provider defaults for api_base / api_key_env if not explicitly set
    provider = filtered.get("provider", "anthropic")
    prov_defaults = _PROVIDER_DEFAULTS.get(provider, {})
    if "api_base" not in overrides and "api_base" not in defaults:
        filtered.setdefault("api_base", prov_defaults.get("api_base", ""))
    if "api_key_env" not in overrides and "api_key_env" not in defaults:
        filtered.setdefault("api_key_env", prov_defaults.get("api_key_env", ""))

    return AgentModelConfig(**filtered)


def load_config_file(path: Path) -> PipelineFileConfig:
    """Parse a ``pipeline.toml`` file into a :class:`PipelineFileConfig`."""
    raw = path.read_text(encoding="utf-8")
    data = tomllib.loads(raw)

    defaults_raw: dict[str, Any] = dict(data.get("defaults", {}))
    defaults = _raw_to_agent_config({}, defaults_raw)

    agents: dict[str, AgentModelConfig] = {}
    for role, role_raw in data.get("agents", {}).items():
        agents[role] = _raw_to_agent_config(defaults_raw, role_raw)

    return PipelineFileConfig(defaults=defaults, agents=agents)


def find_config_file(
    explicit: str | None = None, search_dirs: list[Path] | None = None
) -> Path | None:
    """Locate a config file.

    Priority:
      1. *explicit* path given by the user (``--config`` flag).
      2. ``pipeline.toml`` in each *search_dirs* entry (problem dir, then cwd).
    """
    if explicit:
        p = Path(explicit)
        if not p.exists():
            raise FileNotFoundError(f"Config file not found: {explicit}")
        return p

    for d in search_dirs or []:
        candidate = d / "pipeline.toml"
        if candidate.exists():
            return candidate

    return None
