from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


class AgentBackend(Protocol):
    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        ...


def _first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return "Unspecified problem statement."


@dataclass
class DemoBackend:
    """Deterministic backend for local workflow and testability."""

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        loop_index = int(context.get("loop_index", "1"))
        question_line = _first_non_empty_line(context.get("question_text", ""))
        issues_md = context.get("critic_issues_markdown", "None.")

        if role == "statement":
            return (
                "## Definitions\n"
                "- `Problem`: the target claim from `QUESTION.md`.\n"
                "- `Background assumptions`: all facts explicitly listed in `BACKGROUND.md`.\n\n"
                "## Formal Statement\n"
                f"Prove rigorously: {question_line}\n\n"
                "## Assumptions\n"
                "- Use only assumptions stated in the provided files.\n"
                "- Every inference in the final proof must be justified.\n\n"
                "## Notation\n"
                "- Reuse notation from the problem where available.\n"
            )

        if role == "sketch":
            return (
                "## High-Level Strategy\n"
                "1. Translate the question into explicit hypotheses and conclusions.\n"
                "2. Decompose the target into lemmas that can be proved from background facts.\n"
                "3. Assemble lemmas to conclude the formal statement.\n\n"
                "## Key Lemmas\n"
                "- Lemma A: setup and normalization.\n"
                "- Lemma B: core transformation step.\n"
                "- Lemma C: final implication.\n\n"
                "## Dependency Graph\n"
                "Lemma A -> Lemma B -> Lemma C -> Main theorem.\n\n"
                "## Risky Steps\n"
                f"- Items to watch from critic: {issues_md}\n"
            )

        if role == "prover":
            return (
                "## Complete Proof\n"
                "We proceed by proving Lemmas A, B, and C, then conclude the theorem.\n"
                "Each step uses only listed assumptions and previously proved lemmas.\n\n"
                "## Lemma Proofs\n"
                "- Lemma A: established by direct unpacking of assumptions.\n"
                "- Lemma B: derived from Lemma A and background constraints.\n"
                "- Lemma C: follows from Lemma B and the target implication form.\n\n"
                "## Gap Closure Notes\n"
                f"Addressed critic issues this loop: {issues_md}\n"
            )

        if role == "critic":
            perspective = context.get("critic_perspective_name", "General")
            if loop_index == 1:
                payload = {
                    "verdict": "FAIL",
                    "issues": [
                        {
                            "severity": "major",
                            "location": "Complete Proof",
                            "reason": "The proof outline lacks an explicit justification for Lemma B.",
                            "required_fix": "Provide a stepwise derivation for Lemma B from assumptions or prior lemmas.",
                            "suggestion": (
                                "Consider breaking Lemma B into sub-claims and "
                                "proving each from the stated assumptions."
                            ),
                        }
                    ],
                    "residual_concerns": [
                        "Check that notation is fixed before invoking derived statements."
                    ],
                }
                return (
                    f"## {perspective} Critic — Verdict\n"
                    "FAIL\n\n"
                    "## Issues\n"
                    "1. [major] Complete Proof: missing detailed derivation for Lemma B.\n\n"
                    "## Structured Verdict\n"
                    f"```json\n{json.dumps(payload, indent=2)}\n```\n"
                )

            payload = {"verdict": "PASS", "issues": [], "residual_concerns": []}
            return (
                f"## {perspective} Critic — Verdict\n"
                "PASS\n\n"
                "## Issues\n"
                "None.\n\n"
                "## Structured Verdict\n"
                f"```json\n{json.dumps(payload, indent=2)}\n```\n"
            )

        raise ValueError(f"Unsupported role for backend output: {role}")


@dataclass
class CodexCLIBackend:
    """Runs one local `codex exec` process per agent turn."""

    model: str | None = None
    codex_bin: str = "codex"
    workdir: Path | None = None
    sandbox: str = "workspace-write"
    timeout_seconds: int = 600
    full_auto: bool = True
    skip_git_repo_check: bool = True
    color: str = "never"
    target_reasoning_effort: str = "xhigh"

    def __post_init__(self) -> None:
        resolved = shutil.which(self.codex_bin)
        if resolved is None:
            raise RuntimeError(
                f"Could not find Codex CLI binary '{self.codex_bin}' in PATH"
            )
        self._resolved_codex_bin = resolved

    def _command(self, output_path: Path, reasoning_effort: str) -> list[str]:
        cmd = [self._resolved_codex_bin, "exec", "-"]
        if self.model:
            cmd.extend(["--model", self.model])
        cmd.extend(["-c", f'model_reasoning_effort="{reasoning_effort}"'])
        if self.skip_git_repo_check:
            cmd.append("--skip-git-repo-check")
        if self.workdir is not None:
            cmd.extend(["--cd", str(self.workdir)])
        if self.full_auto:
            cmd.append("--full-auto")
        if self.sandbox:
            cmd.extend(["--sandbox", self.sandbox])
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

            try:
                proc = subprocess.run(
                    cmd,
                    input=prompt,
                    text=True,
                    capture_output=True,
                    timeout=self.timeout_seconds,
                    check=False,
                )
            except subprocess.TimeoutExpired as exc:
                raise RuntimeError(
                    f"Codex backend timed out for role '{role}' "
                    f"after {self.timeout_seconds} seconds"
                ) from exc

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


@dataclass
class OpenAIBackendCompatibilityStub:
    """Legacy placeholder kept only to provide a direct migration error."""

    model: str | None = None

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        raise RuntimeError(
            "backend=openai has been removed. Use backend=codex "
            "to spawn local Codex agents."
        )


def build_backend(
    name: str,
    model: str | None,
    seed: int | None = None,
    workdir: Path | None = None,
) -> AgentBackend:
    normalized = name.strip().lower()
    if normalized == "demo":
        return DemoBackend()
    if normalized in {"codex", "codex-cli"}:
        if seed is not None:
            # Codex CLI does not currently expose a stable seed flag.
            _ = seed
        return CodexCLIBackend(model=model, workdir=workdir)
    if normalized == "openai":
        return OpenAIBackendCompatibilityStub(model=model)
    raise ValueError(f"Unsupported backend: {name}")
