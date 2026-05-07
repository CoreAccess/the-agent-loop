# HumanLayer / CodeLayer Agent Workflow Research

Date: 2026-05-06
Status: orientation research captured for future v0.3 planning

## Required Context

HumanLayer's public `humanlayer/humanlayer` repository is now centered on CodeLayer, an open source IDE and control plane for orchestrating Claude Code sessions in complex codebases. The repository still contains legacy HumanLayer SDK documentation, but that documentation says the SDK has been superseded by CodeLayer.

The project has three relevant layers:

- Product and runtime layer: `hld` daemon, `hlyr` CLI, and `humanlayer-wui` desktop/web UI manage Claude Code sessions, approvals, event streaming, session state, and local daemon communication.
- Workflow prompt layer: `.claude/commands/` and `.claude/agents/` provide reusable commands for codebase research, planning, implementation, validation, handoff, resume, commit, and PR description.
- Memory/docs layer: the `thoughts` system keeps developer notes, research, plans, handoffs, and PR descriptions in a separate git repository while exposing them in the working repo through symlinks and searchable hard links.

The legacy HumanLayer SDK idea is still useful conceptually: high-stakes agent tool calls need deterministic human oversight. The current CodeLayer implementation expresses that through local approvals, MCP, daemon session state, and UI affordances.

## Relationship To The Agent Loop

HumanLayer is strongly related to The Agent Loop, but it is not the same product category.

Shared problem:

- Help coding agents work in large, existing codebases.
- Preserve useful context across long work.
- Create higher-leverage human checkpoints before code generation or risky action.
- Keep agent work inspectable through markdown artifacts.
- Avoid letting long context windows become noisy transcripts.

Key difference:

- HumanLayer/CodeLayer is a productized, Claude Code-oriented IDE/control-plane plus workflow system.
- The Agent Loop is currently a portable markdown framework intended to work across Codex, Claude Code, Gemini, and similar agents.

For v0.3, HumanLayer should be treated as a source of workflow patterns, not as a target architecture to clone.

## What HumanLayer Does Better

- Operational control: daemon, CLI, WUI, session list, approvals, event streaming, and concurrent Claude Code sessions.
- Workflow commands: clear command family for research, planning, implementation, validation, handoff/resume, commit, and PR description.
- Specialized research agents: locator, analyzer, and pattern-finder roles keep research tasks focused.
- Human leverage: research and plan artifacts aim to let humans review high-impact assumptions before code generation.
- Approval infrastructure: tool-call approvals are first-class through MCP and local daemon flow.
- External memory option: `thoughts` separates private/shared/team notes from the code repository while keeping them searchable from the working tree.

## What HumanLayer Does Worse For Our Current Goals

- Portability: the active product is deeply tied to Claude Code, macOS-oriented installation, local daemons, sockets, and HumanLayer tooling.
- Complexity: daemon plus WUI plus CLI plus symlinks/hard links plus git hooks is much heavier than a v0.3 scaffold should become.
- Naming and lifecycle drift: public materials refer to HumanLayer, CodeLayer, Riptide, and legacy SDK concepts at different points.
- Prompt bloat risk: older command prompts contain many instructions. Their newer methodology appears to move away from monolithic prompts toward smaller stages.
- Team/tool assumptions: several flows assume Linear, `gh`, Claude subagents, `thoughts/shared`, and specific team conventions.

## Candidate v0.3 Ideas To Revisit

Use these as candidate design inputs, not accepted scope:

- Add a research-question stage before research. Convert an owner request into objective questions such as where behavior lives, how data flows, and what patterns exist before asking an agent to research.
- Keep research documentarian-first. A research pass should describe what exists before proposing changes.
- Add a compact design brief artifact before full planning. It should capture current state, desired state, found patterns, resolved decisions, open questions, non-goals, and verification path.
- Add a structure-outline artifact for phase shape before detailed plans. Prefer vertical slices that produce testable behavior in each phase over horizontal plans that do all work in one layer at a time.
- Split long workflows into smaller reusable phase skills or workflows: context questions, research, design brief, structure outline, implement, validate, reflect.
- Add a validate-plan workflow that checks implementation against plan/goal, verification evidence, deviations, and manual test gaps.
- Add context-pressure triggers. When research/tool output grows large, compact to a durable artifact and restart with selected context instead of continuing a bloated session.
- Consider external memory only as optional future scope. HumanLayer's `thoughts` design is useful evidence, but The Agent Loop v0.3 should stay project-local unless a specific validation goal proves otherwise.

## Ideas Not To Adopt Yet

- Do not build a daemon, WUI, cloud session manager, or CLI for v0.3.
- Do not make HumanLayer, Claude Code, Linear, or `gh` a required dependency.
- Do not move core memory outside `.agent-loop/project/` for v0.3.
- Do not make multi-agent orchestration a core requirement before the single-agent loop is stronger.
- Do not import large HumanLayer prompt files verbatim. Distill patterns into smaller, portable Agent Loop workflows.

## Source Basis

Primary sources:

- `https://github.com/humanlayer/humanlayer` - repository overview, file layout, release metadata, and active CodeLayer positioning.
- `https://github.com/humanlayer/humanlayer/blob/main/README.md` - CodeLayer positioning as an open source IDE for orchestrating AI coding agents.
- `https://github.com/humanlayer/humanlayer/blob/main/humanlayer.md` - legacy SDK documentation and high-stakes tool approval rationale.
- `https://github.com/humanlayer/humanlayer/blob/main/hlyr/README.md` - CLI commands, MCP approval server, thoughts, and Claude config setup.
- `https://github.com/humanlayer/humanlayer/blob/main/hld/README.md` - daemon API overview and e2e test scope.
- `https://github.com/humanlayer/humanlayer/blob/main/hld/PROTOCOL.md` - JSON-RPC session, approval, conversation, and event protocol.
- `https://github.com/humanlayer/humanlayer/blob/main/hlyr/THOUGHTS.md` - external thoughts repository model.
- `https://github.com/humanlayer/humanlayer/tree/main/.claude/commands` - research, plan, implement, validate, handoff, resume, commit, and PR command set.
- `https://github.com/humanlayer/humanlayer/tree/main/.claude/agents` - codebase locator/analyzer/pattern-finder and thoughts/web research subagent definitions.
- `https://www.humanlayer.dev/docs/introduction` - current public CodeLayer install and FAQ.
- `https://www.humanlayer.dev/docs/workshop` - public research/plan/implement workshop flow.
- `https://www.humanlayer.dev/blog/advanced-context-engineering` - HumanLayer's frequent intentional compaction rationale and brownfield workflow claims.

Secondary source:

- `https://www.zenml.io/llmops-database/evolving-ai-coding-agent-workflows-from-research-plan-implement-to-crispy` - 2026 summary of HumanLayer's reported move from RPI to CRISPY. Treat as useful but not primary evidence unless the original talk/transcript is reviewed later.

## Revisit Triggers

- Defining the first v0.3 improvement goal.
- Researching Category 3: Planning and Architecture Docs.
- Researching Category 5: Skills and Reusable Capabilities.
- Researching Category 7: Testing and Verification Loops.
- Researching Category 9: Context Loading and Management.
- Researching Category 11: Agentic Patterns.
- Considering any CLI, external memory, multi-agent, or UI/control-plane direction.
