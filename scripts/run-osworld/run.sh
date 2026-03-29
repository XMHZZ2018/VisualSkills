#!/usr/bin/env bash
set -euo pipefail

# Baseline (no skills) — Docker
# python3 scripts/run-osworld/run.py \
#   --provider_name docker \
#   --domain chrome --skill_mode none

# Text skills — Docker
# python3 scripts/run-osworld/run.py \
#   --provider_name docker \
#   --domain chrome --skill_mode text

# Multimodal skills — Docker
# python3 scripts/run-osworld/run.py \
#   --provider_name docker \
#   --domain chrome --skill_mode multimodal

# VMware (single VM)
# python3 scripts/run-osworld/run.py \
#   --provider_name vmware \
#   --path_to_vm /path/to/Ubuntu0.vmx \
#   --domain chrome --skill_mode none

# Parallel Docker (2 workers)
# python3 scripts/run-osworld/run.py \
#   --provider_name docker \
#   --domain chrome --skill_mode none --parallel 2
