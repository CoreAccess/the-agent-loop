# Framework Workflows

Status: framework seed

## Intake To First Goal

Use this when `.agent-loop/project/INTENT.md` is uninitialized, no accepted project intent exists, or `.agent-loop/project/ACTIVE_GOAL.md` has no executable active goal.

1. Capture the rough owner intent in plain language.
2. Ask 3 to 5 high-value questions about audience, outcome, constraints, first success, and known risks.
3. State assumptions for unanswered details instead of asking exhaustive questions.
4. Run light orientation research when domain context can prevent naive system choices.
5. Draft the proposed project shape: intent, boundaries, priority order, constraints, non-goals, major systems, first milestone, and first active goal.
6. Explain the proposed shape to the owner and call out the highest-impact decision points.
7. Ask the owner to accept, revise, or reject the proposed shape.
8. After acceptance, record the accepted state in `.agent-loop/project/INTENT.md`, `.agent-loop/project/ROADMAP.md`, `.agent-loop/project/SYSTEM_MAP.md`, and `.agent-loop/project/ACTIVE_GOAL.md`.
9. Update `.agent-loop/START.md` with the next-session handoff and create the first monthly project log entry.
10. Execute only the accepted active goal.

## Discovery To Execution

Use this when an initialized project receives a broad new request that may become new systems, milestones, or active goals.

1. Capture the rough intent in plain language.
2. Ask a small number of high-value questions about audience, outcome, constraints, and first success.
3. State assumptions for unanswered details instead of asking exhaustive questions.
4. Run light orientation research when domain context can prevent naive system choices.
5. Draft major systems, sub-systems, boundaries, priority order, constraints, and non-goals.
6. Sketch project-local operating flows only where they clarify a major system's repeated work, sequencing, handoffs, or checks.
7. Propose milestone-level future goals.
8. Explain the shape to the human and ask for feedback on the high-impact pieces.
9. Agree on a first meaningful milestone.
10. Create one active goal in `.agent-loop/project/ACTIVE_GOAL.md`.
11. Execute only the active goal.
12. Reflect after completion and adjust unstarted future goals when evidence justifies it.

## Question Budget

- Prefer 3 to 5 high-value questions before creating the first rough shape.
- Ask more only when a missing answer would materially change the big picture or cause unsafe work.
- Use explicit assumptions to keep momentum.
- Ask one question at a time during onboarding unless the owner asks for a batch.

## Constructive Challenge Loop

Use this when an owner claim, plan, or requested change appears materially false, risky, conflicting, out of scope, brittle, irreversible, or likely to create hidden cost.

1. Restate the intended outcome neutrally.
2. Name the specific concern without making it personal.
3. Explain the likely negative consequence and what evidence, rule, or uncertainty supports that concern.
4. Offer a safer, smaller, or more reversible option.
5. Ask for a decision only when the tradeoff is material or the action would cross a gate.
6. If the owner confirms the original direction and it remains within rules and safety boundaries, continue with mitigations such as dry runs, checkpoints, backups, staged rollout, or rollback notes.
7. If the concern involves severe harm, impossible requirements, conflicting instructions, external effects, or unsafe ambiguity, enter Exception Mode.

## Research Cadence

### Orientation Research

Timing: before finalizing the first system map.

Purpose:

- Avoid naive system choices.
- Identify sensitive areas, common user expectations, known constraints, and likely non-goals.

Depth:

- Light and broad.
- Enough to shape systems and boundaries.

### Pre-Milestone Research

Timing: before starting a major milestone or system.

Purpose:

- Improve the next chunk before committing effort.
- Refine useful project-local operating flows and goal criteria for that milestone.

Depth:

- Focused on the next milestone.

### Just-In-Time Research

Timing: during an active goal only when needed to unblock or verify a specific decision.

Purpose:

- Solve the immediate implementation or planning question.

Depth:

- Narrow.
- Do not reopen the whole plan unless an exception trigger applies.

### Reflection Research

Timing: after completing an active goal when new evidence suggests future work should change.

Purpose:

- Update unstarted future goals in `.agent-loop/project/ROADMAP.md` without changing the accepted big picture.

Depth:

- Targeted to the discovered uncertainty.

## Active Goal Execution

1. Confirm the active goal has an observable outcome and done criteria.
2. Load only context needed for that goal.
3. Run the Constructive Challenge Loop before implementing a direction with material negative consequences.
4. Execute within the stated scope.
5. If the work removes behavior, run the Dead Code Safe Deletion workflow before considering cleanup complete.
6. If new work appears, add it to `## Future Goals` or `## Parking Lot` in `.agent-loop/project/ROADMAP.md` instead of expanding the active goal.
7. Verify against the active goal's checks.
8. Mark the active goal completed, blocked, or superseded.
9. Update `.agent-loop/START.md` with a resumable handoff after meaningful progress chunks, before risky or long-running transitions, before pausing for owner input, and whenever context pressure could make continuation brittle. Append logs after project intent is accepted.

## Dead Code Safe Deletion

Use this when deleting files or symbols, removing a feature, cleaning up suspected dead code, or deciding whether cleanup is safe.

1. Name the deletion candidate and the behavior, feature, or system that used to own it.
2. Search for all plausible usage paths, not just nearby code: imports, call sites, routes, jobs, events, templates, assets, styles, tests, docs, config, build files, feature flags, generated code, scripts, public APIs, CLIs, migrations, and dynamic string-based references.
3. Use language-aware tooling when available, such as type checkers, compiler errors, IDE safe-delete output, dependency graphs, test coverage, or liveness telemetry. Use text search as a backstop, not the only signal when the language or framework supports better analysis.
4. Classify each candidate:
   - Live: still used by accepted behavior, an entry point, an external contract, runtime configuration, user data path, or another system. Do not delete unless that behavior is explicitly in scope to remove.
   - Dead: no remaining usage path, no external contract, and any remaining references are tied only to removed behavior.
   - Unclear: dynamic reachability, generated ownership, migration/data-retention risk, public API uncertainty, weak test coverage, or ambiguous owner intent. Do not delete without more evidence or owner confirmation.
5. Delete dead candidates in small reviewable groups. Include directly obsolete tests, docs, styles, config, and adapters when their only purpose was the removed behavior.
6. After deletion, rerun usage searches and relevant verification. Treat new compile, lint, type, route, asset, or test failures as evidence that the target was not fully dead or that more cleanup is required.
7. If a candidate is not deleted because evidence is unclear, record it as suspected dead code with the missing proof and a future trigger for revisiting it.
8. In the handoff, summarize what was deleted, what evidence made it safe, what verification ran, and any suspected dead code intentionally left behind.

## Reflection And Closeout

Use this before finishing meaningful work.

1. Compare completed work against `.agent-loop/project/ACTIVE_GOAL.md` done criteria.
2. Record verification evidence or explain skipped verification.
3. Record any material challenged tradeoff, owner decision, and mitigation or rollback path.
4. Add discovered work to `## Future Goals` or `## Parking Lot` in `.agent-loop/project/ROADMAP.md` instead of expanding completed active scope.
5. Update `.agent-loop/project/INTENT.md` only if the owner approved a big-picture change.
6. Update `.agent-loop/project/SYSTEM_MAP.md` when reflection changes accepted project system shape or unstarted project work.
7. Update `.agent-loop/project/OBSERVATIONS.md` for recurring failures or resolved setup facts.
8. Refresh `.agent-loop/START.md` with the next-session handoff when the next session needs different startup context, even if mid-task handoffs were already saved.
9. Append notable events to the current monthly log under `.agent-loop/project/logs/` after project intent is accepted.
10. Run available verification checks and record missing checks as residual risk.

## Scope Drift Handling

- New requirement inside accepted boundaries: add or reorder a future goal.
- New major system: ask before accepting it into scope.
- New risk or conflict: enter Exception Mode.
- Nice-to-have improvement: add it to `## Parking Lot` in `.agent-loop/project/ROADMAP.md` unless it affects the current done criteria.

## Parking Lot Handling

- Use `## Parking Lot` in `.agent-loop/project/ROADMAP.md` for noticed work that is not needed for the active goal, is not yet accepted, is too vague, or is lower priority.
- Write parked items with enough context to recover why they exist: `Consider [thing] because [reason]. Revisit when [trigger or condition].`
- During Intake, Discovery, milestone planning, or Reflection, review parked items and either promote them to `## Future Goals`, leave them parked, or mark them superseded.
