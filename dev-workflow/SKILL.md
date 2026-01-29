---
name: dev-workflow
description: Development workflow orchestrator that coordinates multiple specialized skills for comprehensive development tasks. Use this skill when working on complex projects that require multiple skills like frontend design, React best practices, database optimization, SEO, and quality assurance working together.
---

# Development Workflow Orchestrator

This skill orchestrates multiple specialized skills to provide comprehensive development workflows.

## Available Skills

### Frontend Development
- **frontend-design**: Production-grade frontend interfaces
- **web-design-guidelines**: UI/UX review and improvement
- **vercel-react-best-practices**: React/Next.js optimization
- **building-native-ui**: Expo/React Native development

### Backend & Data
- **supabase-postgres-best-practices**: PostgreSQL optimization

### Quality Assurance
- **audit-website**: Comprehensive website auditing
- **seo-audit**: Search engine optimization
- **web-design-guidelines**: Design quality review

### Automation & Tools
- **agent-browser**: Browser automation
- **skill-creator**: Create custom skills

## Workflow Templates

### Workflow 1: Frontend Development Pipeline
**Use when**: Building new web applications or components

```
Requirements → frontend-design → web-design-guidelines → vercel-react-best-practices → Delivery
```

**Steps**:
1. Use **frontend-design** to create initial implementation
2. Apply **web-design-guidelines** to review UI/UX
3. Optimize with **vercel-react-best-practices**
4. Final validation and delivery

### Workflow 2: Full-Stack Application
**Use when**: Building complete web applications with database

```
Requirements → frontend-design + supabase-postgres-best-practices → vercel-react-best-practices → audit-website → Delivery
```

**Steps**:
1. Design frontend with **frontend-design**
2. Design database schema with **supabase-postgres-best-practices**
3. Optimize React code with **vercel-react-best-practices**
4. Run comprehensive audit with **audit-website**

### Workflow 3: Website Quality Audit
**Use when**: Reviewing existing websites

```
Website URL → agent-browser → seo-audit + audit-website + web-design-guidelines → Report
```

**Steps**:
1. Use **agent-browser** to navigate and screenshot
2. Run **seo-audit** for search optimization
3. Run **audit-website** for comprehensive review
4. Apply **web-design-guidelines** for UI/UX issues

### Workflow 4: Mobile App Development
**Use when**: Building React Native/Expo apps

```
Requirements → building-native-ui → frontend-design → Testing → Delivery
```

**Steps**:
1. Create mobile UI with **building-native-ui**
2. Refine design with **frontend-design**
3. Test on different screen sizes
4. Optimize performance

### Workflow 5: Performance Optimization
**Use when**: Improving existing applications

```
App Analysis → vercel-react-best-practices + supabase-postgres-best-practices → audit-website → Optimization Report
```

**Steps**:
1. Analyze React code with **vercel-react-best-practices**
2. Review database queries with **supabase-postgres-best-practices**
3. Run performance audit with **audit-website**
4. Provide prioritized optimization recommendations

## Usage Examples

### Example 1: Building a Landing Page
```
User: "Create a landing page for my SaaS product"

Orchestrator: Activating frontend-design skill...
[Creates initial design]

Orchestrator: Applying web-design-guidelines...
[Reviews and improves UI/UX]

Orchestrator: Optimizing with vercel-react-best-practices...
[Ensures performance best practices]
```

### Example 2: Auditing a Website
```
User: "Review my website at example.com"

Orchestrator: Using agent-browser to navigate...
[Captures screenshots and analyzes]

Orchestrator: Running seo-audit...
[Analyzes SEO elements]

Orchestrator: Running audit-website...
[Comprehensive quality review]

Orchestrator: Applying web-design-guidelines...
[UI/UX recommendations]
```

### Example 3: Building a Dashboard
```
User: "Create an analytics dashboard"

Orchestrator: Activating frontend-design...
[Designs dashboard interface]

Orchestrator: Applying supabase-postgres-best-practices...
[Designs efficient data queries]

Orchestrator: Optimizing with vercel-react-best-practices...
[Ensures React performance]

Orchestrator: Final review with web-design-guidelines...
[UI/UX polish]
```

## Coordination Rules

1. **Sequential Activation**: Skills activate in logical order
2. **Output Pass-Through**: Each skill receives previous skill's output
3. **Conflict Resolution**: Latest skill's guidance takes precedence
4. **Validation**: Each workflow step validates previous work
5. **Documentation**: All skills contribute to final documentation

## Best Practices

- Start with the most specific skill for the task
- Layer generalist skills (like web-design-guidelines) last
- Use audit skills after implementation is complete
- Always validate with multiple skills when quality is critical
- Document which skills were used in the final output

## Custom Workflow Creation

Use **skill-creator** to create domain-specific workflows:

```markdown
1. Identify the goal
2. Select relevant skills
3. Define skill activation order
4. Specify input/output requirements
5. Create validation checkpoints
```

## Integration Tips

- **React Projects**: Always end with vercel-react-best-practices
- **Public Websites**: Always include seo-audit before delivery
- **User-Facing Apps**: Always apply web-design-guidelines
- **Data-Heavy Apps**: Always include supabase-postgres-best-practices
- **Mobile Apps**: Use building-native-ui as primary skill

## Quick Reference

| Goal | Primary Skill | Supporting Skills |
|------|--------------|-------------------|
| New Web UI | frontend-design | web-design-guidelines, vercel-react-best-practices |
| React Optimization | vercel-react-best-practices | audit-website |
| Website Review | audit-website | seo-audit, web-design-guidelines |
| Mobile App | building-native-ui | frontend-design |
| Database Design | supabase-postgres-best-practices | - |
| SEO Improvement | seo-audit | audit-website, web-design-guidelines |
