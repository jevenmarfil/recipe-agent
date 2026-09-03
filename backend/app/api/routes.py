"""
Phase 4 — FastAPI Routes

Wraps the LangGraph agent for HTTP access. This is what the Vue frontend
talks to.

TODO:
- Decide: streaming (SSE) vs plain request-response — lock this in before
  building the frontend against it
- POST /query -> invokes agent/graph.py, returns structured recipe
"""
