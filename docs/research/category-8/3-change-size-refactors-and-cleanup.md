# Category 8 - Change Size, Refactors, and Cleanup

Date: 2026-05-02

## Purpose

Research how to decide when a change is too large for autonomous execution, and how to make cleanup/deletion a required part of agent work without creating reckless deletion behavior.

## Sources Reviewed

- Google Engineering Practices, Small CLs: https://google.github.io/eng-practices/review/developer/small-cls.html
- Martin Fowler, Branch by Abstraction: https://martinfowler.com/bliki/BranchByAbstraction.html
- Martin Fowler, Refactoring: https://martinfowler.com/books/refactoring.html
- OpenRewrite docs and FAQ: https://docs.openrewrite.org/
- Aider git integration: https://aider.chat/docs/git.html
- Search Engine Land agent-skills article: https://searchengineland.com/build-seo-agent-skills-476252

## Key Findings

### Large change risk is review risk

Google's code review guidance emphasizes that small changes are easier to review, less likely to introduce bugs, easier to merge, easier to roll back, and easier to design well. This is directly relevant to agents because humans reviewing agent work often have even less context than a human author.

The practical definition of "large" should not be only line count. Important dimensions:

- number of files touched;
- number of subsystems touched;
- public API or schema changes;
- dependency and build changes;
- auth/security/infrastructure changes;
- whether behavior and refactoring are mixed;
- whether rollback is simple;
- whether tests isolate the expected behavior.

Google's guideline says there are no hard rules; 100 lines is often reasonable and 1000 lines is often too large, but file spread and conceptual scope matter. A 200-line change across 50 files can be too large.

### Refactors should usually be separated from behavior changes

Google recommends separating refactorings from feature changes when the refactor would make review harder. Fowler's refactoring guidance also frames refactoring as small behavior-preserving transformations.

For The Agent Loop:

- small local cleanup can be included in the same change;
- broad refactoring should usually become its own Goal or sub-goal;
- behavior-changing work should not hide inside a formatting or cleanup pass;
- if a refactor is needed to make a feature clean, the agent should say so before doing it.

### Large migrations should be incremental

Fowler's Branch by Abstraction pattern is useful for agent work: large replacements can be done through intermediate abstractions, parallel implementations, feature flags, and gradual migration while keeping the system working.

For The Agent Loop, this supports a stop rule:

> If the agent believes the task requires a broad rewrite, it should propose an incremental migration plan before implementation.

### Cleanup is mandatory, but deletion needs evidence

The project already decided that agents tend to avoid removing code and that dead code accumulation is a problem. Research adds a second constraint: deletion can also be unsafe without proof.

OpenRewrite is useful because it emphasizes deterministic, semantically informed transformation. Its FAQ warns that even simple removal can be incorrect when semantics are not fully understood. This supports a policy of "remove with trace evidence," not "delete by vibe."

### Deleting whole obsolete files can be easier to review than tangled edits

Google's small-CL guidance treats deletion of an entire file as often simpler to review than many detailed edits. That matters for this project: the framework should not make deletion taboo. It should require proof and scope clarity.

## Decided Large-Rework Gate

The agent should stop and ask before implementation if any of these are true:

- likely touches more than one subsystem;
- likely changes public APIs, schemas, auth, billing, security, deployment, or infrastructure;
- likely touches more than about 10 files or produces a diff too large to review comfortably;
- mixes broad refactoring with behavior change;
- requires migrating data or changing persistent storage shape;
- requires removing or replacing a major dependency;
- changes architecture rather than implementing inside current architecture;
- cannot be safely verified with existing or easily added tests;
- rollback would be hard.

Line count can be a weak signal, not a rule. A small auth change may be high risk; a large generated deletion may be low risk if clearly obsolete and tested.

## Decided Cleanup Checklist

When removing or replacing a feature, the agent should:

1. Identify entrypoints: routes, commands, handlers, UI links, scheduled jobs, config, docs.
2. Search references with `rg` or language-aware tools.
3. Remove unused implementation code.
4. Remove or update tests tied to removed behavior.
5. Remove stale docs, examples, fixtures, and config.
6. Remove dead dependencies only when no remaining references require them.
7. Run focused tests/build/lint.
8. Report anything intentionally left behind and why.

This checklist should live in v0.1 if cleanup is part of the scaffold's behavioral promise.

## Decided Cleanup Stop Rules

Ask before deletion when:

- references are ambiguous;
- code may be public API;
- code may be used dynamically or by reflection;
- deleting generated files could break build artifacts;
- tests are missing and behavior is hard to infer;
- the deletion is broad and not explicitly requested.

Proceed without asking when:

- deletion is explicitly requested;
- references are checked;
- affected behavior is tested or otherwise verified;
- the files are clearly generated/temp artifacts under known safe directories;
- the agent records the cleanup evidence.

## Applied Decisions

- v0.1 uses hybrid large-rework thresholds. Numeric size is a weak signal only.
- Cleanup/deletion discipline is required during both Build and Reflect, with different jobs.
- During Build, cleanup is mandatory when the change removes or replaces behavior.
- During Reflect, cleanup covers stale docs, dead questions, obsolete memory, temp files, contradictions, and experiment hygiene.
- Language-specific cleanup tools are deferred to later skills. v0.1 should mention `rg` plus language-aware tools when available.
- Dynamic-language uncertainty is an ask trigger when reference search is weak or behavior is hard to infer.
