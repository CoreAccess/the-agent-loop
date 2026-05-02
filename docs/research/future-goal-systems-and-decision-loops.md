# Future Research Note - Goal Systems and Decision Loops

Status: out-of-cycle research note. This does not add a category yet.
Date: 2026-04-28

## Why This Matters

AI coding assistants often operate as task responders, not goal-directed workers. They can ask questions, edit files, and run tests, but they often lack a durable endpoint, a reason for the endpoint, a cost model, and a principled way to decide whether to continue, pivot, stop, or escalate.

The framework should treat a user request as more than an instruction. It should convert the request into a bounded goal system: objective, why, success criteria, constraints, resources, loop, stop condition, and learning rule.

This is AGI-adjacent thinking, but v1 should stay practical: build a better goal-directed development framework, not claim to solve AGI.

## Research Threads

### Human Baseline

Human goals emerge from needs, constraints, and environment. Hunter-gatherer societies depended on wild food for subsistence before agriculture emerged roughly 12,000 to 11,000 years ago, and their strategies varied by local environment. That matters because human decision-making is grounded in real external consequences: food, safety, shelter, social trust, time, and limited resources.

Maslow's 1943 motivation theory is useful as a rough lens, not as a rigid law. The key useful idea is that humans do not pursue abstract goals in a vacuum. Lower-level needs and threats change which goals become urgent.

Sources:
- Britannica, hunter-gatherer overview: https://www.britannica.com/topic/hunter-gatherer
- Maslow, A Theory of Human Motivation: https://opencommons.org/A_theory_of_human_motivation

### Money As Resource Constraint

Money is not the deepest human goal; it is a generalized survival and coordination instrument. Economically, money acts as a medium of exchange, unit of account, and store of value. Practically, it lets people convert work into food, shelter, tools, time, and optionality.

For the framework, "money" maps to resource awareness:
- time budget
- compute/API budget
- context-window budget
- user attention budget
- risk budget
- trust budget

An agent that ignores these budgets can technically continue working while still failing the user's real goal.

Sources:
- IMF, What Is Money?: https://www.imf.org/en/publications/fandd/issues/series/back-to-basics/money
- Federal Reserve Education, Functions of Money: https://www.federalreserveeducation.org/teaching-resources/economics/money/functions-of-money

### Loops Are How Goals Survive Reality

Plans are guesses. Loops are how a system reconciles guesses with reality.

The recurring pattern across human decision systems is:
1. Observe reality.
2. Form or revise a model.
3. Choose an action.
4. Act.
5. Compare outcome against expectation.
6. Keep, adjust, or abandon the plan.

Cybernetics frames this as goal-directed feedback control. The scientific method adds testability and active attempts to falsify bad assumptions. OODA emphasizes fast observation, orientation, decision, and action under uncertainty.

Sources:
- Stanford Encyclopedia of Philosophy, scientific method: https://plato.stanford.edu/archives/fall2021/entries/scientific-method/
- OODA loop overview and criticism: https://ooda.wiki/wiki/OODA_loop
- Wired on Norbert Wiener and cybernetics: https://www.wired.com/2008/11/nov-26-1894-cybernetics-pioneer-norbert-wiener-born-2

### AI Agents Already Point This Way

Modern agent research repeatedly converges on the same structure: memory, planning, action, feedback, and reflection.

Examples:
- ReAct interleaves reasoning and action so the model can update plans while interacting with tools and environments.
- Reflexion stores verbal lessons from failed or successful attempts in episodic memory.
- Voyager uses an automatic curriculum, executable skill library, environment feedback, execution errors, and self-verification to improve over time.
- Surveys of LLM agents commonly organize agents around profile, memory, planning, and action.

The gap is not that no one sees loops. The gap is that most coding assistants expose these loops weakly to users and do not bind them to clear project goals, resource constraints, stop conditions, and durable learning.

Sources:
- ReAct paper: https://huggingface.co/papers/2210.03629
- Reflexion paper: https://huggingface.co/papers/2303.11366
- Voyager project: https://voyager.minedojo.org/
- LLM autonomous agents survey: https://link.springer.com/article/10.1007/s11704-024-40231-1

### Gamble Lab Lessons

The local Gamble Lab / poker simulation reinforced a practical lesson: a goal without constraints is too vague to guide intelligent behavior. "Make money" becomes useful only after the environment and constraints are explicit: starting capital, game type, drawdown tolerance, rake, opponent quality, stop rules, and overfitting risk.

For software agents, the equivalent is that "build the feature" or "fix the bug" is incomplete. The agent needs to understand the goal, the environment, the constraints, and the allowed policy under uncertainty.

The strongest testing lesson is that tests should evaluate the policy, not only the outcome. In poker, a winning hand does not prove the decision was good, and a losing hand does not prove the decision was bad. In software work, one passing test does not prove the architecture is healthy, and one failed attempt does not prove the plan is wrong.

The simulator also showed that adaptation can be harmful without confidence thresholds. Adaptive play helped in soft rooms but underperformed in tight or mixed rooms. Framework implication: "adapt more" is not automatically better. Agents need evidence thresholds before changing strategy, plus stop rules when the environment no longer matches the plan.

Candidate evaluation questions:
- Did the agent follow the strategy it chose?
- Did the strategy fit the environment?
- Did the agent confuse luck, noise, or one-off feedback with signal?
- Did the agent stop when the stop rule said stop?
- Did adaptation improve results over enough trials?

### AGI Caution

A broad definition of machine intelligence is an agent's ability to achieve goals across many environments. That makes goal-directedness central, but also dangerous if goals are underspecified.

AI safety research repeatedly warns about wrong objectives, side effects, reward hacking, unsafe exploration, and distribution shift. Open-endedness research argues that self-improving systems may require novelty and learnability, but also raises safety concerns.

For this framework, the answer is not "make the agent autonomous at all costs." The answer is bounded agency: explicit goals, human-owned values, visible tradeoffs, safe exploration, evidence-based progress, and stop rules.

Sources:
- Legg and Hutter, Universal Intelligence: https://www.semanticscholar.org/paper/Universal-Intelligence%3A-A-Definition-of-Machine-Legg-Hutter/8e8ec502208f29ee9f78ded19226578e027ecd16
- Concrete Problems in AI Safety summary: https://www.alignmentwiki.com/wiki/papers/concrete-problems-in-ai-safety
- Open-Endedness is Essential for Artificial Superhuman Intelligence: https://huggingface.co/papers/2406.04268
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

## Framework Implications

### 1. Add Goal

Every meaningful task should be reducible to a small goal packet:

```text
Goal:
Why:
Definition of done:
Non-goals:
Constraints:
Risk budget:
Resources/budget:
Known risks:
Evidence to collect:
Loop strategy:
Stop condition:
Escalation triggers:
Adaptation rule:
Memory candidates:
```

This should be lightweight for small tasks and explicit for large tasks.

### 2. Treat "Why" As Control Data

The "why" is not motivational fluff. It changes technical choices.

Example: "Build a website" is too broad. "Build a website to get paid clients" changes the page structure, copy, SEO, conversion path, analytics, deployment urgency, and maintenance choices. "Build a website to learn React" changes almost every decision.

### 3. Separate Goal, Plan, Action, and Evidence

Agents often collapse these into one stream. The framework should separate them:
- Goal: what outcome matters.
- Plan: current theory of how to get there.
- Action: next concrete step.
- Evidence: what proves progress or failure.

This prevents endless activity from masquerading as progress.

### 4. Test Policy, Not Just Outcome

Framework tests should ask whether the agent followed a sound policy under the stated constraints, not only whether the final artifact happened to pass.

This matters because real work includes noise:
- a bad plan can pass once by accident
- a good plan can hit an external failure
- a local test can pass while the broader goal fails
- a strategy can work in one environment and fail in another

The framework needs evaluation methods that separate outcome quality, process discipline, environmental fit, and adaptation quality.

### 5. Make Loops Finite

The loop should not be "try forever." It should be:

```text
Attempt -> observe result -> diagnose -> revise -> retry or stop
```

Each loop needs limits:
- max attempts
- cost/time budget
- failure threshold
- escalation trigger
- stop condition

This directly addresses recurring bug loops.

### 6. Encode Resource Reality

The framework should teach agents to reason about scarce resources:
- user patience
- token/context usage
- build/test time
- money/API cost
- project risk
- complexity debt

This maps the user's "money = food and shelter" idea into software work: resource constraints are not side notes; they shape rational action.

### 7. Add Goal Review To Reflect

Reflect should not only ask "what changed?" It should ask:
- Did we achieve the goal?
- Did the goal change?
- Did our understanding of the why change?
- What loop worked?
- What loop failed repeatedly?
- What should be remembered so next time starts closer to success?

## Potential Future Design Object

Candidate name: Goal Contract.

Purpose: a task-level or project-level artifact that records the user's objective, why, success criteria, constraints, resource budgets, loop rules, and stop conditions.

Possible homes:
- Category 2 - onboarding and shared vision
- Category 3 - planning and architecture docs
- Category 7 - testing and verification loops
- Category 11 - agentic patterns
- Category 13 - self-improving agent, if created later

Do not add a new category yet. Revisit after Category 6 closes.

## Open Questions

- Should the Goal Contract be a persistent file, a section inside `STATUS.md`, or a generated transient artifact per task?
- What is the smallest possible version for quick bug fixes?
- Should the framework expose resource budgets explicitly to users, or infer soft budgets from task size?
- How do we prevent "goal theater" where the agent writes a goal packet but ignores it?
- How should a goal change be approved and logged?
- How should we test the framework itself for goal pursuit, adaptability, stop-rule obedience, and signal-vs-noise discipline in Codex?
