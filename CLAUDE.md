# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A study project exploring AI-powered Linux log analysis using CrewAI multi-agent framework with Claude as the LLM backend. The agent reads server logs and produces technical diagnoses with remediation commands.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Requires a `.env` file with:
```
ANTHROPIC_API_KEY=your_key_here
```

## Running

```bash
python main.py
```

## Architecture

Single-file app (`main.py`) following the CrewAI pattern:

1. **LLM** — `ChatAnthropic` (Claude 3.5 Sonnet) initialized with `ANTHROPIC_API_KEY`
2. **Tool** — `FileReadTool` lets the agent read files from disk
3. **Agent** (`analista_sre`) — SRE specialist role, receives the tool and LLM
4. **Task** (`tarefa_analise`) — instructs the agent to read `logs_servidor.txt` and return a technical summary + remediation command
5. **Crew** — orchestrates agent + task via `.kickoff()`

## Key Dependencies

- `crewai` / `crewai-tools` — agent orchestration
- `langchain-anthropic` — Claude integration via LangChain
- `python-dotenv` — env var loading
