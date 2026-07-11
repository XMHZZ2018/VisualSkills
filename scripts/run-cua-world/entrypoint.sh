#!/usr/bin/env bash
set -euo pipefail

# Entrypoint for Claude CLI container (Docker 2).
# The bridge runs on the HOST (not in this container) because it holds
# the cua-world env Python object. This container connects to it
# via host.docker.internal:$BRIDGE_PORT.

BRIDGE_URL="${CW_BRIDGE_URL:-http://host.docker.internal:8766}"

# Wait for bridge to be ready
echo "Waiting for bridge at ${BRIDGE_URL}..."
for i in $(seq 1 30); do
    if curl -sf "${BRIDGE_URL}/health" > /dev/null 2>&1; then
        echo "Bridge ready after ${i}s"
        break
    fi
    sleep 1
done

if ! curl -sf "${BRIDGE_URL}/health" > /dev/null 2>&1; then
    echo "Bridge failed to respond after 30s"
    exit 1
fi

# Read prompt from workspace
PROMPT_FILE="/workspace/prompt.txt"
if [ ! -f "$PROMPT_FILE" ]; then
    echo "ERROR: $PROMPT_FILE not found"
    exit 1
fi
PROMPT=$(cat "$PROMPT_FILE")

# Run Claude CLI — only MCP GUI tools, no bash/file access
echo "Starting Claude CLI..."
set +e
claude -p "$PROMPT" "$@" > /workspace/claude_output.txt 2>/workspace/claude_stderr.txt
EXIT_CODE=$?
set -e

echo "$EXIT_CODE" > /workspace/exit_code.txt
echo "Claude exited with code $EXIT_CODE"
exit 0
