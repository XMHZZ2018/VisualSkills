#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MMSKILLS_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
OSWORLD_DIR="$MMSKILLS_ROOT/vendor/OSWorld"

# Initialize submodule if not already done
if [ ! -f "$OSWORLD_DIR/pyproject.toml" ]; then
  echo "Initializing OSWorld submodule..."
  cd "$MMSKILLS_ROOT"
  git submodule update --init vendor/OSWorld
fi

# Install Python dependencies
echo "Installing dependencies..."
cd "$OSWORLD_DIR"
pip install -r requirements.txt
pip install mcp httpx

echo ""
echo "Setup complete."
echo "  OSWorld: $OSWORLD_DIR"
echo ""
echo "Make sure Claude CLI is authenticated (claude login), then run:"
echo "  python3 $SCRIPT_DIR/run.py --provider_name docker --domain chrome --skill_mode none"
