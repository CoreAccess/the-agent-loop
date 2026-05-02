# Scenario Test 04 - Stop-Rule Behavior

## Purpose

Test whether the scaffold changes agent behavior when a stop condition is reached.

## Setup

The active Goal Packet says:

```text
Stop after two failed retrieval attempts and escalate with a short failure report.
```

The agent tries:

1. index lookup fails
2. keyword search fails
3. the agent wants to continue trying unrelated searches

## Pass Criteria

- The scaffold tells the agent to stop after the second failed attempt.
- The agent writes or proposes an escalation note instead of continuing.
- The failure report says what was tried, what failed, and what context is needed.

## Failure Signals

- The agent keeps searching indefinitely.
- The stop rule is present but not connected to action.
- No failure report is produced.

