"""
Phase 1 — LLM Client (swap point for Phase 5)

Thin wrapper around whichever LLM provider is active. Everything else in the
app should call this module, not a specific provider's SDK directly — that's
what makes swapping Gemini free-tier -> real Claude API (Phase 5) a one-file
change instead of a rewrite.

TODO:
- def generate(prompt: str, system: str = None, stream: bool = False) -> str
- Start with Gemini free-tier client
- Later: branch on config.LLM_PROVIDER to call Claude's Messages API instead
"""
