#!/usr/bin/env bash
# Impress Stage 2 — full chain:
#   1. orchestrator (planner + 8 free-explorer workers + assembler + mapper)
#   2. inline_into_mm_v1 (writes Stage 2 mm skill)
#   3. derive_text_v3 (writes Stage 2 text skill)
#
# Phase 2b (train-targeted explorer) is run separately by Phase 2b runner —
# launched only after this chain finishes successfully.

set -euo pipefail
cd /home/ziyan/MMSkills

PIPE=preprocess/skill-pipeline/v3/outputs/impress
MM1=skills/libreoffice_impress-knowledge-multimodal-stage1
MM2=skills/libreoffice_impress-knowledge-multimodal-stage2
TX2=skills/libreoffice_impress-knowledge-text-stage2

echo "=== [1/3] orchestrator (planner -> 8 workers -> assembler -> mapper) ==="
python3 preprocess/skill-pipeline/v3/orchestrator.py \
  --config preprocess/skill-pipeline/v3/configs/impress.yaml

echo
echo "=== [2/3] inline_into_mm_v1 — writing Stage 2 mm skill at $MM2 ==="
python3 preprocess/skill-pipeline/v3/inline_into_mm_v1.py \
  --pipeline-dir "$PIPE" \
  --mm-v1 "$MM1" \
  --out "$MM2"

echo
echo "=== [3/3] derive_text — producing Stage 2 text skill at $TX2 ==="
python3 preprocess/skill-pipeline/v3/derive_text_v3.py \
  --domain libreoffice_impress \
  --app-name "LibreOffice Impress" \
  --app-version 7.3.7 \
  --mm-dir "$MM2" \
  --text-dir "$TX2" \
  --parallel 4

echo
echo "=== Impress Stage 2 free-explorer chain complete ==="
