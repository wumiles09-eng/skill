---
name: skill-evolution
description: Skill lifecycle management and evolution (inventory/update/evolution/closed-loop improvement). Maintain skill inventory, record trigger failures, capture best practices, update evolution.json. Use during task retrospectives, skill optimization.
---

# Skill Evolution - Skill Lifecycle and Evolution

## Goal

Establish closed-loop improvement mechanism for skills to evolve with usage.

## Skill Lifecycle

### 1. Creation Phase

```markdown
## Skill Creation Flow

### Need Identification
- [ ] Identify repeated task patterns
- [ ] Discover skill gaps
- [ ] Evaluate skill value

### Creation Steps
1. Use skill-creator to create skill skeleton
2. Write core SKILL.md content
3. Register in SKILLS_REGISTRY.json
4. Add typical trigger questions
5. Test skill trigger

### Creation Checklist
- [ ] skill name unique
- [ ] description clear and accurate
- [ ] At least 3 typicalQueries
- [ ] No overlap with existing skills
- [ ] Registered in registry
```

### 2. Usage Phase

```markdown
## Skill Usage Monitoring

### Normal Usage
- Skill triggers correctly
- Content satisfies needs
- Output format correct

### Abnormal Situations
- ❌ Skill doesn't trigger
- ❌ Wrong skill triggers
- ❌ Content doesn't satisfy needs
- ❌ Output format incorrect

### Record Format
```json
{
  "timestamp": "2026-01-29T10:00:00Z",
  "userQuery": "Original user question",
  "expectedSkill": "Should trigger skill",
  "actualSkill": "Actually triggered skill",
  "issue": "Problem description",
  "resolution": "Solution"
}
```
```

### 3. Optimization Phase

```markdown
## Skill Optimization Types

### Trigger Optimization
- Add typicalQueries
- Adjust description
- Add antiPatterns

### Content Optimization
- Update skill content
- Add new features
- Fix errors

### Performance Optimization
- Reduce token usage
- Optimize output format
- Simplify flow
```

### 4. Deprecation Phase

```markdown
## Skill Deprecation Conditions

- [ ] Functionality covered by other skills
- [ ] Unused for >6 months
- [ ] Tech stack obsolete
- [ ] Maintenance cost > value

### Deprecation Process
1. Mark as deprecated in registry
2. Document replacement skill
3. Keep for one version cycle
4. Finally delete
```

## Evolution Tracking

### evolution.json Structure

```json
{
  "version": "1.0.0",
  "lastUpdated": "2026-01-29",
  "statistics": {
    "totalSkills": 45,
    "activeSkills": 43,
    "deprecatedSkills": 2
  },
  "triggerFixes": [
    {
      "skillId": "requirements-clarifier",
      "date": "2026-01-29",
      "originalQuery": "Goals unclear",
      "fix": "Added to typicalQueries",
      "result": "Trigger successful"
    }
  ],
  "workflowFixes": [
    {
      "skillId": "workflow-orchestrator",
      "date": "2026-01-29",
      "issue": "Phase determination inaccurate",
      "fix": "Added decision tree",
      "result": "Accuracy improved"
    }
  ],
  "templateAdditions": [
    {
      "skillId": "tech-proposal",
      "date": "2026-01-29",
      "template": "A/B comparison table",
      "reason": "User feedback on missing format"
    }
  ],
  "antiPatterns": [
    {
      "pattern": "Implementing too much in single skill",
      "consequence": "Hard to maintain, inaccurate triggers",
      "solution": "Split into multiple sub-skills"
    }
  ]
}
```

## Retrospective Process

### Post-Task Retrospective

```markdown
## Task Retrospective Template

### Task Info
- Task Name: {Name}
- Completed: {Date}
- Skills Used: {List}

### Skill Usage
| Skill | Trigger Accurate | Content Satisfies | Improvement Suggestions |
|-------|------------------|-------------------|----------------------|
| skill1 | ✅/❌ | ✅/❌ | {Suggestion} |

### Issues Found
1. **Trigger Failure**: {Description}
   - User Query: "{Original}"
   - Expected Skill: {Skill}
   - Actual Trigger: {Skill or None}
   - Solution: {Approach}

2. **Content Gap**: {Description}
   - Missing: {Description}
   - Supplement: {Approach}

### Improvement Actions
- [ ] Update typicalQueries
- [ ] Supplement skill content
- [ ] Optimize flow
- [ ] Record to evolution.json
```

### Monthly Skill Audit

```markdown
## Monthly Skill Audit

### Audit Items
- [ ] All skills registered in registry
- [ ] Each skill has ≥3 typicalQueries
- [ ] Deprecated skills marked
- [ ] evolution.json updated

### Statistics
- Top 5 most used skills
- Bottom 5 least used skills
- Top 3 trigger failures
- New skills added

### Improvement Plan
- [ ] Skills needing optimization list
- [ ] Skills to deprecate list
- [ ] Skills to create list
```

## Closed-Loop Improvement

```
User Usage
    ↓
Record Issues
    ↓
Analyze Root Cause
    ↓
Implement Improvements
    ↓
Verify Effectiveness
    ↓
Update evolution.json
    ↓
Back to Usage
```

## Skill Quality Standards

### Trigger Quality

```markdown
## Trigger Accuracy Metrics

### Excellent (≥90%)
- Triggers correctly most of the time
- typicalQueries comprehensive
- antiPatterns clear

### Good (70-89%)
- Triggers correctly mostly
- Occasionally needs manual specification

### Needs Improvement (<70%)
- Frequently fails to trigger
- Needs many typicalQueries supplements
```

### Content Quality

```markdown
## Content Completeness Metrics

### Excellent
- Clear and complete structure
- Has specific examples
- Has best practices
- Has checklists

### Good
- Basically complete structure
- Has some examples
- Clear flow

### Needs Improvement
- Incomplete structure
- Lacks examples
- Unclear flow
```

## Integration with Other Skills

### Paired Skills
- `skill-indexer` - Index maintenance
- `workflow-orchestrator` - Workflow retrospective
- `planning-with-files` - Continuous improvement records

### Trigger Conditions
- After task retrospectives
- When skill issues found
- During monthly audits

## Best Practices

### 1. Continuous Improvement
- Record after each task
- Review evolution.json weekly
- Full audit monthly

### 2. Data-Driven
- Record actual usage
- Optimize based on data
- Verify optimization results

### 3. Community Contribution
- Share improvement experiences
- Contribute best practices
- Participate in skill reviews

---

**Maintenance**: Continuously optimize based on skill usage experience
**Source**: Cursor Hi Offer skill-lifecycle-and-evolution
**Related**: skill-indexer, skill-creator
