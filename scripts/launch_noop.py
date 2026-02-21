#!/usr/bin/env python3
"""No-op launcher used by a launch configuration that calls the run-task as a preLaunchTask.

This file intentionally does nothing and exits immediately. The preLaunchTask runs the real
script in the integrated terminal; this Python file is launched afterward only to satisfy the
launch configuration lifecycle without re-running the user's script.
"""
import sys

if __name__ == "__main__":
    sys.exit(0)
