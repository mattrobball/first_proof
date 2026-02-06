# Multi-Agent Proof Pipeline

This repository runs a 4-agent workflow for each problem folder:
- `statement`: formalizes the problem.
- `sketch`: proposes lemma-level strategy.
- `prover`: writes a complete proof attempt.
- `critic`: returns PASS/FAIL with structured issues.

The pipeline is iterative and supports up to a configurable loop budget.

## Problem Folder Contract

Each problem must live in its own folder (for example `5/`) and include:
- `QUESTION.md` (required)
- `BACKGROUND.md` (required)

Run artifacts are written to:
- `N/runs/<timestamp>-transcript.md`
- `N/runs/<timestamp>-meta.json`

## Usage

`backend=codex` requires a working local `codex` CLI installation and authentication.
Each agent run forces `model_reasoning_effort="xhigh"` and automatically falls back
to the highest effort supported by the selected model when needed.

Dry-run validation:

```bash
python -m pipeline.runner --problem 5 --dry-run
```

Run with local Codex CLI backend (default):

```bash
python -m pipeline.runner --problem 5
```

Explicit Codex backend + model:

```bash
python -m pipeline.runner --problem 5 --backend codex --model gpt-5.3-codex
```

Run with deterministic demo backend (for local testing):

```bash
python -m pipeline.runner --problem 5 --backend demo
```

Useful flags:
- `--max-loops 5`
- `--rigor graduate`
- `--out-dir runs`
- `--model gpt-5.3-codex` (optional; default uses your Codex CLI profile)
- `--seed 42`

## Exit Codes

- `0`: critic passed within loop budget.
- `1`: critic failed after max loops.
- `2`: input or prompt validation failure.
- `3`: backend or runtime failure.

## Testing

```bash
python -m pytest -q
```
