from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from pipeline.agent_config import AgentModelConfig, PipelineFileConfig
from pipeline.backends import (
    BackendRouter,
    CodexCLIBackend,
    DemoBackend,
    ExtensionRequesterBackend,
    SelfCiterBackend,
    _build_single_backend,
    build_backend,
    build_backend_from_config,
)
from pipeline.validate import parse_reviewer_output


# ---------------------------------------------------------------------------
# Legacy build_backend
# ---------------------------------------------------------------------------


def test_build_backend_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unsupported legacy backend"):
        build_backend("openai", model="gpt-5")


def test_build_backend_demo_returns_router() -> None:
    router = build_backend("demo", model=None)
    assert isinstance(router, BackendRouter)
    assert "default_reviewer" in router.pool_backends


# ---------------------------------------------------------------------------
# BackendRouter
# ---------------------------------------------------------------------------


def test_backend_router_dispatches_by_role() -> None:
    """BackendRouter should dispatch to role-specific backends when defined."""

    class _FakeBackend:
        def __init__(self, tag: str) -> None:
            self.tag = tag

        def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
            return f"{self.tag}:{role}"

    default = _FakeBackend("default")
    prover = _FakeBackend("prover-backend")
    router = BackendRouter(
        role_backends={"prover": prover},
        default_backend=default,
    )
    assert router.generate("prover", "", {}) == "prover-backend:prover"
    assert router.generate("statement", "", {}) == "default:statement"
    assert router.generate("editor_dispatch", "", {}) == "default:editor_dispatch"


def test_generate_with_pool() -> None:
    class _FakeBackend:
        def __init__(self, tag: str) -> None:
            self.tag = tag

        def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
            return f"{self.tag}:{role}"

    default = _FakeBackend("default")
    pool_a = _FakeBackend("pool-a")
    pool_b = _FakeBackend("pool-b")
    router = BackendRouter(
        role_backends={},
        default_backend=default,
        pool_backends={"reviewer_a": pool_a, "reviewer_b": pool_b},
    )
    assert router.generate_with_pool("reviewer_a", "reviewer", "", {}) == "pool-a:reviewer"
    assert router.generate_with_pool("reviewer_b", "reviewer", "", {}) == "pool-b:reviewer"


def test_generate_with_pool_unknown_raises() -> None:
    router = BackendRouter(
        role_backends={},
        default_backend=DemoBackend(),
        pool_backends={},
    )
    with pytest.raises(ValueError, match="Unknown pool backend"):
        router.generate_with_pool("nonexistent", "reviewer", "", {})


def test_build_single_backend_demo() -> None:
    cfg = AgentModelConfig(backend="demo")
    backend = _build_single_backend(cfg)
    assert isinstance(backend, DemoBackend)


def test_build_single_backend_unknown_raises() -> None:
    cfg = AgentModelConfig(backend="nonexistent")
    with pytest.raises(ValueError, match="Unsupported backend type"):
        _build_single_backend(cfg)


def test_build_backend_from_config_creates_router_with_pool() -> None:
    defaults = AgentModelConfig(backend="demo")
    agents = {"prover": AgentModelConfig(backend="demo")}
    pool = {"claude_reviewer": AgentModelConfig(backend="demo")}
    fc = PipelineFileConfig(defaults=defaults, agents=agents, reviewer_pool=pool)
    router, assignments = build_backend_from_config(fc)
    assert isinstance(router, BackendRouter)
    assert "prover" in router.role_backends
    assert "claude_reviewer" in router.pool_backends
    assert assignments == {}  # not randomizing


# ---------------------------------------------------------------------------
# Randomized agent assignment
# ---------------------------------------------------------------------------


def test_randomize_assigns_all_roles() -> None:
    """With randomize_agents=True, all 5 non-reviewer roles get assignments."""
    defaults = AgentModelConfig(backend="demo")
    pool = {
        "reviewer_a": AgentModelConfig(backend="demo"),
        "reviewer_b": AgentModelConfig(backend="demo"),
    }
    fc = PipelineFileConfig(
        defaults=defaults, agents={}, reviewer_pool=pool,
        randomize_agents=True,
    )
    _router, assignments = build_backend_from_config(fc, seed=42)
    expected_roles = {"researcher", "mentor", "prover", "editor_dispatch", "editor_decision"}
    assert set(assignments) == expected_roles
    valid_pool_names = {"defaults", "reviewer_a", "reviewer_b"}
    for pool_name in assignments.values():
        assert pool_name in valid_pool_names


def test_randomize_seed_deterministic() -> None:
    """Same seed produces identical assignments."""
    defaults = AgentModelConfig(backend="demo")
    pool = {
        "reviewer_a": AgentModelConfig(backend="demo"),
        "reviewer_b": AgentModelConfig(backend="demo"),
    }
    fc = PipelineFileConfig(
        defaults=defaults, agents={}, reviewer_pool=pool,
        randomize_agents=True,
    )
    _, a1 = build_backend_from_config(fc, seed=99)
    _, a2 = build_backend_from_config(fc, seed=99)
    assert a1 == a2


def test_randomize_respects_explicit_agents() -> None:
    """Roles with explicit [agents.<role>] overrides are not randomized."""
    defaults = AgentModelConfig(backend="demo")
    agents = {"prover": AgentModelConfig(backend="demo")}
    pool = {"reviewer_a": AgentModelConfig(backend="demo")}
    fc = PipelineFileConfig(
        defaults=defaults, agents=agents, reviewer_pool=pool,
        randomize_agents=True,
    )
    router, assignments = build_backend_from_config(fc, seed=42)
    assert "prover" not in assignments
    assert "prover" in router.role_backends  # still has its explicit backend
    # All other non-reviewer roles should be assigned
    assert "researcher" in assignments
    assert "mentor" in assignments
    assert "editor_dispatch" in assignments
    assert "editor_decision" in assignments


# ---------------------------------------------------------------------------
# Digital-twin joke backends
# ---------------------------------------------------------------------------


def test_self_citer_generates_valid_reviewer_output() -> None:
    backend = SelfCiterBackend()
    ctx = {"perspective_name": "Correctness & Completeness", "loop_index": "1"}
    text = backend.generate("reviewer", "", ctx)
    result = parse_reviewer_output(text, "self_citer", "Correctness & Completeness")
    assert len(result.issues) == 2
    assert all(i.severity == "major" for i in result.issues)
    assert any("Self-Citer" in i.reason for i in result.issues)
    assert any("bibliography" in c.lower() for c in result.residual_concerns)


def test_self_citer_rejects_non_reviewer_role() -> None:
    backend = SelfCiterBackend()
    with pytest.raises(ValueError, match="only handles 'reviewer'"):
        backend.generate("prover", "", {})


def test_extension_requester_generates_valid_reviewer_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("pipeline.backends.time.sleep", lambda _: None)
    backend = ExtensionRequesterBackend()
    ctx = {"perspective_name": "Clarity & Rigor", "loop_index": "1"}
    text = backend.generate("reviewer", "", ctx)
    result = parse_reviewer_output(text, "extension_requester", "Clarity & Rigor")
    assert len(result.issues) == 1
    assert result.issues[0].severity == "minor"
    assert "6-8 months" in result.issues[0].required_fix
    assert any("abstract" in c.lower() for c in result.residual_concerns)


def test_extension_requester_rejects_non_reviewer_role(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("pipeline.backends.time.sleep", lambda _: None)
    backend = ExtensionRequesterBackend()
    with pytest.raises(ValueError, match="only handles 'reviewer'"):
        backend.generate("mentor", "", {})


def test_build_single_backend_self_citer() -> None:
    cfg = AgentModelConfig(backend="self_citer")
    backend = _build_single_backend(cfg)
    assert isinstance(backend, SelfCiterBackend)


def test_build_single_backend_extension_requester() -> None:
    cfg = AgentModelConfig(backend="extension_requester")
    backend = _build_single_backend(cfg)
    assert isinstance(backend, ExtensionRequesterBackend)


# ---------------------------------------------------------------------------
# Required reviewers
# ---------------------------------------------------------------------------


def test_required_reviewers_threaded_to_router() -> None:
    defaults = AgentModelConfig(backend="demo")
    pool = {
        "real_reviewer": AgentModelConfig(backend="demo"),
        "self_citer": AgentModelConfig(backend="self_citer"),
    }
    fc = PipelineFileConfig(
        defaults=defaults, agents={}, reviewer_pool=pool,
        required_reviewers=["self_citer"],
    )
    router, _ = build_backend_from_config(fc)
    assert router.required_reviewers == ["self_citer"]


def test_required_reviewers_empty_by_default() -> None:
    defaults = AgentModelConfig(backend="demo")
    fc = PipelineFileConfig(defaults=defaults, agents={})
    router, _ = build_backend_from_config(fc)
    assert router.required_reviewers == []


# ---------------------------------------------------------------------------
# Legacy CodexCLIBackend
# ---------------------------------------------------------------------------


def test_codex_backend_invokes_codex_exec(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: dict[str, object] = {}

    def fake_which(binary: str) -> str:
        assert binary == "codex"
        return "/usr/bin/codex"

    def fake_run(*run_args: object, **kwargs: object) -> SimpleNamespace:
        assert len(run_args) == 1
        args = run_args[0]
        assert isinstance(args, list)
        seen["args"] = args
        seen["kwargs"] = kwargs
        output_flag_index = args.index("--output-last-message")
        output_path = Path(args[output_flag_index + 1])
        output_path.write_text("## Definitions\nx", encoding="utf-8")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr("pipeline.backends.shutil.which", fake_which)
    monkeypatch.setattr("pipeline.backends.subprocess.run", fake_run)

    backend = CodexCLIBackend(model="gpt-5", workdir=Path("/tmp/work"))
    text = backend.generate("statement", "hello prompt", {})

    assert text == "## Definitions\nx"
    args = seen["args"]
    assert isinstance(args, list)
    assert args[0] == "/usr/bin/codex"
    assert args[1] == "exec"
    assert "-c" in args
    assert 'model_reasoning_effort="xhigh"' in args
    assert "--skip-git-repo-check" in args
    assert "--output-last-message" in args
    kwargs = seen["kwargs"]
    assert isinstance(kwargs, dict)
    assert kwargs["input"] == "hello prompt"
    assert kwargs["text"] is True
    assert kwargs["capture_output"] is True


def test_codex_backend_nonzero_exit_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_which(binary: str) -> str:
        return "/usr/bin/codex"

    def fake_run(*run_args: object, **kwargs: object) -> SimpleNamespace:
        return SimpleNamespace(returncode=17, stdout="out", stderr="err")

    monkeypatch.setattr("pipeline.backends.shutil.which", fake_which)
    monkeypatch.setattr("pipeline.backends.subprocess.run", fake_run)

    backend = CodexCLIBackend(model="gpt-5")
    with pytest.raises(RuntimeError, match="exit code 17"):
        backend.generate("statement", "prompt", {})


def test_codex_backend_omits_model_flag_when_unset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    seen: dict[str, object] = {}

    def fake_which(binary: str) -> str:
        return "/usr/bin/codex"

    def fake_run(*run_args: object, **kwargs: object) -> SimpleNamespace:
        args = run_args[0]
        assert isinstance(args, list)
        seen["args"] = args
        output_flag_index = args.index("--output-last-message")
        output_path = Path(args[output_flag_index + 1])
        output_path.write_text("OK", encoding="utf-8")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr("pipeline.backends.shutil.which", fake_which)
    monkeypatch.setattr("pipeline.backends.subprocess.run", fake_run)

    backend = CodexCLIBackend(model=None)
    _ = backend.generate("statement", "prompt", {})
    args = seen["args"]
    assert isinstance(args, list)
    assert "--model" not in args
    assert 'model_reasoning_effort="xhigh"' in args


def test_codex_backend_retries_with_highest_supported_effort(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    seen_args: list[list[str]] = []
    call_count = {"n": 0}

    def fake_which(binary: str) -> str:
        return "/usr/bin/codex"

    def fake_run(*run_args: object, **kwargs: object) -> SimpleNamespace:
        args = run_args[0]
        assert isinstance(args, list)
        seen_args.append(args)
        call_count["n"] += 1
        if call_count["n"] == 1:
            return SimpleNamespace(
                returncode=1,
                stdout="",
                stderr=(
                    "ERROR: Unsupported value for reasoning effort. "
                    "Supported values are: 'minimal', 'low', 'medium', and 'high'."
                ),
            )
        output_flag_index = args.index("--output-last-message")
        output_path = Path(args[output_flag_index + 1])
        output_path.write_text("OK", encoding="utf-8")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr("pipeline.backends.shutil.which", fake_which)
    monkeypatch.setattr("pipeline.backends.subprocess.run", fake_run)

    backend = CodexCLIBackend(model=None)
    text = backend.generate("statement", "prompt", {})
    assert text == "OK"
    assert len(seen_args) == 2
    assert 'model_reasoning_effort="xhigh"' in seen_args[0]
    assert 'model_reasoning_effort="high"' in seen_args[1]
