"""
Comparison: sys vs pathlib for File System Operations

pathlib is the modern way to handle file paths and replaces many sys operations
"""

import sys
from pathlib import Path

print("=" * 70)
print("sys vs pathlib - File System Operations Comparison")
print("=" * 70)

# ============================================================================
# 1. Get Current Working Directory
# ============================================================================
print("\n1. Current Working Directory:")
print("-" * 70)

# OLD WAY (sys + os)
import os

old_way = os.getcwd()
print(f"sys/os way: {old_way}")

# NEW WAY (pathlib)
new_way = Path.cwd()
print(f"pathlib way: {new_way}")

# ============================================================================
# 2. Get Script Directory
# ============================================================================
print("\n2. Script Directory:")
print("-" * 70)

# OLD WAY (sys + os)
old_script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"sys/os way: {old_script_dir}")

# NEW WAY (pathlib)
new_script_dir = Path(__file__).parent.resolve()
print(f"pathlib way: {new_script_dir}")

# ============================================================================
# 3. Join Paths
# ============================================================================
print("\n3. Join Paths:")
print("-" * 70)

# OLD WAY (sys + os)
old_join = os.path.join(os.getcwd(), "examples", "test.py")
print(f"sys/os way: {old_join}")

# NEW WAY (pathlib) - Much cleaner with / operator!
new_join = Path.cwd() / "examples" / "test.py"
print(f"pathlib way: {new_join}")

# ============================================================================
# 4. Check if File/Directory Exists
# ============================================================================
print("\n4. Check if File Exists:")
print("-" * 70)

# OLD WAY (sys + os)
old_exists = os.path.exists("sys_demo.py")
print(f"sys/os way: {old_exists}")

# NEW WAY (pathlib)
new_exists = Path("sys_demo.py").exists()
print(f"pathlib way: {new_exists}")

# ============================================================================
# 5. Check if it's a File or Directory
# ============================================================================
print("\n5. Check File vs Directory:")
print("-" * 70)

# OLD WAY (sys + os)
print(f"sys/os - Is file? {os.path.isfile('sys_demo.py')}")
print(f"sys/os - Is directory? {os.path.isdir('examples')}")

# NEW WAY (pathlib)
print(f"pathlib - Is file? {Path('sys_demo.py').is_file()}")
print(f"pathlib - Is directory? {Path('examples').is_dir()}")

# ============================================================================
# 6. Get File Name and Extension
# ============================================================================
print("\n6. File Name and Extension:")
print("-" * 70)

# OLD WAY (sys + os)
filepath = "examples/test_script.py"
old_name = os.path.basename(filepath)
old_ext = os.path.splitext(filepath)[1]
print(f"sys/os - Name: {old_name}")
print(f"sys/os - Extension: {old_ext}")

# NEW WAY (pathlib)
p = Path(filepath)
print(f"pathlib - Name: {p.name}")
print(f"pathlib - Extension: {p.suffix}")
print(f"pathlib - Stem (name without extension): {p.stem}")

# ============================================================================
# 7. List All Files in Directory
# ============================================================================
print("\n7. List Python Files in Current Directory:")
print("-" * 70)

# OLD WAY (sys + os)
print("sys/os way:")
for f in os.listdir("."):
    if f.endswith(".py") and os.path.isfile(f):
        print(f"  - {f}")

# NEW WAY (pathlib) - Much cleaner!
print("\npathlib way:")
for f in Path(".").glob("*.py"):
    if f.is_file():
        print(f"  - {f.name}")

# ============================================================================
# 8. Read File Content
# ============================================================================
print("\n8. Read File Content:")
print("-" * 70)

# OLD WAY (sys + os)
with open("sys_demo.py", "r") as file:
    old_content = file.read()
print(f"sys/os way - First 50 chars: {old_content[:50]}...")

# NEW WAY (pathlib) - One line!
new_content = Path("sys_demo.py").read_text()
print(f"pathlib way - First 50 chars: {new_content[:50]}...")

# ============================================================================
# 9. Get Parent Directory
# ============================================================================
print("\n9. Get Parent Directory:")
print("-" * 70)

# OLD WAY (sys + os)
old_parent = os.path.dirname(os.path.abspath("examples/test.py"))
print(f"sys/os way: {old_parent}")

# NEW WAY (pathlib)
new_parent = Path("examples/test.py").parent
print(f"pathlib way: {new_parent}")

# ============================================================================
# 10. Get All Parts of Path
# ============================================================================
print("\n10. Path Parts:")
print("-" * 70)

path = Path("examples/subfolder/test.py")
print(f"Parts: {path.parts}")
print(f"Parent: {path.parent}")
print(f"Parents (all): {list(path.parents)}")
print(f"Name: {path.name}")
print(f"Stem: {path.stem}")
print(f"Suffix: {path.suffix}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY: Why pathlib is better")
print("=" * 70)
print(
    """
✅ More readable: Path('dir') / 'file.txt'  vs  os.path.join('dir', 'file.txt')
✅ Object-oriented: path.exists() vs os.path.exists(path)
✅ Easier to use: path.read_text() vs open(path).read()
✅ Platform independent: Handles Windows/Mac/Linux differences automatically
✅ Rich methods: .parent, .stem, .suffix, .glob(), etc.
✅ Chainable: Path.cwd() / 'folder' / 'file.txt'

Note: For stdin/stdout operations (like reading user input), 
      still use sys.stdin, sys.stdout - pathlib is for FILE PATHS only!
"""
)

print("=" * 70)
