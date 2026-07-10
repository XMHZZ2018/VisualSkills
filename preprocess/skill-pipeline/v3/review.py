"""Phase 2b — region aggregator (consumes per-trajectory diagnoses).

This used to do everything (parse trajectories AND nominate regions in one
Opus call). That conflated diagnosis with aggregation and the per-task
signal was so thin that Opus mostly guessed from verifier feedback.

Now it ONLY aggregates. Input is the JSON files written by `diagnose.py`.
Output is the same `targeted_targets.json` schema worker.py consumes.

Filtering logic (deterministic, before Opus):
  - Keep diagnoses with primary_cause in {ui_knowledge_gap, ui_inefficiency}.
  - From those, keep ui_struggles entries whose engagement == "opened_and_struggled".
  - Drop "never_opened" / "opened_briefly_then_left" — those are workflow or
    feature-discovery gaps, not UI-knowledge gaps.

The aggregator then asks Opus to merge synonymous regions, de-duplicate, and
emit 8-15 concrete targets with evidence pointing back to specific task_ids.

Usage:
    python3 review.py \
        --diagnoses-dir preprocess/skill-pipeline/v3/outputs/writer/diagnose \
        --app-name "LibreOffice Writer" \
        --output-dir preprocess/skill-pipeline/v3/outputs/writer/review \
        --model claude-opus-4-6
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import subprocess
import sys
from pathlib import Path

logger = logging.getLogger("review")


UI_CAUSES = {"ui_knowledge_gap", "ui_inefficiency"}
STRONG_ENGAGEMENT = {"opened_and_struggled"}


def _load_diagnoses(diag_dir: Path) -> list[dict]:
    out: list[dict] = []
    for p in sorted(diag_dir.glob("*.json")):
        if p.name == "diagnoses_summary.json":
            continue
        if p.name.endswith(".usage.json"):
            continue
        try:
            d = json.loads(p.read_text())
            if "primary_cause" not in d:
                continue  # skip non-diagnosis JSON files (e.g. stats)
            out.append(d)
        except Exception as e:
            logger.warning("skipping %s: %s", p, e)
    return out


def _collect_ui_evidence(diagnoses: list[dict]) -> tuple[list[dict], dict]:
    """Returns (filtered_evidence_blocks, stats).

    Each evidence block is one ui_struggle entry tagged with its source task.

    A struggle is kept whenever its `engagement == opened_and_struggled`,
    REGARDLESS of the task's primary_cause. The primary_cause classifies
    the dominant failure mode (e.g. 'other' for step-budget exhaustion or
    'wrong_workflow' for macro use) but a task can still surface real
    UI-fluency issues in regions the agent did engage with.
    """
    blocks: list[dict] = []
    stats = {
        "n_diagnoses": len(diagnoses),
        "by_cause": {},
        "n_struggles_total": 0,
        "n_struggles_kept": 0,
        "dropped_by_engagement": {},
    }
    for d in diagnoses:
        cause = d.get("primary_cause", "other")
        stats["by_cause"][cause] = stats["by_cause"].get(cause, 0) + 1
        for s in d.get("ui_struggles", []) or []:
            stats["n_struggles_total"] += 1
            eng = s.get("engagement", "unknown")
            if eng not in STRONG_ENGAGEMENT:
                stats["dropped_by_engagement"][eng] = \
                    stats["dropped_by_engagement"].get(eng, 0) + 1
                continue
            stats["n_struggles_kept"] += 1
            blocks.append({
                "task_id": d.get("task_id"),
                "score": d.get("score"),
                "primary_cause": cause,
                "task_summary": d.get("summary", ""),
                "region": s.get("region"),
                "what_went_wrong": s.get("what_went_wrong", ""),
                "severity": s.get("severity", ""),
                "evidence_action_indices": s.get("evidence_action_indices", []),
                "evidence_screenshots": s.get("evidence_screenshots", []),
            })
    return blocks, stats


AGGREGATE_PROMPT = """\
You are a UI-coverage planner for a Computer-Use Agent benchmark on \
{app_name}.

A separate per-trajectory diagnoser already classified each failing task \
and isolated the concrete UI regions where the agent *actually opened and \
struggled with* the UI. The list below contains ONLY those vetted struggle \
points — failures caused by wrong-workflow / missing-feature / env issues \
are already filtered out.

Your job: cluster these struggle points into 8-15 concrete UI \
regions / dialogs / panels worth dispatching a fresh UI-explorer worker to \
document. Merge synonyms (e.g., "Format > Paragraph dialog, Indents tab" \
and "Paragraph Indents & Spacing dialog" → one target).

A "UI region" is concrete and operable — e.g., "Format > Page Style dialog, \
Page tab", "Styles deck → Paragraph Styles → context menu", "Insert > \
Section dialog". NEVER abstract concepts like "page numbering" or "tracking \
changes".

Selection rules:
1. Prefer regions surfaced by MULTIPLE tasks over one-offs (but a single \
clearly-blocking struggle is still worth including).
2. If two evidence entries describe overlapping regions, merge them and \
list all source task_ids.
3. Drop entries whose `region` is too vague to act on (you may note this \
in `dropped`).
4. Output ONLY a JSON object with this shape, no markdown fences:

{{
  "targets": [
    {{
      "target_id": "snake_case_unique_id",
      "name": "Human-readable region name",
      "scope": "1-2 sentences telling an explorer worker exactly what menu \
path to follow, which tabs/controls to capture, and what common workflows \
to demonstrate.",
      "source_task_ids": ["task_a", "task_b"],
      "evidence": "1-2 sentences citing what went wrong (paraphrase from \
the input)."
    }}
  ],
  "dropped": [
    {{"region": "...", "reason": "too vague / single weak instance / etc."}}
  ]
}}

--- EVIDENCE ({n_blocks} struggle points across {n_tasks} tasks) ---

{evidence_blocks}
"""


def _format_evidence(blocks: list[dict]) -> str:
    lines: list[str] = []
    for i, b in enumerate(blocks):
        shots = b.get("evidence_screenshots") or []
        shot_str = ", ".join(shots) if shots else "(none cited)"
        lines.append(
            f"## evidence_{i:02d} — task `{b['task_id']}` (score {b['score']}, "
            f"primary_cause={b.get('primary_cause', '?')})\n"
            f"  region: {b['region']}\n"
            f"  severity: {b['severity']}\n"
            f"  evidence screenshots: {shot_str}\n"
            f"  what went wrong: {b['what_went_wrong']}\n"
            f"  diagnoser task summary: {b['task_summary'][:300]}"
        )
    return "\n\n".join(lines)


def _call_claude(prompt: str, model: str = "claude-opus-4-6", timeout: int = 900) -> str:
    res = subprocess.run(
        ["claude", "--print", "--model", model, prompt],
        capture_output=True, text=True, timeout=timeout, cwd="/tmp",
    )
    if res.returncode != 0:
        raise RuntimeError(f"claude CLI failed rc={res.returncode}: {res.stderr[:500]}")
    return res.stdout


def _parse_json(out: str) -> dict:
    txt = out.strip()
    txt = re.sub(r"^```(?:json)?\s*", "", txt)
    txt = re.sub(r"\s*```\s*$", "", txt)
    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", txt, re.DOTALL)
        if not m:
            raise
        return json.loads(m.group(0))


def main() -> int:
    ap = argparse.ArgumentParser(description="UI-region aggregator over diagnoses")
    ap.add_argument("--diagnoses-dir", required=True, type=Path,
                    help="Dir containing per-task <task_id>.json from diagnose.py")
    ap.add_argument("--app-name", required=True)
    ap.add_argument("--output-dir", required=True, type=Path)
    ap.add_argument("--model", default="claude-opus-4-6")
    args = ap.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="[%(asctime)s %(levelname)s %(name)s] %(message)s")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    diagnoses = _load_diagnoses(args.diagnoses_dir)
    if not diagnoses:
        logger.error("no diagnoses found in %s", args.diagnoses_dir)
        return 1

    blocks, stats = _collect_ui_evidence(diagnoses)
    (args.output_dir / "evidence_stats.json").write_text(json.dumps(stats, indent=2))
    logger.info("filter stats: %s", stats)

    if not blocks:
        logger.warning("no UI-knowledge evidence after filtering — writing empty targets")
        (args.output_dir / "targeted_targets.json").write_text("[]")
        return 0

    n_tasks = len({b["task_id"] for b in blocks})
    evidence_md = _format_evidence(blocks)
    (args.output_dir / "aggregation_evidence.md").write_text(evidence_md)

    prompt = AGGREGATE_PROMPT.format(
        app_name=args.app_name,
        n_blocks=len(blocks),
        n_tasks=n_tasks,
        evidence_blocks=evidence_md,
    )
    (args.output_dir / "aggregation_prompt.txt").write_text(prompt)
    logger.info("calling %s on %d evidence blocks (%d-char prompt)",
                args.model, len(blocks), len(prompt))

    raw = _call_claude(prompt, model=args.model)
    (args.output_dir / "aggregation_response.txt").write_text(raw)

    parsed = _parse_json(raw)
    targets = parsed.get("targets", [])
    dropped = parsed.get("dropped", [])

    # Index diagnoses by task_id for post-processing
    diag_by_task = {d.get("task_id"): d for d in diagnoses}

    # Targets get a final shape compatible with worker.py.
    # We deterministically populate:
    #   - setup_task_id: first source task (its setup_task.sh provides the fixture)
    #   - evidence_screenshots: list of {source_task_id, step_NNN.png, what_went_wrong}
    #     gathered from ui_struggles on any of the target's source tasks.
    final = []
    for t in targets:
        sources = t.get("source_task_ids") or []
        evid: list[dict] = []
        for sid in sources:
            d = diag_by_task.get(sid)
            if not d:
                continue
            for s in d.get("ui_struggles", []) or []:
                if s.get("engagement") != "opened_and_struggled":
                    continue
                for shot in s.get("evidence_screenshots", []) or []:
                    evid.append({
                        "source_task_id": sid,
                        "screenshot": shot,
                        "what_went_wrong": s.get("what_went_wrong", ""),
                        "region_hint": s.get("region", ""),
                    })
        final.append({
            "target_id": t.get("target_id"),
            "name": t.get("name"),
            "scope": t.get("scope"),
            "evidence": t.get("evidence", ""),
            "source_task_ids": sources,
            "setup_task_id": sources[0] if sources else None,
            "evidence_screenshots": evid,
        })

    (args.output_dir / "targeted_targets.json").write_text(json.dumps(final, indent=2))
    (args.output_dir / "dropped_regions.json").write_text(json.dumps(dropped, indent=2))
    logger.info("wrote %d targets, %d dropped",
                len(final), len(dropped))
    for t in final:
        logger.info("  • %s — %s (from %s)",
                    t["target_id"], t["name"],
                    ",".join(t.get("source_task_ids", []) or []))
    return 0


if __name__ == "__main__":
    sys.exit(main())
