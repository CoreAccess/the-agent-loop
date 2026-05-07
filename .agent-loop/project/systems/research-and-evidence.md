# Research And Evidence System

Status: accepted

## Function

Preserve the reasoning and validation evidence behind framework decisions without keeping bulky raw experiment workspaces in the active repo.

## Owned Files

- `docs/research/`
- `docs/case-studies/`

## Docs Inventory

Use this system file as the docs navigation entry point. The `docs/` tree should hold source-backed evidence and compact applied lessons, not navigation READMEs.

Research:

- `docs/research/broad-sweep.md` - first-pass validation across the original source set and category list.
- `docs/research/agentic-engineering-brendan-oleary.md` - supporting out-of-cycle talk note.
- `docs/research/future-goal-systems-and-decision-loops.md` - future research seed for goal contracts, decision loops, and evaluation.
- `docs/research/humanlayer-codelayer-agent-workflows.md` - orientation research on HumanLayer/CodeLayer workflow patterns relevant to v0.3.
- `docs/research/project-bootstrap-and-onboarding/summary.md` - Category 2: Project Bootstrap and Onboarding.
- `docs/research/memory-systems/summary.md` - Category 6: Memory Systems.
- `docs/research/change-gates-and-guardrails/summary.md` - Category 8: Change Gates and Guardrails.

Case studies:

- `docs/case-studies/agent-loop-validation-lessons.md` - distilled lessons from Experiments 001-006 after raw experiment folders were removed.
- `docs/case-studies/agent-loop-v2-import.md` - lessons from sanitizing an applied `.agent-loop-v2` folder into the v0.2 release source.
- `docs/case-studies/cms-incubator.md` - lessons from the earlier CMS incubator that clarified The Agent Loop as the main project.

## Loading Guide

- For current project state, start with `.agent-loop/START.md` and `.agent-loop/project/`.
- For framework design decisions, load the relevant `summary.md` under `docs/research/` first, then use git history only if full historical detail is needed.
- For evidence from prior applied work, load only the relevant file under `docs/case-studies/`.
- For old raw experiment details, use git history rather than recreating the removed `experiments/` folder.

## Rules

- Keep source-backed research notes when they inform future framework design.
- Research docs should preserve only the required context needed to understand the finding, source basis, decision implication, and future revisit trigger. Avoid carrying full session transcripts or broad raw research dumps in the active docs tree.
- Completed deep-research categories should normally collapse to one compact `summary.md` unless a future task needs more granular active evidence.
- Distill raw experiments into case studies or validation lessons before deleting raw capsules.
- Do not treat self-application as proof by itself. Use it to generate hypotheses and v0.3 candidate changes.
- For future validation, prefer compact external artifacts or case-study summaries over committing large nested experiment projects into this repo.
- Do not add docs `README.md` files by default. Navigation and loading guidance belong in `.agent-loop/project/SYSTEM_MAP.md` and this system file unless a future public-facing docs section needs its own entry point.
- Docs subfolders should use stable, descriptive, lowercase kebab-case topic slugs. Keep category numbers in indexes and headings rather than folder prefixes.
