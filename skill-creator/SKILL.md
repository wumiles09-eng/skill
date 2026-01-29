---
name: skill-creator
description: Create custom Claude Code skills with proper structure, metadata, and documentation. Use when the user wants to create a new skill for specialized tasks, workflows, or domain-specific knowledge.
---

# Skill Creator

This skill helps you create new Claude Code skills with proper structure and metadata.

## Skill Structure

A skill is a directory containing at minimum a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
author: Optional author name
version: 1.0.0
license: MIT
---

# Skill Title

Detailed instructions for Claude to follow when this skill is active.
```

## Required Fields

### name
- Unique identifier for the skill
- Lowercase with hyphens for spaces
- Must match directory name
- Example: `react-best-practices`

### description
- Complete description of what the skill does
- Must explain WHEN to use the skill
- Should be clear and specific
- Example: "Use when reviewing React code for performance issues"

## Optional Metadata

```yaml
author: Your Name or Organization
version: 1.0.0
license: MIT | Apache-2.0 | GPL-3.0
tags: [category1, category2]
related: [skill1, skill2]
```

## Skill Content Guidelines

### 1. Clear Purpose
The skill should solve a specific, well-defined problem. Avoid overly broad skills.

### 2. When to Use
Explicitly state when this skill should be invoked:
- "Use this skill when..."
- "Invoke this skill for..."
- "This skill activates when..."

### 3. Step-by-Step Instructions
Break down tasks into clear, actionable steps:
```markdown
## Process
1. First, analyze the...
2. Then, identify...
3. Finally, recommend...
```

### 4. Examples
Provide concrete examples of skill usage:
```markdown
## Examples
User: "Review this React component"
Assistant: [Activates skill] "I'll review your component using [skill-name]..."
```

### 5. Guidelines
Include any constraints or best practices:
```markdown
## Guidelines
- Always check for...
- Never suggest...
- Consider...
```

## Installation Location

Skills should be installed in:
```
~/.claude/skills/
├── skill-name/
│   └── SKILL.md
```

## Skill Template

```markdown
---
name: my-skill
description: Use this skill when [specific condition]. It helps [what it does].
---

# My Skill

## Purpose
This skill helps with [specific task].

## When to Use
Activate this skill when the user asks for [specific type of request].

## Process
1. [First step]
2. [Second step]
3. [Third step]

## Guidelines
- [Important rule 1]
- [Important rule 2]
- [Important rule 3]

## Examples
User: "[Example request]"
Assistant: "[Example response using skill]"
```

## Best Practices

1. **Single Responsibility**: Each skill should do one thing well
2. **Clear Naming**: Use descriptive, self-explanatory names
3. **Comprehensive Description**: Explain when and why to use the skill
4. **Testable**: Skills should produce consistent, predictable results
5. **Maintainable**: Keep skills focused and avoid scope creep
6. **Documented**: Include examples and usage patterns
