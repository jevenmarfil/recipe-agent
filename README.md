# Recipe Agent — Learning Project

A hands-on project to learn agentic AI development (LangChain/LangGraph, RAG, MCP) and
prepare for the **Claude Certified Developer – Foundations (CCDV-F)** exam, by building a
full-stack recipe-builder agent: FastAPI + LangGraph backend, Vue.js frontend, deployed on AWS.

## What it does

Takes a natural-language query (e.g. "I have chicken, spinach, and rice — something under
500 calories?"), retrieves relevant real recipes via RAG, reasons over constraints via a
LangGraph agent, calls tools (nutrition calc, unit conversion, substitutions) via an MCP
server, and returns a structured recipe.

## Tech stack

- **Backend:** Python, FastAPI, LangChain/LangGraph, MCP
- **LLM:** Free-tier (Gemini) during build phases → real Claude API from Phase 5 onward
- **RAG:** Local vector store (Chroma/FAISS)
- **Frontend:** Vue 3 + Vite
- **Deploy (capstone):** AWS (Lambda/ECS + Bedrock, S3 + CloudFront)

## Folder structure

See `backend/app/` for the module breakdown (api, agent, rag, tools, mcp_server, llm).

---

## Getting Started (Fresh Machine Setup)

> Written for someone who just got this repo off GitHub and has a brand-new PC with
> nothing installed yet. If you already have these tools, skip ahead.

### 1. Install Git
Git is the version control tool GitHub is built on — you need it locally to
clone (download) and push changes to this repo.
- **Windows:** download from [git-scm.com](https://git-scm.com/downloads), run the
  installer, default options are fine.
- **Mac:** open Terminal and run `git --version` — macOS will prompt you to install
  developer tools if it's missing.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or your distro's package manager.
- **Verify:** open a terminal and run `git --version`. You should see a version number.

### 2. Install an IDE (VS Code)
An IDE is where you'll actually write and edit code. VS Code is free and works on
Windows/Mac/Linux.
- Download from [code.visualstudio.com](https://code.visualstudio.com/)
- Install it, then open it once so it finishes first-time setup.
- Useful extensions to install from VS Code's Extensions panel (optional but helpful):
  Python, Vue - Official, GitLens.

### 3. Install Python and Node.js
- **Python** (backend): download from [python.org](https://www.python.org/downloads/),
  3.10+ recommended. Verify with `python --version` (or `python3 --version` on Mac/Linux).
- **Node.js** (frontend): download from [nodejs.org](https://nodejs.org/) — get the LTS
  version. Verify with `node --version`.

### 4. Clone this repo
In a terminal, navigate to the folder where you want the project to live, then:
```
git clone <your-repo-url>
cd recipe-agent
```
This downloads the whole project (matching the skeleton structure below) onto your machine.

### 5. Open it in VS Code
```
code .
```
(Run this from inside the `recipe-agent` folder.) This opens the whole project so you can
see the folder tree on the left and edit files directly.

### 6. Set up the backend environment
```
cd backend
python -m venv .venv
```
Activate it:
- **Windows:** `.venv\Scripts\activate`
- **Mac/Linux:** `source .venv/bin/activate`

Then install dependencies (once `requirements.txt` has real entries, from Phase 1 onward):
```
pip install -r requirements.txt
```
A virtual environment (`venv`) keeps this project's Python packages separate from
anything else on your machine — this avoids version conflicts between projects.

### 7. Set up the frontend (from Phase 4 onward)
```
cd frontend
npm install
npm run dev
```

### 8. Create your own `.env` file
Copy any `.env.example` provided (once one exists) to `.env` in the `backend/` folder,
and fill in your own API keys there. `.env` is already in `.gitignore` — it will never
be committed or pushed to GitHub, which is intentional (never share API keys in a repo).

---

## Progress Tracker

> Update this after each session so picking the project back up doesn't require re-deriving
> where you left off. Check items off as you complete them; add dated notes for anything
> half-finished or any decision you made mid-phase.

### Phase 1 — Claude API + SDK basics
- [ ] `config.py` — env vars, model settings
- [ ] `llm/client.py` — basic LLM call wrapper (Gemini free tier)
- [ ] Tested a plain no-tools, no-RAG call
- [ ] Understand: message structure, system vs user prompt, streaming vs non-streaming
- **Notes:**

### Phase 2 — Tool use + RAG
- [ ] `rag/ingest.py` — load/chunk/embed recipe dataset
- [ ] `rag/retriever.py` — vector search
- [ ] `tools/nutrition.py`
- [ ] `tools/conversion.py`
- [ ] `tools/substitution.py`
- [ ] Each tool tested standalone
- [ ] Manual tool-calling test with LLM
- **Notes:**

### Phase 3 — LangGraph agent + MCP server
- [ ] `agent/state.py` — agent state schema
- [ ] `mcp_server/server.py` — tools exposed via MCP
- [ ] `agent/graph.py` — LangGraph state graph (retrieve → decide → tool call → format)
- [ ] End-to-end query works through the graph
- **Notes:**

### Phase 4 — API wrapper + Vue frontend
- [ ] Decide: streaming vs request-response
- [ ] `api/routes.py` — FastAPI endpoint wrapping the agent
- [ ] Vue app — input + rendered recipe output
- [ ] End-to-end: Vue UI → FastAPI → agent → real response
- **Notes:**

### Phase 5 — Model selection, cost, security 💰 *(first paid step)*
- [ ] Claude API key obtained, small balance added
- [ ] Swapped `llm/client.py` to real Claude API (Haiku)
- [ ] Compared Haiku vs Sonnet on test queries
- [ ] Added prompt caching where useful
- [ ] Input validation + prompt-injection guardrails
- [ ] CORS config for frontend
- **Notes:**

### Phase 6 — Eval, debugging, Claude Code touchpoint
- [ ] Eval set written (10–20 representative queries)
- [ ] Ran eval, logged/debugged failures
- [ ] Used Claude Code for at least one scaffold/refactor task
- **Notes:**

### Phase 7 — AWS deployment (capstone) 💰 *(second paid step)*
- [ ] Chose Lambda vs ECS/Fargate
- [ ] Backend + Bedrock/AgentCore deployed
- [ ] Vue frontend on S3 + CloudFront
- [ ] Ran CCDV-F practice questions per domain

---

## Session Log

> One line per session: date, what you worked on, what's next. Cheap insurance against
> losing context between sessions.

- `YYYY-MM-DD` — Project structure designed, git set up.
