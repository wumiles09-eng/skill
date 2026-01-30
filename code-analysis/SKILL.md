---
name: code-analysis
description: Language-agnostic code analysis principles. Use for general code quality assessment, architecture analysis, dependency mapping, and refactoring strategies that apply across all programming languages.
---

# Code Analysis

Language-agnostic code analysis for comprehensive code quality assessment.

## Purpose

Analyze codebases for quality, maintainability, and improvement opportunities across any programming language or framework.

## Core Principles

### 1. Language-Agnostic Analysis

Focus on universal code quality principles:
- **Readability**: Code should be self-documenting
- **Simplicity**: Prefer simple solutions over clever ones
- **Modularity**: Small, focused units with single responsibilities
- **Consistency**: Uniform patterns and conventions
- **Testability**: Code should be easy to test

### 2. Analysis Dimensions

| Dimension | What to Check | Indicators |
|-----------|---------------|------------|
| **Structure** | Code organization | Module boundaries, dependency direction, coupling |
| **Complexity** | Cognitive load | Cyclomatic complexity, nesting depth, function length |
| **Duplication** | Repeated patterns | Copy-paste code, similar logic blocks |
| **Smells** | Maintainability issues | God classes, long methods, feature envy |
| **Dependencies** | External coupling | Third-party usage, circular dependencies |

## Analysis Workflow

### Phase 1: Discovery

```
1. Map codebase structure
2. Identify modules and boundaries
3. Trace dependency graph
4. Locate complexity hotspots
5. Find code duplication
```

### Phase 2: Assessment

```
1. Evaluate code smells
2. Assess coupling and cohesion
3. Review error handling
4. Check test coverage
5. Identify security risks
```

### Phase 3: Recommendations

```
1. Prioritize by impact
2. Suggest refactoring strategies
3. Recommend testing improvements
4. Document architecture decisions
```

## Common Code Smells (Language-Agnostic)

### Structural Smells

| Smell | Description | Impact |
|-------|-------------|--------|
| **God Class/Object** | Class does too much | Hard to maintain, test |
| **Long Method** | Method too complex | Hard to understand, test |
| **Feature Envy** | Method uses another class's data | Wrong responsibility |
| **Data Clumps** | Same data passed together | Should be object/class |
| **Primitive Obsession** | Using primitives instead of types | Loss of type safety |

### Behavioral Smells

| Smell | Description | Impact |
|-------|-------------|--------|
| **Shotgun Surgery** | One change requires many files | High coupling |
| **Divergent Change** | One class changed for different reasons | Wrong cohesion |
| **Parallel Inheritance** | Must create subclass of A when subclassing B | Tight coupling |
| **Refused Bequest** | Subclass rejects parent methods | Broken inheritance |

## Refactoring Strategies

### Safe Refactoring Process

```
1. Characterize the change
2. Find test coverage (or create tests)
3. Apply refactoring incrementally
4. Run tests after each step
5. Commit after each verified step
```

### Common Refactorings

| Pattern | When to Use | Benefit |
|---------|-------------|---------|
| **Extract Method** | Long method | Readability, reusability |
| **Extract Class** | God class | Single responsibility |
| **Introduce Parameter Object** | Data clumps | Type safety, clarity |
| **Replace Conditional with Polymorphism** | Complex conditionals | Extensibility |
| **Decompose Conditional** | Complex if/else | Readability |

## Dependency Analysis

### Dependency Graph

Map relationships between:
- Modules → Modules
- Classes → Classes
- Functions → Functions

### Healthy Dependencies

```markdown
✅ Good: Dependencies point inward (core has no dependencies)
✅ Good: Acyclic (no circular dependencies)
✅ Good: Stable depend on unstable (inversion)

❌ Bad: Circular dependencies
❌ Bad: Everything depends on everything
❌ Bad: Core depends on UI/presentation
```

### Coupling Levels

| Level | Description | Example |
|-------|-------------|---------|
| **No Coupling** | Independent | Utility functions |
| **Data Coupling** | Pass data | Simple parameters |
| **Stamp Coupling** | Pass data structure | Object with many fields |
| **Control Coupling** | Pass control flags | Boolean flags affecting flow |
| **Global Coupling** | Shared state | Global variables |

## Integration with Domain Skills

### When to Use Domain-Specific Skills

| Skill | When to Use | Examples |
|-------|-------------|----------|
| **code-analysis** | General code quality | "Review my code", "Find code smells" |
| **react-optimization** | React/Next.js specific | "Optimize React rendering", "Fix hooks" |
| **postgres-optimization** | PostgreSQL specific | "Optimize queries", "Index strategy" |
| **code-review** | Pull request review | "Review this PR", "Check my changes" |

### Workflow Example

```
User: "Analyze my React app for performance issues"

Step 1: code-analysis (general assessment)
   → Identify: Large components, unclear state flow

Step 2: react-optimization (React-specific)
   → Fix: Hook dependencies, memoization, bundle size

Step 3: code-review (validation)
   → Verify: Changes follow best practices
```

## Output Format

### Analysis Report

```markdown
# Code Analysis Report

## Summary
- Total files: X
- Lines of code: Y
- Complexity: Low/Medium/High
- Test coverage: Z%

## Key Findings
1. [Priority] Issue description
   - Location: file:line
   - Impact: description
   - Suggestion: actionable fix

2. [Priority] Another issue
   ...

## Recommendations
Prioritized list of improvements
```

## Best Practices

### For Large Codebases

1. **Start Small**: Analyze one module at a time
2. **Measure First**: Establish baseline metrics
3. **Incremental Changes**: Small, verifiable steps
4. **Document Decisions**: ADRs for architecture changes

### For Teams

1. **Shared Standards**: Agree on code quality principles
2. **Regular Reviews**: Scheduled analysis sessions
3. **Track Metrics**: Monitor trends over time
4. **Celebrate Improvements**: Recognize progress

## Anti-Patterns

### Don't Do This

❌ Rewrite everything from scratch
❌ Optimize prematurely
❌ Ignore tests while refactoring
❌ Make changes without understanding
❌ Apply patterns blindly

### Do This Instead

✅ Understand before changing
✅ Small, incremental improvements
✅ Test-driven refactoring
✅ Document the "why"
✅ Adapt patterns to context

## Related Skills

- **code-review**: Pull request review workflow
- **react-optimization**: React/Next.js specific optimization
- **postgres-optimization**: PostgreSQL specific optimization
- **skill-from-masters**: Pattern extraction from expert code

---

**Language**: Language-agnostic (applies to all programming languages)
**Layer**: Development
**Phase**: Iteration/Analysis
