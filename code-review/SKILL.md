---
name: code-review
description: Systematic pull request and code change review. Use during PR review, merge request evaluation, or when checking code changes before committing. Covers 6 dimensions: correctness, maintainability, security, performance, testing, and documentation.
---

# Code Review

Systematic code review workflow ensuring quality standards for pull requests and code changes.

## Purpose

Review pull requests and code changes systematically to ensure:
- Code meets quality standards
- Changes are safe to merge
- Knowledge is shared across team
- Best practices are followed

## When to Use

| Trigger | Description |
|---------|-------------|
| "Review my PR" | Pull request needs review |
| "Check this code" | Quick code quality check |
| "Ready to merge?" | Pre-merge validation |
| "Code review needed" | Formal review process |

## When NOT to Use

| Situation | Use Instead |
|-----------|-------------|
| Analyzing existing codebase | `code-analysis` |
| Optimizing React performance | `react-optimization` |
| Finding performance bottlenecks | Domain-specific skills |
| Learning from expert code | `skill-from-masters` |

## Review Dimensions

### 1. Correctness

```markdown
## Functional Correctness

### Logic Verification
- [ ] Code implements stated requirements
- [ ] Edge cases handled properly
- [ ] Error handling comprehensive
- [ ] No obvious bugs

### Boundary Conditions
- [ ] Null/undefined checks
- [ ] Array/string boundaries
- [ ] Min/max values
- [ ] Concurrent/race conditions

### Error Handling
- [ ] Try-catch where needed
- [ ] Error messages clear
- [ ] No sensitive data in errors
- [ ] Proper logging
```

### 2. Maintainability

```markdown
## Code Maintainability

### Readability
- [ ] Clear variable/function names
- [ ] Logical code structure
- [ ] Comments for complex logic
- [ ] Reasonable nesting depth

### Modularity
- [ ] Single responsibility functions
- [ ] Reasonable function length (<50 lines)
- [ ] No code duplication
- [ ] Appropriate abstraction

### Documentation
- [ ] Complex logic explained
- [ ] Public APIs documented
- [ ] Examples correct
- [ ] README updated if needed
```

### 3. Security

```markdown
## Security Review

### Input Validation
- [ ] User input validated
- [ ] SQL injection prevention
- [ ] XSS attack prevention
- [ ] File type validation

### Data Security
- [ ] Sensitive data encrypted
- [ ] No information leakage
- [ ] Secure password storage
- [ ] HTTPS for communication

### Access Control
- [ ] Permission checks
- [ ] Resource authorization
- [ ] API authentication
- [ ] Privilege escalation prevention
```

### 4. Performance

```markdown
## Performance Considerations

### Algorithm Complexity
- [ ] Reasonable time complexity
- [ ] Unnecessary loops avoided
- [ ] Appropriate data structures
- [ ] Reasonable nesting depth

### Resource Usage
- [ ] No memory leaks
- [ ] Resources released properly
- [ ] DOM operations minimized
- [ ] Caching used appropriately

### Async Handling
- [ ] Non-blocking where needed
- [ ] Proper Promise handling
- [ ] No callback hell
- [ ] Comprehensive error handling
```

### 5. Testing

```markdown
## Test Coverage

### Unit Tests
- [ ] Core logic tested
- [ ] Edge cases covered
- [ ] Error paths tested
- [ ] Tests are meaningful

### Test Quality
- [ ] Clear test names
- [ ] Tests are independent
- [ ] Accurate assertions
- [ ] No flaky tests

### Coverage
- [ ] New code meets coverage threshold
- [ ] Critical paths covered
- [ ] Coverage not decreased
```

### 6. Documentation

```markdown
## Documentation Completeness

### Code Comments
- [ ] Complex logic explained
- [ ] Comments explain "why" not "what"
- [ ] Comments match code
- [ ] No outdated comments

### API Documentation
- [ ] Public APIs documented
- [ ] Parameter types specified
- [ ] Return values described
- [ ] Usage examples included

### Change Documentation
- [ ] README updated if needed
- [ ] CHANGELOG updated
- [ ] Migration guide if breaking
```

## Review Process

### Step 1: Quick Scan (2 minutes)

```markdown
## Initial Assessment

### Basic Checks
- PR title clear and descriptive?
- Description explains what and why?
- Related issues linked?
- Scope of changes reasonable?

### Automated Checks
- [ ] CI pipeline passes
- [ ] All tests pass
- [ ] Coverage threshold met
- [ ] No new warnings introduced
```

### Step 2: Deep Review (10-15 minutes)

```markdown
## Detailed Review

### Code Changes
```diff
# Review the actual diff
{content}
```

### Focus Areas
- Core logic changes
- Complex algorithms
- Security-sensitive code
- Performance-critical paths
```

### Step 3: Feedback

```markdown
## Feedback Format

### Issue Report
```markdown
### Issue: {Brief description}

**Location**: `{file}:{line}`

**Problem**: {Detailed explanation}

**Suggestion**: {Actionable recommendation}

**Priority**: [Must fix / Should fix / Nice to have]
```

### Positive Feedback
```markdown
### Good practice: {Description}

**Location**: `{file}:{line}`

**Why it's good**: {Reason}
```
```

## Common Issues

### 1. Correctness Problems

```markdown
## Common Correctness Errors

### Missing Boundary Checks
```javascript
// ❌ Wrong: No empty check
function getFirst(arr) {
  return arr[0];
}

// ✅ Correct: Boundary check
function getFirst(arr) {
  if (!arr || arr.length === 0) {
    return null;
  }
  return arr[0];
}
```

### Async Error Handling
```javascript
// ❌ Wrong: No error handling
async function fetchData() {
  const data = await fetch(url);
  return data.json();
}

// ✅ Correct: Comprehensive error handling
async function fetchData() {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Fetch failed:', error);
    throw error;
  }
}
```
```

### 2. Performance Issues

```markdown
## Common Performance Issues

### Unnecessary Re-renders (React)
```javascript
// ❌ Wrong: New function each render
function Component() {
  return <Button onClick={() => handleClick()} />;
}

// ✅ Correct: useCallback
function Component() {
  const handleClick = useCallback(() => {
    // ...
  }, []);
  return <Button onClick={handleClick} />;
}
```

### DOM Operations in Loops
```javascript
// ❌ Wrong: Multiple reflows
for (let i = 0; i < 1000; i++) {
  document.body.appendChild(createElement());
}

// ✅ Correct: Single reflow with DocumentFragment
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  fragment.appendChild(createElement());
}
document.body.appendChild(fragment);
```
```

## Review Checklist

```markdown
## Code Review Checklist

### Quick Checks (2 minutes)
- [ ] CI passes
- [ ] Tests pass
- [ ] Description clear
- [ ] Changes reasonable

### Deep Review (10-15 minutes)
- [ ] Functional correctness
- [ ] Code readability
- [ ] Security reviewed
- [ ] Performance considered
- [ ] Tests adequate
- [ ] Documentation complete

### Feedback
- [ ] Issues clearly described
- [ ] Suggestions actionable
- [ ] Priorities indicated
- [ ] Tone constructive
```

## Integration with Other Skills

### Pre-requisites
- `coding-executor`: Code is ready for review after implementation
- `testing-orchestrator`: Tests passing before review

### Post-review
- `quality-gate`: Review must pass before quality gate
- `deployment-and-ops`: Approved code can proceed to deployment

### Collaboration
- `code-analysis`: Deep dive into code quality issues found
- `react-optimization`: React-specific performance fixes
- Domain skills: Specific optimization recommendations

## Best Practices

### 1. Timely Reviews
- Review PRs within 24 hours
- Avoid large code accumulation
- Request partial reviews for large changes

### 2. Constructive Feedback
- Explain the "why" behind suggestions
- Provide actionable alternatives
- Acknowledge good practices

### 3. Collaborative Approach
- Ask questions instead of demanding changes
- Suggest, don't dictate
- Share knowledge, not just criticism

## Output Format

### Review Summary

```markdown
# Code Review Summary

## Status: [Approved / Approved with changes / Request changes]

## Overview
Brief summary of the changes and overall impression.

## Must Fix (Blocking)
- [ ] Issue 1
- [ ] Issue 2

## Should Fix (Non-blocking)
- [ ] Suggestion 1
- [ ] Suggestion 2

## Nice to Have
- [ ] Enhancement 1

## Positive Notes
- Good practice observed
```

---

**Workflow**: Pull Request / Merge Request Review
**Layer**: Quality Assurance
**Phase**: Testing / Quality Gate
**Related**: code-analysis, quality-gate, testing-orchestrator
