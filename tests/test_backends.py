from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from pipeline.backends import CodexCLIBackend, build_backend


def test_build_backend_openai_raises_migration_error() -> None:
    backend = build_backend("openai", model="gpt-5")
    with pytest.raises(RuntimeError, match="removed"):
        backend.generate("statement", "prompt", {})


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
