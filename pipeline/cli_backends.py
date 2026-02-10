"""Local CLI backends for the proof pipeline.

Each backend spawns a subprocess, feeds the rendered prompt on stdin, and
captures the model's textual response.

Supported CLI tools:

  * **codex** – ``codex exec -`` (OpenAI Codex CLI).
  * **claude** – ``claude -p`` (Anthropic Claude Code CLI).
  * Any other CLI that reads a prompt from stdin and writes its response to
    stdout can be used by setting ``cli_command`` to the binary name.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from .agent_config import AgentModelConfig


# ---------------------------------------------------------------------------
# Codex CLI
# ---------------------------------------------------------------------------

@dataclass
class CodexCLIBackend:
    """Runs one local ``codex exec`` process per agent turn."""

    cfg: AgentModelConfig
    workdir: Path | None = None
    full_auto: bool = True
    skip_git_repo_check: bool = True
    color: str = "never"
    target_reasoning_effort: str = "xhigh"

    def __post_init__(self) -> None:
        self.target_reasoning_effort = self.cfg.reasoning_effort or self.target_reasoning_effort
        binary = self.cfg.resolved_cli_command()
        resolved = shutil.which(binary)
        if resolved is None:
            raise RuntimeError(
                f"Could not find Codex CLI binary '{binary}' in PATH"
            )
        self._resolved_bin = resolved

    def _command(self, output_path: Path, reasoning_effort: str) -> list[str]:
        cmd = [self._resolved_bin, "exec", "-"]
        if self.cfg.model:
            cmd.extend(["--model", self.cfg.model])
        cmd.extend(["-c", f'model_reasoning_effort="{reasoning_effort}"'])
        if self.skip_git_repo_check:
            cmd.append("--skip-git-repo-check")
        if self.workdir is not None:
            cmd.extend(["--cd", str(self.workdir)])
        if self.full_auto:
            cmd.append("--full-auto")
        if self.color:
            cmd.extend(["--color", self.color])
        cmd.extend(["--output-last-message", str(output_path)])
        return cmd

    @staticmethod
    def _trim(text: str, limit: int = 4000) -> str:
        cleaned = text.strip()
        if len(cleaned) <= limit:
            return cleaned
        return cleaned[: limit - 3] + "..."

    @staticmethod
    def _effort_rank(effort: str) -> int:
        order = {
            "minimal": 0,
            "low": 1,
            "medium": 2,
            "high": 3,
            "xhigh": 4,
        }
        return order.get(effort.strip().lower(), -1)

    @classmethod
    def _highest_supported_effort(cls, stderr_text: str) -> str | None:
        match = re.search(r"Supported values are:\s*([^\n.]+)\.", stderr_text)
        if not match:
            return None
        candidates = re.findall(r"'([^']+)'", match.group(1))
        if not candidates:
            return None
        normalized = [item.strip().lower() for item in candidates if item.strip()]
        normalized.sort(key=cls._effort_rank, reverse=True)
        if not normalized:
            return None
        if cls._effort_rank(normalized[0]) < 0:
            return None
        return normalized[0]

    def _run_codex(self, role: str, prompt: str, reasoning_effort: str) -> str:
        with tempfile.TemporaryDirectory(prefix=f"proof-pipeline-{role}-") as tmp_dir:
            output_path = Path(tmp_dir) / "last_message.txt"
            cmd = self._command(output_path, reasoning_effort)

            proc = subprocess.run(
                cmd,
                input=prompt,
                text=True,
                capture_output=True,
                check=False,
            )

            if proc.returncode == 0:
                if output_path.exists():
                    content = output_path.read_text(encoding="utf-8").strip()
                    if content:
                        return content
                stdout_fallback = proc.stdout.strip()
                if stdout_fallback:
                    return stdout_fallback
                raise RuntimeError(
                    f"Codex backend returned no output for role '{role}'"
                )

            highest_supported = self._highest_supported_effort(proc.stderr)
            if (
                reasoning_effort != highest_supported
                and highest_supported is not None
                and self._effort_rank(highest_supported) >= 0
            ):
                return self._run_codex(role, prompt, highest_supported)

            stderr_snippet = self._trim(proc.stderr)
            stdout_snippet = self._trim(proc.stdout)
            raise RuntimeError(
                f"Codex backend failed for role '{role}' with exit code "
                f"{proc.returncode}. stderr: {stderr_snippet!r}; "
                f"stdout: {stdout_snippet!r}"
            )

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        return self._run_codex(role, prompt, self.target_reasoning_effort)


# ---------------------------------------------------------------------------
# Claude Code CLI
# ---------------------------------------------------------------------------

@dataclass
class ClaudeCLIBackend:
    """Runs one agentic ``claude --print`` invocation per agent turn."""

    cfg: AgentModelConfig
    workdir: Path | None = None
    max_turns: int = 25

    def __post_init__(self) -> None:
        binary = self.cfg.resolved_cli_command()
        resolved = shutil.which(binary)
        if resolved is None:
            raise RuntimeError(
                f"Could not find Claude CLI binary '{binary}' in PATH"
            )
        self._resolved_bin = resolved

    def _command(self) -> list[str]:
        cmd = [
            self._resolved_bin, "--print",
            "--output-format", "json",
            "--dangerously-skip-permissions",
            "--max-turns", str(self.max_turns),
            "--tools", "Read,Glob,Grep,WebSearch,WebFetch",
            "--no-session-persistence",
        ]
        if self.cfg.model:
            cmd.extend(["--model", self.cfg.model])
        if self.cfg.reasoning_effort:
            cmd.extend(["--effort", self.cfg.reasoning_effort])
        return cmd

    @staticmethod
    def _trim(text: str, limit: int = 4000) -> str:
        cleaned = text.strip()
        if len(cleaned) <= limit:
            return cleaned
        return cleaned[: limit - 3] + "..."

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        cmd = self._command()
        cwd = str(self.workdir) if self.workdir else None

        proc = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            check=False,
            cwd=cwd,
        )

        stdout = proc.stdout.strip()

        # Try to parse structured JSON output
        try:
            data = json.loads(stdout)
            subtype = data.get("subtype", "")
            if subtype.startswith("error_"):
                raise RuntimeError(
                    f"Claude CLI agent error for role '{role}': "
                    f"{subtype} — {data.get('result', '')}"
                )
            result = data.get("result", "").strip()
            if result:
                return result
        except (json.JSONDecodeError, AttributeError):
            # Fall back to raw stdout if JSON parsing fails
            if proc.returncode == 0 and stdout:
                return stdout

        if proc.returncode != 0:
            stderr_snippet = self._trim(proc.stderr)
            raise RuntimeError(
                f"Claude CLI failed for role '{role}' with exit code "
                f"{proc.returncode}. stderr: {stderr_snippet!r}"
            )

        raise RuntimeError(
            f"Claude CLI returned empty output for role '{role}'"
        )


# ---------------------------------------------------------------------------
# Generic CLI (stdin → stdout)
# ---------------------------------------------------------------------------

@dataclass
class GenericCLIBackend:
    """Runs an arbitrary CLI command: ``<binary> [model-flags] < prompt``."""

    cfg: AgentModelConfig
    workdir: Path | None = None

    def __post_init__(self) -> None:
        binary = self.cfg.resolved_cli_command()
        resolved = shutil.which(binary)
        if resolved is None:
            raise RuntimeError(
                f"Could not find CLI binary '{binary}' in PATH"
            )
        self._resolved_bin = resolved

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        cmd = [self._resolved_bin]
        if self.cfg.model:
            cmd.extend(["--model", self.cfg.model])
        cwd = str(self.workdir) if self.workdir else None

        proc = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            check=False,
            cwd=cwd,
        )

        if proc.returncode == 0:
            text = proc.stdout.strip()
            if text:
                return text
            raise RuntimeError(
                f"CLI backend '{self.cfg.cli_command}' returned empty output "
                f"for role '{role}'"
            )

        stderr_snippet = proc.stderr.strip()[:4000]
        raise RuntimeError(
            f"CLI backend '{self.cfg.cli_command}' failed for role '{role}' "
            f"with exit code {proc.returncode}. stderr: {stderr_snippet!r}"
        )


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

def build_cli_backend(
    cfg: AgentModelConfig, workdir: Path | None = None
) -> CodexCLIBackend | ClaudeCLIBackend | GenericCLIBackend:
    """Construct the right CLI backend based on *cfg*."""
    provider = cfg.provider.lower()
    if provider == "codex":
        return CodexCLIBackend(cfg=cfg, workdir=workdir)
    if provider == "claude":
        return ClaudeCLIBackend(cfg=cfg, workdir=workdir)
    return GenericCLIBackend(cfg=cfg, workdir=workdir)
