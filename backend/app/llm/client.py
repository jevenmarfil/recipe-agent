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
from google import genai
from app import config

client = genai.Client(api_key=config.GEMINI_API_KEY)

def generate(prompt: str, system: str = None) -> str:
    response = client.models.generate_content(
        model=config.LLM_MODEL,
        contents=prompt,
        config={"system_instruction": system} if system else None,
    )
    print("Full response object:")
    print(response)
    print("---")
    print("Just the text:", response.text)
    print("---")
    print("Usage metadata:", response.usage_metadata)
    print("Configured model:", config.LLM_MODEL)
    print("Actual model used:", response.model_version)
    return response.text

