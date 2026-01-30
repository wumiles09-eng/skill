---
name: workflow-orchestrator
description: End-to-end engineering workflow orchestration (idea→requirement→design→solution→coding→testing→deployment→retrospective→promotion→knowledge→iteration→evolution). Use for large requests spanning multiple phases or files; responsible for phase determination, deliverable generation, skill chaining, and persistent file maintenance.
---

# Workflow Orchestrator - Engineering Workflow Orchestrator

## Goal

Determine the current phase, generate/update phase deliverables, break down work into executable tasks, and switch to specialized skills when needed.

## Complete R&D Workflow

```
Idea → Requirement → Design → Solution → Development → Testing → Deployment → Promotion → Knowledge → Iteration → Evolution
  ↓        ↓           ↓          ↓            ↓           ↓            ↓          ↓            ↓           ↓          ↓
Idea   PRD      Design    TechPlan     Code       Test       Deploy     Promo    Knowledge   Iterate   Evolution
```

## Phase Determination (Quick Triage)

Determine current phase using these signals:

- **Idea**: User has a vague idea, needs productization
- **Requirement**: Goals/scope/constraints/acceptance unclear
- **Design**: User discusses "how to interact/organize info/data flow"
- **Solution**: User discusses "how to split tasks/implement/tech stack"
- **Development**: Plan confirmed, starting to write/modify code
- **Testing**: Writing/running/completing tests, debugging failures
- **Deployment**: Packaging/releasing/launching/migrating/rolling back
- **Promotion**: Marketing strategy, user growth, operations
- **Knowledge**: Documenting, knowledge base, best practices
- **Iteration**: Feature iteration, optimization, refactoring
- **Evolution**: Feedback on workflow issues, skill optimization

## Phase Deliverables (Default to work directory)

### Idea → Requirement
- **Deliverable**: `prd.md` (Product Requirements Document)
- **Trigger**: requirements-clarifier, prd-generator
- **Content**: Target users, core value, feature list, acceptance criteria

### Design
- **Deliverable**: `design.md` + `adr/` (Architecture Decision Records)
- **Trigger**: architecture-designer, ui-ux-design-system-generator
- **Content**: Information architecture, interaction flows, data flows

### Solution
- **Deliverable**: `tech-plan.md` + `test-plan.md`
- **Trigger**: tech-proposal, implementation-planner
- **Content**: A/B comparison, cost/time/risk assessment, task breakdown

### Development
- **Deliverable**: `task-plan.md` + `progress.md`
- **Trigger**: coding-executor, react-performance-optimizer
- **Content**: Task checklist, implementation, continuous logging

### Testing
- **Deliverable**: `test-report.md`
- **Trigger**: testing-orchestrator, visual-test, quality-gate
- **Content**: Unit/integration/E2E, coverage, failure analysis

### Deployment
- **Deliverable**: `release-notes.md` + `runbook.md`
- **Trigger**: deployment-and-ops, versioning-and-release
- **Content**: Deployment steps, rollback, monitoring

### Promotion
- **Deliverable**: `promotion-plan.md`
- **Trigger**: (To add promotion skills)
- **Content**: Marketing strategy, user growth, operations

### Knowledge
- **Deliverable**: Obsidian vault / Wiki
- **Trigger**: obsidian-skills, documentation
- **Content**: Document archive, knowledge graph, best practices

### Iteration
- **Deliverable**: `iteration-plan.md`
- **Trigger**: planning-with-files
- **Content**: Next iteration plan, improvements, technical debt

### Evolution
- **Deliverable**: `evolution.json`
- **Trigger**: skill-lifecycle-and-evolution, skill-indexer
- **Content**: Trigger fixes, workflow optimization, new skills

## Persistent File System

### Establish "Files as Memory"

Create work directory (`.work/` or `project-work/`) with three files:

- `task-plan.md`: Phase checklist and task list
- `findings.md`: Research, discoveries, pitfalls, links, command outputs
- `progress.md`: Timeline of actions and results

### Writing Rules

1. **2-Action Rule**: After every 1-2 "read/search/run command/observe output", write key points to `findings.md` or `progress.md`

2. **Decision Recording**: When making decisions (tech choice/interface/data model/quality gate/release strategy), write to `task-plan.md` or ADR

3. **Session Recovery**: When conversation restarts, read these three files to restore context

## Quick Start Templates

### Initialize Work Directory

```markdown
# task-plan.md

# Project Name
## Current Phase
- [ ] Current task 1
- [ ] Current task 2

## Roadmap
1. [ ] Requirements
2. [ ] Design
3. [ ] Solution
4. [ ] Development
5. [ ] Testing
6. [ ] Deployment
```

```markdown
# findings.md

## Research Notes

### Tech Decisions
- Decision: Use X instead of Y
- Reason: ...

### Issues Found
- Problem: Description
- Solution: ...

### Command Outputs
```bash
# Key commands
```

### References
- [Doc Title](URL)
```

```markdown
# progress.md

## Timeline

### 2026-01-29 10:00
- Created project structure
- Set up environment

### 2026-01-29 11:30
- Completed PRD draft
- Waiting for PM confirmation
```

## Skill Chaining Examples

### Scenario 1: New Feature Development (Complete Flow)

```
User: "I want to add user login"

↓ workflow-orchestrator determines: Requirement phase

↓ triggers requirements-clarifier
→ Output: prd.md

↓ User confirms PRD

↓ workflow-orchestrator determines: Design phase

↓ triggers architecture-designer + ui-ux-design-system-generator
→ Output: design.md + design system

↓ workflow-orchestrator determines: Solution phase

↓ triggers tech-proposal
→ Output: tech-plan.md (A/B comparison)

↓ User confirms solution

↓ workflow-orchestrator determines: Development phase

↓ triggers coding-executor + react-performance-optimizer
→ Updates: task-plan.md + progress.md

↓ Development complete

↓ workflow-orchestrator determines: Testing phase

↓ triggers testing-orchestrator + visual-test
→ Output: test-report.md

↓ Tests pass

↓ workflow-orchestrator determines: Deployment phase

↓ triggers deployment-and-ops
→ Output: release-notes.md + runbook.md

↓ Deployment successful

↓ workflow-orchestrator determines: Knowledge phase

↓ triggers obsidian-skills
→ Archive to Obsidian vault
```

## Output Format Preferences

- Default: Write to work directory files, not in conversation
- Execution-oriented: Checklists, tables, clear "next steps"
- Structured: Markdown headings, lists, code blocks

## Quality Checkpoints

At each phase end, check:

- [ ] Deliverable file generated
- [ ] Deliverable updated in work directory
- [ ] findings.md or progress.md updated
- [ ] Next phase identified
- [ ] Skills to trigger identified

## Related Skills

### Requirement Phase
- requirements-clarifier
- prd-generator
- optimize-iteration-spec

### Design Phase
- architecture-designer
- ui-ux-design-system-generator
- pencil-design-workflow
- stitch-design-workflow

### Solution Phase
- tech-proposal
- implementation-planner

### Development Phase
- coding-executor
- react-performance-optimizer
- systematic-debugging

### Testing Phase
- testing-orchestrator
- visual-test
- quality-gate

### Deployment Phase
- deployment-and-ops
- versioning-and-release
- ios-simulator-deployment

### Knowledge Phase
- obsidian-skills
- documentation

### Evolution Phase
- skill-lifecycle-and-evolution
- skill-indexer

---

**Maintenance**: Continuously optimize based on usage
**Source**: Based on Cursor Hi Offer workflow-orchestrator, adapted for complete R&D workflow
**Related**: planning-with-files, all phase-specific skills
