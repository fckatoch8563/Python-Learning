#!/usr/bin/env bash
set -euo pipefail

echo "=== Heredoc Examples Demo ==="

echo "\n--- Example 1: here-string (<<<) ---"
grep foo <<< "foo bar baz" || true

echo "\n--- Example 2: simple heredoc to cat (no expansion, quoted) ---"
cat <<'EOF'
This is a literal heredoc block.
Shell variables like $HOME are NOT expanded here.
EOF

echo "\n--- Example 3: heredoc with expansion (unquoted) ---"
NAME=heredoc_user
cat <<EOF
Hello $NAME (variable expanded)
EOF

echo "\n--- Example 4: write a file via heredoc (/tmp/heredoc_demo.txt) ---"
cat > /tmp/heredoc_demo.txt <<'PY'
This file was written with a heredoc.
User: $USER
PY
echo "Wrote /tmp/heredoc_demo.txt:"
sed -n '1,5p' /tmp/heredoc_demo.txt || true

echo "\n--- Example 5: inline Python via heredoc (uses ./.venv/bin/python if present) ---"
if [ -x "./.venv/bin/python" ]; then
  PYTHON=./.venv/bin/python
else
  PYTHON=python
fi
$PYTHON - <<'PY'
import sys
print('python executable:', sys.executable)
print('Hello from heredoc Python')
PY

echo "\n--- Example 6: tee example (no sudo) ---"
tee /tmp/heredoc_tee.txt > /dev/null <<'EOF'
example content via tee
EOF
sed -n '1,5p' /tmp/heredoc_tee.txt || true

echo "\n--- Example 7: <<- strips leading TABs (demo) ---"
cat <<-TAB
	This line had a leading tab (TAB) and it's stripped by <<-
		Second line with two tabs: first tab stripped, second remains
TAB

echo "\nDemo finished. Files created: /tmp/heredoc_demo.txt, /tmp/heredoc_tee.txt"
exit 0
