# Git Notes — Quick Reference

## Basic Commands
git status              # Check what changed
git add .               # Stage all changes
git commit -m "message" # Commit staged changes
git push                # Push commits to GitHub
git pull                # Pull new changes from GitHub

## Branching (later)
git branch              # List branches
git checkout -b new-feature  # Create new branch
git checkout main        # Switch back to main
git merge new-feature    # Merge branch into main

## Logs & inspection
git log --oneline        # Compact commit history
git diff                 # See what's changed but not staged

## Undoing / cleaning up
git restore <file>       # Discard local changes to a file
git reset --hard HEAD    # Reset to last commit (careful)
