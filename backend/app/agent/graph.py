"""
Phase 3 — LangGraph Agent

The state graph: nodes for retrieve -> decide -> call tool (via MCP client)
-> format output, with branching/looping for "need more info" cases.

TODO:
- Define nodes as functions operating on state.py's state
- Wire edges (including conditional edges for branching)
- Compile and expose a callable graph for api/routes.py to invoke
"""
