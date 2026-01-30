# Skill Merge Plan - Code Quality Skills

## Current State Analysis

### Skills with Overlap

| Skill | Purpose | Coverage | Language |
|-------|---------|----------|----------|
| **code-analysis** (khazix-skills) | General code analysis, refactoring, documentation | Code smells, dependency mapping, refactoring strategies | English |
| **code-review** (code-review-checklist) | Systematic PR review with 6 dimensions | Correctness, maintainability, security, performance, testing, docs | Chinese |
| **skill-from-masters** | Pattern extraction from experts | Learning from expert codebases | English |

### Overlap Matrix

```
                    ┌─────────────────────────────────────┐
                    │         Code Quality Activities      │
                    └─────────────────────────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
        ▼                              ▼                              ▼
┌───────────────┐            ┌───────────────┐            ┌───────────────┐
│ code-analysis │            │ code-review   │            │  react-opt    │
├───────────────┤            ├───────────────┤            ├───────────────┤
│ Code analysis │  ◀────────►│ PR review     │            │ React perf    │
│ Code smells   │   OVERLAP   │ 6 dimensions  │            │ Hooks usage   │
│ Refactoring   │            │ Approval gate │            │ Rendering     │
│ Documentation │            │ Feedback      │            │ Bundle size   │
└───────────────┘            └───────────────┘            └───────────────┘
        │                              │                              │
        └──────────────────────────────┼──────────────────────────────┘
                                       │
                                       ▼
                            skill-from-masters
                            (Meta-skill for learning)
```

## Proposed Merge Structure

### Option 1: Unified Code Quality Skill (Recommended)

```
code-quality/
├── SKILL.md (unified code quality skill)
└── capabilities/
    ├── analysis.md (from code-analysis)
    ├── review.md (from code-review)
    └── patterns.md (from skill-from-masters)
```

**New Skill: `code-quality`**

| Capability | Source | Description |
|------------|--------|-------------|
| Code Analysis | code-analysis | Proactive codebase analysis |
| PR Review | code-review | Reactive pull request review |
| Pattern Extraction | skill-from-masters | Learning from expert code |

### Option 2: Separate by Phase

Keep separate but clarify differentiation:
- **code-analysis**: Proactive, pre-commit analysis
- **code-review**: Reactive, PR review workflow
- **skill-from-masters**: Meta-skill for pattern extraction

### Option 3: Domain-Specific Split

```
code-analysis (general, language-agnostic)
├── react-optimization (React-specific)
├── postgres-optimization (PostgreSQL-specific)
└── [future] python-optimization, etc.
```

## Merge Execution Plan (Option 1 - Recommended)

### Phase 1: Create Unified Skill

1. Create `code-quality/SKILL.md` with:
   - Frontmatter: `name: code-quality`
   - Description: Comprehensive code quality skill covering analysis, review, and pattern extraction
   - Three main sections: Analysis, Review, Patterns

2. Content from code-analysis:
   - Code structure analysis
   - Dependency mapping
   - Code smell detection
   - Refactoring strategies

3. Content from code-review:
   - 6-dimension review checklist
   - PR review workflow
   - Feedback templates

4. Content from skill-from-masters:
   - Pattern extraction process
   - Expert analysis methods
   - Skill creation templates

### Phase 2: Update References

1. Update README.md skill references
2. Update SKILLS_REGISTRY.json
3. Update integration documentation
4. Create migration guide

### Phase 3: Remove Old Skills

1. Archive old directories:
   - `code-analysis/` → `_archive/code-analysis/`
   - `code-review/` → `_archive/code-review/`
   - `skill-from-masters/` → `_archive/skill-from-masters/`

2. Git commit with descriptive message

### Phase 4: Test and Verify

1. Verify skill triggers correctly
2. Test all capabilities
3. Update documentation
4. Push to GitHub

## Skill Differentiation After Merge

| Skill | Focus | Trigger |
|-------|-------|---------|
| **code-quality** | General code quality (all languages) | "Review my code", "Analyze codebase", "Code smells" |
| **react-optimization** | React/Next.js specific | "React performance", "Next.js optimization" |
| **postgres-optimization** | PostgreSQL specific | "Database optimization", "Query performance" |

## Benefits of Merge

1. **Reduced Confusion**: Single entry point for code quality
2. **Comprehensive Coverage**: All aspects in one skill
3. **Easier Maintenance**: One place to update
4. **Better Discovery**: Clearer triggers and use cases

## Risks

1. **Skill Size**: May become too large (mitigate with sub-capabilities)
2. **Breaking Changes**: Existing workflows may reference old skills (mitigate with redirects)
3. **Loss of Specialization**: May dilute specific focuses (mitigate with clear sections)

## Recommendation

✅ **Proceed with Option 1** - Unified `code-quality` skill

This provides the best balance of:
- Comprehensive coverage
- Clear differentiation
- Easy maintenance
- Reduced confusion

## Next Steps

Await user approval to proceed with merge execution.
