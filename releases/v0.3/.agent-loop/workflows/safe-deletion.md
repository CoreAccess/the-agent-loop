# Safe Deletion Workflow

Use when deleting files or symbols, removing a feature, cleaning up suspected dead code, or deciding whether cleanup is safe.

1. Name the deletion candidate and the behavior, feature, or system that used to own it.
2. Search all plausible usage paths: imports, call sites, routes, jobs, events, templates, assets, styles, tests, docs, config, build files, feature flags, generated code, scripts, public APIs, CLIs, migrations, and dynamic string references.
3. Use language-aware tooling when available, such as type checkers, compiler errors, dependency graphs, test coverage, or liveness telemetry. Use text search as a backstop.
4. Classify each candidate:
   - Live: still used by accepted behavior, an entry point, external contract, runtime config, user data path, or another system. Do not delete unless that behavior is explicitly in scope to remove.
   - Dead: no remaining usage path, no external contract, and remaining references are tied only to removed behavior.
   - Unclear: dynamic reachability, generated ownership, migration/data-retention risk, public API uncertainty, weak test coverage, or ambiguous owner intent. Do not delete without more evidence or owner confirmation.
5. Delete dead candidates in small reviewable groups. Include obsolete tests, docs, styles, config, and adapters when their only purpose was removed behavior.
6. After deletion, rerun usage searches and relevant verification.
7. Record suspected dead code left behind with missing proof and a trigger for revisiting.
8. In handoff, summarize what was deleted, what evidence made it safe, verification run, and suspected dead code intentionally left behind.
