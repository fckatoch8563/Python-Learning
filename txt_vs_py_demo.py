"""Demonstration: Python code in .txt vs .py files"""

from pathlib import Path

# 1. Save Python code in a .txt file
print("=" * 60)
print("1. SAVING PYTHON CODE IN .txt FILE")
print("=" * 60)

python_code = """
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result = add(5, 3)
print(f"5 + 3 = {result}")
"""

txt_file = Path("code_in_txt.txt")
txt_file.write_text(python_code)
print(f"✓ Created: {txt_file}")
print(f"Content:\n{python_code}")

# 2. Try to execute the .txt file
print("=" * 60)
print("2. EXECUTING CODE FROM .txt FILE")
print("=" * 60)

code = txt_file.read_text()
print("Using exec():")
exec(code)  # This works!

print()

# 3. Try to import (will fail)
print("=" * 60)
print("3. TRYING TO IMPORT FROM .txt FILE")
print("=" * 60)

try:
    from code_in_txt import add  # This won't work
except ModuleNotFoundError as e:
    print(f"❌ Error: {e}")
    print("Cannot import from .txt files!")

print()

# 4. Create a proper .py file instead
print("=" * 60)
print("4. CREATING PROPER .py FILE")
print("=" * 60)

py_file = Path("code_in_py.py")
py_file.write_text(python_code)
print(f"✓ Created: {py_file}")

# Now we can import!
from code_in_py import add, multiply

print(f"\nImported functions from {py_file.name}:")
print(f"add(10, 5) = {add(10, 5)}")
print(f"multiply(10, 5) = {multiply(10, 5)}")

print()

# 5. Comparison
print("=" * 60)
print("5. SUMMARY - .txt vs .py for Python code")
print("=" * 60)

print(
    """
.txt file:
  ✓ Can store Python code
  ✓ Can execute with exec()
  ✗ Cannot import as module
  ✗ No syntax highlighting in most editors
  ✗ No IDE support (autocomplete, linting)
  
.py file:
  ✓ Can store Python code
  ✓ Can execute with exec()
  ✓ Can import as module
  ✓ Syntax highlighting
  ✓ Full IDE support
  ✓ Recognized as Python by tools

Recommendation: ALWAYS use .py for Python code!
"""
)

# Cleanup
print("\nCleaning up demo files...")
txt_file.unlink()
py_file.unlink()
print("✓ Deleted: code_in_txt.txt")
print("✓ Deleted: code_in_py.py")
