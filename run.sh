#!/usr/bin/env bash
# Helper to run Python scripts with the workspace virtualenv
# Usage: ./run.sh test.py

VENV_PYTHON="${PWD}/.venv/bin/python"
if [ ! -x "$VENV_PYTHON" ]; then
  echo "Virtualenv python not found at $VENV_PYTHON"
  exit 1
fi

$VENV_PYTHON "$@"
