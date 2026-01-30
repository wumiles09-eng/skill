# Skill Naming Optimization Plan

## Current Issues

### 1. Contains Source/Author Names (should describe function, not source)
| Current | Proposed | Reason |
|---------|----------|--------|
| khazix-skills | code-analysis | Describes function, not author |
| obsidian-skills | obsidian | Describes tool, not plural |
| supabase-postgres-best-practices | postgres-optimization | Shorter, clearer |

### 2. Too Long (should be concise)
| Current | Proposed | Reason |
|---------|----------|--------|
| docs-and-knowledge-management | documentation | Much shorter |
| code-review-checklist | code-review | Simpler |
| implementation-plan-writer | implementation-planner | Consistent with -er suffix |
| ios-simulator-deployment | ios-deployment | Shorter, clearer |
| ui-ux-design-system-generator | design-system-generator | Remove redundant prefix |
| supabase-postgres-best-practices | postgres-optimization | Much shorter |
| vercel-react-best-practices | react-optimization | Shorter, clearer |

### 3. Plural Forms (should be singular)
| Current | Proposed | Reason |
|---------|----------|--------|
| khazix-skills | code-analysis | Singular |
| obsidian-skills | obsidian | Singular |

### 4. Source Prefixes (already standardized)
| Current | Proposed | Reason |
|---------|----------|--------|
| pencil-design-workflow | pencil-workflow | Remove redundant word |
| stitch-loop | stitch | Already short enough |

### 5. Too Short/Unclear
| Current | Proposed | Reason |
|---------|----------|--------|
| design-md | design-doc-generator | More descriptive |

## Proposed Renaming (14 changes)

| # | Current | New | Category |
|---|---------|-----|----------|
| 1 | khazix-skills | code-analysis | Learning |
| 2 | obsidian-skills | obsidian | Knowledge |
| 3 | supabase-postgres-best-practices | postgres-optimization | Backend |
| 4 | vercel-react-best-practices | react-optimization | Frontend |
| 5 | docs-and-knowledge-management | documentation | Knowledge |
| 6 | code-review-checklist | code-review | Quality |
| 7 | implementation-plan-writer | implementation-planner | Development |
| 8 | ios-simulator-deployment | ios-deployment | Deployment |
| 9 | ui-ux-design-system-generator | design-system-generator | Design |
| 10 | design-md | design-doc-generator | Stitch |
| 11 | pencil-design-workflow | pencil-workflow | Design |
| 12 | ui-ux-pro-max | design-system-reference | Design (legacy) |
| 13 | skill-indexing-maintainer | skill-indexer | Tools (already done) |
| 14 | skill-lifecycle-and-evolution | skill-evolution | Tools (already done) |

## Naming Principles

### 1. Descriptive
- Names should describe what the skill does
- Not where it comes from or who made it

### 2. Concise
- Aim for 1-3 words
- Avoid unnecessary prefixes
- Remove redundant words

### 3. Consistent
- Use kebab-case consistently
- Similar skills use similar patterns
- Suffixes: -er for tools, -generator for generative skills

### 4. Singular
- Skill names should be singular
- Not plural forms

### 5. Clear
- Names should be self-explanatory
- Avoid ambiguity

## Execution Plan

### Phase 1: Rename Directories
```bash
# Rename 14 directories
mv khazix-skills code-analysis
mv obsidian-skills obsidian
mv supabase-postgres-best-practices postgres-optimization
mv vercel-react-best-practices react-optimization
mv docs-and-knowledge-management documentation
mv code-review-checklist code-review
mv implementation-plan-writer implementation-planner
mv ios-simulator-deployment ios-deployment
mv ui-ux-design-system-generator design-system-generator
mv design-md design-doc-generator
mv pencil-design-workflow pencil-workflow
mv ui-ux-pro-max design-system-reference
```

### Phase 2: Update References
- Update README.md
- Update SKILLS_REGISTRY.json
- Update all SKILL.md files with references
- Update INTEGRATION docs

### Phase 3: Test and Commit
- Verify all references updated
- Commit changes
- Push to GitHub

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking existing workflows | High | Update all documentation, create redirects |
| Git history | Medium | Use git mv to preserve history |
| User confusion | Medium | Document changes clearly |

## Recommendation

✅ **Proceed with optimization** - Benefits outweigh risks:
- More professional naming
- Easier to understand
- Better consistency
- International friendly

Let me proceed with the optimization.
