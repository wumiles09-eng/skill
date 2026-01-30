---
name: skill-indexer
description: Maintain skill intelligent indexing (add typical queries/update capability summary/split sub-capabilities/check coverage). Use after task retrospectives, when triggers are inaccurate, or when creating new skills.
---

# Skill Indexer - Skill Indexing Maintainer

## Goal

Make skill indexing intelligent using "Smart Indexing" strategy to improve skill trigger accuracy.

## Smart Indexing Strategy

### Core Concept

> **Index ≠ Retrieval**
> Index is structured for "being found"; retrieval just queries that structure.

### 4-Layer Hybrid Indexing

```
User Query
    ↓
Parallel Match:
  ├─ Query Index (typicalQueries)
  ├─ Summary Index (summaryIndex)
  └─ Sub-Capability Index (subCapabilities)
    ↓
Best Match
    ↓
Return: Complete SKILL.md + references
```

## When to Use

1. **After task retrospectives**: Add "actual user phrasing" to index
2. **When triggers are inaccurate**: Add typicalQueries or adjust summaryIndex
3. **When creating new skill**: Register in SKILLS_REGISTRY.json
4. **During periodic audits**: Check index coverage, find gaps

## Operation Types

### 1. Add Typical Questions (Query Index Maintenance)

**Trigger**: User said something but skill didn't trigger

**Steps**:
1. Read `_meta/SKILLS_REGISTRY.json`
2. Find the skill
3. Add new phrasing to `queryIndex.typicalQueries`
4. Write back to file

**Example**:
```json
// User said "goals unclear" but requirements-clarifier didn't trigger
// → Add to typicalQueries

{
  "id": "requirements-clarifier",
  "queryIndex": {
    "typicalQueries": [
      "requirements unclear",
      "goals unclear"  // ← Added
    ]
  }
}
```

### 2. Update Capability Summary (Summary Index Maintenance)

**Trigger**: Skill capability changed, description inaccurate

**Steps**:
1. Read SKILL.md to confirm latest capability
2. Update `summaryIndex`:
   - `capability` (core capability)
   - `input` (when to use)
   - `output` (what it produces)
   - `keyPhrases` (key terminology)

### 3. Split Sub-Capabilities (Sub-Capability Index Maintenance)

**Trigger**:
- SKILL.md > 300 lines
- Contains multiple independent capability points
- Users often only need one part

**Steps**:
1. Identify independent capability points
2. Define for each:
   - `id` (unique identifier)
   - `name` (capability name)
   - `description` (what it does)
   - `triggers` (typical trigger words)
3. Add to `subCapabilities` array
4. **Note**: Don't modify original SKILL.md

### 4. Register New Skill

**Trigger**: Created new SKILL.md

**Steps**:
1. Add entry in `SKILLS_REGISTRY.json`
2. Required fields:
   - `id` / `name` / `path` / `type` / `layer`
3. Required indexing:
   - `queryIndex.typicalQueries` (at least 3-5)
   - `summaryIndex` (capability/input/output/keyPhrases)
4. Optional:
   - `subCapabilities`
   - `antiPatterns`
   - `dependencies`
   - `originRepo`

### 5. Index Coverage Audit

**Trigger**: Periodic check (recommended monthly)

**Check items**:
- [ ] All skills registered in SKILLS_REGISTRY.json?
- [ ] Each skill has ≥3 typicalQueries?
- [ ] Any common user questions without matching skill?
- [ ] Long skills (>300 lines) split into subCapabilities?

**Output**:
- Missing items list
- Suggested typicalQueries to add
- Suggested skills to split

## Maintenance Frequency

| Timing | Action | Time |
|--------|--------|------|
| After each task | Add 1-2 typicalQueries | 1 min |
| Create new skill | Register in SKILLS_REGISTRY.json | 3 min |
| Weekly | Audit inaccurate triggers | 5 min |
| Monthly | Full coverage audit + cleanup | 15 min |

## Output Format

After maintenance:

```markdown
## Indexing Complete

### This Update
- ✅ Added 2 typicalQueries for `xxx`
- ✅ Updated summaryIndex for `yyy`
- ✅ Registered new skill `zzz`

### Index Statistics
- Total skills: 45
- With queryIndex: 45
- With subCapabilities: 5
- Avg typicalQueries: 4.2

### Suggestions
- ⚠️ `aaa` >300 lines, suggest splitting subCapabilities
- ⚠️ `bbb` only 1 typicalQuery, suggest adding more
```

## Index Quality Standards

### Excellent Indexing

```markdown
### Query Index
- Typical queries ≥5
- Covers various phrasings
- Includes anti-patterns

### Summary Index
- capability clear and accurate
- input/output well-defined
- keyPhrases precisely extracted

### Sub-Capability Index
- Long skills split
- Each sub-capability has independent triggers
```

## Integration with Other Skills

- **In skill-lifecycle-and-evolution retrospectives**: Auto-trigger this skill to update index
- **When workflow-orchestrator triggers inaccurately**: Use this skill to add typicalQueries
- **When creating new skill**: Use this skill to register index

## References

- 4-layer intelligent indexing strategy: Based on RAG best practices
- Registry file: `_meta/SKILLS_REGISTRY.json`
- Evolution tracking: Use with evolution.json

---

**Maintenance**: Continuously optimize based on indexing effectiveness
**Source**: Cursor Hi Offer skill-indexing-maintainer
**Related**: skill-lifecycle-and-evolution, skill-creator
