# Multi-Agent Proof Pipeline

A multi-agent pipeline that iteratively generates and validates mathematical
proofs using LLMs, organized around a managing-editor model: agents draft a
proof, a panel of reviewers evaluates it from multiple perspectives, and an
editor synthesizes their feedback into a revision decision.

The `digital_twin` branch additionally provides a faithful simulation of the
academic peer review process as it is actually experienced by working
mathematicians. Two of the three reviewer slots are filled by backends that
reproduce, with some fidelity, the most common species of referee encountered
in the wild:

- **Self-Citer** — Finds that every aspect of the proof would benefit from
  citing the reviewer's own body of work. Engages with the mathematics zero
  times. Suggests adding themselves as co-author.
- **Extension Requester** — After a noticeable delay, reports having read the
  title and part of the abstract. Requests six to eight additional months,
  contingent on the completion of a sabbatical and the resolution of several
  scheduling conflicts including, but not limited to, a particularly engrossing
  season of television.

The managing editor, upon receiving these reviews, expresses measured
exasperation and rejects the manuscript — not on its mathematical merits, which
remain unexamined, but because the review process itself has become untenable.
The authors are thanked for their interest in the *Annals of Conditions Under
Which Peer Review Actually Functions* and encouraged to seek alternative venues.
No further correspondence is entered into.

This is, of course, entirely fictional and bears no resemblance to any real
journal, referee, or editorial board, living or dead.

## Pipeline Flow

0. **Researcher** (once, pre-loop) — gathers relevant theorems and strategies
1. **Mentor** — formalizes the problem and proposes proof strategy
2. **Prover** — writes the complete proof
3. **Editor Dispatch** — assigns pool reviewers to perspectives
4. **Reviewers** — one per perspective, from the configured pool
5. **Editor Decision** — synthesizes reviews into `accept`, `right_track`,
   `wrong_track`, or (on the `digital_twin` branch) `reject`

## Problem Folder Contract

Each problem must live in its own folder (for example `5/`) and include:
- `QUESTION.md` (required)
- `BACKGROUND.md` (required)

Run artifacts are written to:
- `N/runs/<timestamp>-transcript.md`
- `N/runs/<timestamp>-report.tex`
- `N/runs/<timestamp>-meta.json`

## Usage

Dry-run validation:

```bash
python -m pipeline.runner --problem 5 --dry-run
```

Run with local Codex CLI backend (default):

```bash
python -m pipeline.runner --problem 5
```

Run with deterministic demo backend (for local testing):

```bash
python -m pipeline.runner --problem 5 --backend demo
```

Useful flags:
- `--max-loops 5`
- `--rigor graduate`
- `--out-dir runs`
- `--seed 42`
- `--config pipeline.toml`

## Configuration

The pipeline reads `pipeline.toml` for per-agent backend and model selection.
On the `digital_twin` branch, the default config enables `randomize_agents`
(each non-reviewer role is randomly assigned a backend from the pool) and
`required_reviewers` (the self-citer and extension requester are guaranteed
seats on the review panel).

```toml
randomize_agents = true
required_reviewers = ["self_citer", "extension_requester"]
```

## Exit Codes

- `0`: proof accepted within loop budget
- `1`: not accepted (or rejected) after max loops
- `2`: input or prompt validation failure
- `3`: backend or runtime failure

## Testing

```bash
python -m pytest -q
```
