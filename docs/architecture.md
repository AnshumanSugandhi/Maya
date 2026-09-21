# MAYA Architecture

## Overview
MAYA is a personal desktop AI agent manager. The architecture is designed to offload heavy reasoning to online models (via OmniRoute) while keeping the orchestration, state, memory, tools, and visual dashboard local on the user's desktop.

## Core Components

### 1. Agent Runtime (`maya.core`)
The brain orchestrating the execution loop:
- **Planner:** Breaks down user intent into steps.
- **Executor:** Runs the plan, selects appropriate tools.
- **Evaluator:** Verifies outcomes and handles failures.
- **Agent Loop:** The core `Understand -> Plan -> Tool -> Execute -> Observe -> Evaluate -> Respond` cycle.

### 2. The Brain & Model Gateway (`maya.brain`)
Handles reasoning by communicating with remote models.
- **OmniRoute Integration:** Routes tasks to the best or most efficient LLM.
- **Model Selection:** Determines whether to use Gemini, Claude, or a fast/free model based on the task (e.g., coding vs simple chat).

### 3. Memory System (`maya.memory`)
Context and state persistence without retraining the model.
- **Short-term Memory:** Active task, recent steps, immediate context.
- **Long-term Memory:** User preferences, project setups.
- **Episodic Memory:** Past errors and lessons learned.
- **Procedural Memory:** Learned automated workflows.

### 4. Tool Registry (`maya.tools`)
Explicit capabilities granted to MAYA to interact with the system.
- Filesystem
- Terminal
- VS Code
- Git
- Windows/Google integrations

### 5. Permission & Security (`maya.security`)
Strict tiered access.
- **Level 0 (Read):** Inspect screen, read files.
- **Level 1 (Suggest):** Generate code, drafts.
- **Level 2 (Execute Safely):** Run tests, build files.
- **Level 3 (Sensitive):** Requires confirmation (e.g., delete files, push Git, send email).
- **Level 4 (Never Autonomous):** Financial, destructive actions.

### 6. Desktop Dashboard (`maya.dashboard`)
A visually appealing desktop UI to monitor Agent Status, Memory, Tasks, Models, and request user permissions.

## Directory Structure
```
MAYA/
├── src/
│   └── maya/
│       ├── core/       # Agent loop, Planner, Executor
│       ├── brain/      # OmniRoute, reasoning logic
│       ├── memory/     # Different memory stores
│       ├── tools/      # Filesystem, OS interactions
│       ├── agents/     # Specialized (Dev, Research)
│       ├── security/   # Permissions manager
│       └── dashboard/  # Desktop UI
├── tests/
├── docs/
├── scripts/
└── config/
```
