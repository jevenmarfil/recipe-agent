"""
Phase 3 — MCP Server

Wraps the plain functions in tools/ and exposes them over MCP so the agent
(as an MCP client) can discover and call them without hardcoded schemas.

TODO:
- Register nutrition, conversion, substitution tools
- Handle the MCP protocol handshake / tool discovery
- Run as a standalone process the agent connects to
"""
