---
name: vercel-react-best-practices
description: React and Next.js performance optimization best practices from Vercel Engineering. Use when writing, reviewing, or refactoring React code to ensure optimal performance, proper hooks usage, efficient rendering, and production-grade patterns.
---

# Vercel React Best Practices

This skill contains 40+ performance patterns and best practices for React and Next.js applications.

## Core Principles

### 1. Component Design
- Keep components small and focused
- Use composition over inheritance
- Prefer function components with hooks
- Avoid prop drilling with context or composition

### 2. Performance Optimization
```javascript
// ❌ Bad: Re-renders on every parent update
function ExpensiveComponent({ data }) {
  return <div>{heavyComputation(data)}</div>
}

// ✅ Good: Memoized result
function ExpensiveComponent({ data }) {
  const result = useMemo(() => heavyComputation(data), [data])
  return <div>{result}</div>
}
```

### 3. useCallback for Event Handlers
```javascript
// ✅ Prevent child re-renders
const handleClick = useCallback((id) => {
  setSelectedId(id)
}, [])
```

### 4. Code Splitting
```javascript
// Lazy load routes and heavy components
const HeavyComponent = dynamic(() => import('./HeavyComponent'))
```

### 5. Image Optimization
```javascript
// Use Next.js Image component
import Image from 'next/image'

<Image
  src="/hero.jpg"
  alt="Hero"
  width={1920}
  height={1080}
  priority // For above-fold images
/>
```

## Common Pitfalls

### ❌ Don't Do This
```javascript
// Inline objects create new references each render
<Component style={{ margin: 20 }} />
<button onClick={() => handleClick()} />

// Index as key (causes bugs)
{items.map((item, index) => <Item key={index} {...item} />)}

// Mutating state directly
state.items.push(newItem)
setState(state)
```

### ✅ Do This Instead
```javascript
// Stable references
const style = useMemo(() => ({ margin: 20 }), [])
const handleClick = useCallback(() => { ... }, [])

// Unique stable keys
{items.map(item => <Item key={item.id} {...item} />)}

// Immutable updates
setState(prev => ({
  ...prev,
  items: [...prev.items, newItem]
}))
```

## State Management Guidelines

1. **Co-locate State**: Keep state as close to where it's used as possible
2. **Minimize State**: Derive values when possible instead of storing them
3. **Context for Global State**: Use React Context for app-wide state
4. **URL as Source of Truth**: Store filter/search params in URL

## Server Components (Next.js 13+)

```javascript
// Default: Server Component (no client JS)
async function UserProfile({ id }) {
  const user = await db.user.findUnique({ where: { id } })
  return <div>{user.name}</div>
}

// Use 'use client' for interactivity
'use client'
export function InteractiveButton() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>
}
```

## Performance Checklist

- [ ] Eliminated unnecessary re-renders
- [ ] Memoized expensive computations
- [ ] Implemented code splitting
- [ ] Optimized images with next/image
- [ ] Used server components where possible
- [ ] Minimized client-side JavaScript
- [ ] Implemented proper loading states
- [ ] Added error boundaries
- [ ] Optimized bundle size
- [ ] Tested on low-end devices
