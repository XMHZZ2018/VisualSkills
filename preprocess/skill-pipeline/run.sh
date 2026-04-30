#!/usr/bin/env bash
# Skill generation pipeline entry point.
#
# Usage:
#   ./run.sh --config configs/libreoffice_impress.yaml
#   ./run.sh --config configs/libreoffice_impress.yaml --mode text --parallel 4
#
# Produces:
#   skills/<domain>-knowledge-text-v1/
#   skills/<domain>-knowledge-multimodal-v1/

set -euo pipefail

CONFIG=""
MODE="both"
PARALLEL="1"
EXTRA=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)
            CONFIG="$2"
            shift 2
            ;;
        --mode)
            MODE="$2"
            shift 2
            ;;
        --parallel)
            PARALLEL="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 --config <path.yaml> [--mode both|text|multimodal] [--parallel N]"
            exit 0
            ;;
        *)
            EXTRA+=("$1")
            shift
            ;;
    esac
done

if [[ -z "$CONFIG" ]]; then
    echo "Error: --config is required" >&2
    echo "Usage: $0 --config <path.yaml> [--mode both|text|multimodal] [--parallel N]" >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Resolve config path relative to either CWD or the script dir.
if [[ ! -f "$CONFIG" ]]; then
    if [[ -f "$SCRIPT_DIR/$CONFIG" ]]; then
        CONFIG="$SCRIPT_DIR/$CONFIG"
    else
        echo "Error: config not found: $CONFIG" >&2
        exit 1
    fi
fi

cd "$SCRIPT_DIR"

export PYTHONUNBUFFERED=1

exec python3 -u generate_skill_from_knowledge_source.py \
    --config "$CONFIG" \
    --mode "$MODE" \
    --parallel "$PARALLEL" \
    ${EXTRA[@]+"${EXTRA[@]}"}
