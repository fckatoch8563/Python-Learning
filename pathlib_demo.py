"""Demonstration of pathlib module capabilities"""

from pathlib import Path
from datetime import datetime

# Get current project directory
project_root = Path.cwd()
print(f"Project root: {project_root}\n")

# 1. CREATE DIRECTORY STRUCTURE
print("=" * 60)
print("1. CREATING DIRECTORY STRUCTURE")
print("=" * 60)

# Create nested directories
demo_dir = project_root / "pathlib_demo"
demo_dir.mkdir(exist_ok=True)

subdirs = ["data", "logs", "output"]
for subdir in subdirs:
    (demo_dir / subdir).mkdir(exist_ok=True)
    print(f"✓ Created: {demo_dir / subdir}")

print()

# 2. CREATE FILES
print("=" * 60)
print("2. CREATING FILES")
print("=" * 60)

# Create a text file
readme = demo_dir / "README.md"
readme.write_text(
    """# Pathlib Demo

This is a demonstration of pathlib capabilities.

Created: {}
""".format(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
)
print(f"✓ Created: {readme}")

# Create data file
data_file = demo_dir / "data" / "sample.txt"
data_file.write_text("Line 1\nLine 2\nLine 3\n")
print(f"✓ Created: {data_file}")

# Create log file
log_file = demo_dir / "logs" / "app.log"
log_file.write_text(f"[{datetime.now()}] Application started\n")
print(f"✓ Created: {log_file}")

print()

# 3. READ FILES
print("=" * 60)
print("3. READING FILES")
print("=" * 60)

content = data_file.read_text()
print(f"Content of {data_file.name}:")
print(content)

# Read lines
lines = data_file.read_text().splitlines()
print(f"Number of lines: {len(lines)}")
print()

# 4. LIST DIRECTORY CONTENTS
print("=" * 60)
print("4. LISTING DIRECTORY CONTENTS")
print("=" * 60)

print(f"Contents of {demo_dir}:")
for item in demo_dir.iterdir():
    item_type = "DIR " if item.is_dir() else "FILE"
    print(f"  [{item_type}] {item.name}")

print()

# 5. FIND FILES BY PATTERN
print("=" * 60)
print("5. FINDING FILES BY PATTERN")
print("=" * 60)

print("All .txt files in demo_dir:")
for txt_file in demo_dir.rglob("*.txt"):
    print(f"  {txt_file.relative_to(demo_dir)}")

print("\nAll .md files:")
for md_file in demo_dir.glob("*.md"):
    print(f"  {md_file.name}")

print()

# 6. PATH INFORMATION
print("=" * 60)
print("6. PATH INFORMATION")
print("=" * 60)

sample_path = demo_dir / "data" / "sample.txt"
print(f"Full path: {sample_path}")
print(f"Name: {sample_path.name}")
print(f"Stem (no extension): {sample_path.stem}")
print(f"Suffix (extension): {sample_path.suffix}")
print(f"Parent directory: {sample_path.parent}")
print(f"Exists: {sample_path.exists()}")
print(f"Is file: {sample_path.is_file()}")
print(f"Is directory: {sample_path.is_dir()}")
print(f"File size: {sample_path.stat().st_size} bytes")

print()

# 7. WORKING WITH PYTHON FILES IN PROJECT
print("=" * 60)
print("7. FINDING PYTHON FILES IN PROJECT")
print("=" * 60)

print("Python files in current directory:")
for py_file in project_root.glob("*.py"):
    size = py_file.stat().st_size
    print(f"  {py_file.name:30} {size:>6} bytes")

print()

# 8. CREATE A FILE WITH TIMESTAMP
print("=" * 60)
print("8. CREATING TIMESTAMPED FILE")
print("=" * 60)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
timestamped_file = demo_dir / "output" / f"report_{timestamp}.txt"
timestamped_file.write_text(f"Report generated at {datetime.now()}\n")
print(f"✓ Created: {timestamped_file.name}")

print()

# 9. SUMMARY
print("=" * 60)
print("9. SUMMARY - What pathlib can do:")
print("=" * 60)
print(
    """
✓ Create directories (mkdir)
✓ Create files (write_text, write_bytes)
✓ Read files (read_text, read_bytes)
✓ List directory contents (iterdir)
✓ Find files by pattern (glob, rglob)
✓ Get path information (name, stem, suffix, parent, etc.)
✓ Check existence (exists, is_file, is_dir)
✓ Rename/move files (rename)
✓ Delete files (unlink)
✓ Get file stats (stat)
✓ Join paths with / operator
✓ Cross-platform path handling

All demo files created in: {}/
""".format(
        demo_dir
    )
)

print("\nTo clean up, you can delete the demo directory:")
print(f"  rm -rf {demo_dir}")
