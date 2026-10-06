from app import config
from app.llm.client import generate

# Sanity check first — confirm config loaded correctly
print("Key loaded:", config.GEMINI_API_KEY is not None)
print("Model:", config.LLM_MODEL)
print("---")

# The real test call
result = generate(
    prompt="Given chicken, spinach, and rice, suggest a dish name.",
    system="You are a helpful recipe assistant."
)

print("Response:")
print(result)

