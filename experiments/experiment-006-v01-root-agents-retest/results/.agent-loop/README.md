# The Agent Loop

This folder holds The Agent Loop project-local framework files.

In v0.1, the framework lives inside `.agent-loop/` so it does not collide with normal project files such as `README.md`, source folders, docs, or test files.

The v0.1 release ZIP should contain this `.agent-loop/` folder only.

To start onboarding, the user gives their coding agent the starter prompt from the GitHub README. That prompt tells the agent to read `.agent-loop/AGENTS.md`.

No `START_HERE.md`, root `README.md`, root `templates/`, or root adapter file belongs in the v0.1 ZIP.

During onboarding, the agent creates or carefully updates root `AGENTS.md` as a small adapter so future prompts automatically load The Agent Loop. All other framework working files stay inside `.agent-loop/`.
