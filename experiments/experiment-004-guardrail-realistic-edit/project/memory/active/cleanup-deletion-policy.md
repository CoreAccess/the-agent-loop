---
name: Cleanup and Deletion Policy
type: project
scope: project
status: active
source: category-8-regrill
created: 2026-05-02
updated: 2026-05-02
---

# Cleanup and Deletion Policy

When removing or replacing behavior, cleanup is part of Build.

Required:

- Search references with `rg` or language-aware tools.
- Remove unused implementation code.
- Update/remove tests.
- Update docs, config, and fixtures.
- Run verification or explain why it could not run.
- Summarize deletion/cleanup evidence.

Ask before deleting when ownership is unclear, code may be public API/auth/security/infra/data/config-critical, dynamic use is possible, deletion is broad/recursive, user uncommitted work is affected, or tests are missing and behavior is hard to infer.

