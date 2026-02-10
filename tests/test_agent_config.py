from __future__ import annotations

from pathlib import Path

import pytest

from pipeline.agent_config import (
    APPROVED_BACKENDS,
    AgentModelConfig,
    PipelineFileConfig,
    find_config_file,
    load_config_file,
    validate_approved_backends,
)


def _write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# load_config_file
# ---------------------------------------------------------------------------


def test_load_minimal_config(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
[defaults]
backend  = "demo"
provider = "anthropic"
model    = "test-model"
""",
    )
    fc = load_config_file(cfg_path)
    assert fc.defaults.backend == "demo"
    assert fc.defaults.provider == "anthropic"
    assert fc.defaults.model == "test-model"
    assert fc.agents == {}
    assert fc.agent_pool == {}


def test_load_config_with_per_agent_overrides(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
[defaults]
backend  = "api"
provider = "anthropic"
model    = "claude-base"

[agents.prover]
provider = "openai"
model    = "gpt-4o"

[agents.editor]
backend     = "cli"
provider    = "claude"
""",
    )
    fc = load_config_file(cfg_path)

    # defaults
    assert fc.defaults.backend == "api"
    assert fc.defaults.model == "claude-base"

    # prover inherits backend=api, overrides provider+model
    prover = fc.resolve("prover")
    assert prover.backend == "api"
    assert prover.provider == "openai"
    assert prover.model == "gpt-4o"

    # editor overrides backend to cli
    editor = fc.resolve("editor")
    assert editor.backend == "cli"
    assert editor.provider == "claude"

    # statement falls back to defaults
    statement = fc.resolve("statement")
    assert statement.backend == "api"
    assert statement.provider == "anthropic"
    assert statement.model == "claude-base"


def test_load_config_temperature_and_timeout(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
[defaults]
backend     = "demo"
temperature = 0.7
timeout     = 300

[agents.sketch]
temperature = 0.0
""",
    )
    fc = load_config_file(cfg_path)
    assert fc.defaults.temperature == 0.7
    assert fc.defaults.timeout == 300
    sketch = fc.resolve("sketch")
    assert sketch.temperature == 0.0
    assert sketch.timeout == 300  # inherited


def test_load_config_with_agent_pool(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
[defaults]
backend  = "demo"
provider = "anthropic"

[agent_pool.claude_reviewer]
backend  = "api"
provider = "anthropic"
model    = "claude-sonnet-4-20250514"

[agent_pool.gpt_reviewer]
backend  = "api"
provider = "openai"
model    = "gpt-4o"
""",
    )
    fc = load_config_file(cfg_path)
    assert "claude_reviewer" in fc.agent_pool
    assert "gpt_reviewer" in fc.agent_pool
    assert fc.agent_pool["claude_reviewer"].provider == "anthropic"
    assert fc.agent_pool["gpt_reviewer"].provider == "openai"
    assert fc.agent_pool["gpt_reviewer"].model == "gpt-4o"


def test_agent_pool_inherits_defaults(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
[defaults]
backend     = "api"
provider    = "anthropic"
temperature = 0.3

[agent_pool.my_reviewer]
model = "custom-model"
""",
    )
    fc = load_config_file(cfg_path)
    reviewer = fc.agent_pool["my_reviewer"]
    assert reviewer.backend == "api"
    assert reviewer.provider == "anthropic"
    assert reviewer.temperature == 0.3
    assert reviewer.model == "custom-model"


def test_resolve_pool_found() -> None:
    pool = {"reviewer_a": AgentModelConfig(backend="demo")}
    fc = PipelineFileConfig(
        defaults=AgentModelConfig(backend="demo"),
        agents={},
        agent_pool=pool,
    )
    cfg = fc.resolve_pool("reviewer_a")
    assert cfg.backend == "demo"


def test_resolve_pool_unknown_raises() -> None:
    fc = PipelineFileConfig(
        defaults=AgentModelConfig(backend="demo"),
        agents={},
        agent_pool={},
    )
    with pytest.raises(ValueError, match="Unknown agent pool name"):
        fc.resolve_pool("nonexistent")


# ---------------------------------------------------------------------------
# resolve helpers
# ---------------------------------------------------------------------------


def test_resolved_api_base_default() -> None:
    cfg = AgentModelConfig(provider="openai")
    assert "openai.com" in cfg.resolved_api_base()


def test_resolved_api_base_custom() -> None:
    cfg = AgentModelConfig(provider="openai_compat", api_base="http://localhost:8000/")
    assert cfg.resolved_api_base() == "http://localhost:8000"


def test_resolved_api_key_raises_when_missing() -> None:
    cfg = AgentModelConfig(provider="anthropic")
    # If ANTHROPIC_API_KEY is not set in the test env, this should raise
    import os
    if "ANTHROPIC_API_KEY" not in os.environ:
        with pytest.raises(ValueError, match="ANTHROPIC_API_KEY"):
            cfg.resolved_api_key()


def test_resolved_cli_command_defaults() -> None:
    cfg = AgentModelConfig(provider="codex")
    assert cfg.resolved_cli_command() == "codex"
    cfg2 = AgentModelConfig(provider="claude")
    assert cfg2.resolved_cli_command() == "claude"
    cfg3 = AgentModelConfig(provider="custom", cli_command="my-llm")
    assert cfg3.resolved_cli_command() == "my-llm"


# ---------------------------------------------------------------------------
# find_config_file
# ---------------------------------------------------------------------------


def test_find_config_explicit(tmp_path: Path) -> None:
    cfg_path = tmp_path / "my_config.toml"
    _write(cfg_path, "[defaults]\nbackend = 'demo'\n")
    found = find_config_file(explicit=str(cfg_path))
    assert found == cfg_path


def test_find_config_explicit_missing() -> None:
    with pytest.raises(FileNotFoundError):
        find_config_file(explicit="/no/such/file.toml")


def test_find_config_search_dirs(tmp_path: Path) -> None:
    d1 = tmp_path / "dir1"
    d1.mkdir()
    d2 = tmp_path / "dir2"
    d2.mkdir()
    _write(d2 / "pipeline.toml", "[defaults]\nbackend = 'demo'\n")
    found = find_config_file(search_dirs=[d1, d2])
    assert found == d2 / "pipeline.toml"


def test_find_config_returns_none_when_absent(tmp_path: Path) -> None:
    found = find_config_file(search_dirs=[tmp_path])
    assert found is None


# ---------------------------------------------------------------------------
# pipeline.toml loading
# ---------------------------------------------------------------------------


def test_randomize_agents_parsed(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
randomize_agents = true

[defaults]
backend = "demo"
""",
    )
    fc = load_config_file(cfg_path)
    assert fc.randomize_agents is True


def test_randomize_agents_default_false(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
[defaults]
backend = "demo"
""",
    )
    fc = load_config_file(cfg_path)
    assert fc.randomize_agents is False


def test_load_pipeline_toml() -> None:
    """The real pipeline.toml at the project root parses without error."""
    root = Path(__file__).resolve().parent.parent / "pipeline.toml"
    fc = load_config_file(root)
    # No [defaults] section — defaults synthesised from first pool entry
    assert fc.defaults.backend in ("cli", "api")
    assert len(fc.agent_pool) >= 3


def test_no_defaults_uses_first_pool_entry(tmp_path: Path) -> None:
    """When [defaults] is absent, defaults come from first pool entry."""
    cfg_path = tmp_path / "pipeline.toml"
    cfg_path.write_text(
        '[agent_pool.my_backend]\nbackend = "demo"\nprovider = "test"\nmodel = "m1"\n',
        encoding="utf-8",
    )
    fc = load_config_file(cfg_path)
    assert fc.defaults.backend == "demo"
    assert fc.defaults.provider == "test"


# ---------------------------------------------------------------------------
# validate_approved_backends
# ---------------------------------------------------------------------------


def _approved_config(**pool_overrides: dict) -> PipelineFileConfig:
    """Build a PipelineFileConfig using only approved backends."""
    pool = {
        "claude_code": AgentModelConfig(
            backend="cli", provider="claude", model="claude-opus-4-6",
        ),
        "codex_cli": AgentModelConfig(
            backend="cli", provider="codex", model="gpt-5.3-codex",
        ),
        "gemini_api": AgentModelConfig(
            backend="api", provider="gemini", model="gemini-3-pro-preview",
        ),
        **pool_overrides,
    }
    # Defaults from first pool entry (mirrors no-[defaults] behaviour)
    defaults = next(iter(pool.values()))
    return PipelineFileConfig(
        defaults=defaults,
        agents={},
        agent_pool=pool,
    )


def test_approved_backends_pass() -> None:
    fc = _approved_config()
    validate_approved_backends(fc)  # should not raise


def test_unapproved_provider_rejected() -> None:
    fc = PipelineFileConfig(
        defaults=AgentModelConfig(backend="api", provider="openai", model="gpt-4o"),
        agents={},
    )
    with pytest.raises(ValueError, match="Unapproved backend"):
        validate_approved_backends(fc)


def test_unapproved_model_rejected() -> None:
    fc = PipelineFileConfig(
        defaults=AgentModelConfig(backend="cli", provider="codex", model="codex-1.0"),
        agents={},
    )
    with pytest.raises(ValueError, match="Unapproved backend"):
        validate_approved_backends(fc)


def test_all_pool_entries_validated() -> None:
    fc = _approved_config(
        bad_reviewer=AgentModelConfig(
            backend="cli", provider="gemini", model="gemini-3-pro-preview",
        ),
    )
    with pytest.raises(ValueError, match="agent_pool.bad_reviewer"):
        validate_approved_backends(fc)


def test_default_backend_validated() -> None:
    fc = PipelineFileConfig(
        defaults=AgentModelConfig(backend="demo", provider="anthropic", model="x"),
        agents={},
    )
    with pytest.raises(ValueError, match="defaults"):
        validate_approved_backends(fc)


def test_pipeline_toml_all_approved() -> None:
    """The real pipeline.toml passes approved-backend validation."""
    root = Path(__file__).resolve().parent.parent / "pipeline.toml"
    fc = load_config_file(root)
    validate_approved_backends(fc)  # should not raise


# ---------------------------------------------------------------------------
# reasoning_effort wiring
# ---------------------------------------------------------------------------


def test_codex_reasoning_effort_from_config() -> None:
    from unittest.mock import patch

    cfg = AgentModelConfig(
        backend="cli", provider="codex", model="gpt-5.3-codex",
        reasoning_effort="xhigh",
    )
    with patch("shutil.which", return_value="/usr/bin/codex"):
        from pipeline.cli_backends import CodexCLIBackend
        backend = CodexCLIBackend(cfg=cfg)
    assert backend.target_reasoning_effort == "xhigh"


def test_claude_effort_from_config() -> None:
    from unittest.mock import patch

    cfg = AgentModelConfig(
        backend="cli", provider="claude", model="claude-opus-4-6",
        reasoning_effort="high",
    )
    with patch("shutil.which", return_value="/usr/bin/claude"):
        from pipeline.cli_backends import ClaudeCLIBackend
        backend = ClaudeCLIBackend(cfg=cfg)
    cmd = backend._command()
    assert "--effort" in cmd
    idx = cmd.index("--effort")
    assert cmd[idx + 1] == "high"
