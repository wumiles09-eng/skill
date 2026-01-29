# Obsidian to GitHub Sync

You are a specialized skill for syncing Obsidian vault to GitHub.

## Configuration

- **Vault Path**: `/Users/nancy/Documents/Obsidian Vault`
- **Git User**: Nancy
- **Git Email**: wumiles09@gmail.com
- **Remote**: origin
- **Branch**: main

## Operation

When invoked, perform the following steps to sync the Obsidian vault to GitHub:

1. **Navigate to vault**: `cd "/Users/nancy/Documents/Obsidian Vault"`

2. **Check status**: Run `git status -s` to see if there are any changes

3. **If no changes**: Inform the user that the vault is already up to date, nothing to sync.

4. **If there are changes**:
   - Stage all changes: `git add .`
   - Create commit with timestamp: `git commit -m "auto: sync at $(date '+%Y-%m-%d %H:%M:%S')"`
   - Push to remote: `git push origin main`
   - Show detailed changes: `git diff HEAD~1 HEAD --stat --name-status`

5. **Report result**: Clearly inform the user whether the sync was successful or if there were any errors.
   - List each changed file with its status (A=added, M=modified, D=deleted, R=renamed)

## Notes

- The `.gitignore` is already configured to exclude `.obsidian/`, `.trash/`, `.DS_Store`, etc.
- The GitHub token is already configured in the remote URL
- Only Markdown files and necessary assets should be synced

## Output Format

Provide clear, concise feedback:
- If no changes: "No changes detected. Vault is already up to date."
- On success: "Sync complete: [X files changed]"
- On error: Describe the error clearly with suggested fix
