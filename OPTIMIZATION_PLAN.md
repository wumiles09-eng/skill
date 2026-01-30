# Skills Optimization Plan

## Current State Analysis

### Issues Identified

1. **Duplicate/Empty Directories**
   - `supabase-postgres/` - Empty, duplicate of `supabase-postgres-best-practices/`
   - `sync/` - Temporary directory, should be removed

2. **Naming Inconsistencies**
   - Some names very long: `supabase-postgres-best-practices`
   - Mix of patterns
   - No clear category prefixes

3. **Language Issues**
   - Many SKILL.md files contain Chinese content
   - Documentation files in Chinese
   - Need consistent English

## Optimization Plan

### Phase 1: Cleanup
- Remove `supabase-postgres/`
- Remove `sync/`

### Phase 2: Rename for Consistency

Better naming suggestions:
| Current | Proposed | Reason |
|---------|----------|--------|
| supabase-postgres-best-practices | postgres-best-practices | Shorter, clear |
| ui-ux-pro-max | design-system-generator | More descriptive |
| docs-and-knowledge-management | documentation | Simpler |
| code-review-checklist | code-review | Cleaner |
| skill-indexing-maintainer | skill-indexer | Shorter |
| skill-lifecycle-and-evolution | skill-evolution | Shorter |
| implementation-plan-writer | implementation-planner | More consistent |

### Phase 3: English Translation
- Update all SKILL.md to English
- Update README files
- Update documentation

### Phase 4: Categorization
Keep flat structure but ensure clear categorization in:
- _meta/SKILLS_REGISTRY.json
- README.md sections

## Execution Order

1. Remove duplicate/empty directories
2. Rename directories (if needed)
3. Update SKILL.md content to English
4. Update registry and documentation
5. Test and commit

Let me proceed with these optimizations.
