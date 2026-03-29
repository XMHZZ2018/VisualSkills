#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OSWORLD_DIR="${OSWORLD_ROOT:-$HOME/OSWorld}"

# Clone OSWorld if not present
if [ ! -d "$OSWORLD_DIR" ]; then
  echo "Cloning OSWorld to $OSWORLD_DIR..."
  git clone https://github.com/xlang-ai/OSWorld "$OSWORLD_DIR"
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
echo "Make sure ANTHROPIC_API_KEY is set, then run:"
echo "  python3 $SCRIPT_DIR/run.py --provider_name docker --osworld_root $OSWORLD_DIR --domain chrome --skill_mode none"
