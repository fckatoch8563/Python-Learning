import sys
import pkgutil
import importlib

print("sys.executable =", sys.executable)
print("sys.path[0:6] =", sys.path[0:6])

# list a few installed top-level packages
names = [m.name for m in pkgutil.iter_modules()]
print("\nTop modules found (first 20):")
print(", ".join(names[:20]))

# try importing pandas and show version
try:
    import pandas as pd

    print("\nPandas version:", pd.__version__)
except Exception as e:
    print("\nPandas import failed:", type(e).__name__, e)
