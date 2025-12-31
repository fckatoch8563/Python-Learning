# With strings (old way):
import os

path = "/Users/fckatoch/projects"
file_path = os.path.join(path, "Environments", "test.py")

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    print(f"File path: {file_path}")
    print(content)


# With PosixPath (modern way):
from pathlib import Path

path = Path("/Users/fckatoch/projects")
file_path = path / "Environments" / "test.py"
if file_path.exists():
    content = file_path.read_text()
    print(f"File path: {file_path}")
    print(content)


#################################################################################################


import pandas as pd

# Read a CSV file into a DataFrame
df = pd.read_csv("orders.csv")
# See all columns without truncation
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
print(df)
