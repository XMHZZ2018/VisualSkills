#!/usr/bin/env bash
set -euo pipefail

# Start bridge in background
python3 /opt/bridge.py &
BRIDGE_PID=$!

# Wait for bridge to be ready (poll /screenshot endpoint)
echo "Waiting for bridge to be ready..."
for i in $(seq 1 30); do
    if curl -sf http://127.0.0.1:8765/screenshot > /dev/null 2>&1; then
        echo "Bridge ready after ${i}s"
        break
    fi
    if ! kill -0 "$BRIDGE_PID" 2>/dev/null; then
        echo "Bridge process died"
        exit 1
    fi
    sleep 1
done

# Check bridge is actually up
if ! curl -sf http://127.0.0.1:8765/screenshot > /dev/null 2>&1; then
    echo "Bridge failed to start after 30s"
    exit 1
fi

# Read prompt from workspace
PROMPT_FILE="/workspace/prompt.txt"
if [ ! -f "$PROMPT_FILE" ]; then
    echo "ERROR: $PROMPT_FILE not found"
    exit 1
fi
PROMPT=$(cat "$PROMPT_FILE")

# Run Claude CLI
echo "Starting Claude CLI..."
set +e
claude -p "$PROMPT" "$@" > /workspace/claude_output.txt 2>/workspace/claude_stderr.txt
EXIT_CODE=$?
set -e

echo "$EXIT_CODE" > /workspace/exit_code.txt
echo "Claude exited with code $EXIT_CODE"

# Cleanup
kill "$BRIDGE_PID" 2>/dev/null || true
exit 0
