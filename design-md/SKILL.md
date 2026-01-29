---
name: design-md
description: Google Stitch official skill for generating comprehensive design system documentation (DESIGN.md). Analyzes Stitch projects and creates complete design documentation including color palettes, typography, layout specs, and component guidelines in natural, semantic language optimized for readability.
---

# Design MD - Stitch Design System Documentation

Google Stitch official skill for generating comprehensive design system documentation.

## Purpose

Analyzes Stitch projects and generates comprehensive DESIGN.md files that document the complete design system in natural, semantic language optimized for AI and human readability.

## What It Does

Creates a complete DESIGN.md file containing:

### 1. Color System
- Primary/secondary/neutral color palettes
- Semantic color tokens (success, warning, error, info)
- Dark/light mode variants
- Usage guidelines and accessibility info

### 2. Typography
- Font families (display, heading, body, code)
- Type scale (font sizes, weights, line heights)
- Letter spacing and line height ratios
- Usage guidelines for each typography level

### 3. Layout & Spacing
- Spacing scale (4px/8px base grid)
- Container widths and breakpoints
- Margin/padding conventions
- Grid systems and layouts

### 4. Components
- Button styles and variants
- Form elements
- Cards and containers
- Navigation elements
- Modals and overlays
- Component composition guidelines

### 5. Design Tokens
- Complete token reference
- Token naming conventions
- Token usage patterns
- Design system architecture

### 6. Guidelines
- Do's and don'ts
- Anti-patterns to avoid
- Best practices
- Accessibility requirements

## When to Use

Use this skill when:
- Starting a new Stitch project
- Need to document an existing design system
- Want to share design specifications
- Creating design system guidelines
- Need AI to understand your design system

## Workflow

```
Stitch Project
    ↓
design-md skill
    ↓
DESIGN.md
    ↓
Shared reference for:
- AI agents (for consistent generation)
- Team members (for understanding specs)
- Developers (for implementation)
- Designers (for system documentation)
```

## Integration with Other Skills

**design-md → stitch-loop**
- Create DESIGN.md first
- Use stitch-loop to generate pages based on design system

**design-md → react-components**
- DESIGN.md provides design tokens
- react-components uses tokens for consistent implementation

**Complete Workflow:**
```
1. design-md - Create design system documentation
2. stitch-loop - Generate pages following the system
3. react-components - Convert to React code
```

## Input Requirements

The skill needs:
- Access to Stitch project files
- Existing design tokens or style definitions
- Component definitions (if available)

## Output

A comprehensive DESIGN.md file with:
- Clear section headers
- Semantic, readable descriptions
- Code examples where appropriate
- Usage guidelines
- Accessibility considerations

## Best Practices

1. **Generate Early**: Create DESIGN.md at project start
2. **Keep Updated**: Regenerate when design system changes
3. **Share Widely**: Use as single source of truth
4. **Version Control**: Track DESIGN.md in git
5. **AI-Friendly**: Write descriptions that AI can understand

## Example Output Structure

```markdown
# Design System Documentation

## Color Palette
### Primary Colors
- Primary: #007AFF
- Secondary: #5856D6
...

## Typography
### Display
- Font: Inter
- Size: 48px
- Weight: 700
...

## Components
### Button
- Variants: primary, secondary, ghost
- Sizes: sm, md, lg
...

## Design Tokens
### Spacing
- scale: [4, 8, 12, 16, 24, 32, 48, 64]
...
```

## Related Skills

- **stitch-loop**: Generate pages following design system
- **react-components**: Convert designs to React code
- **frontend-design**: Create distinctive interfaces
- **ui-ux-pro-max**: Professional UI/UX design intelligence

## Links

- [Stitch by Google](https://stitch.withgoogle.com/)
- [Stitch Skills Repository](https://github.com/google-labs-code/stitch-skills)
- [Stitch Documentation](https://stitch.withgoogle.com/docs/)

---

**Author**: Google Labs Code
**Version**: 1.0
**License**: See repository license
