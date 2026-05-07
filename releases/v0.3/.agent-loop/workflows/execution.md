# Execution Workflows

## Constructive Challenge Loop

Use when an owner claim, plan, or requested change appears materially false, risky, conflicting, out of scope, brittle, irreversible, or likely to create hidden cost.

1. Restate the intended outcome neutrally.
2. Name the specific concern.
3. Explain the likely consequence and the evidence, rule, or uncertainty behind it.
4. Offer a safer, smaller, or more reversible option.
5. Ask for a decision only when the tradeoff is material or the action would cross a gate.
6. If the owner confirms the original direction and it remains within rules and safety boundaries, continue with mitigations.
7. If the concern involves severe harm, impossible requirements, conflicting instructions, external effects, or unsafe ambiguity, enter Exception Mode.

## Active Goal Execution

1. Confirm the active goal has an observable outcome and done criteria.
2. Load only context needed for that goal.
3. Run Constructive Challenge Loop before implementing a materially risky direction.
4. Execute within the stated scope.
5. If work removes behavior, load `.agent-loop/workflows/safe-deletion.md`.
6. Add newly discovered work to `## Future Goals` or `## Parking Lot` instead of expanding the active goal.
7. Verify against the active goal's checks.
8. Mark the active goal completed, blocked, or superseded.
9. Update `.agent-loop/START.md` after meaningful progress chunks, before risky or long-running transitions, before pausing for owner input, and whenever context pressure could make continuation brittle.
