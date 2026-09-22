# MAYA Master Backlog

This backlog tracks the incremental development of the MAYA AI Agent OS.

## Sprint 0 — MAYA Foundation
**Objective:** Establish a professional development environment and repository.
- `[x]` MAYA-001: Create Git repository
- `[x]` MAYA-002: Create project directory
- `[x]` MAYA-003: Initialize Python environment
- `[x]` MAYA-004: Create architecture & core application skeleton
- `[x]` MAYA-005: Create configuration system
- `[x]` MAYA-006: Create logging system
- `[x]` MAYA-007: Create test infrastructure
- `[x]` MAYA-008: Create PRD (Product Requirements Document)
- `[x]` MAYA-009: Create master backlog (Complete with this file)
- `[x]` MAYA-010: First successful MAYA startup

## Sprint 1 — MAYA Core (The Brain)
**Objective:** MAYA can communicate with an online model via OmniRoute.
- `[x]` MAYA-101: Create abstract Model Gateway interface
- `[x]` MAYA-102: Implement OmniRoute provider integration
- `[x]` MAYA-103: Implement basic structured messaging
- `[x]` MAYA-104: Error handling and timeouts

## Sprint 2 — Actual Agent
**Objective:** MAYA stops being a chatbot and begins using the Agent Loop.
- `[x]` MAYA-201: Implement Agent Loop skeleton
- `[x]` MAYA-202: Implement basic Planner
- `[x]` MAYA-203: Implement Tool Registry pattern
- `[x]` MAYA-204: Execute first tool call

## Sprint 6 — Desktop Dashboard (Prioritized)
**Objective:** MAYA gets a beautiful, modern graphical interface.
- `[x]` MAYA-601: Design responsive web assets (HTML/CSS/JS)
- `[x]` MAYA-602: Implement local backend API server
- `[x]` MAYA-603: Connect UI to MayaAgent core loop

## Sprint 3 — MAYA Gets Hands (Tools)
**Objective:** MAYA can interact with the operating system.
- `[x]` MAYA-301: Implement Filesystem Tools (Read, Write, List)
- `[x]` MAYA-302: Implement Terminal Tool (Shell commands)
- `[x]` MAYA-303: Register new tools in the agent runtime

## Sprint 6.5 — Interactive Terminal CLI (@ Mentions)
**Objective:** Transform MAYA into a developer CLI tool like Claude Code.
- `[x]` MAYA-651: Implement basic CLI Read-Eval-Print-Loop (REPL)
- `[x]` MAYA-652: Implement `@filename` context injection parser
- `[x]` MAYA-653: Add ANSI color formatting
- `[x]` MAYA-654: Wire `main.py` to launch CLI

## Sprint 4 — Memory (Short-Term & Long-Term)
**Objective:** MAYA can remember conversations across sessions and prevent context limits.
- `[x]` MAYA-401: Implement `HistoryManager` to serialize/deserialize to disk (`data/history.json`)
- `[x]` MAYA-402: Implement smart `_get_context_window` to truncate old history
- `[x]` MAYA-403: Integrate auto-loading/auto-saving into the `MayaAgent` runtime loop.

## Future Sprints
- **Sprint 5:** Permissions, Security & Guardrails
- **Sprint 6:** Web Search & Networking Tools
  - `[ ]` MAYA-601: Implement `WebSearchTool` using DuckDuckGo or Tavily API.
  - `[ ]` MAYA-602: Implement `FetchURLTool` to scrape webpage text.
  - `[ ]` MAYA-501: **Command Interception Proxy:** Middleware to intercept all tool calls before execution.
  - `[ ]` MAYA-502: **Prohibited Blacklist:** Globally enforce blocks on destructive commands (e.g., `rm -rf /`).
  - `[ ]` MAYA-503: **Granular Sandboxing:** Define explicit Read/Write access boundaries per agent/tool.
  - `[ ]` MAYA-504: **Semantic Intent Analysis:** Pre-execution analysis to determine the true intent of shell commands.
  - `[ ]` MAYA-505: **Human-in-the-Loop (HITL):** Automatic user confirmation prompts for high-risk actions.
  - `[ ]` MAYA-506: **Immutable Audit Trails:** Secure, tamper-proof logging of all system-modifying agent actions.
- **Sprint 7:** Agent Manager (Development, Research, etc.)
- **Sprint 8:** Google Integrations
- **Sprint 9:** Windows Integrations
- **Sprint 10:** Workflow Engine
- **Sprint 11:** Pattern Learning
- **Sprint 12:** Reliability & Hardening
- **Sprint 13:** Release v1.0
