# Skills Integration Analysis

## Summary of Integration

This analysis compares three skill collections and identifies unique, high-value additions to integrate.

---

## Source Collections

### 1. Current GitHub Repo (21 skills)
- Basic frontend, backend, QA skills
- Stitch AI integration (design-md, stitch-loop, react-components)
- Simple indexing (skills-index.json, FIND_SKILL.md)

### 2. Cursor Hi Offer (21 skills)
**Unique Value:**
- **workflow-orchestrator**: End-to-end workflow with phase determination
- **ui-ux-design-system-generator**: 67 styles, 96 palettes, 57 fonts with industry reasoning
- **skill-indexing-maintainer**: 4-layer intelligent indexing (query + summary + sub-chunk + block)
- **SKILLS_REGISTRY.json**: Machine-readable registry with evolution tracking
- Specialized skills for each R&D phase
- Pencil & Stitch design workflows

### 3. VerveFlow (7-phase workflow)
**Unique Value:**
- Strict sequential phases with mandatory checkpoints
- Progressive delivery methodology
- PRD generator with Mermaid flowcharts
- Tech proposal with A/B comparison
- iOS simulator deployment with complete troubleshooting
- Obsidian integration patterns
- OpenSpec SDD methodology

### 4. Visual-Test (Already integrated)
- Playwright MCP visual testing workflow
- Comprehensive UI checklist
- Multi-viewport testing patterns

---

## Integration Decision Matrix

| Feature | Current | Cursor | VerveFlow | Decision |
|---------|---------|--------|-----------|----------|
| Basic orchestration | dev-workflow | workflow-orchestrator | - | **Keep both**, enhance dev-workflow |
| Design system | ui-ux-pro-max | ui-ux-design-system-generator (67/96/57) | - | **Replace with Cursor version** (richer data) |
| Intelligent indexing | 3-layer simple | 4-layer with evolution | - | **Upgrade to Cursor system** |
| Requirements | planning-with-files | requirements-clarifier + optimize-iteration-spec | prd-generator + tech-proposal | **Merge all three** |
| Design phase | frontend-design | architecture-designer + docs-and-knowledge-management | pencil-prd-compliance-audit | **Add all** |
| Testing | audit-website | testing-orchestrator + quality-gate | - | **Add Cursor skills** |
| Deployment | - | deployment-and-ops + versioning-and-release | ios-simulator-deployment | **Add all** |
| Evolution | skills-updater | skill-lifecycle-and-evolution + skill-indexing-maintainer | - | **Add Cursor system** |
| Design workflows | stitch-loop | pencil-design-workflow + stitch-design-workflow | - | **Add Pencil workflow** |
| Visual testing | visual-test | (included) | (integrated) | **Already integrated** |

---

## New Skills to Add (12 unique)

### High Priority (P0) - Unique Capabilities

1. **workflow-orchestrator** (Cursor)
   - Phase determination + deliverable generation
   - File-based persistent memory
   - Better than current dev-workflow

2. **ui-ux-design-system-generator** (Cursor)
   - 67 styles, 96 palettes, 57 fonts
   - Industry reasoning engine
   - Script-based search with --persist
   - Replaces current ui-ux-pro-max

3. **skill-indexing-maintainer** (Cursor)
   - 4-layer intelligent indexing
   - Evolution tracking (evolution.json)
   - Self-improving system

4. **SKILLS_REGISTRY.json** (Cursor)
   - Machine-readable registry
   - Query + summary + sub-chunk indices
   - Dependencies and anti-patterns

5. **requirements-clarifier** (Cursor)
   - Structured requirement extraction
   - Given-When-Then format
   - PRD skeleton generation

6. **optimize-iteration-spec** (Cursor)
   - Four-layer structure scoring
   - Auto-completion templates
   - Sub-capabilities: scoring, completion, examples

7. **architecture-designer** (Cursor)
   - System boundaries + modules + data flow
   - ADR recording
   - API design

8. **testing-orchestrator** (Cursor)
   - Test strategy (Unit/Integration/E2E)
   - Coverage requirements
   - Failure analysis

9. **quality-gate** (Cursor)
   - TDD first requirement
   - Regression testing
   - Pre-completion verification

10. **deployment-and-ops** (Cursor)
    - Deployment + migration + rollback
    - Runbook generation
    - Monitoring & alerting

11. **versioning-and-release** (Cursor)
    - SemVer management
    - Changelog generation
    - Release process

12. **prd-generator** (VerveFlow)
    - Business language PRD
    - Mermaid flowchart standard
    - Obsidian integration

13. **tech-proposal** (VerveFlow)
    - A/B方案对比
    - Cost/time/risk evaluation
    - Quantified assessment

14. **ios-simulator-deployment** (VerveFlow)
    - Complete iOS build/install/launch
    - Troubleshooting guide
    - Best practices

15. **pencil-design-workflow** (Cursor)
    - Pixel-perfect design-to-code
    - Component library alignment
    - Pencil MCP integration

### Medium Priority (P1) - Enhancements

16. **docs-and-knowledge-management** (Cursor)
    - PRD/Design/ADR/Test/Runbook governance
    - Optional Obsidian integration

17. **implementation-plan-writer** (Cursor)
    - Task breakdown with estimates
    - Test plan generation
    - Risk assessment

18. **coding-executor** (Cursor)
    - Execute by task checklist
    - Small steps + verification
    - Persistent records

19. **code-review-checklist** (Cursor)
    - Correctness/maintainability/security
    - Performance/testing/docs checks

20. **skill-lifecycle-and-evolution** (Cursor)
    - Skill inventory/update/evolution
    - Closed-loop improvement
    - Evolution.json tracking

---

## Skills to Replace/Upgrade

| Current Skill | Replacement | Reason |
|--------------|-------------|--------|
| ui-ux-pro-max | ui-ux-design-system-generator | Cursor version has 67/96/57 data + scripts |
| dev-workflow | workflow-orchestrator (merge) | Cursor has better phase determination + persistent memory |
| skills-index.json | SKILLS_REGISTRY.json (Cursor) | 4-layer indexing + evolution tracking |
| planning-with-files | planning-with-files-lite (Cursor) | Lighter version, 2-action rule |

---

## Files to Keep Unchanged

All basic skills remain:
- agent-browser
- audit-website
- building-native-ui
- design-md
- document-suite
- frontend-design
- khazix-skills
- obsidian-skills
- seo-audit
- skill-creator
- skill-from-masters
- supabase-postgres-best-practices
- superpowers
- vercel-react-best-practices
- web-design-guidelines
- visual-test (already integrated)

---

## Updated Index Structure

After integration, the repo will have:
- **Total skills**: ~40 (21 current + ~15-20 new)
- **Categories**: 10 (stitch, design, development, qa, productivity, documentation, automation, learning, tools, orchestrator)
- **Phases covered**: Idea → Requirement → Design → Tech Solution → Development → Testing → Deployment → Promotion → Knowledge Management → Iteration → Skill Evolution

---

## Integration Order

1. Create _meta/ directory structure
2. Add SKILLS_REGISTRY.json
3. Add high-priority skills (P0)
4. Add medium-priority skills (P1)
5. Update indexing files
6. Update README.md
7. Update skills-index.json
8. Commit and push

---

## Next Steps

1. Create new skill directories with SKILL.md
2. Copy data/ and scripts/ for ui-ux-design-system-generator
3. Create _meta/ with registry and indexing strategy docs
4. Update all index files
5. Test integration
6. Push to GitHub
