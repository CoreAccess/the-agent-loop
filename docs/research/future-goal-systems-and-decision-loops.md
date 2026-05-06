# Future Research Note - Goal Systems And Decision Loops

Date: 2026-04-28
Status: compact future-scope note; not an accepted category

## Required Context

AI coding agents often respond to tasks without carrying a durable endpoint, why, cost model, loop rule, or stop condition. The useful future idea is a lightweight goal contract:

- goal
- why
- definition of done
- non-goals
- constraints
- risk/resource budgets
- evidence to collect
- loop strategy
- stop condition
- escalation triggers
- adaptation rule
- memory candidates

The goal contract should be small for simple fixes and explicit for large or uncertain work.

## Applied Implications

- "Why" is control data. It changes technical choices and should not be treated as motivational filler.
- Goal, plan, action, and evidence should be distinct. Otherwise activity can masquerade as progress.
- Tests should evaluate policy under constraints, not only final outcome.
- Loops need finite budgets: attempts, time, cost, failure thresholds, escalation triggers, and stop conditions.
- Reflect should ask whether the goal changed, whether the loop worked, and what should be remembered.

## Source Basis

- Scientific method, OODA, and cybernetics: observe, model, act, compare, revise.
- ReAct, Reflexion, Voyager, and LLM-agent surveys: planning, action, memory, feedback, and reflection recur across agent research.
- Gamble Lab simulation: goals without constraints lead to poor policy; adaptation needs confidence thresholds.
- AI safety and risk-management sources: underspecified objectives, side effects, reward hacking, unsafe exploration, and distribution shift are real risks.

## Revisit Triggers

- Designing a v0.3 active-goal format.
- Category 7 testing and verification loops.
- Category 10 error recovery and failure loops.
- Category 11 agentic-pattern work.
- Deciding whether "Goal Contract" belongs in Category 2, 3, 7, 11, or a future category.
