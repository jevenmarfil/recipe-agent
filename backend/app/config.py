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

import os
from pathlib import Path
from dotenv import load_dotenv

# Explicitly point to backend/.env, regardless of current working directory
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.5-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("Looking for .env at:", env_path)
print("Does it exist?", env_path.exists())