# Git & GitHub Setup Guide

## What We Accomplished

✓ Git configuration  
✓ SSH key setup  
✓ Repository initialization  
✓ Committing files  
✓ Pushing to GitHub  

---

## Step-by-Step Commands

### 1. Check Git Installation
```bash
git --version
# Output: git version 2.50.1 (Apple Git-155)
```

### 2. Configure Git with Your Identity
```bash
# Set your username
git config --global user.name "fckatoch8563"

# Set your email
git config --global user.email "fckatoch45@gmail.com"

# Verify configuration
git config --global --list | grep -E "(user.name|user.email)"
```

### 3. Generate SSH Key for GitHub
```bash
# Generate new SSH key
ssh-keygen -t ed25519 -C "fckatoch45@gmail.com" -f ~/.ssh/id_ed25519 -N ""

# Start SSH agent
eval "$(ssh-agent -s)"

# Add SSH key to agent
ssh-add ~/.ssh/id_ed25519

# Copy public key to clipboard
cat ~/.ssh/id_ed25519.pub | pbcopy
```

### 4. Add SSH Key to GitHub
1. Go to GitHub: **Settings** → **SSH and GPG keys**
2. Click **"New SSH key"**
3. Title: "MacBook" (or any name)
4. Paste key from clipboard
5. Click **"Add SSH key"**

### 5. Test SSH Connection
```bash
# Add GitHub to known hosts
ssh-keyscan github.com >> ~/.ssh/known_hosts

# Test connection
ssh -T git@github.com
# Output: Hi fckatoch8563! You've successfully authenticated...
```

### 6. Create .gitignore File
Created `.gitignore` to exclude:
- `__pycache__/`
- `.venv/`
- `.DS_Store`
- `*.pyc`
- And more...

### 7. Stage and Commit Files
```bash
# Check repository status
git status

# Reset any staged changes
git reset

# Add .gitignore
git add .gitignore

# Add all Python files
git add *.py examples/ pathlib_demo/ scripts/*.py scripts/*.sh pyproject.toml python_learning.ipynb README_TK.md

# Create first commit
git commit -m "Initial commit: Python learning files"

# Add all remaining changes (cleanup)
git add -A

# Commit cleanup
git commit -m "Clean up old files"
```

### 8. Create GitHub Repository
1. Go to GitHub
2. Click **"+"** → **"New repository"**
3. Repository name: **Python-Learning**
4. Visibility: **Public**
5. **DON'T** check "Add a README file"
6. Click **"Create repository"**

### 9. Connect Local Repository to GitHub
```bash
# Set remote URL (using SSH)
git remote set-url origin git@github.com:fckatoch8563/Python-Learning.git

# Verify remote
git remote -v
```

### 10. Push to GitHub
```bash
# Push code to GitHub
git push -u origin main
```

---

## Important Concepts

### Git Workflow
```
Working Directory → Staging Area → Local Repository → Remote Repository
     (edit)      →   (git add)   →  (git commit)   →   (git push)
```

### Common Git Commands

#### Checking Status
```bash
git status              # See what's changed
git log                 # View commit history
git log --oneline       # Compact commit history
```

#### Making Changes
```bash
git add <file>          # Stage specific file
git add .               # Stage all changes in current directory
git add -A              # Stage all changes in repository
git commit -m "message" # Commit with message
```

#### Syncing with GitHub
```bash
git pull                # Download changes from GitHub
git push                # Upload your commits to GitHub
git push -u origin main # First push (sets upstream)
```

#### Viewing Differences
```bash
git diff                # See unstaged changes
git diff --staged       # See staged changes
```

#### Undoing Changes
```bash
git restore <file>      # Discard changes in working directory
git restore --staged <file>  # Unstage file
git reset               # Unstage all files
git reset --hard HEAD   # Discard all local changes (dangerous!)
```

---

## Your Repository Information

- **GitHub Username:** fckatoch8563
- **Email:** fckatoch45@gmail.com
- **Repository:** https://github.com/fckatoch8563/Python-Learning
- **SSH URL:** git@github.com:fckatoch8563/Python-Learning.git
- **HTTPS URL:** https://github.com/fckatoch8563/Python-Learning.git

---

## Daily Workflow (Going Forward)

### When You Create/Edit Files:
```bash
# 1. Check what changed
git status

# 2. Add files you want to commit
git add filename.py
# or add everything:
git add .

# 3. Commit with a descriptive message
git commit -m "Add new feature X" 

# 4. Push to GitHub
git push
```

### Example: Adding a New Python File
```bash
# Create new file
touch new_script.py

# Edit the file...

# Add to git
git add new_script.py

# Commit
git commit -m "Add new script for learning loops"

# Push to GitHub
git push
```

---

## Tips & Best Practices

1. **Commit often** - Make small, focused commits
2. **Write clear messages** - Describe what changed and why
3. **Check status** - Use `git status` before committing
4. **Pull before push** - If working on multiple machines
5. **Don't commit** - Sensitive data, passwords, large files

### Good Commit Messages
```bash
✓ "Add function to calculate factorial"
✓ "Fix bug in sorting algorithm"
✓ "Update README with installation steps"

✗ "update"
✗ "fix"
✗ "asdf"
```

---

## Troubleshooting

### Push Rejected
```bash
# Pull latest changes first
git pull --rebase
git push
```

### Accidentally Committed Wrong Files
```bash
# Undo last commit, keep changes
git reset --soft HEAD~1

# Re-add correct files
git add correct_file.py
git commit -m "Correct commit"
```

### Want to See What Changed
```bash
git diff filename.py
```

---

## Next Steps to Learn

- [ ] Branching (`git branch`, `git checkout`)
- [ ] Merging branches
- [ ] Resolving conflicts
- [ ] Using `.gitignore` effectively
- [ ] Viewing history (`git log`)
- [ ] Reverting commits
- [ ] GitHub Pull Requests
- [ ] GitHub Issues
- [ ] Collaborating with others

---

## Quick Reference Card

| Command | Description |
|---------|-------------|
| `git status` | Check what's changed |
| `git add <file>` | Stage file |
| `git add .` | Stage all |
| `git commit -m "msg"` | Commit changes |
| `git push` | Upload to GitHub |
| `git pull` | Download from GitHub |
| `git log` | View history |
| `git diff` | See changes |
| `git restore <file>` | Discard changes |
| `git remote -v` | View remote URL |

---

**Created:** December 31, 2025  
**Repository:** Python-Learning  
**Status:** ✅ Successfully pushed to GitHub
