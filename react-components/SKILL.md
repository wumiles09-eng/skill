---
name: react-components
description: Google Stitch official skill for converting Stitch designs into production-ready React components. Transforms UI designs into modular Vite + React components with AST-based validation, design token consistency, and modern development practices.
---

# React Components - Stitch to React Conversion

Google Stitch official skill for converting Stitch designs into production-ready React components.

## Purpose

Converts Stitch AI-generated designs directly into modular, production-ready React components while maintaining design token consistency and following modern React best practices.

## What It Does

Transforms Stitch designs into:

### 1. React Components
- Functional components with hooks
- TypeScript support
- Proper prop types and interfaces
- Component composition patterns

### 2. Vite Integration
- Modern Vite build setup
- Fast development server
- Optimized production builds
- Hot module replacement

### 3. Design Token Consistency
- Design tokens from DESIGN.md
- CSS variables for theming
- Consistent spacing, colors, typography
- Token-based component styling

### 4. AST-Based Validation
- Abstract Syntax Tree validation
- Type checking
- Code quality verification
- Best practices enforcement

## Component Features

### Generated Components Include:
- Proper prop interfaces
- Default values and variants
- Event handlers
- Accessibility attributes
- Responsive design support
- Dark mode support (when applicable)

### Styling Approach:
- CSS Modules or styled-components
- Design token integration
- Responsive utilities
- Animation support

## When to Use

Use this skill when:
- Converting Stitch designs to code
- Building React applications from designs
- Need production-ready components
- Want design system consistency
- Creating component libraries

## Workflow

```
Stitch Design
    ↓
DESIGN.md (design tokens)
    ↓
react-components skill
    ↓
React Components
├── src/
│   ├── components/
│   │   ├── Button/
│   │   ├── Card/
│   │   └── ...
│   ├── tokens/
│   │   ├── colors.ts
│   │   ├── spacing.ts
│   │   └── typography.ts
│   └── styles/
└── vite.config.ts
```

## Integration with Other Skills

**design-md → react-components**
- DESIGN.md provides design tokens
- Components use tokens for consistency

**stitch-loop → react-components**
- stitch-loop generates designs
- react-components converts to code

**Complete Workflow:**
```
1. design-md - Create design system
2. stitch-loop - Generate pages
3. react-components - Convert to React code
```

## Input Requirements

The skill needs:
- Stitch design files
- DESIGN.md with design tokens
- Component specifications

## Output Structure

```
project/
├── src/
│   ├── components/
│   │   ├── Button.tsx
│   │   ├── Button.test.tsx
│   │   ├── Card.tsx
│   │   ├── Card.test.tsx
│   │   └── index.ts
│   ├── tokens/
│   │   ├── colors.ts
│   │   ├── spacing.ts
│   │   ├── typography.ts
│   │   └── index.ts
│   ├── utils/
│   │   └── cn.ts (classnames utility)
│   ├── App.tsx
│   └── main.tsx
├── styles/
│   └── globals.css
├── package.json
├── tsconfig.json
├── vite.config.ts
└── tailwind.config.js (if using Tailwind)
```

## Component Example

```typescript
// src/components/Button/Button.tsx
import { buttonVariants } from './Button.types';
import { cn } from '../../utils/cn';

export interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  children,
  onClick,
  disabled = false,
}) => {
  return (
    <button
      className={cn(buttonVariants({ variant, size }))}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};
```

## Design Tokens

```typescript
// src/tokens/colors.ts
export const colors = {
  primary: {
    50: '#EFF6FF',
    100: '#DBEAFE',
    500: '#3B82F6',
    600: '#2563EB',
    700: '#1D4ED8',
  },
  // ... from DESIGN.md
} as const;

// src/tokens/spacing.ts
export const spacing = {
  xs: '4px',
  sm: '8px',
  md: '16px',
  lg: '24px',
  xl: '32px',
} as const;
```

## Best Practices

1. **Type Safety**: Use TypeScript for all components
2. **Composition**: Build composable component patterns
3. **Testing**: Include test files for each component
4. **Documentation**: Add JSDoc comments
5. **Accessibility**: Include ARIA attributes
6. **Performance**: Use React.memo where appropriate
7. **Tokens**: Always use design tokens, never hardcode values

## Advanced Features

### Theming
- CSS custom properties for easy theming
- Dark mode support
- Theme context provider

### Variants
- Multiple component variants
- Consistent variant API
- Composable variant styles

### Responsiveness
- Mobile-first approach
- Responsive props
- Breakpoint utilities

## Related Skills

- **design-md**: Create design system documentation first
- **stitch-loop**: Generate designs before conversion
- **vercel-react-best-practices**: Optimize generated code
- **frontend-design**: Create distinctive interfaces

## Links

- [Stitch by Google](https://stitch.withgoogle.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Stitch Skills Repository](https://github.com/google-labs-code/stitch-skills)

---

**Author**: Google Labs Code
**Version**: 1.0
**License**: See repository license
