---
name: stitch-loop
description: Google Stitch official skill for automated iterative design generation. Runs AI-driven loops to automatically generate multiple Stitch pages and components while maintaining design system consistency. Use when bulk-generating UI designs from a design system.
---

# Stitch Loop - Automated Iterative Design Generation

Google Stitch official skill for automated, iterative design generation with AI.

## Purpose

Automates the generation of multiple Stitch pages and components through AI-driven iteration loops, maintaining design system consistency throughout.

## What It Does

### Automated Generation Loops
- Generates multiple pages automatically
- Follows design system from DESIGN.md
- Maintains consistency across iterations
- Iterates based on feedback/requirements

### Loop Process
```
1. Read DESIGN.md (design system)
2. Generate page/component
3. Validate against design tokens
4. Adjust if needed
5. Repeat for next item
```

## When to Use

Use this skill when:
- Generating multiple pages at once
- Bulk-creating UI components
- Need consistent design across pages
- Building complete applications
- Want automated design iteration

## Workflow

### Complete Stitch Workflow
```
1. design-md
   Create DESIGN.md with design system
   ↓
2. stitch-loop
   Generate multiple pages following system
   ↓
3. react-components
   Convert designs to React code
```

### Using stitch-loop
```
User: "Generate 5 pages for my blog: home, about, blog list, blog post, contact"

stitch-loop:
1. Reads DESIGN.md for design system
2. Generates each page sequentially
3. Maintains consistency across pages
4. Creates navigation between pages
5. Outputs complete Stitch project
```

## Loop Strategy

### Page Generation Loop
For each page:
1. **Analyze Requirements**
   - Page purpose and content
   - Target audience
   - Key features needed

2. **Apply Design System**
   - Use colors from DESIGN.md
   - Apply typography scale
   - Follow spacing conventions
   - Use defined components

3. **Generate Layout**
   - Create responsive layout
   - Add necessary sections
   - Include interactive elements
   - Ensure accessibility

4. **Validate**
   - Check against design tokens
   - Verify consistency
   - Test responsiveness
   - Validate accessibility

5. **Iterate** (if needed)
   - Adjust based on feedback
   - Refine design details
   - Optimize user experience

### Batch Generation
```
Input: List of pages to generate
Loop:
  For each page:
    - Read design system
    - Generate design
    - Validate
    - Save to project
Output: Complete multi-page project
```

## Integration

### With design-md
```
design-md creates DESIGN.md
    ↓
stitch-loop reads DESIGN.md
    ↓
Generates consistent designs
```

### With react-components
```
stitch-loop generates designs
    ↓
react-components converts to code
    ↓
Production-ready app
```

## Use Cases

### 1. Blog Website
```
Pages:
- Home (hero, featured posts)
- About (profile, background)
- Blog List (post grid, filters)
- Blog Post (content, comments)
- Contact (form, info)

Result: Complete blog design system
```

### 2. SaaS Application
```
Pages:
- Landing page
- Features/pricing
- Dashboard
- Settings
- Documentation

Result: Full SaaS app design
```

### 3. E-commerce
```
Pages:
- Home (featured, categories)
- Product listing
- Product detail
- Cart/checkout
- User account

Result: Complete store design
```

## Configuration

### Loop Options
- **Number of iterations**: How many times to refine
- **Consistency level**: Strict vs loose adherence
- **Page count**: Total pages to generate
- **Generation speed**: Fast vs thorough

### Customization
```markdown
# Design Preferences
- Style: modern/minimalist/brutalist
- Tone: professional/playful/luxury
- Colors: follow DESIGN.md or custom
- Typography: from design system
```

## Best Practices

1. **Start with DESIGN.md**: Always create design system first
2. **Define Page List**: Specify all pages upfront
3. **Set Consistency Level**: Decide how strict to be
4. **Review Iteratively**: Check results between loops
5. **Adjust as Needed**: Provide feedback for refinement

## Example Usage

```
User: "Use stitch-loop to generate these pages:
1. Landing page with hero and CTA
2. Features page with 3 sections
3. Pricing page with 3 tiers
4. Contact page with form
Follow the design system in DESIGN.md"

stitch-loop:
[Loop 1] Generating landing page...
[Loop 2] Generating features page...
[Loop 3] Generating pricing page...
[Loop 4] Generating contact page...
[Validation] Checking consistency...
[Output] All 4 pages generated successfully
```

## Output Structure

```
stitch-project/
├── DESIGN.md
├── pages/
│   ├── landing/
│   ├── features/
│   ├── pricing/
│   └── contact/
└── components/
    ├── shared/
    └── ...
```

## Validation Checks

- Color consistency with DESIGN.md
- Typography scale adherence
- Spacing convention compliance
- Component reuse
- Responsive design
- Accessibility standards

## Related Skills

- **design-md**: Create design system documentation
- **react-components**: Convert designs to code
- **dev-workflow**: Coordinate complete workflow
- **planning-with-files**: Plan page structure

## Advanced Features

### Smart Page Generation
- Analyzes content requirements
- Suggests page sections
- Recommends component usage

### Consistency Enforcement
- Design token validation
- Component library usage
- Layout pattern adherence

### Iterative Refinement
- Multiple generation passes
- Progressive improvement
- Feedback incorporation

## Links

- [Stitch by Google](https://stitch.withgoogle.com/)
- [Stitch Documentation](https://stitch.withgoogle.com/docs/)
- [Stitch Skills Repository](https://github.com/google-labs-code/stitch-skills)

---

**Author**: Google Labs Code
**Version**: 1.0
**License**: See repository license
