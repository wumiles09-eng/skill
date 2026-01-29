---
name: supabase-postgres-best-practices
description: PostgreSQL optimization best practices for Supabase projects. Use when designing databases, writing queries, optimizing performance, or working with Supabase-specific features like RLS, stored procedures, and real-time subscriptions.
---

# Supabase Postgres Best Practices

This skill covers PostgreSQL optimization and best practices specifically for Supabase projects.

## Database Design

### Table Structure
```sql
-- Use proper primary keys
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT NOT NULL UNIQUE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Add indexes for frequently queried columns
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at DESC);

-- Use foreign keys with ON DELETE
CREATE TABLE posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  title TEXT NOT NULL
);
```

### Row Level Security (RLS)
```sql
-- Enable RLS on all user-data tables
ALTER TABLE posts ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Users can view own posts"
  ON posts FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own posts"
  ON posts FOR INSERT
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own posts"
  ON posts FOR UPDATE
  USING (auth.uid() = user_id);

CREATE POLICY "Users can delete own posts"
  ON posts FOR DELETE
  USING (auth.uid() = user_id);
```

## Query Optimization

### Use Views for Complex Queries
```sql
CREATE VIEW user_post_counts AS
SELECT
  u.id,
  u.email,
  COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON p.user_id = u.id
GROUP BY u.id, u.email;
```

### Materialized Views for Cached Data
```sql
CREATE MATERIALIZED VIEW popular_posts AS
SELECT p.id, p.title, COUNT(*) as view_count
FROM posts p
JOIN post_views pv ON pv.post_id = p.id
GROUP BY p.id, p.title
ORDER BY view_count DESC;

-- Refresh periodically
REFRESH MATERIALIZED VIEW popular_posts;
```

### Efficient JSONB Queries
```sql
-- Check if JSONB contains key/value
SELECT * FROM products
WHERE metadata->>'category' = 'electronics';

-- GIN index for JSONB
CREATE INDEX idx_products_metadata ON products USING GIN (metadata);
```

## Supabase-Specific Features

### Database Functions
```sql
-- Create custom functions
CREATE OR REPLACE FUNCTION get_user_posts(user_uuid UUID)
RETURNS TABLE (
  id UUID,
  title TEXT,
  created_at TIMESTAMPTZ
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  RETURN QUERY
  SELECT p.id, p.title, p.created_at
  FROM posts p
  WHERE p.user_id = user_uuid
  ORDER BY p.created_at DESC;
END;
$$;

-- Grant execute to authenticated users
GRANT EXECUTE ON FUNCTION get_user_posts(UUID) TO authenticated;
```

### Triggers for Automations
```sql
-- Update timestamp on modification
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_updated_at
  BEFORE UPDATE ON users
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at();
```

### Real-time Subscriptions
```javascript
// Client-side subscription
const { data, error } = supabase
  .channel('public:posts')
  .on('postgres_changes', {
    event: '*',
    schema: 'public',
    table: 'posts'
  }, payload => {
    console.log('Change:', payload)
  })
  .subscribe()
```

## Performance Tips

1. **Use EXPLAIN ANALYZE**: Always analyze slow query plans
2. **Avoid SELECT ***: Only select needed columns
3. **Use connection pooling**: Supabase provides PgBouncer
4. **Limit result sets**: Use pagination with limit/offset
5. **Index foreign keys**: Automatically created but verify
6. **Use prepared statements**: Prevent SQL injection and improve performance

## Common Pitfalls

- ❌ N+1 queries: Use JOINs or include syntax
- ❌ Missing indexes: Identify slow queries with pg_stat_statements
- ❌ Over-selecting: Only fetch needed data
- ❌ Unoptimized JSONB: Use GIN indexes for JSON queries
- ❌ Ignoring RLS: Always enable on user data tables

## Monitoring

```sql
-- Check slow queries
SELECT query, mean_exec_time, calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Check table sizes
SELECT
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```
