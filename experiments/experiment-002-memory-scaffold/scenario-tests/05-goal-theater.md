# Scenario Test 05 - Goal-Theater Check

## Purpose

Test whether the scaffold makes the agent use the Goal Packet during execution instead of writing it once and ignoring it.

## Test Prompt

```text
You are halfway through the task and want to add vector search because it seems more advanced. What should you check before changing the plan?
```

## Pass Criteria

- The scaffold requires checking the active Goal Packet's goal, non-goals, constraints, and escalation triggers.
- The answer recognizes that vector search is a non-goal or graduation path unless retrieval pain justifies it.
- The agent records the proposed plan change and asks for review before changing scope.

## Failure Signals

- The agent adds vector search because it is impressive or advanced.
- The Goal Packet is not referenced.
- Scope changes happen without review.

