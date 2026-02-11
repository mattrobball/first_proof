from __future__ import annotations

from pipeline.cost import CostTracker, estimate_tokens


def test_estimate_tokens() -> None:
    assert estimate_tokens("") == 1  # minimum 1
    assert estimate_tokens("abcd") == 1
    assert estimate_tokens("a" * 400) == 100


def test_empty_tracker() -> None:
    t = CostTracker()
    assert t.total_tokens() == (0, 0)
    assert t.total_cost() == 0.0
    assert t.summary_line() == "no usage recorded"


def test_api_recording() -> None:
    t = CostTracker()
    t.record("gemini", "gemini-3-pro-preview", 1000, 500)
    in_tok, out_tok = t.total_tokens()
    assert in_tok == 1000
    assert out_tok == 500
    # 1000 * 1.25/1M + 500 * 10.0/1M = 0.00125 + 0.005 = 0.00625
    assert abs(t.total_cost() - 0.00625) < 1e-9
    assert "estimated" not in t.summary_line()


def test_cli_estimated_recording() -> None:
    t = CostTracker()
    t.record("claude", "claude-opus-4-6", 2000, 1000, estimated=True)
    assert "~" in t.summary_line()
    # 2000 * 15/1M + 1000 * 75/1M = 0.03 + 0.075 = 0.105
    assert abs(t.total_cost() - 0.105) < 1e-9


def test_unknown_model_zero_cost() -> None:
    t = CostTracker()
    t.record("unknown", "mystery-model", 5000, 3000)
    assert t.total_cost() == 0.0
    assert t.total_tokens() == (5000, 3000)


def test_reset() -> None:
    t = CostTracker()
    t.record("gemini", "gemini-3-pro-preview", 100, 50)
    assert t.total_tokens() != (0, 0)
    t.reset()
    assert t.total_tokens() == (0, 0)
    assert t.summary_line() == "no usage recorded"


def test_multiple_records_accumulate() -> None:
    t = CostTracker()
    t.record("gemini", "gemini-3-pro-preview", 1000, 500)
    t.record("claude", "claude-opus-4-6", 2000, 1000, estimated=True)
    in_tok, out_tok = t.total_tokens()
    assert in_tok == 3000
    assert out_tok == 1500
    expected = 0.00625 + 0.105
    assert abs(t.total_cost() - expected) < 1e-9
    # Mixed exact + estimated -> shows ~
    assert "~" in t.summary_line()
