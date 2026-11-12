from typing import Literal
from pydantic import BaseModel, ConfigDict, computed_field

# --- Unit vocabulary ---
Unit = Literal["g", "kg", "ml", "l", "tsp", "tbsp", "cup", "piece", "pinch"]

# --- Sub-models ---
class Ingredient(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    quantity: float | None = None   # None for "salt to taste"
    unit: Unit | None = None
    note: str | None = None         # "minced", "divided"

class Times(BaseModel):
    model_config = ConfigDict(extra="forbid")
    prep_minutes: int | None = None
    cook_minutes: int | None = None

    @computed_field
    @property
    def total_minutes(self) -> int | None:
        if self.prep_minutes is None and self.cook_minutes is None:
            return None
        return (self.prep_minutes or 0) + (self.cook_minutes or 0)
    
class Nutrition(BaseModel):
    model_config = ConfigDict(extra="forbid")
    calories: float | None = None
    protein_g: float | None = None
    carbohydrates_g: float | None = None
    fat_g: float | None = None

class Source(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    url: str | None = None
    license: str | None = None

# --- Main model ---
class Recipe(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    title: str
    description: str | None = None
    status: Literal["draft", "finished"] = "finished"
    cuisine: str | None = None
    category: str | None = None
    tags: list[str] = []
    servings: int | None = None
    times: Times
    ingredients: list[Ingredient]
    instructions: list[str]
    nutrition_per_serving: Nutrition | None = None
    dietary: list[str] = []
    source: Source | None = None