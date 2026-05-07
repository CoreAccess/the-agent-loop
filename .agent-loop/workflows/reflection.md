# Reflection Workflows

## Reflection And Closeout

Use before finishing meaningful work.

1. Compare completed work against `.agent-loop/project/ACTIVE_GOAL.md` done criteria.
2. Record verification evidence or explain skipped verification.
3. Record any material challenged tradeoff, owner decision, and mitigation or rollback path.
4. Add discovered work to `## Future Goals` or `## Parking Lot` instead of expanding completed active scope.
5. Update `.agent-loop/project/INTENT.md` only if the owner approved a big-picture change.
6. Update `.agent-loop/project/SYSTEM_MAP.md` when reflection changes accepted project system shape or unstarted project work.
7. Update `.agent-loop/project/OBSERVATIONS.md` for recurring failures or resolved setup facts.
8. Refresh `.agent-loop/START.md` when the next session needs different startup context.
9. Append notable events to the current monthly log after project intent is accepted.
10. Run available verification checks and record missing checks as residual risk.

## Scope Drift Handling

- New requirement inside accepted boundaries: add or reorder a future goal.
- New major system: ask before accepting it into scope.
- New risk or conflict: enter Exception Mode.
- Nice-to-have improvement: add it to `## Parking Lot` unless it affects current done criteria.

## Parking Lot Handling

Use `## Parking Lot` for noticed work that is not needed for the active goal, is not yet accepted, is too vague, or is lower priority.

Write parked items with enough context to recover why they exist:

```text
Consider [thing] because [reason]. Revisit when [trigger or condition].
```

During Intake, Discovery, milestone planning, or Reflection, review parked items and either promote them to `## Future Goals`, leave them parked, or mark them superseded.
