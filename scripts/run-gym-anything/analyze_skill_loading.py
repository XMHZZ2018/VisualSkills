"""Scan existing claude_output.txt files to compute skill-loading rate
per (env, skill_mode) — without re-running any tasks.

A task counts as "skill loaded" if anywhere in its claude_output.txt
(excluding the very first `init` line, which always lists every
installed skill) the agent either:
  (a) invokes the `Skill` tool, or
  (b) references a path under the plugin's skill directory in any
      tool_use input (e.g. Read-ing a sub-guide.md from the skill).

Usage:
    python3 analyze_skill_loading.py \
        [--result_dir scripts/run-gym-anything/workspaces] \
        [--json /tmp/skill_load_report.json]

Prints a table grouped by (model, mode, env) with:
  total   = tasks scanned
  loaded  = tasks that touched the skill
  rate    = loaded / total
  also lists the per-task signal (via=Skill-tool or via=skill-file)
  so you can eyeball which tasks invoked and how.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

SKILL_TOOL_RE = re.compile(r'"name":"Skill"')
SKILL_PATH_RE = re.compile(r'/opt/mmskills/skills/|/workspace/plugin/skills/')

MMSKILLS_ROOT = Path(__file__).resolve().parents[2]


def analyze_one(path: Path) -> dict:
    """Return {loaded, via, skill_name, task_size_kb} for one claude_output.txt."""
    try:
        raw = path.read_text(errors="replace")
    except Exception as e:
        return {"loaded": False, "via": None, "skill_name": None,
                "size_kb": 0, "error": str(e)}
    # Skip first line (init message always lists all skills).
    nl = raw.find("\n")
    body = raw[nl + 1:] if nl >= 0 else ""
    tool_hit = SKILL_TOOL_RE.search(body)
    path_hit = SKILL_PATH_RE.search(body)

    if tool_hit:
        # Grab the `"skill":"..."` argument so we can see which variant
        # the agent chose.
        m = re.search(
            r'"name":"Skill","input":\{"skill":"([^"]+)"',
            body,
        )
        skill_name = m.group(1) if m else "(unknown)"
        return {"loaded": True, "via": "Skill-tool",
                "skill_name": skill_name, "size_kb": len(raw) // 1024}
    if path_hit:
        return {"loaded": True, "via": "skill-file",
                "skill_name": "(from path ref)", "size_kb": len(raw) // 1024}
    return {"loaded": False, "via": None, "skill_name": None,
            "size_kb": len(raw) // 1024}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--result_dir",
        default=str(MMSKILLS_ROOT / "scripts" / "run-gym-anything" / "workspaces"),
    )
    ap.add_argument("--json", default=None,
                    help="Optional: write full report as JSON")
    ap.add_argument("--skip-mode", default="none",
                    help="Comma-separated modes to skip (default: none)")
    args = ap.parse_args()

    skip_modes = set(args.skip_mode.split(","))
    root = Path(args.result_dir)
    if not root.is_dir():
        print(f"ERROR: result dir not found: {root}", file=sys.stderr)
        return 1

    # Layout: <root>/<model>/skill-<mode>/<env>/<task>/claude_output.txt
    by_group: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for out_file in root.rglob("claude_output.txt"):
        parts = out_file.relative_to(root).parts
        if len(parts) < 5:
            continue
        model, skill_dir_name, env, task = parts[0], parts[1], parts[2], parts[3]
        mode = skill_dir_name.replace("skill-", "")
        if mode in skip_modes:
            continue
        r = analyze_one(out_file)
        r["task"] = task
        r["path"] = str(out_file)
        by_group[(model, mode, env)].append(r)

    # Print summary table.
    print(f"{'model':22s} {'mode':12s} {'env':25s} {'loaded/total':>14s} {'rate':>8s}")
    print("-" * 85)
    full_report = {}
    for (model, mode, env), rows in sorted(by_group.items()):
        loaded = sum(1 for r in rows if r["loaded"])
        total = len(rows)
        rate = f"{(loaded / total) * 100:.1f}%" if total else "n/a"
        print(f"{model:22s} {mode:12s} {env:25s} {loaded:>7d}/{total:<5d} {rate:>8s}")
        full_report[f"{model}|{mode}|{env}"] = {
            "loaded": loaded, "total": total,
            "rate": loaded / total if total else None,
            "tasks": rows,
        }

    # Per-task detail for the loaded ones.
    print("\n" + "=" * 85)
    print("TASKS THAT LOADED THE SKILL:")
    for (model, mode, env), rows in sorted(by_group.items()):
        for r in rows:
            if r["loaded"]:
                print(f"  [{model}/{mode}/{env}/{r['task']}] via={r['via']}"
                      f"  skill={r['skill_name']}")

    # Optional JSON dump.
    if args.json:
        Path(args.json).write_text(json.dumps(full_report, indent=2))
        print(f"\n[info] Full per-task report: {args.json}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
