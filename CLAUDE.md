# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All commands use the project virtualenv at `.venv/`. Use `.venv/bin/python` (there is no system `python`).

```bash
# Run tests
.venv/bin/python -m pytest -q

# Run a single test file
.venv/bin/python -m pytest tests/test_runner.py -q

# Run pipeline with demo backend (no API keys needed)
.venv/bin/python -m pipeline.runner --problem 5 --backend demo

# Run pipeline with TOML config (auto-discovered)
.venv/bin/python -m pipeline.runner --problem 5

# Dry-run (validate prompts only, no backend calls)
.venv/bin/python -m pipeline.runner --problem 5 --dry-run
```

## Architecture

This is a multi-agent proof pipeline that iteratively generates and validates mathematical proofs using LLMs. The pipeline uses a **managing editor** model: agents generate a proof, reviewers evaluate it from multiple perspectives, and an editor synthesizes reviews into a three-way decision.

### Pipeline Flow

#### Per-Loop Flow

0. **Researcher** — Gathers relevant theorems, definitions, proof strategies, and identifies gaps. Runs every loop with access to prior transcript and editor feedback so it can refine research. Output is passed to subsequent agents as `{researcher_output}`.
1. **Mentor** — Formalizes the problem, normalizes notation, and proposes lemma-level proof strategy (skipped on `right_track` feedback)
2. **Prover** — Writes complete proof with justified steps
3. **Editor Dispatch** — Assigns pool reviewers to perspectives (LLM call)
4. **Reviewers** — One per perspective, using assigned pool backends
5. **Editor Decision** — Synthesizes reviews into a verdict (LLM call):
   - `accept`: proof passes, pipeline exits successfully
   - `right_track`: minor issues, feedback goes to prover next loop
   - `wrong_track`: fundamental problems, feedback goes to mentor next loop

The loop repeats until the editor accepts or the loop budget (default 5) is exhausted. Exit codes: 0=accept, 1=not accepted after max loops, 2=input validation error, 3=backend/runtime error.

### Module Layout

- `pipeline/runner.py` — Entry point and orchestration loop (`run_pipeline()`, `main()`)
- `pipeline/models.py` — Frozen dataclasses: `ProblemInputs`, `ReviewerResult`, `EditorDispatch`, `EditorDecision`, `LoopRecord`, `PipelineRunResult`
- `pipeline/config.py` — `PipelineConfig` and default reviewer perspectives
- `pipeline/backends.py` — `AgentBackend` protocol, `BackendRouter` (routes per-agent + pool dispatch), `DemoBackend`
- `pipeline/api_backends.py` — HTTP backends (Anthropic, OpenAI, Gemini) using only `urllib`
- `pipeline/cli_backends.py` — CLI backends (Codex, Claude, generic stdin→stdout)
- `pipeline/agent_config.py` — TOML config loading with cascading defaults + per-agent overrides + agent pool
- `pipeline/agents.py` — Prompt template loading/rendering from `prompts/` directory
- `pipeline/validate.py` — Output section validation, reviewer/editor JSON parsing
- `pipeline/io.py` — Problem input loading, transcript/LaTeX/meta file generation

### Backend System

Backends implement the `AgentBackend` protocol (`generate(role, prompt, context) -> str`). The `BackendRouter` allows mixing different backends per agent role and maintains a pool of agent backends:

```toml
[defaults]
backend = "cli"
provider = "codex"

[agents.editor]
backend = "api"
provider = "anthropic"
model = "claude-sonnet-4-20250514"

[agent_pool.claude_reviewer]
backend = "api"
provider = "anthropic"
model = "claude-sonnet-4-20250514"

[agent_pool.gpt_reviewer]
backend = "api"
provider = "openai"
model = "gpt-4o"
```

Config discovery order: `--config` flag → `pipeline.toml` in problem dir → `pipeline.toml` in cwd → legacy `--backend` flag.

### Problem Folder Contract

Each problem lives under `runs/<N>/` (e.g., `runs/5/`) containing `QUESTION.md` and `BACKGROUND.md`. Pipeline outputs (transcripts, LaTeX, metadata, checkpoints) are written directly into the same directory. The `runs/` tree is gitignored on `main`.

## Key Conventions

- **No external runtime dependencies** — all networking uses `urllib.request`
- **Prompt templates** in `prompts/` use `{key}` placeholder syntax (not Jinja)
- Agent roles are always one of: `"researcher"`, `"mentor"`, `"prover"`, `"editor_dispatch"`, `"editor_decision"`, `"reviewer"`
- Reviewer output must contain a JSON block in a fenced code block with structured issues
- Editor decision output must contain a JSON block with verdict (`accept`/`right_track`/`wrong_track`), summary, and feedback
- Data models are frozen dataclasses (immutable)
- Python 3.9+ (`from __future__ import annotations`)
