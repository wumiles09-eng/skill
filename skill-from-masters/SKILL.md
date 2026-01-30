---
name: skill-from-masters
description: Meta-skill for extracting patterns from expert developers and creating reusable skills. Use when you want to learn from expert codebases, codify best practices, or create new skills based on master-level patterns.
---

# Skill From Masters

Meta-skill for learning from expert developers and creating reusable skills.

## Purpose

Extract patterns and practices from expert codebases to:
- Learn from proven approaches
- Create reusable skills from best practices
- Codify expert-level patterns
- Accelerate team learning

## When to Use

| Trigger | Description |
|---------|-------------|
| "Learn from expert code" | Want to study master-level code |
| "Create skill from patterns" | Extract patterns into reusable form |
| "Analyze expert's approach" | Understand how experts solve problems |
| "Codify best practices" | Document proven patterns |

## When NOT to Use

| Situation | Use Instead |
|-----------|-------------|
| Reviewing a PR | `code-review` |
| Analyzing your codebase | `code-analysis` |
| Improving code quality | Domain-specific skills |
| Optimizing performance | `react-optimization`, `postgres-optimization` |

## Process

### Phase 1: Identify Expert Source

Find codebases known for:
- Clean code practices
- Performance optimization
- Security expertise
- Scalability patterns
- Domain excellence

### Phase 2: Analyze Patterns

Extract patterns in these areas:

#### Code Organization
```
- File structure and hierarchy
- Module boundaries
- Layer separation
- Dependency flow
- Naming conventions
```

#### Coding Style
```
- Function design principles
- Class structure patterns
- Variable naming
- Comment style
- Error handling approach
```

#### Architecture
```
- Design patterns used
- Abstraction levels
- Interface design
- State management
- Data flow patterns
```

#### Testing
```
- Test organization
- Coverage strategies
- Mocking patterns
- Test data management
- Integration testing
```

### Phase 3: Codify as Skill

Create structured skill with:

```markdown
---
name: [skill-name]
description: [clear description of when to use]
---

# [Skill Name]

## Purpose
[What this skill does and when to use it]

## Patterns
[Extracted patterns with examples]

## Usage
[How to apply these patterns]

## Examples
[Real code examples from source]
```

### Phase 4: Validate and Iterate

```
1. Test skill on new codebases
2. Refine pattern descriptions
3. Add more examples
4. Document edge cases
```

## Pattern Categories

### 1. Structural Patterns

| Pattern | Description | Example Source |
|---------|-------------|----------------|
| **Layered Architecture** | Clear separation of concerns | Enterprise apps |
| **Repository Pattern** | Data access abstraction | Database-backed apps |
| **Factory Pattern** | Object creation abstraction | UI libraries |
| **Observer Pattern** | Event-driven updates | Reactive systems |

### 2. Behavioral Patterns

| Pattern | Description | Example Source |
|---------|-------------|----------------|
| **Strategy Pattern** | Interchangeable algorithms | Validation systems |
| **Command Pattern** | Encapsulated actions | Undo/redo systems |
| **Chain of Responsibility** | Sequential processing | Middleware systems |
| **State Machine** | State-driven behavior | Workflow systems |

### 3. Quality Patterns

| Pattern | Description | Example Source |
|---------|-------------|----------------|
| **Test-Driven Development** | Tests before implementation | TDD practitioners |
| **Continuous Integration** | Automated validation | DevOps experts |
| **Code Review Culture** | Collaborative quality | Open source projects |
| **Documentation First** | Docs before code | Well-documented projects |

## Example Workflow

```
User: "Learn how master developer X structures their React apps"

[Step 1] Identify patterns
   → Component hierarchy
   → State management approach
   → Hook patterns
   → Testing strategy

[Step 2] Extract with examples
   → Code snippets from X's projects
   → Annotate decisions

[Step 3] Create skill
   → Name: react-patterns-from-x
   → Document patterns
   → Include examples

[Step 4] Validate
   → Apply to new project
   → Refine descriptions
```

## Integration with Other Skills

### Uses Output From
- `code-analysis`: Identifies patterns worth extracting
- `code-review`: Finds good practices in PRs

### Produces Input For
- `skill-creator`: Creates new skills from extracted patterns
- Domain skills: Enhances existing skills with expert patterns

### Collaboration
- `documentation`: Documents extracted patterns
- `dev-workflow`: Applies learned patterns to projects

## Best Practices

### 1. Respect Source
- Attribute patterns to original source
- Don't claim others' work as your own
- Follow licensing requirements

### 2. Context Matters
- Document why patterns work
- Note applicable contexts
- Identify anti-patterns

### 3. Validate Patterns
- Test on multiple codebases
- Check for edge cases
- Refine with feedback

### 4. Teach, Don't Copy
- Explain principles behind patterns
- Provide context for decisions
- Enable adaptation, not just copying

## Output Format

### Extracted Skill Template

```markdown
---
name: [pattern-name]
description: [Clear description]
source: [Original expert/codebase]
---

# [Pattern Name]

## Source
Learned from: [Expert/Project]
URL: [Link if available]

## The Pattern
[Description of the pattern]

## When to Use
[Conditions where pattern applies]

## How to Apply
[Step-by-step implementation]

## Examples
[Code examples from source]

## Trade-offs
[Pros and cons of this pattern]

## Related Patterns
[Links to related approaches]
```

## Anti-Patterns

### Don't Do This

❌ Copy code without understanding
❌ Apply patterns without context
❌ Claim others' work as original
❌ Ignore license restrictions
❌ Over-engineer with patterns

### Do This Instead

✅ Understand the principles
✅ Adapt to your context
✅ Attribute sources properly
✅ Respect licenses and copyright
✅ Use patterns judiciously

## Examples of Learned Patterns

### From React Core Team
- Component composition over inheritance
- Hooks for encapsulating side effects
- Colocation of related code

### From Database Experts
- Index selection strategies
- Query optimization patterns
- Transaction design principles

### From Security Researchers
- Defense in depth
- Principle of least privilege
- Secure by default patterns

---

**Type**: Meta-skill (creates other skills)
**Layer**: Learning / Evolution
**Phase**: Knowledge Management / Skill Evolution
**Related**: skill-creator, code-analysis, documentation
