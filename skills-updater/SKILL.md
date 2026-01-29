---
name: skills-updater
description: Automatically updates and manages installed skills by checking for new versions, applying updates, and maintaining compatibility. Use this skill to keep all Claude Code skills current with the latest improvements and bug fixes.
---

# Skills Updater

Automated skill management and update system for keeping all skills current.

## Features

### Automatic Updates
- Checks for skill updates
- Applies updates safely
- Maintains backups
- Preserves customizations

### Dependency Management
- Checks skill dependencies
- Updates related skills
- Resolves conflicts
- Maintains compatibility

### Version Control
- Tracks skill versions
- Manages changelogs
- Handles rollbacks
- Shows update history

## Usage

### Update All Skills
```
User: "Update all my skills"

[Checks all installed skills]
[Downloads updates]
[Applies changes]
"Updated 10 skills:
- frontend-design: 1.2 → 1.5
- vercel-react-best-practices: 2.1 → 2.3
..."
```

### Update Specific Skill
```
User: "Update the frontend-design skill"

[Checks for updates]
[Shows changelog]
[Applies update]
"Updated frontend-design to version 1.5"
```

### Check for Updates
```
User: "Check if any skills need updates"

[Scans all skills]
[Lists available updates]
"5 skills have updates available:
- frontend-design (1.2 → 1.5)
- ..."
```

## Update Process

### 1. Discovery
- Scan installed skills
- Check remote repositories
- Compare versions
- Identify updates

### 2. Preparation
- Create backups
- Check dependencies
- Verify compatibility
- Plan update order

### 3. Update
- Download new versions
- Replace files
- Migrate settings
- Update metadata

### 4. Verification
- Test skill loading
- Check functionality
- Validate integration
- Confirm success

### 5. Rollback (if needed)
- Restore backups
- Revert changes
- Report issues
- Maintain stability

## Safety Features

### Automatic Backups
- Creates backup before each update
- Stores rollback points
- Preserves customizations
- Maintains history

### Dependency Checking
- Verifies compatibility
- Checks related skills
- Tests integrations
- Prevents conflicts

### Gradual Updates
- Updates one skill at a time
- Verifies between updates
- Stops on errors
- Reports issues

## Configuration

### Update Schedule
```yaml
# Check for updates
frequency: weekly  # daily, weekly, monthly

# Auto-update behavior
auto_update: false  # true to auto-apply
backup_before: true  # always backup
```

### Skill Priorities
```yaml
# Update order (dependencies first)
priority:
  - skill-creator
  - dev-workflow
  - frontend-design
  # ... other skills
```

### Exclusions
```yaml
# Skills to exclude from updates
exclude:
  - custom-skill
  - experimental-skill
```

## Best Practices

1. **Regular Updates**: Check weekly for updates
2. **Backup First**: Always backup before bulk updates
3. **Test After**: Verify skills work after updating
4. **Read Changelogs**: Know what's changing
5. **Report Issues**: Help fix bugs

## Integration

Works with:
- **skill-creator**: For creating new skills
- All installed skills: For keeping them current

## Commands

### Check Updates
```
/skills-updater check
```

### Update All
```
/skills-updater update all
```

### Update Specific
```
/skills-updater update <skill-name>
```

### Show History
```
/skills-updater history
```

### Rollback
```
/skills-updater rollback <skill-name> <version>
```

## Troubleshooting

### Update Failed
1. Check internet connection
2. Verify skill source
3. Check disk space
4. Review error logs
5. Try manual update

### Skill Broken After Update
1. Use rollback feature
2. Check changelog for breaking changes
3. Verify dependencies
4. Report issue

### Conflict Detected
1. Review conflicting skills
2. Check version compatibility
3. Update dependencies first
4. Contact maintainers

## Tips

1. **Update Regularly**: Keep skills current
2. **Read Changes**: Understand what's new
3. **Test First**: Try in safe environment
4. **Backup Often**: Keep restore points
5. **Give Feedback**: Help improve skills
