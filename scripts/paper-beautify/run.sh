#!/usr/bin/env bash
# Usage: ./run.sh <paper.zip>
set -euo pipefail

ZIP_FILE="${1:?Usage: $0 <paper.zip>}"
WORK_DIR="$(cd "$(dirname "$0")" && pwd)/workspace"

rm -rf "$WORK_DIR"
mkdir -p "$WORK_DIR"
unzip -o "$ZIP_FILE" -d "$WORK_DIR"

grep -rl '\\documentclass' "$WORK_DIR" --include="*.tex" | head -1
