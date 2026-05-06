# Active Goal

Status: completed

Owner approval: requested and accepted in chat on 2026-05-06.

## Parent

- Intent: Self-apply The Agent Loop v0.2 to build v0.3.
- System: Research And Evidence; Release Packages; Project Operations.
- Milestone: v0.2 self-application follow-up cleanup.

## Outcome

Compress the active docs tree into v0.2-style evidence briefs and record how v0.3 work should move from live workspace to release package.

## Done When

- [x] Docs `README.md` navigation files are removed.
- [x] Completed deep-research categories are represented by compact `summary.md` evidence briefs.
- [x] Standalone research and case-study docs preserve only required context, source basis, applied implication, and revisit triggers.
- [x] `.agent-loop/project/systems/research-and-evidence.md` owns docs inventory and loading guidance.
- [x] `.agent-loop/project/systems/release-packages.md` explains that root `.agent-loop/` is the mutable v0.3 development workspace and `releases/v0.3/` is created only for release-candidate packaging.
- [x] Handoff/log/roadmap state is updated for choosing the first v0.3 improvement goal.

## Scope

In scope:

- `docs/`
- `.agent-loop/project/`
- `.agent-loop/START.md`

Out of scope:

- Editing frozen release source folders under `releases/v0.1/.agent-loop/` or `releases/v0.2/.agent-loop/`.
- Creating `releases/v0.3/` before a release-candidate packaging step.
- Publishing GitHub Releases or uploading assets.

## Verification

```text
git status -sb
git diff --check
Get-ChildItem -Recurse docs -Filter README.md
rg -n "docs/README|docs/research/README|docs/case-studies/README|category-2|category-6|category-8|docs/research/category" .agent-loop docs README.md AGENTS.md --glob "!**/ACTIVE_GOAL.md"
rg -n "2[.]1-onboarding|2[.]2-shared|2[.]3-bootstrap|2[.]4-development|1-kinds-of-memory|2-what-to-save|3-what-to-load|4-keeping-memory|5-memory-boundaries|6-storage-backends|1-permission-models|2-high-impact|3-change-size|4-sandboxing|5-developer-pain|6-v0[.]1-guardrail" .agent-loop docs README.md AGENTS.md --glob "!**/ACTIVE_GOAL.md"
```
