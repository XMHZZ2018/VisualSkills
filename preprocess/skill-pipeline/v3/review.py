"""Phase 2b — trajectory-targeted exploration target generator.

Reads completed training-task trajectories (from a gym-anything-style
workspace), extracts failures + verifier feedback + agent action summaries,
and asks Opus to nominate UI regions worth re-exploring. The output JSON
is structurally identical to v3's plan.json so the existing worker.py
runner can consume it directly.

Usage:
    python3 review.py \
        --rollouts-dir scripts/run-gym-anything/workspaces/claude-opus-4-6/skill-multimodal/libreoffice_writer_env \
        --app-name "LibreOffice Writer" \
        --output-dir preprocess/skill-pipeline/v3/outputs/writer/review

Writes:
    <output-dir>/review_summary.md     — per-task failure summary (Opus input)
    <output-dir>/targeted_targets.json — list of {target_id, name, scope}

Worker.py is then invoked once per entry in targeted_targets.json,
identically to how it processes plan.json entries.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

logger = logging.getLogger("review")


# ---------------------------------------------------------------------------
# Trajectory + verifier extraction
# ---------------------------------------------------------------------------

def _load_result(task_dir: Path) -> dict | None:
    rj = task_dir / "result.json"
    if not rj.exists():
        return None
    try:
        return json.loads(rj.read_text())
    except Exception:
        return None


def _summarize_actions(claude_output: Path, max_actions: int = 30) -> list[str]:
    """Compact list of GUI actions the agent took, in order. Each action is
    one short line. Caps at `max_actions` (kept early actions; trims middle).
    """
    actions: list[str] = []
    if not claude_output.exists():
        return actions
    for line in claude_output.open():
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("type") != "assistant":
            continue
        for c in d.get("message", {}).get("content", []):
            if c.get("type") != "tool_use":
                continue
            name = c.get("name", "").replace("mcp__gym-anything-controller__", "")
            name = name.replace("mcp__skill-loader__", "skill-loader.")
            inp = c.get("input", {})
            short = json.dumps(inp)[:120]
            actions.append(f"{name} {short}")
    if len(actions) <= max_actions:
        return actions
    half = max_actions // 2
    return actions[:half] + [f"... (omitted {len(actions) - max_actions} actions)"] + actions[-half:]


def _extract_skill_consultation(claude_output: Path) -> dict:
    """Count load_topic / list_topics calls; collect distinct topics loaded."""
    n_load = 0
    n_list = 0
    topics: list[str] = []
    if not claude_output.exists():
        return {"load_topic": 0, "list_topics": 0, "topics": []}
    for line in claude_output.open():
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("type") != "assistant":
            continue
        for c in d.get("message", {}).get("content", []):
            if c.get("type") != "tool_use":
                continue
            name = c.get("name", "")
            if "load_topic" in name:
                n_load += 1
                t = c.get("input", {}).get("topic")
                if t and t not in topics:
                    topics.append(t)
            elif "list_topics" in name:
                n_list += 1
    return {"load_topic": n_load, "list_topics": n_list, "topics": topics}


def _build_per_task_block(task_dir: Path) -> str | None:
    """Build the markdown block for one task that we'll send to Opus."""
    task_id = task_dir.name
    result = _load_result(task_dir)
    if result is None:
        return None
    score = float(result.get("score", 0.0) or 0.0)
    instruction = result.get("instruction", "<unknown>")
    feedback = (result.get("verifier_result") or {}).get("feedback", "")
    actions = _summarize_actions(task_dir / "claude_output.txt")
    consult = _extract_skill_consultation(task_dir / "claude_output.txt")
    flag = "PASS" if score >= 0.65 else "FAIL"
    lines = [
        f"## {task_id} — score {score:.3f} ({flag})",
        f"**Instruction:** {instruction[:500]}",
        f"**Verifier feedback:** {feedback[:500]}",
        f"**Skill consultation:** list_topics={consult['list_topics']}, "
        f"load_topic={consult['load_topic']}, topics={consult['topics'][:6]}",
        "**Action sequence (truncated):**",
    ]
    for a in actions:
        lines.append(f"  - `{a}`")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Opus call: nominate UI regions
# ---------------------------------------------------------------------------

REVIEW_PROMPT = """\
You are a UI-coverage analyst for a Computer-Use Agent benchmark.

Below are trajectories from a Computer-Use Agent attempting LibreOffice Writer
tasks with access to a documentation-derived skill that exposes guides via
load_topic(<topic>). For each task we show the agent's instruction, the final
verifier feedback, what (if any) skill topics it consulted, and the sequence
of GUI actions it took.

Your job: identify a SHORT list (8-15) of \
specific UI regions / dialogs / panels in {app_name} that the agent \
demonstrably struggled with across these trajectories. We will dispatch a \
new round of UI-explorer workers to autonomously document each region in \
detail (screenshots + per-control notes) so a future agent has the visual \
knowledge it was missing.

A "UI region" is concrete and operable — e.g., "Format > Page Style dialog, \
Page tab", "Styles deck → Paragraph Styles → context menu", "Insert > Section \
dialog", "File > Save As format dropdown". NOT abstract concepts like "page \
numbering" or "tracking changes".

OUTPUT FORMAT:
A JSON array; each entry has exactly these fields:
{{
  "target_id": "snake_case_unique_id",
  "name": "Human-readable region name",
  "scope": "1-2 sentence description of what to document (menu path, visible \
controls, common workflows). Concrete enough that an explorer worker can find \
the region from the bare app and produce a useful screenshot+description.",
  "evidence": "Short sentence citing 1-3 task IDs where this region appeared \
in a failure"
}}

Rules:
1. Prefer regions surfaced by MULTIPLE failures over one-offs.
2. Don't list regions the skill already covers well (judge by whether the \
agent consulted a relevant topic and still failed at the UI step — that \
implies the topic existed but the visual reference was weak).
3. Don't include trivially-known regions (e.g., "File menu") unless a \
specific submenu is the failure point.
4. Output ONLY the JSON array, no surrounding prose, no markdown fences.

--- Trajectories ---

{trajectory_blocks}
"""


def _call_claude(prompt: str, model: str = "claude-opus-4-6", timeout: int = 900) -> str:
    """Call Claude CLI in non-interactive mode and return stdout."""
    # cwd=/tmp so the project's .claude/ config doesn't confuse non-interactive
    # invocations (same trick the v1 pipeline uses).
    res = subprocess.run(
        ["claude", "--print", "--model", model, prompt],
        capture_output=True, text=True, timeout=timeout, cwd="/tmp",
    )
    if res.returncode != 0:
        raise RuntimeError(f"claude CLI failed (rc={res.returncode}): {res.stderr[:500]}")
    return res.stdout


def _parse_targets(opus_output: str) -> list[dict]:
    """Extract a JSON array of targets from Opus's output."""
    txt = opus_output.strip()
    # Strip code fences if present (defensive).
    txt = re.sub(r"^```(?:json)?\s*", "", txt)
    txt = re.sub(r"\s*```\s*$", "", txt)
    try:
        data = json.loads(txt)
    except json.JSONDecodeError:
        # Try to find a JSON array substring.
        m = re.search(r"\[\s*\{.*?\}\s*\]", txt, re.DOTALL)
        if not m:
            raise
        data = json.loads(m.group(0))
    if not isinstance(data, list):
        raise ValueError(f"Opus output not a list: {type(data).__name__}")
    return data


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Trajectory-targeted UI exploration target generator")
    ap.add_argument("--rollouts-dir", required=True, type=Path,
                    help="gym-anything workspace dir containing per-task subfolders")
    ap.add_argument("--app-name", default="LibreOffice Writer")
    ap.add_argument("--output-dir", required=True, type=Path)
    ap.add_argument("--model", default="claude-opus-4-6")
    ap.add_argument("--include-passes", action="store_true",
                    help="Include passed tasks in the review (default: failures only)")
    ap.add_argument("--max-tasks", type=int, default=24,
                    help="Cap the number of trajectories sent to Opus")
    args = ap.parse_args()

    logging.basicConfig(level=logging.INFO, format="[%(asctime)s %(levelname)s %(name)s] %(message)s")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Collect per-task summary blocks
    blocks: list[str] = []
    for task_dir in sorted(args.rollouts_dir.iterdir()):
        if not task_dir.is_dir():
            continue
        result = _load_result(task_dir)
        if result is None:
            logger.info("skipping %s (no result.json)", task_dir.name)
            continue
        score = float(result.get("score", 0.0) or 0.0)
        if not args.include_passes and score >= 0.65:
            logger.info("skipping %s (passed, score=%.3f)", task_dir.name, score)
            continue
        b = _build_per_task_block(task_dir)
        if b:
            blocks.append(b)
        if len(blocks) >= args.max_tasks:
            break

    if not blocks:
        logger.error("no failed trajectories found in %s", args.rollouts_dir)
        return 1

    logger.info("collected %d failure trajectories for review", len(blocks))
    summary_md = "\n\n".join(blocks)
    (args.output_dir / "review_summary.md").write_text(summary_md)
    logger.info("wrote %s", args.output_dir / "review_summary.md")

    prompt = REVIEW_PROMPT.format(app_name=args.app_name, trajectory_blocks=summary_md)
    (args.output_dir / "review_prompt.txt").write_text(prompt)
    logger.info("calling %s with %d-char prompt", args.model, len(prompt))

    out = _call_claude(prompt, model=args.model)
    (args.output_dir / "review_response.txt").write_text(out)

    targets = _parse_targets(out)
    logger.info("Opus emitted %d targets", len(targets))
    (args.output_dir / "targeted_targets.json").write_text(json.dumps(targets, indent=2))
    logger.info("wrote %s", args.output_dir / "targeted_targets.json")
    for t in targets:
        logger.info("  • %s — %s", t.get("target_id"), t.get("name"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
