# Colorful Terminal Commands Reference

## Quick Aliases (Set Up in ~/.zshrc)

| Alias | What It Does | Example |
|-------|-------------|---------|
| `cat` | View file with syntax highlighting | `cat testing_code.py` |
| `ls` | List files with colors and icons | `ls` |
| `ll` | Long list with icons and git status | `ll` |
| `la` | List all files (including hidden) | `la` |
| `tree` | Show directory tree with icons | `tree` |

---

## Detailed Usage

### 1. **bat** - Colorful File Viewer
```bash
cat filename.py          # View with syntax highlighting
cat -n filename.py       # With line numbers
cat -A filename.py       # Show all (tabs, spaces, etc.)
cat file1.py file2.py    # View multiple files
```

### 2. **eza** - Colorful File Listing
```bash
ls                       # Basic colorful list with icons
ll                       # Long format with git status
la                       # Show all files (including hidden)
tree                     # Tree view of directories
eza -T --level=2         # Tree with max depth 2
eza -l --sort=size       # Sort by size
eza -l --sort=modified   # Sort by modification time
```

### 3. **git-delta** - Colorful Git Diffs
Already configured! Just use normal git commands:

```bash
git diff                 # Beautiful side-by-side diff
git diff filename.py     # Diff specific file
git log -p              # Log with diffs
git show <commit>        # Show commit with diff
git status               # Already colorful
```

---

## Common Examples

### View Python File
```bash
cat testing_code.py      # Syntax highlighted
```

### List Current Directory
```bash
ls                       # Simple list
ll                       # Detailed list with git info
```

### Show Directory Structure
```bash
tree                     # Full tree
tree --level=2           # 2 levels deep
```

### Git Operations
```bash
git status               # Colorful status
git diff                 # Side-by-side diff
git log --oneline        # Compact colorful log
git log --graph          # Branch graph
```

---

## Before vs After

### Before (Plain):
```bash
cat testing_code.py      # Plain text, no colors
ls                       # Just filenames
git diff                 # Plain text diff
```

### After (Colorful):
```bash
cat testing_code.py      # 🎨 Syntax highlighting
ls                       # 🎨 Colored files with icons
git diff                 # 🎨 Side-by-side colored diff
```

---

## Tips

1. **All aliases work in new terminals** - They're saved in `~/.zshrc`
2. **Use original commands** - If needed, use `\cat` or `command cat`
3. **Customize colors** - Edit `~/.zshrc` to change aliases
4. **More eza options** - Run `eza --help` to see all options
5. **More bat themes** - Run `bat --list-themes` to see themes

---

## Cheat Sheet (Keep This Handy!)

```
# File Viewing
cat file.py              # View with colors

# Directory Listing  
ls                       # List with icons
ll                       # Long list + git
la                       # All files (hidden too)
tree                     # Tree view

# Git
git diff                 # Colorful diff
git log                  # Colorful log
git status               # Already colorful
```

---

**Created:** December 31, 2025  
**Terminal:** zsh with colorful commands enabled ✨

#  tree → directory tree view
tree --level=2           # Show only 2 levels deep
tree --level=1           # Show only first level (like folders only)
tree examples/ 
# OR
tree -L 1               # Same as --level=1
tree -L 2               # Same as --level=2
# 
That's correct! tree examples/ shows the tree inside the examples folder.

What you probably saw:

This means the examples folder only contains one file: dict_hash_demo.py

# Different tree commands:
tree                    # Tree of current directory (everything)
tree examples/          # Tree of INSIDE examples folder
tree --level=1          # Only show top level
tree -L 2               # Show 2 levels deep

# Or to see what's inside examples with more detail:
ll examples/            # List contents of examples