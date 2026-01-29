---
name: planning-with-files
description: Persistent markdown planning system based on Manus AI workflow patterns. Use the filesystem as persistent memory for complex, multi-step tasks. Creates task_plan.md, findings.md, and progress.md to track progress across sessions.
---

# Planning with Files

Persistent memory system using the filesystem instead of relying on context window. Based on Manus AI workflow patterns.

## Core Philosophy

```
Context Window = RAM (volatile, limited)
Filesystem = Disk (persistent, unlimited)

→ Anything important gets written to disk.
```

## The 3-File Pattern

For complex tasks, create these files:

### 1. task_plan.md
Track phases and progress with checkboxes:

```markdown
# Task: [Description]

## Phase 1: [Name]
- [ ] Step 1
- [ ] Step 2
- [ ] Step 3

## Phase 2: [Name]
- [ ] Step 1
- [ ] Step 2

## Findings
<!-- Key discoveries and notes -->

## Errors
<!-- Track failures to avoid repetition -->
```

### 2. findings.md
Store research and discoveries:

```markdown
# Findings

## Research
- [Finding 1]
- [Finding 2]

## Code Analysis
- [Observation 1]
- [Observation 2]

## Decisions Made
- [Decision 1 with rationale]
- [Decision 2 with rationale]
```

### 3. progress.md
Session log and test results:

```markdown
# Progress Log

## Session [Date]
### Actions Taken
1. [Action 1]
2. [Action 2]

### Results
- [Result 1]
- [Result 2]

### Next Steps
- [Next action 1]
- [Next action 2]
```

## Workflow Rules

### 1. Create Plan First
Never start a complex task without creating `task_plan.md` first.

### 2. The 2-Action Rule
Save findings to `findings.md` after every 2 view/browser operations.

### 3. Log All Errors
Record every error in `task_plan.md` under the Errors section.

### 4. Never Repeat Failures
Track all attempts and mutate approach when something fails.

## Session Recovery

When context fills up and you run `/clear`:

1. The skill automatically checks for previous session data
2. Finds last time planning files were updated
3. Extracts potentially lost conversation
4. Shows catchup report for syncing

## Optimal Workflow

1. **Disable auto-compact** in settings (use full context window)
2. **Start fresh session** in project
3. **Run command** when ready for complex task
4. **Work until context fills up**
5. **Run `/clear`** to start fresh
6. **Run command again** — auto-recovers where you left off

## When to Use

**Use for:**
- Multi-step tasks (3+ steps)
- Research tasks
- Building/creating projects
- Tasks spanning many tool calls
- Complex debugging
- Large refactoring

**Skip for:**
- Simple questions
- Single-file edits
- Quick lookups
- Trivial changes

## Templates

### Task Plan Template
```markdown
# Task: [Brief Description]

**Created:** [Date]
**Status:** In Progress | Completed | Blocked

## Overview
[High-level description of what needs to be done]

## Phase 1: [Phase Name]
- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

## Phase 2: [Phase Name]
- [ ] [Task 1]
- [ ] [Task 2]

## Findings
<!-- Add discoveries as you go -->

## Errors
<!-- Track failures to avoid repeating -->
### [Date]
- Error: [description]
- Attempt: [what you tried]
- Result: [outcome]
```

### Findings Template
```markdown
# Findings

## Initial Analysis
<!-- Your initial understanding -->

## Research Results
<!-- What you discovered -->

## Code Observations
<!-- Notable code patterns -->

## External Resources
<!-- Links and references -->

## Decisions
<!-- Decisions made with rationale -->
```

### Progress Template
```markdown
# Progress Log

## Session 1 - [Date]
### Goals
- [Goal 1]
- [Goal 2]

### Completed
- [Completion 1]
- [Completion 2]

### Blocked On
- [Blocker 1]
- [Blocker 2]

### Next Session
- [Action 1]
- [Action 2]
```

## Best Practices

1. **Be Specific**: Make tasks actionable and measurable
2. **Check Often**: Re-read plan before major decisions
3. **Update Frequently**: Keep files current with progress
4. **Celebrate Wins**: Check off completed items
5. **Learn from Failures**: Document what didn't work
6. **Think in Phases**: Break complex work into phases

## Example Workflow

```
User: "Build a REST API for a todo app"

Assistant: Creating task_plan.md...
[Generates plan with phases: Design, Implement, Test, Deploy]

Session 1: Design phase completed
[Updates task_plan.md with findings]
[Progress.md logs session work]

Session 2 (after /clear):
[Auto-recovers from planning files]
"Continuing from where we left off..."
[Phase 2: Implementation begins]
```

## Integration

Works well with:
- **dev-workflow**: For complex project coordination
- **skill-creator**: For creating new skills systematically
- Any specialized skill for domain-specific planning
