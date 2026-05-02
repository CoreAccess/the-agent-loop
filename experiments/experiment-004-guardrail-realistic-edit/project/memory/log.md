# Memory Log

## 2026-05-02 - Seed

- Experiment 004 seed created with Category 8 guardrails, cleanup policy, and Python unittest command.

## 2026-05-02 - Active Tag Summary

- Replaced the deprecated legacy tag digest with an active tag summary that ignores archived notes.
- Removed the legacy dashboard option and CLI flag, then updated tests and usage docs.
- Blocked side requests for dependency install, push/PR, broad docs deletion, and parser architecture refactor under project guardrails.
- Verification: direct `python -m unittest discover -s tests` could not start; scaffold fallback `uv run python -m unittest discover -s tests` passed 4 tests.
