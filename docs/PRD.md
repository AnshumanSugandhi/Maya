# MAYA Product Requirements Document (PRD)

## 1. Vision & Purpose
MAYA is a personal desktop AI agent manager. The primary objective is to build an agentic assistant that can automate tasks, maintain context and memory, and orchestrate execution using local capabilities and online Large Language Models (via OmniRoute). 

Unlike a standard chatbot, MAYA acts as a localized operating layer that decides *how* to solve a problem by generating plans and calling local tools.

## 2. Core Architecture
- **Desktop Runtime (Local):** Controls the agent loop, memory, state, planning, evaluation, and tool execution.
- **Model Gateway (Remote via OmniRoute):** Offloads heavy reasoning to the best or most efficient LLM (e.g., Gemini for reasoning, simple models for basic generation).

## 3. Key Features

### 3.1. Agent Loop
MAYA will follow a strict reasoning cycle:
`Understand -> Plan -> Verify Memory -> Select Tools -> Execute -> Observe -> Evaluate -> Respond / Replan`

### 3.2. Memory Systems
Instead of relying purely on conversation history, MAYA implements structured memory stores:
- **Short-Term:** Immediate context of the active task.
- **Long-Term:** User preferences, API keys, global configurations.
- **Episodic:** Past interactions, errors, and lessons learned.
- **Procedural:** Learned workflows (e.g., "how to start a Django project").

### 3.3. Tool System
MAYA executes actions via strict tool interfaces:
- Filesystem (read/write/search)
- Terminal (run commands)
- VS Code (project inspection)
- Browser/Web search

### 3.4. Permission & Security Tiering
To ensure safety, actions are strictly tiered.
- **Level 0 (Read):** Unrestricted local read access.
- **Level 1 (Suggest):** Generates ideas and code.
- **Level 2 (Execute Safely):** Runs builds/tests locally.
- **Level 3 (Sensitive):** Requires explicit user confirmation (e.g., Git Push, Delete Files, Send Email).
- **Level 4 (Never Autonomous):** Destructive or financial operations are hard-blocked.

## 4. Technical Constraints
- The core runtime must remain lightweight and dependency-free where possible to run on an i5-8350U laptop.
- Configuration and API keys must not be hardcoded or checked into version control.
- Must run on Windows via PowerShell.
