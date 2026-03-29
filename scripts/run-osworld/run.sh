#!/usr/bin/env bash
set -euo pipefail

# Baseline (no skills)
# python3 scripts/run-osworld/run.py \
#   --path_to_vm /Users/ziyan/Documents/OSWorld/vmware_vm_data/Ubuntu0/Ubuntu0.vmx \
#   --domain chrome --skill_mode none

# # Text skills
# python3 scripts/run-osworld/run.py \
#   --path_to_vm /Users/ziyan/Documents/OSWorld/vmware_vm_data/Ubuntu0/Ubuntu0.vmx \
#   --domain chrome --skill_mode text

# # Multimodal skills
# python3 scripts/run-osworld/run.py \
#   --path_to_vm /Users/ziyan/Documents/OSWorld/vmware_vm_data/Ubuntu0/Ubuntu0.vmx \
#   --domain chrome --skill_mode multimodal

# # Parallel (4 VMs)
# python3 scripts/run-osworld/run.py \
#   --path_to_vm /path/to/vms/ \
#   --domain chrome --skill_mode multimodal --parallel 4
