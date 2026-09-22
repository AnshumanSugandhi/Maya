# Changelog

All notable changes to the MAYA AI Agent OS project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] (End of Sprint 1)

### Added
- **Structured Messaging:** Implemented `Message` and `Role` dataclasses in `src/maya/brain/messages.py` to enforce strict communication protocols.
- **Model Gateway Interface:** Created abstract `ModelGateway` interface in `src/maya/brain/gateway.py` to decouple MAYA from specific LLM providers.
- **OmniRoute Integration:** Built a robust, dependency-free HTTP client `OmniRouteGateway` in `src/maya/brain/omniroute.py` that routes requests dynamically based on task type.

## [Unreleased] (End of Sprint 6)

### Added
- **Desktop Dashboard:** Implemented a stunning local web-based UI (`src/maya/dashboard/static/`) featuring glassmorphism, dark mode, and dynamic animated backgrounds.
- **Dashboard Server:** Built a lightweight Python HTTP server (`src/maya/dashboard/server.py`) serving the UI assets and exposing a `/api/chat` endpoint.
- **UI to Agent Integration:** Wired `main.py` to launch the dashboard server instead of the terminal prompt, fully integrating the frontend with the `MayaAgent` core loop.

## [v0.2.0-alpha] - 2026-09-22 (End of Sprint 2)

### Added
- **Tool Registry:** Implemented abstract `Tool` base class and `ToolRegistry` in `src/maya/tools/registry.py` to manage agent capabilities.
- **Agent Planner:** Built `Planner` in `src/maya/core/planner.py` to dynamically construct system prompts with available tools.
- **Core Agent Loop:** Created `MayaAgent` in `src/maya/core/agent.py` to handle the `UNDERSTAND -> PLAN -> EXECUTE` execution loop.
- **Test Tool:** Built `GetTimeTool` in `src/maya/tools/system_tools.py` as a proof of concept.

## [v0.1.1-alpha] - 2026-09-22 (End of Sprint 1)

### Added
- **Architecture Skeleton:** Established the core directory structure (`src/maya/core`, `brain`, `memory`, `tools`, `agents`, `dashboard`, `security`).
- **Configuration System:** Added lightweight, dependency-free `AppConfig` and `ConfigManager` to load settings from `.env` and `config/models.json`.
- **Logging System:** Added standard-library logging that outputs to console and a rotating file in `logs/maya.log`.
- **Test Infrastructure:** Added `tests/conftest.py` for environment variables mocking and initial tests for the configuration system (`tests/test_core/test_config.py`).
- **Documentation:** Added Architecture (`docs/architecture.md`), Product Requirements Document (`docs/PRD.md`), and Master Backlog (`docs/master_backlog.md`).
- **Entry Point:** Added `src/maya/main.py` which successfully initializes the MAYA OS state.
