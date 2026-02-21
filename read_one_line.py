import sys
# 1) Read a single line from stdin (interactive or piped)
def read_one_line():
    line = input("hi")  # blocks until a line is entered or EOF when piped
    print("Got line:", line)

# Usage example:
read_one_line()
