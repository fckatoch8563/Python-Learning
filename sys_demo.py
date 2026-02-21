import sys


def read_one_line():
    # Interactive terminal: show prompt and use input()
    if sys.stdin.isatty():
        try:
            line = input("Enter a line: ")
        except EOFError:
            print("No input (EOF).")
            return
    else:
        # Non-interactive (pipe/heredoc): don't print prompt, read from stdin
        line = sys.stdin.readline().rstrip("\n")
        if not line:
            print("No input (EOF).")
            return
    print("Got line:", line)


if __name__ == "__main__":
    read_one_line()
##################################################################################
# When input() is enough:
# Simple interactive programs
name = input("What's your name? ")
age = input("What's your age? ")
print(f"Hello {name}, you are {age}")
# Works great for: Basic user interaction

# When you NEED sys.stdin/sys.stdout:
# 1. Reading from Pipes/Redirects

import sys

# This works:
# echo "Hello" | python script.py
# cat file.txt | python script.py

for line in sys.stdin:
    print(line.upper())

# input() doesn't work well with pipes!
# 2. Detecting Interactive vs Non-Interactive

import sys

if sys.stdin.isatty():
    # Running interactively - show prompt
    line = input("Enter text: ")
else:
    # Input from file/pipe - don't show prompt
    line = sys.stdin.readline()

# 3. Reading Multiple Lines Efficiently

import sys

# OLD WAY (slow for many lines)
lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

# BETTER WAY
lines = sys.stdin.readlines()  # Read all at once

# 4. Writing Without Newline

import sys

# input() always adds newline when printing
print("Hello", end="")  # OK but limited

# sys.stdout gives more control
sys.stdout.write("Hello")  # No newline
sys.stdout.flush()  # Force immediate output

# 5. Real Example from Your File:

import sys


def read_one_line():
    if sys.stdin.isatty():
        # Terminal: use input() - it's friendlier
        line = input("Enter a line: ")
    else:
        # Piped/redirected: use sys.stdin - no prompt needed
        line = sys.stdin.readline().rstrip("\n")
    print("Got line:", line)


# Try this:

# Interactive - shows prompt
# python sys_demo.py

# Piped - no prompt (cleaner!)
# echo "test" | python sys_demo.py

"""
Summary:
Use Case                    Use This
--------	                --------
Simple Q&A with user	    input() ✅
Reading from pipes/files	sys.stdin ✅
Detecting terminal vs pipe	sys.stdin.isatty() ✅
Multiple lines from user	sys.stdin.readlines() ✅
Output without newline	    sys.stdout.write() ✅
Redirecting output	        sys.stdout ✅

input() = convenience function for simple cases
sys.stdin/stdout = full control for complex scenarios 🎯
"""
