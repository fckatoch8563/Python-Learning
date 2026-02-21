"""Complete demonstration of Path class methods"""

from pathlib import Path
from datetime import datetime

print("=" * 70)
print("PATH CLASS METHODS DEMONSTRATION")
print("=" * 70)

# Create a sample path
path = Path(__file__)  # This script's path

print("\n1. PATH INFORMATION METHODS")
print("-" * 70)
print(f"path                 = {path}")
print(f"path.name            = {path.name}")
print(f"path.stem            = {path.stem}")
print(f"path.suffix          = {path.suffix}")
print(f"path.parent          = {path.parent}")
print(f"path.parts           = {path.parts}")
print(f"path.anchor          = {path.anchor}")
print(f"path.absolute()      = {path.absolute()}")
print(f"path.resolve()       = {path.resolve()}")
print(f"path.as_posix()      = {path.as_posix()}")
print(f"path.as_uri()        = {path.as_uri()}")

print("\n2. PATH MANIPULATION METHODS")
print("-" * 70)
print(f"path.with_suffix('.txt')  = {path.with_suffix('.txt')}")
print(f"path.with_name('new.py')  = {path.with_name('new.py')}")
print(f"path.with_stem('demo')    = {path.with_stem('demo')}")

# Join paths
project = Path.cwd()
new_path = project / "data" / "file.txt"
print(f"project / 'data' / 'file.txt' = {new_path}")

print("\n3. CHECK METHODS")
print("-" * 70)
print(f"path.exists()        = {path.exists()}")
print(f"path.is_file()       = {path.is_file()}")
print(f"path.is_dir()        = {path.is_dir()}")
print(f"path.is_symlink()    = {path.is_symlink()}")
print(f"path.is_absolute()   = {path.is_absolute()}")

print("\n4. FILE STAT METHODS")
print("-" * 70)
stats = path.stat()
print(f"path.stat().st_size  = {stats.st_size} bytes")
print(f"path.stat().st_mtime = {datetime.fromtimestamp(stats.st_mtime)}")
try:
    print(f"path.owner()         = {path.owner()}")
    print(f"path.group()         = {path.group()}")
except:
    print("path.owner()/group() - Not available on this system")

print("\n5. DIRECTORY METHODS")
print("-" * 70)
cwd = Path.cwd()
print(f"Path.cwd()           = {cwd}")
print(f"Path.home()          = {Path.home()}")

print(f"\nFirst 5 items in current directory:")
for i, item in enumerate(cwd.iterdir()):
    if i >= 5:
        break
    item_type = "DIR " if item.is_dir() else "FILE"
    print(f"  [{item_type}] {item.name}")

print("\n6. GLOB/SEARCH METHODS")
print("-" * 70)
print("Python files in current directory (*.py):")
for i, py_file in enumerate(cwd.glob("*.py")):
    if i >= 5:
        print("  ...")
        break
    print(f"  {py_file.name}")

print("\n7. PATTERN MATCHING")
print("-" * 70)
print(f"path.match('*.py')         = {path.match('*.py')}")
print(f"path.match('**/demo.py')   = {path.match('**/demo.py')}")
print(f"path.match('path_*.py')    = {path.match('path_*.py')}")

print("\n8. CREATE/DELETE METHODS (demo only, not executed)")
print("-" * 70)
demo_file = cwd / "demo_file.txt"
demo_dir = cwd / "demo_directory"

print("Create file:")
print(f"  {demo_file}.touch()              # Creates empty file")
print(f"  {demo_file}.write_text('data')   # Write text to file")
print(f"  {demo_file}.read_text()          # Read file content")
print(f"  {demo_file}.unlink()             # Delete file")

print("\nCreate directory:")
print(f"  {demo_dir}.mkdir()               # Create directory")
print(f"  {demo_dir}.mkdir(parents=True)   # Create with parents")
print(f"  {demo_dir}.rmdir()               # Delete empty directory")

print("\n9. SPECIAL CLASSMETHODS")
print("-" * 70)
print(f"Path.cwd()           = {Path.cwd()}")
print(f"Path.home()          = {Path.home()}")

# Expanduser example
user_path = Path("~/Documents")
print(f"Path('~/Documents').expanduser() = {user_path.expanduser()}")

print("\n10. PRACTICAL EXAMPLES")
print("-" * 70)

# Example 1: Find all Python files
print("Find all .py files (first 5):")
for i, py_file in enumerate(Path.cwd().rglob("*.py")):
    if i >= 5:
        print("  ...")
        break
    print(f"  {py_file.relative_to(Path.cwd())}")

# Example 2: Get file size
print(f"\nThis script size: {path.stat().st_size} bytes")

# Example 3: Iterate parents
print(f"\nParent directories of {path.name}:")
for i, parent in enumerate(path.parents):
    if i >= 3:
        break
    print(f"  {i}: {parent}")

print("\n" + "=" * 70)
print("SUMMARY: Path class has methods for:")
print("=" * 70)
print(
    """
✓ Getting path information (name, stem, suffix, parent, parts)
✓ Manipulating paths (with_suffix, with_name, joining with /)
✓ Checking existence and type (exists, is_file, is_dir)
✓ Reading/writing files (read_text, write_text, read_bytes, write_bytes)
✓ Creating/deleting (mkdir, touch, unlink, rmdir)
✓ Listing directories (iterdir, glob, rglob)
✓ Getting file stats (stat, owner, group)
✓ Pattern matching (match)
✓ Path resolution (absolute, resolve, relative_to)
✓ Special paths (cwd, home, expanduser)

Use Path instead of os.path for cleaner, more readable code!
"""
)
##########################################################################################################
# The Path class has many useful methods! Here are the most important ones:

# Path Information
from pathlib import Path

path = Path("/Users/fckatoch/projects/Environments/test.py")

path.name  # 'test.py' (filename)
path.stem  # 'test' (filename without extension)
path.suffix  # '.py' (extension)
path.suffixes  # ['.py'] (all extensions, e.g., ['.tar', '.gz'])
path.parent  # Path('/Users/fckatoch/projects/Environments')
path.parents  # All parent directories (iterable)
path.parts  # ('/', 'Users', 'fckatoch', 'projects', 'Environments', 'test.py')
path.anchor  # '/' (root)
path.as_posix()  # '/Users/fckatoch/projects/Environments/test.py'
path.as_uri()  # 'file:///Users/fckatoch/projects/Environments/test.py'
########################################################
# Path Operations

# 1 Join paths
project = Path("/Users/fckatoch/projects")
file_path = project / "Environments" / "test.py"

# 2Get absolute path
path.absolute()  # Full path
path.resolve()  # Resolve symlinks and get absolute path

# 3 Relative path
path.relative_to("/Users/fckatoch")  # 'projects/Environments/test.py'

# 4 Change extension
path.with_suffix(".txt")  # Path('.../test.txt')
path.with_name("new.py")  # Path('.../new.py')
path.with_stem("renamed")  # Path('.../renamed.py')
##########################################################
# File/Directory Checks

path.exists()  # True if exists
path.is_file()  # True if it's a file
path.is_dir()  # True if it's a directory
path.is_symlink()  # True if it's a symbolic link
path.is_absolute()  # True if absolute path
##########################################################
# File Operations

# Read
path.read_text()  # Read as text
path.read_text(encoding="utf-8")  # With encoding
path.read_bytes()  # Read as bytes

# Write
path.write_text("Hello")  # Write text
path.write_bytes(b"data")  # Write bytes

# Open (traditional way)
with path.open("r") as f:
    content = f.read()
##########################################################
# Directory Operations

# Create directory
path.mkdir()  # Create directory
path.mkdir(parents=True)  # Create parent directories too
path.mkdir(exist_ok=True)  # Don't error if exists

# List contents
path.iterdir()  # Iterator of all items
list(path.iterdir())  # List of all items

# Find files
path.glob("*.py")  # All .py files in this directory
path.glob("**/*.py")  # All .py files recursively (deprecated)
path.rglob("*.py")  # All .py files recursively (recommended)

# Change directory
import os

os.chdir(path)  # Change to this directory
os.getcwd()  # Get current working directory
##########################################################
# File/Directory Manipulation

# Rename/move
path.rename("new_name.py")  # Rename
path.replace("other_path.py")  # Replace (overwrite if exists)

# Delete
path.unlink()  # Delete file
path.unlink(missing_ok=True)  # Don't error if doesn't exist
path.rmdir()  # Delete empty directory

# Touch (create empty file or update timestamp)
path.touch()  # Create empty file
path.touch(exist_ok=True)  # Don't error if exists
##########################################################################################################
# File Stats

stats = path.stat()
stats.st_size  # File size in bytes
stats.st_mtime  # Last modified time
stats.st_ctime  # Creation time
stats.st_mode  # File permissions

# Shortcuts
path.owner()  # File owner
path.group()  # File group
##########################################################################################################
# Special Path Methods

# Current directory
Path.cwd()  # Current working directory

# Home directory
Path.home()  # User's home directory (~)

# Expand user
Path("~/Documents").expanduser()  # '/Users/username/Documents'

# Match patterns
path.match("*.py")  # True if matches pattern
path.match("**/test.py")  # True if matches recursive pattern
path.match("Environments/*.py")  # True if matches specific folder
##########################################################################################################
