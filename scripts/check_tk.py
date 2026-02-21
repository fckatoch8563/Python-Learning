#!/usr/bin/env python3
"""Check Tk / tkinter availability and print helpful info.

Usage:
    ./scripts/check_tk.py
    python scripts/check_tk.py

Returns exit code 0 on success (tk available), 1 on failure.
"""
import sys


def main() -> int:
    try:
        import _tkinter as _tk  # type: ignore
        import tkinter
    except Exception as exc:  # pragma: no cover - runtime check
        print("Tk/tkinter check failed:", exc, file=sys.stderr)
        print()
        print("Suggestions:")
        print(" - On Debian/Ubuntu: sudo apt install python3-tk")
        print(" - On Fedora: sudo dnf install python3-tkinter")
        print(
            " - On macOS (Homebrew): brew install tcl-tk and use a Python that links to it"
        )
        print(" - On headless servers, use xvfb-run to provide an X server")
        return 1

    # If we reached here, tkinter/_tkinter are importable
    try:
        print("_tkinter:", _tk.TK_VERSION, _tk.TCL_VERSION)
    except Exception:
        print("_tkinter imported, but could not read version info")

    try:
        print("tkinter TkVersion:", tkinter.TkVersion)
    except Exception:
        print("tkinter imported, but could not read TkVersion")

    print()
    print("turtle demo quick test: run: python -m turtledemo.penrose")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
