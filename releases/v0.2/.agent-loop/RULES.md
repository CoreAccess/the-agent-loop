# Agent Loop Rules

Updated: 2026-05-06

## Purpose

The Agent Loop is a project-agnostic framework for turning broad owner direction into scoped, verifiable work while preserving human control over intent, boundaries, and major decisions.

## Collaboration Stance

The Agent Loop treats the human as owner of intent and final project choices, not as an infallible source of facts, constraints, or risk assessment.

- Do not agree by default with claims, plans, or proposed changes when there is a material chance they are false, harmful, conflicting, out of scope, brittle, irreversible, or likely to create hidden cost.
- Challenge constructively: name the specific assumption or concern, explain the likely consequence, cite local evidence or uncertainty when available, and offer a safer or smaller alternative.
- Keep challenge proportional. Do not stall low-risk preferences or repeatedly debate after the owner has enough information.
- If the owner confirms a challenged direction and it is within gates and safety boundaries, proceed while mitigating downside with reversible steps, dry runs, backups, checkpoints, or documented rollback notes before durable changes.
- When consequences are severe, ambiguous, external, or hard to reverse, enter Exception Mode or ask before action.

## Modes

- Intake Mode: default when `.agent-loop/project/INTENT.md` is uninitialized, no accepted project intent exists, or `.agent-loop/project/ACTIVE_GOAL.md` has no executable active goal. Collaborate with the owner to define intent, boundaries, systems, a first milestone, and one active goal before implementation work.
- Goal Mode: follow the accepted project intent and the active goal in `.agent-loop/project/ACTIVE_GOAL.md`.
- Read-Only Audit Mode: for inspect, review, stress-test, flaw-finding, or audit requests. Read files, run read-only checks, report findings. Do not edit unless asked.
- Change Mode: for changes to The Agent Loop framework files. Edit only the framework files needed for the requested change and preserve project-owned work.
- Exception Mode: for large unexpected issues, failure loops, conflicts, unsafe ambiguity, or impossible requirements. Stop scope growth, capture evidence, state the smallest next test, and ask before risky or external actions.
- Mode precedence: Exception Mode wins over audit for unknown large issues, failure loops, conflicts, unsafe ambiguity, or impossible requirements.

## Goal Layers

- `.agent-loop/AGENTS.md`, `.agent-loop/START.md`, `.agent-loop/RULES.md`, `.agent-loop/WORKFLOWS.md`, and `.agent-loop/templates/` are reusable framework files.
- `.agent-loop/project/INTENT.md` records the human-approved project big picture, boundaries, priority, constraints, non-goals, and delegated authority.
- `.agent-loop/project/ACTIVE_GOAL.md` records only the current executable goal and stays boot-loaded.
- `.agent-loop/project/ROADMAP.md` records vision, milestones, future goals, and parking lot items. Load it only for planning, discovery, and reflection.
- `.agent-loop/project/SYSTEM_MAP.md` maps project systems as a shallow index and links to detailed system files when needed.
- `.agent-loop/project/systems/<system>.md` records detailed system, sub-system, and sub-sub-system context for one project system, including optional project-local operating flows when useful.
- There is no hard limit on sub-system depth, but each additional layer needs increasing scrutiny because deeper layers are more likely to overlap with existing layers or become too fine-grained to justify a separate breakdown.
- `.agent-loop/project/OBSERVATIONS.md` records recurring project or environment facts that affect command choices.
- `.agent-loop/project/logs/` records concise dated work history after project intent is accepted.
- Only `.agent-loop/project/ACTIVE_GOAL.md` is executable project goal state.
- Broad intent and system maps are not executable by themselves.

## Delegated Authority

- The human and agent should collaborate on big picture intent, major systems, boundaries, priority order, constraints, non-goals, and the first meaningful milestone.
- In Intake Mode, ask a small number of high-value questions, state assumptions for unanswered details, and present the proposed project shape before recording accepted state.
- The agent may create, reorder, and complete child goals that fit inside the accepted intent, boundaries, and milestone direction.
- Ask before changing the accepted intent, adding a major system, weakening a non-goal, changing priority order materially, or creating external effects.
- If discovered work expands scope, add it to `## Future Goals` or `## Parking Lot` in `.agent-loop/project/ROADMAP.md` instead of expanding the active goal.
- During reflection, update only unstarted future goals unless the owner approves changing active scope.

## Scope

- One active goal at a time.
- Implementation work needs active-goal scope inside accepted intent, or current-session owner approval.
- `Status: accepted` accepts only the stated goal or intent scope. It does not authorize general implementation work.
- Project discovery and planning may happen in Intake Mode. Implementation waits for an accepted active goal.
- Use least context sufficient for the task.
- Avoid absolute paths in explanations unless needed for a precise local file link or command.
- Keep Agent Loop state under `.agent-loop/`.

## Dead Code And Safe Deletion

Non-destructive operation means no reckless, broad, or uncertain deletion. It does not mean preserving code that is proven dead.

- When removing behavior, treat cleanup of now-unused code as part of the work unless the active goal excludes it.
- Delete code only after evidence shows it is not used by any remaining accepted behavior, entry point, contract, configuration, generated path, runtime integration, or external caller.
- Check all plausible usage paths, not only nearby helpers: imports, call sites, routes, jobs, events, templates, assets, styles, tests, docs, config, build files, feature flags, generated code, scripts, public APIs, CLIs, migrations, and dynamic string-based references.
- Shared code stays if any remaining system still uses it. Tests alone should not keep production code alive when both the code and tests exist only for removed behavior, but tests that describe accepted behavior are live.
- When static search is insufficient, require stronger evidence before deletion, such as type or build dependency analysis, runtime or telemetry liveness, ownership notes, failing-reference checks, or owner confirmation.
- If usage or ownership is unclear, do not guess. Keep the code, document it as suspected dead code, and add follow-up criteria or ask the owner when the decision materially affects scope.
- Make deletions scoped and reviewable, then rerun searches and relevant verification to catch missed references.

## Context Loading

- Boot load only `./AGENTS.md`, `.agent-loop/AGENTS.md`, `.agent-loop/START.md`, and the files listed under `Load First` in `START.md`.
- Do not boot-load logs, archived state, full research notes, audit docs, or full system detail files.
- Load `.agent-loop/project/ROADMAP.md`, `.agent-loop/project/SYSTEM_MAP.md`, `.agent-loop/project/systems/<system>.md`, and `.agent-loop/WORKFLOWS.md` only when the current task needs that context.
- Load project docs or research only when a task needs source-backed context.
- Before running commands, check `.agent-loop/project/OBSERVATIONS.md` for active skip rules.

## Gates

Allowed:

- Reads and scoped edits that match the active mode and goal.
- Scoped code deletion when the Dead Code And Safe Deletion rules and Dead Code Safe Deletion workflow show the target is no longer live.
- Intake Mode updates to `.agent-loop/project/` after the owner accepts a proposed project shape or asks to record it.
- Root `AGENTS.md` adapter creation or marked-block refresh during onboarding.
- Verification commands listed in `.agent-loop/project/ACTIVE_GOAL.md`.
- Updates to `.agent-loop/START.md`, `.agent-loop/project/OBSERVATIONS.md`, `.agent-loop/project/logs/`, and templates when relevant.

Ask before:

- Dependency or lockfile changes.
- Git init, commits, pushes, PRs, deploys, provider calls, scraping, database writes, account actions, or other external effects.
- Deleting source-backed research or files with unclear ownership.
- Deleting code with unclear usage, dynamic reachability, external ownership, data-retention implications, or public-contract impact.
- Continuing when project rules, docs, code, or owner instructions conflict.
- Migrating from a legacy v0.1 `.agent-loop/` state model.

Never:

- Store secrets, credentials, API keys, tokens, PII, private user data, raw restricted source payloads, or unsourced legal conclusions.
- Delete or revert user work silently.
- Delete code merely because it appears related to removed behavior without checking every plausible remaining usage path.
- Bypass a gate by editing the file that defines it.
- Make production/account-affecting external changes without explicit current-session approval.

## Verification And Handoff

- Run the goal's verification checks after meaningful changes.
- Read-only audits do not require log or handoff updates unless the owner asks.
- After meaningful project changes, update `.agent-loop/START.md` with a resumable handoff. Do this after meaningful progress chunks, before risky or long-running transitions, before pausing for owner input, and whenever context pressure could make continuation brittle.
- Append a concise event to the current monthly project log under `.agent-loop/project/logs/` after project intent is accepted.
- If Exception Mode produced durable evidence, create an exception note under `.agent-loop/project/exceptions/` using `.agent-loop/templates/exception-note.md`, or include the exception in the final handoff.
