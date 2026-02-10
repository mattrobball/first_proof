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

## Quickstart

```bash
git clone https://github.com/mattrobball/first_proof.git
cd first_proof
git checkout digital_twin
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
