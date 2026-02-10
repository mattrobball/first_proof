"""Backend protocol, demo backend, routing, and factory functions.

The :class:`AgentBackend` protocol is the central interface for all backends.
:class:`BackendRouter` maps each agent *role* to its own backend instance,
allowing per-agent model selection driven by a TOML configuration file.
The router also holds a pool of reviewer backends that the editor can
dispatch to individual perspectives.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

from .agent_config import AgentModelConfig, PipelineFileConfig
from .api_backends import build_api_backend
from .cli_backends import build_cli_backend


# ---------------------------------------------------------------------------
# Protocol
# ---------------------------------------------------------------------------

class AgentBackend(Protocol):
    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        ...


# ---------------------------------------------------------------------------
# BackendRouter – dispatches per-role and per-pool
# ---------------------------------------------------------------------------

@dataclass
class BackendRouter:
    """Routes each agent role to its own backend instance.

    Implements :class:`AgentBackend` so the runner can use it transparently.
    Also holds ``pool_backends`` for reviewer dispatch.
    """

    role_backends: dict[str, AgentBackend]
    default_backend: AgentBackend
    pool_backends: dict[str, AgentBackend] = field(default_factory=dict)

    def generate(self, role: str, prompt: str, context: dict[str, str]) -> str:
        backend = self.role_backends.get(role, self.default_backend)
        return backend.generate(role, prompt, context)

    def generate_with_pool(
        self, pool_name: str, role: str, prompt: str, context: dict[str, str]
    ) -> str:
        """Generate using a named pool backend."""
        if pool_name not in self.pool_backends:
            raise ValueError(
                f"Unknown pool backend: '{pool_name}'. "
                f"Available: {sorted(self.pool_backends)}"
            )
        backend = self.pool_backends[pool_name]
        return backend.generate(role, prompt, context)


# ---------------------------------------------------------------------------
# DemoBackend (deterministic, for tests)
# ---------------------------------------------------------------------------

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
        editor_feedback = context.get("editor_feedback", "None.")

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
                f"- Items to watch from editor: {editor_feedback}\n"
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
                f"Addressed editor feedback this loop: {editor_feedback}\n"
            )

        if role == "editor_dispatch":
            # Assign all perspectives to the first available pool reviewer
            pool_desc = context.get("pool_description", "")
            persp_desc = context.get("perspectives_description", "")
            # Parse pool names from pool_description
            pool_names = re.findall(r"- \*\*(\S+)\*\*", pool_desc)
            pool_name = pool_names[0] if pool_names else "default_reviewer"
            # Parse perspective names from perspectives_description
            persp_names = re.findall(r"\d+\.\s+\*\*(.+?)\*\*", persp_desc)
            assignments = {p: pool_name for p in persp_names}
            payload = {
                "assignments": assignments,
                "reasoning": "Demo: assigning all perspectives to the first pool reviewer.",
            }
            return (
                "## Editor Dispatch\n"
                "Assigning all perspectives to the primary reviewer.\n\n"
                "## Assignments\n"
                f"```json\n{json.dumps(payload, indent=2)}\n```\n"
            )

        if role == "reviewer":
            perspective = context.get("perspective_name", "General")
            if loop_index == 1:
                payload = {
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
                    f"## {perspective} Review\n"
                    "Issues found.\n\n"
                    "## Structured Review\n"
                    f"```json\n{json.dumps(payload, indent=2)}\n```\n"
                )

            payload = {"issues": [], "residual_concerns": []}
            return (
                f"## {perspective} Review\n"
                "No issues.\n\n"
                "## Structured Review\n"
                f"```json\n{json.dumps(payload, indent=2)}\n```\n"
            )

        if role == "editor_decision":
            if loop_index == 1:
                payload = {
                    "verdict": "right_track",
                    "summary": "The proof has the right approach but Lemma B needs a detailed derivation.",
                    "feedback": (
                        "Provide a stepwise derivation for Lemma B. "
                        "Break it into sub-claims and prove each from stated assumptions."
                    ),
                }
                return (
                    "## Editor Decision\n"
                    "The proof needs revisions.\n\n"
                    "## Verdict\n"
                    f"```json\n{json.dumps(payload, indent=2)}\n```\n"
                )

            payload = {
                "verdict": "accept",
                "summary": "All reviewers are satisfied. The proof is correct and complete.",
                "feedback": "",
            }
            return (
                "## Editor Decision\n"
                "The proof is accepted.\n\n"
                "## Verdict\n"
                f"```json\n{json.dumps(payload, indent=2)}\n```\n"
            )

        raise ValueError(f"Unsupported role for backend output: {role}")


# ---------------------------------------------------------------------------
# Legacy CodexCLIBackend (kept for backward-compatible --backend=codex path)
# ---------------------------------------------------------------------------

@dataclass
class CodexCLIBackend:
    """Runs one local ``codex exec`` process per agent turn.

    This class is retained for backward compatibility with the ``--backend
    codex`` CLI flag.  New deployments should prefer a ``pipeline.toml`` config
    file with ``backend = "cli"`` and ``provider = "codex"``.
    """

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


# ---------------------------------------------------------------------------
# Factory functions
# ---------------------------------------------------------------------------

def _build_single_backend(cfg: AgentModelConfig, workdir: Path | None = None) -> AgentBackend:
    """Create one backend from an :class:`AgentModelConfig`."""
    kind = cfg.backend.lower()
    if kind == "demo":
        return DemoBackend()
    if kind == "api":
        return build_api_backend(cfg)
    if kind == "cli":
        return build_cli_backend(cfg, workdir=workdir)
    raise ValueError(f"Unsupported backend type: '{cfg.backend}'")


def build_backend_from_config(
    file_config: PipelineFileConfig, workdir: Path | None = None
) -> BackendRouter:
    """Create a :class:`BackendRouter` from a parsed TOML config.

    Each agent role defined in ``[agents.<role>]`` gets its own backend; all
    other roles fall back to ``[defaults]``.  Reviewer pool entries become
    ``pool_backends``.
    """
    default_backend = _build_single_backend(file_config.defaults, workdir)
    role_backends: dict[str, AgentBackend] = {}
    for role, cfg in file_config.agents.items():
        role_backends[role] = _build_single_backend(cfg, workdir)

    pool_backends: dict[str, AgentBackend] = {}
    for pool_name, cfg in file_config.reviewer_pool.items():
        pool_backends[pool_name] = _build_single_backend(cfg, workdir)

    return BackendRouter(
        role_backends=role_backends,
        default_backend=default_backend,
        pool_backends=pool_backends,
    )


def build_backend(
    name: str,
    model: str | None,
    seed: int | None = None,
    workdir: Path | None = None,
) -> BackendRouter:
    """Legacy factory used by the ``--backend`` CLI flag.

    Retained for backward compatibility.  Returns a :class:`BackendRouter`
    with a ``"default_reviewer"`` pool entry so the editor flow works.
    """
    normalized = name.strip().lower()
    if normalized == "demo":
        demo = DemoBackend()
        return BackendRouter(
            role_backends={},
            default_backend=demo,
            pool_backends={"default_reviewer": demo},
        )
    if normalized in {"codex", "codex-cli"}:
        if seed is not None:
            _ = seed
        backend = CodexCLIBackend(model=model, workdir=workdir)
        return BackendRouter(
            role_backends={},
            default_backend=backend,
            pool_backends={"default_reviewer": backend},
        )
    raise ValueError(f"Unsupported legacy backend: {name}")
