# Tk / tkinter Quick Notes

This project includes a small helper script to verify that your Python
interpreter is linked to Tk/Tkinter: `scripts/check_tk.py`.

What the script does
- Attempts to import `_tkinter` and `tkinter` and prints version information.
- On failure it prints quick platform-specific install suggestions.

Run the helper
```bash
./scripts/check_tk.py
# or
python scripts/check_tk.py
```

Common fixes
- Debian/Ubuntu: `sudo apt install python3-tk`
- Fedora: `sudo dnf install python3-tkinter`
- macOS (Homebrew): `brew install tcl-tk` and use a Python build that links to it
- Windows: the official python.org installer usually includes Tk/Tcl

Headless servers
- Use an X virtual framebuffer if you need to run turtle demos without a physical display:
  `xvfb-run python -m turtledemo.penrose`

Running demos
- Open the turtledemo viewer: `python -m turtledemo`
- Run a specific demo: `python -m turtledemo.penrose`

If you need, I can add platform-specific instructions to the main README.
