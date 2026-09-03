"""
Phase 2 — RAG Ingestion

Loads the raw recipe dataset, chunks it sensibly (probably per-recipe, not
arbitrary character splits), generates embeddings, and stores them in a local
vector store.

TODO:
- def load_recipes(path: str) -> list[dict]
- def chunk_recipe(recipe: dict) -> list[str]
- def embed_and_store(chunks: list[str]) -> None  (Chroma or FAISS)
"""
