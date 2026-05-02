# Run Prompt

Use this prompt in a fresh coding-agent session after copying `.agent-loop/` into the test project:

```text
Read `.agent-loop/AGENTS.md` and start The Agent Loop onboarding for this project. First create or carefully update root `AGENTS.md` so future prompts load The Agent Loop, then inspect the repo. If the project objective is not clear yet, explain that there are five quick onboarding questions and ask me Question 1 of 5 only. Do not suggest a project objective, do not draft `.agent-loop/GOAL.md` or `.agent-loop/STATUS.md`, and do not make code changes until the blocking questions are answered.
```

For the blank-project run, do not provide a project idea in the first prompt. The actor should ask Question 1 of 5 and wait. It should not suggest an objective from the folder name.

For the existing-project run, seed a small root `AGENTS.md` before copying `.agent-loop/` so adapter merge behavior can be evaluated.
