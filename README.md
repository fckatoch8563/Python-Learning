# Project: Environments

This workspace uses a virtual environment located at `.venv/`.

Quick run instructions (macOS / zsh):

Activate the venv for the current shell:

```bash
source .venv/bin/activate
```

Then run Python scripts normally, for example:

```bash
python test.py
```

Or run a specific interpreter without activating the venv:

```bash
.venv/bin/python test.py
```

If you see `ModuleNotFoundError` for a package (for example `pandas`), install it into the venv:

```bash
source .venv/bin/activate
pip install pandas
```

If you use VS Code, select the interpreter from the Command Palette: `Python: Select Interpreter` → choose the `.venv` entry.

Convenience helper
------------------

You can use the included `run.sh` helper to run scripts with the venv python without activating it:

```bash
./run.sh test.py
```

Optional: add a shell alias to make this even shorter (add to `~/.zshrc`):

```bash
alias vpython="${PWD}/.venv/bin/python"
# then use:
vpython test.py
```

More tools and tips are in the repository files.

Dependencies
------------

To install runtime dependencies only:

```bash
source .venv/bin/activate
pip install -r requirements-runtime.txt
```

To install development dependencies as well:

```bash
source .venv/bin/activate
pip install -r requirements-dev.txt
```

VS Code: Run workflow (quick)
---------------------------

The workspace includes a Run task and a launch configuration that execute the active Python file using the workspace `.venv` Python. A small internal `save-all` pre-launch task silently saves all open files before running so you always execute the latest code.

- Run the active file with the venv: press Control + Option + R (shown as Ctrl+Alt+R) while the editor has focus.
- Or use the Run and Debug view or the Command Palette → `Tasks: Run Task` → select "Run current Python file (venv)".

The task uses `scripts/run_with_venv.sh` which prefers `.venv/bin/python` if present, otherwise falls back to `python3`.

Customizing keybinding and Run button behavior
----------------------------------------------

Change the keyboard shortcut
 - To change the Ctrl+Alt+R shortcut, open VS Code Keyboard Shortcuts (⌘K ⌘S) and search for `Run current Python file (venv)` (the workspace keybinding is in `.vscode/keybindings.json`). Edit or remove it as you prefer. You can also edit `keybindings.json` directly in the workspace.

Make the Run button execute the task
 - By default the editor Run button uses the launch configuration in `.vscode/launch.json`. If you prefer the Run button to execute the task instead, you can create or edit a launch configuration that runs the task as a `preLaunchTask` and immediately exits after the task completes, or create a compound configuration. Example (add to `.vscode/launch.json`):

```jsonc
{
	"name": "Run current file via task",
	"type": "cppdbg", // a dummy type may be required; some VS Code versions accept "type": "pwa-node" or the existing "debugpy"
	"request": "launch",
	"preLaunchTask": "Run current Python file (venv)",
	"program": "${file}",
	"console": "integratedTerminal",
	"cwd": "${workspaceFolder}"
}
```

Note: VS Code's schema sometimes requires a specific `type` value for proper Run-button support. The safer, supported approach is to keep the existing `debugpy` launch configuration (which we already use) and keep `save-all` as its `preLaunchTask` so the Run/Play button still runs the file in the integrated terminal with the venv environment. If you prefer, I can craft a precise launch configuration that maps the Run button to the task for your VS Code version.

