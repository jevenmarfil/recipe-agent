# from app import config
# from app.llm.client import generate

# # Sanity check first — confirm config loaded correctly
# print("Key loaded:", config.GEMINI_API_KEY is not None)
# print("Model:", config.LLM_MODEL)
# print("---")

# # The real test call
# result = generate(
#     prompt="Given chicken, spinach, and rice, suggest a dish name.",
#     system="You are a helpful recipe assistant."
# )

# print("Response:")
# print(result)

# import json
# from app.schemas import Recipe

# r = Recipe.model_validate(json.load(open("data/recipes/recipes.json")))
# print(r.times.total_minutes)   # should print 60

import json
from pydantic import ValidationError
from app.schemas import Recipe

data = json.load(open("data/recipes/recipes.json"))
try:
    recipe = Recipe.model_validate(data)        # from a dict
    print("validated")
    # or: Recipe.model_validate_json(text)      # straight from a JSON string
except ValidationError as e:
    print(e.errors())    # which field, which problem