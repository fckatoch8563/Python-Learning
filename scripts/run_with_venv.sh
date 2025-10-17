#!/usr/bin/env bash
# Run a Python file using the workspace .venv python if it exists, otherwise fall back to python3
set -euo pipefail

WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_PY="$WORKSPACE_DIR/.venv/bin/python"
PY="python3"

if [ -x "$VENV_PY" ]; then
  PY="$VENV_PY"
fi

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <python-file> [args...]" >&2
  exit 2
fi

FILE="$1"
shift || true
exec "$PY" -u "$FILE" "$@"
