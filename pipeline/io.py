from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from .config import PipelineConfig
from .models import LoopRecord, PipelineRunResult, ProblemInputs

_PAPER_FILENAME = "first_proof.md"

# Regex: matches **Question N.** at the start of a line (N is one or more digits)
_QUESTION_START_RE = re.compile(r"^\*\*Question\s+(\d+)\.\*\*", re.MULTILINE)


class InputValidationError(ValueError):
    pass


def _extract_question_from_paper(paper_text: str, problem_number: int) -> str | None:
    """Extract Question *problem_number* from the First Proof paper text.

    Returns the raw question text (including the ``**Question N.**`` prefix)
    or ``None`` if no matching question is found.
    """
    matches = list(_QUESTION_START_RE.finditer(paper_text))
    target_match = None
    for m in matches:
        if int(m.group(1)) == problem_number:
            target_match = m
            break
    if target_match is None:
        return None

    start = target_match.start()
    # Find the end: next **Question or a ## heading
    rest = paper_text[target_match.end():]
    end_re = re.search(r"^\*\*Question\s+\d+\.\*\*|^## ", rest, re.MULTILINE)
    if end_re:
        end = target_match.end() + end_re.start()
    else:
        end = len(paper_text)
    return paper_text[start:end].strip()


def ensure_problem_files(problem_dir: Path, repo_root: Path | None = None) -> None:
    """Create the problem directory and generate QUESTION.md if missing.

    If *problem_dir* does not exist it is created.  If ``QUESTION.md`` is
    absent and the ``first_proof.md`` paper file is found, the question is
    extracted from the paper and written to ``QUESTION.md``.  A minimal
    ``BACKGROUND.md`` stub is created when that file is also absent.
    """
    problem_dir.mkdir(parents=True, exist_ok=True)

    question_path = problem_dir / "QUESTION.md"
    background_path = problem_dir / "BACKGROUND.md"

    # Try to parse the problem number from the directory name
    try:
        problem_number = int(problem_dir.name)
    except ValueError:
        problem_number = None

    # --- QUESTION.md ---
    if not question_path.exists() and problem_number is not None:
        search_dirs = [problem_dir.parent]
        if repo_root is not None and repo_root not in search_dirs:
            search_dirs.append(repo_root)
        search_dirs.append(Path.cwd())

        for d in search_dirs:
            paper_path = d / _PAPER_FILENAME
            if paper_path.is_file():
                paper_text = paper_path.read_text(encoding="utf-8")
                extracted = _extract_question_from_paper(paper_text, problem_number)
                if extracted is not None:
                    question_path.write_text(
                        f"# Question {problem_number}\n\n{extracted}\n",
                        encoding="utf-8",
                    )
                    print(
                        f"[info] Generated {question_path} from {paper_path}",
                        file=sys.stderr,
                    )
                else:
                    print(
                        f"[warn] Question {problem_number} not found in {paper_path}",
                        file=sys.stderr,
                    )
                break

    # --- BACKGROUND.md stub ---
    if not background_path.exists():
        background_path.write_text(
            "# Background\n\n"
            "<!-- Add relevant definitions, theorems, and context here. -->\n",
            encoding="utf-8",
        )
        print(
            f"[info] Created stub {background_path} — please add background material",
            file=sys.stderr,
        )


def _read_required_markdown(path: Path) -> str:
    if not path.exists():
        raise InputValidationError(f"Missing required file: {path}")
    if not path.is_file():
        raise InputValidationError(f"Expected a file at: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise InputValidationError(f"Required file is empty: {path}")
    return text


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_problem_inputs(problem_dir: Path) -> ProblemInputs:
    if not problem_dir.exists():
        raise InputValidationError(f"Problem directory does not exist: {problem_dir}")
    if not problem_dir.is_dir():
        raise InputValidationError(f"Problem path is not a directory: {problem_dir}")

    question_path = problem_dir / "QUESTION.md"
    background_path = problem_dir / "BACKGROUND.md"
    question_text = _read_required_markdown(question_path)
    background_text = _read_required_markdown(background_path)
    problem_id = problem_dir.name

    return ProblemInputs(
        problem_id=problem_id,
        question_text=question_text,
        background_text=background_text,
        question_hash=sha256_text(question_text),
        background_hash=sha256_text(background_text),
    )


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def format_timestamp(ts: datetime) -> str:
    return ts.astimezone(timezone.utc).strftime("%Y%m%d-%H%M%S")


def ensure_output_dir(problem_dir: Path) -> Path:
    problem_dir.mkdir(parents=True, exist_ok=True)
    return problem_dir


def build_transcript(
    problem_inputs: ProblemInputs,
    config: PipelineConfig,
    loops: list[LoopRecord],
    started_at: str,
    finished_at: str,
    final_verdict: str,
) -> str:
    lines: list[str] = []
    lines.append("# Proof Pipeline Transcript")
    lines.append("")
    lines.append(f"- Problem: `{problem_inputs.problem_id}`")
    lines.append(f"- Started (UTC): `{started_at}`")
    lines.append(f"- Finished (UTC): `{finished_at}`")
    lines.append(f"- Max loops: `{config.max_loops}`")
    lines.append(f"- Executed loops: `{len(loops)}`")
    lines.append(f"- Rigor: `{config.rigor}`")
    lines.append(f"- Reviewer perspectives: {len(config.reviewer_perspectives)}")
    lines.append(f"- Final verdict: `{final_verdict}`")
    lines.append("")

    for loop in loops:
        lines.append(f"## Loop {loop.loop_index}")
        lines.append("")
        lines.append("### Researcher Agent")
        lines.append("")
        lines.append(loop.researcher_text.rstrip())
        lines.append("")
        lines.append("### Mentor Agent")
        lines.append("")
        lines.append(loop.mentor_text.rstrip())
        lines.append("")
        lines.append("### Prover Agent")
        lines.append("")
        lines.append(loop.prover_text.rstrip())
        lines.append("")
        lines.append("### Editor Dispatch")
        lines.append("")
        lines.append(f"**Reasoning:** {loop.editor_dispatch.reasoning}")
        lines.append("")
        for persp, pool in loop.editor_dispatch.assignments.items():
            lines.append(f"- {persp} -> {pool}")
        lines.append("")
        lines.append("### Reviews")
        lines.append("")
        for rr in loop.editor_decision.reviewer_results:
            lines.append(f"#### {rr.perspective_name} (by {rr.reviewer_name})")
            lines.append("")
            reviewer_text = loop.reviewer_texts.get(rr.perspective_name, "")
            lines.append(reviewer_text.rstrip())
            lines.append("")
        lines.append("### Editor Decision")
        lines.append("")
        decision = loop.editor_decision
        lines.append(f"**Verdict: `{decision.verdict}`**")
        lines.append("")
        lines.append(f"**Summary:** {decision.summary}")
        lines.append("")
        if decision.feedback:
            lines.append(f"**Feedback ({decision.feedback_target}):** {decision.feedback}")
            lines.append("")

    lines.append("## Final Status")
    lines.append("")
    lines.append(f"Pipeline finished with verdict: `{final_verdict}`.")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# LaTeX generation
# ---------------------------------------------------------------------------

_LATEX_SPECIAL = re.compile(r"([#%&_{}])")
_MATH_DELIMITERS = re.compile(r"(\$\$.*?\$\$|\$.*?\$)", re.DOTALL)


def _escape_latex(text: str) -> str:
    """Escape LaTeX special characters while preserving math mode content."""
    parts = _MATH_DELIMITERS.split(text)
    result: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Inside math delimiters — pass through unchanged
            result.append(part)
        else:
            escaped = _LATEX_SPECIAL.sub(r"\\\1", part)
            escaped = escaped.replace("~", r"\textasciitilde{}")
            escaped = escaped.replace("^", r"\textasciicircum{}")
            result.append(escaped)
    return "".join(result)


def _md_to_latex_body(md_text: str) -> str:
    """Convert lightweight Markdown to LaTeX body text.

    Handles headings, bold, italic, unordered/ordered lists, inline code,
    and fenced code blocks. Math delimiters are preserved.
    """
    lines = md_text.splitlines()
    out: list[str] = []
    in_code_block = False
    in_list = False
    list_kind = ""

    for raw_line in lines:
        # --- fenced code blocks ---
        if raw_line.strip().startswith("```"):
            if in_code_block:
                out.append(r"\end{verbatim}")
                in_code_block = False
            else:
                if in_list:
                    out.append(r"\end{" + list_kind + "}")
                    in_list = False
                out.append(r"\begin{verbatim}")
                in_code_block = True
            continue
        if in_code_block:
            out.append(raw_line)
            continue

        line = raw_line

        # --- headings ---
        heading_match = re.match(r"^(#{1,4})\s+(.*)", line)
        if heading_match:
            if in_list:
                out.append(r"\end{" + list_kind + "}")
                in_list = False
            depth = len(heading_match.group(1))
            title = _escape_latex(heading_match.group(2))
            mapping = {1: "section", 2: "subsection", 3: "subsubsection", 4: "paragraph"}
            cmd = mapping.get(depth, "paragraph")
            out.append(f"\\{cmd}{{{title}}}")
            continue

        # --- list items ---
        ul_match = re.match(r"^(\s*)[-*]\s+(.*)", line)
        ol_match = re.match(r"^(\s*)\d+\.\s+(.*)", line)
        if ul_match or ol_match:
            kind = "itemize" if ul_match else "enumerate"
            content = (ul_match or ol_match).group(2)  # type: ignore[union-attr]
            if not in_list or list_kind != kind:
                if in_list:
                    out.append(r"\end{" + list_kind + "}")
                out.append(r"\begin{" + kind + "}")
                in_list = True
                list_kind = kind
            out.append(r"\item " + _escape_latex(content))
            continue

        # Close list on non-list, non-blank line
        if in_list and line.strip():
            out.append(r"\end{" + list_kind + "}")
            in_list = False

        # --- blank line ---
        if not line.strip():
            out.append("")
            continue

        # --- normal paragraph line ---
        escaped = _escape_latex(line)
        # bold
        escaped = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", escaped)
        # italic
        escaped = re.sub(r"\*(.+?)\*", r"\\textit{\1}", escaped)
        # inline code
        escaped = re.sub(r"`([^`]+)`", r"\\texttt{\1}", escaped)
        out.append(escaped)

    if in_list:
        out.append(r"\end{" + list_kind + "}")
    if in_code_block:
        out.append(r"\end{verbatim}")

    return "\n".join(out)


_SEVERITY_COLORS = {
    "critical": "red",
    "major": "orange",
    "minor": "blue",
}

_VERDICT_COLORS = {
    "accept": "green",
    "right_track": "orange",
    "wrong_track": "red",
}


def build_latex(
    problem_inputs: ProblemInputs,
    config: PipelineConfig,
    loops: list[LoopRecord],
    started_at: str,
    finished_at: str,
    final_verdict: str,
) -> str:
    """Generate a self-contained LaTeX document from pipeline results."""
    verdict_color = _VERDICT_COLORS.get(final_verdict, "black")
    escaped_id = _escape_latex(problem_inputs.problem_id)

    preamble = (
        r"\documentclass[11pt,a4paper]{article}" "\n"
        r"\usepackage[utf8]{inputenc}" "\n"
        r"\usepackage[T1]{fontenc}" "\n"
        r"\usepackage{amsmath,amssymb,amsthm}" "\n"
        r"\usepackage[margin=1in]{geometry}" "\n"
        r"\usepackage{enumitem}" "\n"
        r"\usepackage[dvipsnames]{xcolor}" "\n"
        r"\usepackage{hyperref}" "\n"
        r"\usepackage{booktabs}" "\n"
        r"\usepackage{fancyhdr}" "\n"
        "\n"
        r"\definecolor{red}{RGB}{204,0,0}" "\n"
        r"\definecolor{orange}{RGB}{204,102,0}" "\n"
        r"\definecolor{blue}{RGB}{0,102,204}" "\n"
        r"\definecolor{green}{RGB}{0,153,51}" "\n"
        "\n"
        r"\newtheorem{theorem}{Theorem}" "\n"
        r"\newtheorem{lemma}[theorem]{Lemma}" "\n"
        "\n"
        r"\pagestyle{fancy}" "\n"
        r"\fancyhf{}" "\n"
        r"\fancyhead[L]{Proof Pipeline Report}" "\n"
        r"\fancyhead[R]{Problem \texttt{" + escaped_id + r"}}" "\n"
        r"\fancyfoot[C]{\thepage}" "\n"
        "\n"
        r"\title{Proof Pipeline Report\\[0.5em]"
        r"\large Problem \texttt{" + escaped_id + r"}}" "\n"
        r"\author{Multi-Agent Proof Pipeline}" "\n"
        r"\date{" + _escape_latex(started_at[:10]) + r"}" "\n"
    )

    summary_body = (
        r"\begin{document}" "\n"
        r"\maketitle" "\n"
        r"\begin{abstract}" "\n"
        r"Automated proof analysis report generated by the multi-agent proof pipeline. "
        r"The pipeline executed \textbf{" + str(len(loops)) + r"} loop(s) with "
        r"\textbf{" + str(len(config.reviewer_perspectives)) + r"} reviewer perspectives. "
        r"Final verdict: \textcolor{" + verdict_color + r"}{\textbf{" + final_verdict + r"}}." "\n"
        r"\end{abstract}" "\n"
        "\n"
        r"\section*{Summary}" "\n"
        r"\begin{tabular}{ll}" "\n"
        r"\toprule" "\n"
        r"Problem ID & \texttt{" + escaped_id + r"} \\" "\n"
        r"Started & \texttt{" + _escape_latex(started_at) + r"} \\" "\n"
        r"Finished & \texttt{" + _escape_latex(finished_at) + r"} \\" "\n"
        r"Max loops & " + str(config.max_loops) + r" \\" "\n"
        r"Executed loops & " + str(len(loops)) + r" \\" "\n"
        r"Rigor target & " + _escape_latex(config.rigor) + r" \\" "\n"
        r"Reviewer perspectives & " + str(len(config.reviewer_perspectives)) + r" \\" "\n"
        r"Final verdict & \textcolor{" + verdict_color + r"}{\textbf{" + final_verdict + r"}} \\" "\n"
        r"\bottomrule" "\n"
        r"\end{tabular}" "\n"
        "\n"
        r"\bigskip" "\n"
        r"\noindent\textbf{Reviewer perspectives:}" "\n"
        r"\begin{enumerate}" "\n"
    )
    for p in config.reviewer_perspectives:
        summary_body += (
            r"\item \textbf{" + _escape_latex(p.name) + r"}: "
            + _escape_latex(p.description) + "\n"
        )
    summary_body += r"\end{enumerate}" "\n\n"

    # --- Per-loop sections ---
    loop_sections = ""
    for loop in loops:
        decision = loop.editor_decision
        v_color = _VERDICT_COLORS.get(decision.verdict, "black")
        loop_sections += (
            r"\section{Loop " + str(loop.loop_index) + r"}" "\n"
            r"\noindent Editor verdict for this loop: "
            r"\textcolor{" + v_color + r"}{\textbf{" + decision.verdict + r"}}" "\n\n"
        )

        # Researcher
        loop_sections += r"\subsection{Researcher}" "\n"
        loop_sections += _md_to_latex_body(loop.researcher_text) + "\n\n"

        # Mentor
        loop_sections += r"\subsection{Mentor}" "\n"
        loop_sections += _md_to_latex_body(loop.mentor_text) + "\n\n"

        # Proof
        loop_sections += r"\subsection{Proof}" "\n"
        loop_sections += _md_to_latex_body(loop.prover_text) + "\n\n"

        # Editor dispatch
        loop_sections += r"\subsection{Editor Dispatch}" "\n"
        loop_sections += (
            r"\noindent\textit{Reasoning:} "
            + _escape_latex(loop.editor_dispatch.reasoning) + "\n"
        )
        loop_sections += r"\begin{itemize}" "\n"
        for persp, pool in loop.editor_dispatch.assignments.items():
            loop_sections += (
                r"\item " + _escape_latex(persp) + r" $\to$ "
                + _escape_latex(pool) + "\n"
            )
        loop_sections += r"\end{itemize}" "\n\n"

        # Reviewer feedback
        loop_sections += r"\subsection{Reviewer Feedback}" "\n"
        for rr in decision.reviewer_results:
            loop_sections += (
                r"\subsubsection{" + _escape_latex(rr.perspective_name)
                + r" (by " + _escape_latex(rr.reviewer_name) + r")}" "\n"
            )
            if not rr.issues:
                loop_sections += r"\noindent No issues identified." "\n\n"
            else:
                loop_sections += r"\begin{enumerate}" "\n"
                for issue in rr.issues:
                    sev_color = _SEVERITY_COLORS.get(issue.severity, "black")
                    loop_sections += (
                        r"\item[\textcolor{" + sev_color + r"}{\textbullet}] "
                        r"\textbf{[" + issue.severity.upper() + r"]} "
                        + _escape_latex(issue.location) + ": "
                        + _escape_latex(issue.reason) + "\n"
                        r"\\" "\n"
                        r"\textit{Required fix:} " + _escape_latex(issue.required_fix) + "\n"
                        r"\\" "\n"
                        r"\textit{Suggestion:} " + _escape_latex(issue.suggestion) + "\n"
                    )
                loop_sections += r"\end{enumerate}" "\n\n"

            if rr.residual_concerns:
                loop_sections += (
                    r"\noindent\textit{Residual concerns:}" "\n"
                    r"\begin{itemize}" "\n"
                )
                for concern in rr.residual_concerns:
                    loop_sections += r"\item " + _escape_latex(concern) + "\n"
                loop_sections += r"\end{itemize}" "\n\n"

        # Editor decision
        loop_sections += r"\subsection{Editor Decision}" "\n"
        loop_sections += (
            r"\noindent\textbf{Verdict:} \textcolor{"
            + v_color + r"}{\textbf{" + decision.verdict + r"}}" "\n\n"
        )
        loop_sections += (
            r"\noindent\textbf{Summary:} " + _escape_latex(decision.summary) + "\n\n"
        )
        if decision.feedback:
            loop_sections += (
                r"\noindent\textbf{Feedback ("
                + _escape_latex(decision.feedback_target)
                + r"):} " + _escape_latex(decision.feedback) + "\n\n"
            )

    # --- Final verdict ---
    final_section = (
        r"\section{Final Verdict}" "\n"
        r"\noindent The pipeline finished with verdict: "
        r"\textcolor{" + verdict_color + r"}{\textbf{" + final_verdict + r"}}." "\n\n"
    )

    last_loop = loops[-1]
    if last_loop.editor_decision.verdict == "accept":
        final_section += (
            r"\noindent The managing editor accepted the proof in loop "
            + str(last_loop.loop_index) + r"." "\n"
        )

    closing = r"\end{document}" "\n"

    return preamble + "\n" + summary_body + loop_sections + final_section + closing


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def write_meta(
    path: Path,
    run_result: PipelineRunResult,
    input_hashes: dict[str, str],
) -> None:
    payload = run_result.to_meta_dict()
    payload["input_hashes"] = input_hashes
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
