# Multi-Agent Proof Pipeline

A multi-agent pipeline that iteratively generates and validates mathematical
proofs using LLMs, organized around a managing-editor model: agents draft a
proof, a panel of reviewers evaluates it from multiple perspectives, and an
editor synthesizes their feedback into a revision decision.

## Pipeline Flow

0. **Researcher** (once, pre-loop) — gathers relevant theorems and strategies
1. **Mentor** — formalizes the problem and proposes proof strategy
2. **Prover** — writes the complete proof
3. **Editor Dispatch** — assigns pool reviewers to perspectives
4. **Reviewers** — one per perspective, from the configured pool
5. **Editor Decision** — synthesizes reviews into `accept`, `right_track`,
   or `wrong_track`

The loop repeats until the editor accepts or the loop budget is exhausted.

## Problem Folders

Problem folders are created automatically at pipeline start. When you run
`--problem 5`, the pipeline will:

1. Create the `5/` directory if it doesn't exist
2. Extract **Question 5** from `first_proof.md` into `5/QUESTION.md`
3. Create a stub `5/BACKGROUND.md` if missing

You can also create these files manually. Existing files are never overwritten.

Run artifacts are written to `N/runs/` (gitignored on `main`; archived on the
`live_runs` branch).

## Quickstart

```bash
git clone https://github.com/mattrobball/first_proof.git
cd first_proof
```

Python 3.11 or later is required (`tomllib` is used from the standard library).

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the demo (no API keys needed):

```bash
python -m pipeline.runner --problem 5 --backend demo
```

This runs the full pipeline with a deterministic stub backend — researcher,
mentor, prover, reviewers, and editor — and writes a transcript, LaTeX report,
and metadata file to `5/runs/`.

## Other usage

Dry-run (validate inputs and prompt rendering only):

```bash
python -m pipeline.runner --problem 5 --dry-run
```

Run with real backends via `pipeline.toml` (requires API keys or local CLI
tools as configured):

```bash
python -m pipeline.runner --problem 5
```

Flags:
- `--max-loops 5` — revision loop budget
- `--rigor graduate` — rigor target label included in prompts
- `--seed 42` — deterministic backend assignment when `randomize_agents` is on
- `--config pipeline.toml` — explicit config file path

## Configuration

The pipeline reads `pipeline.toml` for per-agent backend and model selection.
When `randomize_agents` is enabled, each non-reviewer role is randomly
assigned a backend from the agent pool, reshuffled every loop.

The default `pipeline.toml` configures three backends:

```toml
randomize_agents = true

[agent_pool.claude_code]
backend  = "cli"
provider = "claude"
model    = "claude-opus-4-6"

[agent_pool.codex_cli]
backend  = "cli"
provider = "codex"
model    = "gpt-5.3-codex"

[agent_pool.gemini_api]
backend  = "api"
provider = "gemini"
model    = "gemini-3-pro-preview"
```

### Backend prerequisites

| Pool entry    | Type | Requires                                                  |
|---------------|------|-----------------------------------------------------------|
| `claude_code` | CLI  | `claude` CLI installed and authenticated                  |
| `codex_cli`   | CLI  | `codex` CLI installed and authenticated                   |
| `gemini_api`  | API  | `GEMINI_API_KEY` environment variable set                 |

API backends read their key from the environment variable mapped to the
provider (`GEMINI_API_KEY` for Gemini, `ANTHROPIC_API_KEY` for Anthropic,
`OPENAI_API_KEY` for OpenAI/OpenAI-compatible).

The pipeline auto-loads a `.secrets` file (if found in the problem directory
or working directory) containing `export KEY=value` lines, so you can put
credentials there instead of exporting them in your shell.

## Exit Codes

- `0`: proof accepted within loop budget
- `1`: not accepted after max loops
- `2`: input or prompt validation failure
- `3`: backend or runtime failure

## Branches

- **`main`** — production pipeline code (run artifacts are gitignored)
- **`digital_twin`** — a more realistic model of the academic peer review
  process 😉
- **`live_runs`** — archived transcripts, LaTeX reports, and metadata from
  past pipeline runs

## Testing

```bash
python -m pytest -q
```
