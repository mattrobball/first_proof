from __future__ import annotations

from pathlib import Path

import pytest

from pipeline.agent_config import (
    AgentModelConfig,
    PipelineFileConfig,
    find_config_file,
    load_config_file,
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
    assert fc.reviewer_pool == {}


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


def test_load_config_with_reviewer_pool(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
[defaults]
backend  = "demo"
provider = "anthropic"

[reviewer_pool.claude_reviewer]
backend  = "api"
provider = "anthropic"
model    = "claude-sonnet-4-20250514"

[reviewer_pool.gpt_reviewer]
backend  = "api"
provider = "openai"
model    = "gpt-4o"
""",
    )
    fc = load_config_file(cfg_path)
    assert "claude_reviewer" in fc.reviewer_pool
    assert "gpt_reviewer" in fc.reviewer_pool
    assert fc.reviewer_pool["claude_reviewer"].provider == "anthropic"
    assert fc.reviewer_pool["gpt_reviewer"].provider == "openai"
    assert fc.reviewer_pool["gpt_reviewer"].model == "gpt-4o"


def test_reviewer_pool_inherits_defaults(tmp_path: Path) -> None:
    cfg_path = tmp_path / "pipeline.toml"
    _write(
        cfg_path,
        """\
[defaults]
backend     = "api"
provider    = "anthropic"
temperature = 0.3

[reviewer_pool.my_reviewer]
model = "custom-model"
""",
    )
    fc = load_config_file(cfg_path)
    reviewer = fc.reviewer_pool["my_reviewer"]
    assert reviewer.backend == "api"
    assert reviewer.provider == "anthropic"
    assert reviewer.temperature == 0.3
    assert reviewer.model == "custom-model"


def test_resolve_reviewer_found() -> None:
    pool = {"reviewer_a": AgentModelConfig(backend="demo")}
    fc = PipelineFileConfig(
        defaults=AgentModelConfig(backend="demo"),
        agents={},
        reviewer_pool=pool,
    )
    cfg = fc.resolve_reviewer("reviewer_a")
    assert cfg.backend == "demo"


def test_resolve_reviewer_unknown_raises() -> None:
    fc = PipelineFileConfig(
        defaults=AgentModelConfig(backend="demo"),
        agents={},
        reviewer_pool={},
    )
    with pytest.raises(ValueError, match="Unknown reviewer pool name"):
        fc.resolve_reviewer("nonexistent")


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
