"""
Phase 1 — Config

Central place for environment-based settings: API keys, model name/provider,
and anything else that should change between local dev, real Claude API, and
AWS deployment without touching code elsewhere.

TODO:
- Load from a .env file (python-dotenv or pydantic-settings)
- LLM_PROVIDER = "gemini" | "claude"  (this is the switch Phase 5 flips)
- MODEL_NAME
- API keys (never commit these — see .gitignore)
"""
