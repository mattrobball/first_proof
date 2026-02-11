"""Rough cost tracking for pipeline runs.

Accumulates token usage reported by API backends (exact) and estimated
from text length for CLI backends (~4 chars per token).  The module-level
``tracker`` instance is written to by backends and read by the runner.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# (provider, model) -> (input $/MTok, output $/MTok)
# Approximate — update when pricing changes.
MODEL_PRICING: dict[tuple[str, str], tuple[float, float]] = {
    ("anthropic", "claude-opus-4-6"): (15.0, 75.0),
    ("claude", "claude-opus-4-6"): (15.0, 75.0),
    ("openai", "gpt-5.3-codex"): (3.0, 15.0),
    ("codex", "gpt-5.3-codex"): (3.0, 15.0),
    ("gemini", "gemini-3-pro-preview"): (1.25, 10.0),
}

_CHARS_PER_TOKEN = 4


def estimate_tokens(text: str) -> int:
    """Estimate token count from character length."""
    return max(1, len(text) // _CHARS_PER_TOKEN)


def _lookup_pricing(provider: str, model: str) -> tuple[float, float]:
    """Return (input $/MTok, output $/MTok), falling back to (0, 0)."""
    key = (provider, model)
    if key in MODEL_PRICING:
        return MODEL_PRICING[key]
    for (_, m), rates in MODEL_PRICING.items():
        if m == model:
            return rates
    return (0.0, 0.0)


@dataclass
class CostTracker:
    """Accumulates token usage across backend calls."""

    _records: list[tuple[str, str, int, int, bool]] = field(default_factory=list)

    def record(
        self,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        *,
        estimated: bool = False,
    ) -> None:
        self._records.append(
            (provider, model, input_tokens, output_tokens, estimated)
        )

    def total_tokens(self) -> tuple[int, int]:
        return (
            sum(r[2] for r in self._records),
            sum(r[3] for r in self._records),
        )

    def total_cost(self) -> float:
        total = 0.0
        for provider, model, in_tok, out_tok, _ in self._records:
            in_rate, out_rate = _lookup_pricing(provider, model)
            total += in_tok * in_rate / 1_000_000
            total += out_tok * out_rate / 1_000_000
        return total

    def summary_line(self) -> str:
        if not self._records:
            return "no usage recorded"
        in_tok, out_tok = self.total_tokens()
        cost = self.total_cost()
        any_estimated = any(r[4] for r in self._records)
        prefix = "~" if any_estimated else ""
        return (
            f"{prefix}{in_tok + out_tok:,} tokens "
            f"({in_tok:,} in, {out_tok:,} out), "
            f"est. cost ~${cost:.2f}"
        )

    def reset(self) -> None:
        self._records.clear()


# Module-level instance — backends record here, runner reads at the end.
tracker = CostTracker()
