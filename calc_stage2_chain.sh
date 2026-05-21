#!/usr/bin/env bash
# Calc Stage 2 free explorer chain.
set -euo pipefail
cd /home/ziyan/MMSkills

PIPE=preprocess/skill-pipeline/v3/outputs/calc
MM1=skills/libreoffice_calc-knowledge-multimodal-stage1
MM2=skills/libreoffice_calc-knowledge-multimodal-stage2
TX2=skills/libreoffice_calc-knowledge-text-stage2

echo "=== [1/3] orchestrator (planner -> 8 workers -> assembler -> mapper) ==="
python3 preprocess/skill-pipeline/v3/orchestrator.py \
  --config preprocess/skill-pipeline/v3/configs/calc.yaml

echo
echo "=== [2/3] inline_into_mm_v1 — writing Stage 2 mm skill at $MM2 ==="
python3 preprocess/skill-pipeline/v3/inline_into_mm_v1.py \
  --pipeline-dir "$PIPE" \
  --mm-v1 "$MM1" \
  --out "$MM2"

echo
echo "=== [3/3] derive_text — producing Stage 2 text skill at $TX2 ==="
python3 preprocess/skill-pipeline/v3/derive_text_v3.py \
  --domain libreoffice_calc \
  --app-name "LibreOffice Calc" \
  --app-version 7.3.7 \
  --mm-dir "$MM2" \
  --text-dir "$TX2" \
  --parallel 4

echo
echo "=== Calc Stage 2 free-explorer chain complete ==="
