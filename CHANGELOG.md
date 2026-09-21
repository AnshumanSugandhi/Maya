# Changelog

All notable changes to the MAYA AI Agent OS project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.1.0-alpha] - Unreleased (End of Sprint 0)

### Added
- **Architecture Skeleton:** Established the core directory structure (`src/maya/core`, `brain`, `memory`, `tools`, `agents`, `dashboard`, `security`).
- **Configuration System:** Added lightweight, dependency-free `AppConfig` and `ConfigManager` to load settings from `.env` and `config/models.json`.
- **Logging System:** Added standard-library logging that outputs to console and a rotating file in `logs/maya.log`.
- **Test Infrastructure:** Added `tests/conftest.py` for environment variables mocking and initial tests for the configuration system (`tests/test_core/test_config.py`).
- **Documentation:** Added Architecture (`docs/architecture.md`), Product Requirements Document (`docs/PRD.md`), and Master Backlog (`docs/master_backlog.md`).
- **Entry Point:** Added `src/maya/main.py` which successfully initializes the MAYA OS state.
