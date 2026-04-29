# Broad Sweep Research — All Links

Date: 2026-04-27
Phase: Category validation — first pass across all 12 links in links.md

---

## Summary Verdict

All 12 categories validated. Two new categories surfaced (Observable Development added as Category 12; Workflow Design absorbed as sub-category of Category 2). spec-kit is research inspiration, not a competitor. The framework fills ground spec-kit explicitly does not cover.

---

## Link-by-Link Findings

### 1. github/spec-kit ⭐ PRIORITY
**URL:** https://github.com/github/spec-kit  
**What it is:** A Spec-Driven Development toolkit. Specifications become executable — they directly generate implementations. Works with 30+ agents including Claude Code, Gemini CLI, Copilot, Cursor.  
**Relevant categories:** 4 (primary), 3 (partial), 2 (partial)  
**Key insights:**
- File structure: `.specify/` → `memory/constitution.md`, `specs/`, `plans/`, `tasks/`, `research/`
- Commands: `/speckit.constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.clarify` → `/speckit.tasks` → `/speckit.implement`
- `constitution.md` is their version of an Agent Contract but much simpler — project principles only, no authority hierarchy, no change gates
- Extensible via Extensions (new capabilities) and Presets (workflow customization)
- Supports greenfield, brownfield, and exploratory workflows
**What it misses:** Memory Systems, Change Gates, Context Loading, Error Handling, Skills ecosystem, Testing Loops, Agentic Patterns, Observable Development
**Relationship to our framework:** Research inspiration for Category 4. Could be a component a user adopts alongside our framework. We own Category 4 ourselves and may diverge significantly.

---

### 2. paulDuvall/ai-development-patterns
**URL:** https://github.com/paulDuvall/ai-development-patterns  
**What it is:** 28+ patterns for AI-assisted development organized in Foundation, Development, and Operations tiers.  
**Relevant categories:** 4, 7, 8, 9, 10, 11  
**Key insights:**
- "Codified Rules" pattern: coding standards as versioned configuration files — directly maps to Agent Contract
- "Developer Lifecycle" pattern: 9-stage workflow from problem definition to deployment — validates our Think→Plan→Build→Review→Test→Ship→Reflect sub-category
- "Observable Development": comprehensive logging enabling AI system understanding — this surfaced Category 12
- "Atomic Decomposition": breaking work into parallel-executable micro-tasks — relevant to Category 11
- "Error Resolution": AI-powered root cause diagnosis — validates Category 10
- "Security Sandbox" + "Policy Generation": isolated environments and compliance automation — validates Category 8
**What it misses:** Memory Systems, Skills ecosystem design, Context Loading efficiency
**Relevance:** High. Treat as a pattern library to draw from during deep research per category.

---

### 3. google-gemini/gemini-skills
**URL:** https://github.com/google-gemini/gemini-skills  
**What it is:** Lightweight context-injection skills for Gemini agents. Currently 4 skills covering the Gemini API ecosystem.  
**Relevant categories:** 5  
**Key insights:**
- Skills are context bridges — they don't add capabilities, they add current knowledge about APIs/SDKs that the model's training data doesn't have
- Improved API code correctness from near-zero to 87% (Flash) / 96% (Pro) with skills
- Installed via CLI: `npx skills add` or `npx ctx7 skills install`
- Very narrow scope currently — all 4 skills are Gemini-API-specific, not general dev patterns
**Relevance:** Moderate. Shows Gemini's approach to skills: context injection over capability extension. Useful for Category 5 cross-agent portability design.

---

### 4. mattpocock/skills
**URL:** https://github.com/mattpocock/skills  
**What it is:** 15 skills for real engineering work, organized in 4 categories. ~60k subscribers.  
**Relevant categories:** 5, 2, 3  
**Key insights:**
- 4 categories: Planning & Design, Development, Tooling & Setup, Writing & Knowledge
- Skills leverage `CONTEXT.md` and `docs/adr/` to make informed recommendations — validates our Planning & Architecture Docs category
- Invocation: `npx skills@latest add mattpocock/skills/[skill-name]` — consistent cross-project pattern
- `grill-me` skill exists here — validates our onboarding skill concept
- `tdd` skill enforces red-green-refactor cycles — validates Category 7
- `to-prd` converts conversation to GitHub issues — relevant to Category 3
**Relevance:** High. The closest existing implementation to what we're building. Study structure carefully during Category 5 deep research.

---

### 5. karpathy/442a6bf555914893e9891c11519de94f (gist)
**URL:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
**What it is:** A proposal for LLM-maintained persistent knowledge wikis. The core alternative to query-time RAG.  
**Relevant categories:** 6, 3  
**Key insights:**
- Three layers: raw sources → wiki (markdown pages) → schema (config)
- Key files: `index.md` (content catalog, read first) + `log.md` (append-only chronological record)
- Three operations: Ingest (source → wiki pages), Query (search + synthesize), Lint (health check for contradictions, orphans)
- Memory as a compounding artifact — cross-references and contradictions already resolved
- "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping." LLMs handle bookkeeping.
- Optional modularity — pick what works
- References Vannevar Bush's Memex (1945) — historical grounding
**Relevance:** Very high for Category 6. The wiki + log.md pattern should directly inform how our Memory Systems category works. Also relevant to how `docs/` planning docs function in Category 3.

---

### 6. databricks/memory-scaling-ai-agents
**URL:** https://www.databricks.com/blog/memory-scaling-ai-agents  
**What it is:** Research on how AI agent performance scales with external memory.  
**Relevant categories:** 6  
**Key insights:**
- Two memory types: **Episodic** (raw records — logs, trajectories, feedback) vs. **Semantic** (distilled skills and facts extracted from episodic)
- Two memory scopes: **Personal** (user-specific, private) vs. **Organizational** (shared naming conventions, business rules)
- Memory distillation: episodic → semantic is an active process, not automatic
- Three memory management processes: bootstrap (seed with existing assets), distill (episodic → reusable patterns), consolidate (remove duplicates/outdated)
- PostgreSQL-based systems outperform standalone vector DBs for agent memory
- Accuracy improved from ~0% to 70% with proper memory; reasoning steps reduced from ~20 to ~5
**Relevance:** Very high for Category 6. The episodic/semantic hierarchy and distillation process are core concepts to include in memory system design.

---

### 7. dev.to — Agentic Platform Engineering (sarony11)
**URL:** https://dev.to/sarony11/agentic-platform-engineering-how-to-build-an-agent-infrastructure-that-scales-from-your-laptop-to-11np  
**What it is:** A disciplined approach to versioning, distributing, and composing AI agent configuration.  
**Relevant categories:** 1, 5, 9  
**Key insights:**
- Three-repo architecture: `agent-library` (intelligence), `agent-setup` (deployment bridge), `resource-catalog` (map)
- **Layered context loading**: global identity → domain rules → task-specific procedures. Cumulative from parent to child directories.
- Scoped skills: invoked explicitly on-demand (`/skill:name`), not always-loaded — reduces token overhead
- Token efficiency: 2k-4k scoped contexts vs. 10-20k monolithic configs
- Symlink-based deployment: changes to agent-library propagate instantly
- Enterprise extension: `.well-known/agent-capabilities.json` (RFC 8615) for multi-team agent discovery
**Relevance:** Very high for Category 9 (Context Loading) and Category 1 (Agent Contract architecture). The layered loading pattern should be a core recommendation in both categories.

---

### 8. Microsoft — Agentic Platform Engineering with GitHub Copilot
**URL:** https://devblogs.microsoft.com/all-things-azure/agentic-platform-engineering-with-github-copilot/  
**What it is:** Microsoft's three-act model for maturing agentic development workflows with Copilot.  
**Relevant categories:** 8, 11  
**Key insights:**
- Three acts: Platform Awareness (embed tribal knowledge) → Standards Enforcement (AI-powered guardrails) → Autonomous Operations (agent-driven remediation)
- Prompt-driven enforcement: AI-powered GitHub Actions checks adapt to standards stored as markdown — guardrails without code changes
- Persona-based agent definitions stored as markdown files
- PR-based remediation: agents propose fixes via pull requests, humans approve
- "Crawl-walk-run" maturity model transfers across domains even if Azure tooling doesn't
**Relevance:** Moderate. Azure-specific infrastructure dominates, but the three-act maturity model and PR-gated remediation pattern are useful for Category 8 and Category 11.

---

### 9. garrytan/gstack
**URL:** https://github.com/garrytan/gstack  
**What it is:** A Claude Code toolkit by Garry Tan (YC President) implementing a full engineering team via 23+ slash command roles.  
**Relevant categories:** 2, 5, 7, 11  
**Key insights:**
- Sprint cycle: **Think → Plan → Build → Review → Test → Ship → Reflect** — this is the development lifecycle sub-category
- 23+ specialized roles: `/office-hours` (challenge assumptions before coding), `/plan-ceo-review`, `/plan-eng-review`, `/design-review`, `/qa`, `/cso` (security audit), `/ship`
- Parallel sprints: 10-15 simultaneous sprints via "Conductor" — v2 territory for us
- Productivity claim: 810× 2013 baseline coding pace (Garry Tan)
- Skills as specialized role personas — validates our Skills category design
**Relevance:** Very high. The sprint cycle is now the backbone of our Category 2 sub-category. The role-based skill model is a strong pattern for Category 5.

---

### 10. OpenAI Codex — Frontend Designs
**URL:** https://developers.openai.com/codex/use-cases/frontend-designs  
**What it is:** Codex use case guide for AI-assisted frontend development.  
**Relevant categories:** 9, 4  
**Key insights:**
- "Reuse existing patterns" — direct to repo conventions, not generic generation
- Design systems first: Codex performs better with clear component layers
- Visual validation via Playwright: catches layout issues static review misses
- Multiple reference states (desktop/mobile/hover/loading) beat single screenshots
**Relevance:** Low for framework design. Validates Category 9 (existing patterns over invention) and Category 4 (spec quality matters). No framework-level patterns surfaced.

---

### 11. OpenAI Codex — Iterate on Difficult Problems
**URL:** https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems  
**What it is:** Codex workflow guide for hard optimization/generation problems.  
**Relevant categories:** 7, 12  
**Key insights:**
- Scored improvement loop: Baseline → Iterate (change → eval → log → inspect) → Stop (score > 90%)
- LLM-as-judge: combine deterministic checks with LLM evaluation for subjective qualities
- Single-change iterations: one change at a time prevents attribution ambiguity
- Progress log: current best score, what changed, eval feedback, next attempts
- Stopping criteria: explicit rules prevent premature stop or endless loop
**Relevance:** Moderate. Validates Category 7 (LLM-as-judge, stopping criteria) and Category 12 (progress log as observable development pattern).

---

### 12. ML Mastery — Agentic AI Design Patterns
**URL:** https://machinelearningmastery.com/the-roadmap-to-mastering-agentic-ai-design-patterns/  
**Status:** 403 — blocked. Supplemented via web search.  
**Relevant categories:** 11  
**Key insights (from web search):**
- Core pattern taxonomy: ReAct, Reflection, Tool Use, Planning, Multi-Agent Collaboration, Sequential Workflows, Human-in-the-Loop
- Deeper taxonomy: Perception, Brain (planning/reflection), Action, Tool Use, Collaboration
- Multi-agent surge: 1,445% increase in enterprise inquiries Q1 2024 → Q2 2025
- Agentic coding is restructuring the software development lifecycle in 2026
**Relevance:** Moderate for Category 11. Confirms the core pattern vocabulary we should document.

---

## Cross-Cutting Insights

1. **Token efficiency is a first-class concern.** Dev.to quantified it: monolithic configs cost 10-20k tokens; scoped layered loading costs 2-4k. Our framework should bake this into Category 1 and Category 9 templates.

2. **Skills are not just capabilities — they are context injectors.** Gemini's framing: skills bridge the gap between model training data and current project reality. Mattpocock's framing: skills read CONTEXT.md and ADRs before acting. This dual nature should define how we design Category 5.

3. **Memory needs active management, not passive accumulation.** Karpathy + Databricks both emphasize this: memory without distillation, linting, and consolidation degrades. Category 6 needs to include the maintenance processes, not just the storage types.

4. **The sprint cycle (Think→Plan→Build→Review→Test→Ship→Reflect) is structural, not decorative.** gstack built 23 tools around it. It's the spine of productive AI-assisted development.

5. **Observable Development is distinct from Error Handling.** Observable Development is a dashboard (proactive, during work). Error Handling is a fire alarm (reactive, after failure). Both are needed.

---

## What's Still Needed

- Deep research per category (Phase 2)
- ML Mastery article — attempt alternative access or find equivalent
- Anthropic 2026 Agentic Coding Trends Report — PDF blocked, find text summary
- Category 5 deep research: how to design skills for cross-agent portability
- Category 11 deep research: which agentic patterns are v1 vs. v2
