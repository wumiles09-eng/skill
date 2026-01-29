---
name: superpowers
description: Collection of specialized development workflows including TDD, systematic debugging, collaboration patterns, and meta-skills for writing skills. Use when following rigorous development processes or coordinating team workflows.
---

# Superpowers

Collection of specialized development workflows and best practices.

## Available Skills

### Testing Skills

#### test-driven-development
Follow the RED-GREEN-REFACTOR cycle:
1. **RED**: Write a failing test
2. **GREEN**: Write minimal code to pass
3. **REFACTOR**: Improve code while tests pass

### Debugging Skills

#### systematic-debugging
4-phase root cause analysis:
1. **Gather Information**: Collect symptoms and context
2. **Form Hypothesis**: Propose potential causes
3. **Test Hypothesis**: Verify with controlled experiments
4. **Verify Fix**: Confirm resolution and prevent regression

#### verification-before-completion
Always verify work before marking complete:
- Run tests
- Check edge cases
- Validate requirements
- Review code quality

### Collaboration Skills

#### brainstorming
Structured ideation process:
1. Define problem space
2. Generate diverse ideas
3. Cluster and prioritize
4. Select best approaches

#### writing-plans
Create clear, actionable plans:
1. Define objectives
2. Break into phases
3. Identify dependencies
4. Set milestones

#### executing-plans
Execute plans systematically:
1. Follow phase order
2. Track progress
3. Handle blockers
4. Update documentation

#### dispatching-parallel-agents
Coordinate multiple agents:
1. Divide work into independent tasks
2. Assign tasks to agents
3. Collect results
4. Integrate outputs

#### requesting-code-review
Request effective code reviews:
1. Summarize changes
2. Highlight concerns
3. Provide context
4. Ask specific questions

#### receiving-code-review
Handle code review feedback:
1. Understand feedback
2. Discuss alternatives
3. Implement changes
4. Verify improvements

#### using-git-worktrees
Use Git worktrees for parallel work:
1. Create worktree for each task
2. Work independently
3. Test in isolation
4. Merge when ready

#### finishing-a-development-branch
Complete branches properly:
1. Final testing
2. Update documentation
3. Clean up code
4. Create pull request
5. Delete worktrees

#### subagent-driven-development
Leverage subagents effectively:
1. Identify suitable tasks
2. Provide clear context
3. Review agent outputs
4. Integrate results

### Meta Skills

#### writing-skills
Create new skills effectively:
1. Define skill scope
2. Write clear instructions
3. Provide examples
4. Test thoroughly

#### using-superpowers
Use this skill collection:
1. Select appropriate skill
2. Follow its process
3. Adapt as needed
4. Provide feedback

## Usage Patterns

### Test-Driven Development
```
1. Activate test-driven-development
2. Write failing test
3. Write minimal passing code
4. Refactor for quality
5. Repeat for next feature
```

### Systematic Debugging
```
1. Activate systematic-debugging
2. Gather symptoms and logs
3. Form hypotheses
4. Test with controlled experiments
5. Verify root cause
6. Implement fix
7. Verify resolution
```

### Code Review Workflow
```
Requester:
1. Activate requesting-code-review
2. Prepare review request
3. Send to reviewer

Reviewer:
1. Activate receiving-code-review
2. Review changes
3. Provide feedback
4. Discuss alternatives
```

### Parallel Development
```
1. Activate using-git-worktrees
2. Create worktree per feature
3. Work independently
4. Test each worktree
5. Merge sequentially
```

## Integration

Superpowers skills work with:
- **planning-with-files**: For persistent planning
- **dev-workflow**: For coordination
- **skill-creator**: For creating new skills
- All domain-specific skills

## Best Practices

1. **Explicit Activation**: Always state which skill you're using
2. **Follow Process**: Each skill has specific steps—follow them
3. **Adapt When Needed**: Processes are guidelines, not laws
4. **Document Deviations**: Note why and how you adapted
5. **Provide Feedback**: Help improve the skills

## Quick Reference

| Skill | Use When | Key Output |
|-------|----------|------------|
| test-driven-development | Writing new code | Tested, refactored code |
| systematic-debugging | Investigating bugs | Root cause identified |
| verification-before-completion | Finishing work | Verified quality |
| brainstorming | Generating ideas | Prioritized options |
| writing-plans | Starting projects | Actionable plans |
| executing-plans | Implementing | Completed work |
| requesting-code-review | Ready for review | Review request |
| receiving-code-review | Got feedback | Improved code |
| using-git-worktrees | Parallel work | Isolated branches |
| finishing-a-development-branch | Completing branch | Clean PR ready |

## Contributing

These skills evolve based on usage. Provide feedback on:
- What works well
- What needs improvement
- New skills to add
- Better processes
