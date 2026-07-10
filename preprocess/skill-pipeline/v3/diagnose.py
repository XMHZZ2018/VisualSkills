"""Phase 2b — per-trajectory diagnosis (chunked multi-turn).

For each completed train-task rollout, ONE Claude CLI invocation in
stream-json multi-turn mode. The trajectory's screenshots are split into
chunks of ~10 each. Each chunk is sent as one user message containing the
corresponding action/text segments interleaved with the 10 image blocks.
Claude reviews each chunk in turn (context accumulates across turns), then
a final user message asks for a structured diagnosis as JSON.

Why chunked: when you dump 80 screenshots at once Claude skims; when you
send 10 per turn it actually engages with each.

Output: one JSON file per task with primary_cause, summary, ui_struggles.

Usage:
    python3 diagnose.py \
        --rollouts-dir ... --tasks-dir ... --app-name "LibreOffice Writer" \
        --output-dir ... --model claude-sonnet-4-6 --parallel 4
"""
from __future__ import annotations

import argparse
import base64
import json
import logging
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

logger = logging.getLogger("diagnose")


GUI_TOOLS = {"click", "double_click", "right_click", "triple_click", "drag_to",
             "scroll", "hotkey", "type_text", "key_press", "screenshot", "move_to"}


def _load_result(task_dir: Path) -> dict | None:
    rj = task_dir / "result.json"
    if not rj.exists():
        return None
    try:
        return json.loads(rj.read_text())
    except Exception:
        return None


def _load_instruction(tasks_dir: Path, task_id: str) -> str:
    tj = tasks_dir / task_id / "task.json"
    if not tj.exists():
        return ""
    try:
        return json.loads(tj.read_text()).get("description", "") or ""
    except Exception:
        return ""


def _extract_trajectory(claude_output: Path, screenshots_dir: Path,
                        max_input_chars: int = 200) -> list[dict]:
    """JSONL → list of {i, kind, ...}. kind ∈ {text, action, tool_result}."""
    steps: list[dict] = []
    if not claude_output.exists():
        return steps
    i = 0
    gui_step = 0
    pending: dict[str, tuple[str, bool]] = {}
    for line in claude_output.open():
        try:
            d = json.loads(line)
        except Exception:
            continue
        t = d.get("type")
        if t == "assistant":
            for c in d.get("message", {}).get("content", []):
                ctype = c.get("type")
                if ctype == "text":
                    txt = (c.get("text") or "").strip()
                    if txt:
                        snippet = txt if len(txt) <= 400 else txt[:380] + " …"
                        steps.append({"i": i, "kind": "text", "text": snippet})
                        i += 1
                elif ctype == "tool_use":
                    short = c.get("name", "").split("__")[-1]
                    inp = json.dumps(c.get("input", {}))
                    if len(inp) > max_input_chars:
                        inp = inp[:max_input_chars] + " …"
                    steps.append({"i": i, "kind": "action", "tool": short, "input": inp})
                    pending[c.get("id", "")] = (short, short in GUI_TOOLS)
                    i += 1
        elif t == "user":
            for c in d.get("message", {}).get("content", []):
                if c.get("type") != "tool_result":
                    continue
                tid = c.get("tool_use_id", "")
                tool, is_gui = pending.pop(tid, ("?", False))
                raw = c.get("content", "")
                has_image = False
                if isinstance(raw, list):
                    parts = []
                    for sub in raw:
                        if isinstance(sub, dict):
                            if sub.get("type") == "text":
                                parts.append(sub.get("text", ""))
                            elif sub.get("type") == "image":
                                has_image = True
                        else:
                            parts.append(str(sub))
                    raw = " ".join(parts)
                raw = str(raw).strip()
                shot_path = None
                if is_gui and has_image:
                    gui_step += 1
                    candidate = screenshots_dir / f"step_{gui_step:03d}.png"
                    if candidate.exists():
                        shot_path = str(candidate)
                if not raw and not shot_path:
                    continue
                summary = raw[:200] + f" … (+{len(raw)-200} chars)" if len(raw) > 240 else raw
                steps.append({"i": i, "kind": "tool_result", "tool": tool,
                              "result": summary, "screenshot": shot_path})
                i += 1
    return steps


def _build_chunks(steps: list[dict], shots_per_chunk: int = 10) -> list[list[dict]]:
    """Split the step list into chunks, each containing up to `shots_per_chunk`
    screenshots plus all the surrounding text/action steps. Returns a list
    where each chunk is a list of trajectory steps to send in one turn.
    """
    chunks: list[list[dict]] = [[]]
    shots_in_current = 0
    for s in steps:
        chunks[-1].append(s)
        if s.get("kind") == "tool_result" and s.get("screenshot"):
            shots_in_current += 1
            if shots_in_current >= shots_per_chunk:
                chunks.append([])
                shots_in_current = 0
    if not chunks[-1]:
        chunks.pop()
    return chunks


def _chunk_to_content_blocks(chunk: list[dict]) -> list[dict]:
    """Build interleaved text/image content blocks for one chunk."""
    blocks: list[dict] = []
    text_buf: list[str] = []

    def _flush():
        if text_buf:
            blocks.append({"type": "text", "text": "\n".join(text_buf)})
            text_buf.clear()

    for s in chunk:
        i = s["i"]
        kind = s["kind"]
        if kind == "text":
            text_buf.append(f"[{i:03d}] THINK: {s['text']}")
        elif kind == "action":
            text_buf.append(f"[{i:03d}] ACT   {s['tool']} {s['input']}")
        elif kind == "tool_result":
            shot = s.get("screenshot")
            shot_name = Path(shot).name if shot else ""
            tail = f"   screenshot: {shot_name}" if shot_name else ""
            text_buf.append(f"[{i:03d}] RESULT({s['tool']}): {s['result']}{tail}")
            if shot:
                try:
                    data = base64.b64encode(Path(shot).read_bytes()).decode()
                except Exception as e:
                    text_buf.append(f"        (screenshot unreadable: {e})")
                    continue
                _flush()
                blocks.append({"type": "image",
                               "source": {"type": "base64",
                                          "media_type": "image/png",
                                          "data": data}})
    _flush()
    return blocks


# ---------------------------------------------------------------------------

HEADER_TEMPLATE = """\
You are a failure-mode analyst for a Computer-Use Agent benchmark on {app_name}.

You will review ONE rollout trajectory in chunks. The agent had access to a
documentation-derived skill exposed as `load_topic(<topic>)`. Your goal at
the end is to decide whether the agent's failure / inefficiency was caused
by a *visual UI gap* — something we can fix by sending a UI-explorer worker
to document the relevant dialog or panel with screenshots — versus other
failure modes that more UI documentation will NOT fix.

=== TASK INSTRUCTION (what the agent was told to do) ===
{instruction}

=== VERIFIER FEEDBACK (programmatic grading of the final document) ===
{verifier_feedback}

=== FINAL SCORE: {score} ({verdict}) ===

=== HOW THIS REVIEW WORKS ===
I will send you the trajectory in chunks of up to {chunk_size} screenshots
per turn. After each chunk, briefly note (in 1-2 sentences) what the agent
did and any UI difficulty you observed in that chunk. **Do NOT** produce the
final diagnosis until I explicitly ask for it on the last turn.

Here is the FIRST chunk of the trajectory:
"""


INTERMEDIATE_TEMPLATE = (
    "Continuing the trajectory — chunk {n}/{total}. Briefly note what you "
    "see; don't produce the final diagnosis yet.\n"
)


FINAL_PROMPT = """\
That was the last chunk of the trajectory. Now produce the structured
diagnosis based on EVERYTHING you saw across all chunks.

CLASSIFICATION RULES — pick ONE primary_cause:
  - `ui_knowledge_gap`         — agent opened the right region but couldn't
                                 operate it correctly (clicked wrong control,
                                 misread a label, couldn't find the right tab).
                                 "Doesn't understand the UI at all."
  - `ui_inefficiency`          — agent eventually operated the region correctly
                                 but took many wasted actions. "Knows the UI
                                 but is not fluent / slow at it."
  - `wrong_workflow`           — agent picked a non-UI path (macro, terminal,
                                 manual retyping) instead of the obvious UI
                                 feature. Documenting the bypassed UI won't help.
  - `missing_feature_knowledge` — agent never attempted the right feature
                                 because it didn't know it existed. SKILL.md
                                 / topic-index gap, not a UI gap.
  - `env_failure`              — env / save / launch issue not under the
                                 agent's control.
  - `other`                    — none of the above (e.g. forgot to save,
                                 task-comprehension gap, ran out of steps on
                                 irrelevant work).

HARD RULES:
  1. Every entry in `ui_struggles` MUST cite at least one specific
     `step_NNN.png` you actually saw in `evidence_screenshots`. No empty
     evidence arrays — that signals speculation.
  2. If the screenshots showed the input was VISIBLY ACCEPTED by the UI
     (field shows the expected value, dialog closed normally, correct tab
     active), the UI interaction succeeded. **Do NOT list that region as a
     `ui_struggle`** even if the verifier reports the value missing
     downstream — that's a save/workflow issue, not a UI gap.
  3. Prefer fewer well-evidenced struggles over many speculative ones.

OUTPUT — reply with EXACTLY one JSON object wrapped in a ```json code
fence (no prose before or after):

```json
{{
  "primary_cause": "<one of the labels above>",
  "summary": "<3-5 sentences explaining what happened, citing action indices like [042] and screenshot names like step_022.png as evidence>",
  "ui_struggles": [
    {{
      "region": "<concrete, e.g. 'Format > Page Style dialog, Page tab, margin spinboxes'; never abstract>",
      "evidence_action_indices": [<int>, ...],
      "evidence_screenshots": ["step_022.png", ...],
      "what_went_wrong": "<one sentence describing what you SAW the agent do wrong in those screenshots>",
      "severity": "blocking" | "inefficient",
      "engagement": "opened_and_struggled" | "never_opened" | "opened_briefly_then_left"
    }}
  ]
}}
```

If `primary_cause` is not `ui_knowledge_gap` or `ui_inefficiency`,
`ui_struggles` may be `[]`.
"""


def _call_claude_multiturn(user_messages: list[list[dict]], model: str,
                           timeout: int = 1800) -> tuple[str, dict, list[str]]:
    """Stream a sequence of user messages through claude CLI and collect all
    assistant text. Returns (last_assistant_text, result_event, all_texts)."""
    lines = []
    for content_blocks in user_messages:
        msg = {"type": "user",
               "message": {"role": "user", "content": content_blocks}}
        lines.append(json.dumps(msg))
    stdin = "\n".join(lines) + "\n"

    cmd = ["claude", "--print",
           "--input-format", "stream-json",
           "--output-format", "stream-json",
           "--verbose",
           "--model", model]
    res = subprocess.run(cmd, input=stdin, capture_output=True, text=True,
                         timeout=timeout, cwd="/tmp")
    if res.returncode != 0:
        raise RuntimeError(f"claude CLI failed rc={res.returncode}: "
                           f"stderr={res.stderr[-500:]} stdout_tail={res.stdout[-500:]}")
    result_event = None
    texts: list[str] = []
    cur_text_parts: list[str] = []
    msgs_seen = 0
    for line in res.stdout.splitlines():
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("type") == "assistant":
            mid = d.get("message", {}).get("id")
            # Detect message boundary: new id ⇒ flush previous turn's text
            for c in d.get("message", {}).get("content", []):
                if c.get("type") == "text":
                    cur_text_parts.append(c.get("text", ""))
        elif d.get("type") == "user":
            # End of a turn (user message comes between assistants).
            if cur_text_parts:
                texts.append("".join(cur_text_parts))
                cur_text_parts = []
                msgs_seen += 1
        elif d.get("type") == "result":
            result_event = d
    if cur_text_parts:
        texts.append("".join(cur_text_parts))
    if result_event is None:
        raise RuntimeError(f"no result event; stdout tail: {res.stdout[-500:]}")
    if result_event.get("is_error"):
        raise RuntimeError(f"claude returned error: {result_event}")
    last = texts[-1] if texts else result_event.get("result", "")
    return last, result_event, texts


def _parse_json(text: str) -> dict:
    m = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        return json.loads(m.group(1))
    m = re.search(r"\{[^{}]*\"primary_cause\"[^{}]*\}", text, re.DOTALL)
    if m:
        return json.loads(m.group(0))
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        raise ValueError("no JSON object found")
    return json.loads(m.group(0))


def _diagnose_one(task_dir: Path, tasks_dir: Path, app_name: str,
                  output_dir: Path, model: str, chunk_size: int) -> dict:
    task_id = task_dir.name
    out_json = output_dir / f"{task_id}.json"
    if out_json.exists():
        try:
            return json.loads(out_json.read_text())
        except Exception:
            pass

    task_dir = task_dir.resolve()
    result = _load_result(task_dir)
    if result is None:
        raise RuntimeError(f"no result.json in {task_dir}")
    score = float(result.get("score", 0.0) or 0.0)
    verdict = "pass" if score >= 0.65 else "fail"
    feedback = (result.get("verifier_result") or {}).get("feedback", "") or ""
    instruction = _load_instruction(tasks_dir, task_id) or "<missing>"

    screenshots_dir = task_dir / "screenshots"
    steps = _extract_trajectory(task_dir / "claude_output.txt", screenshots_dir)
    chunks = _build_chunks(steps, shots_per_chunk=chunk_size)
    n_chunks = len(chunks)

    # Build sequence of user messages.
    user_messages: list[list[dict]] = []
    for k, chunk in enumerate(chunks):
        chunk_blocks = _chunk_to_content_blocks(chunk)
        if k == 0:
            header = HEADER_TEMPLATE.format(
                app_name=app_name,
                instruction=instruction[:2500],
                verifier_feedback=feedback[:2000],
                score=score, verdict=verdict,
                chunk_size=chunk_size,
            )
            user_messages.append(
                [{"type": "text", "text": header}] + chunk_blocks
            )
        else:
            user_messages.append(
                [{"type": "text",
                  "text": INTERMEDIATE_TEMPLATE.format(n=k+1, total=n_chunks)}]
                + chunk_blocks
            )
    # Final turn: ask for structured output
    user_messages.append([{"type": "text", "text": FINAL_PROMPT}])

    n_shots = sum(1 for m in user_messages for b in m if b.get("type") == "image")
    logger.info("[%s] calling %s — %d steps split into %d chunks × ~%d shots each (total %d shots, %d turns)",
                task_id, model, len(steps), n_chunks, chunk_size, n_shots, len(user_messages))

    last, result_event, texts = _call_claude_multiturn(user_messages, model=model)
    (output_dir / f"{task_id}.response.txt").write_text(
        "\n\n=====\n\n".join(f"--- assistant turn {k+1} ---\n{t}"
                              for k, t in enumerate(texts))
    )
    (output_dir / f"{task_id}.usage.json").write_text(json.dumps(
        {"cost_usd": result_event.get("total_cost_usd"),
         "usage": result_event.get("usage"),
         "n_assistant_turns": len(texts)}, indent=2))

    try:
        diag = _parse_json(last)
    except Exception as e:
        logger.error("[%s] failed to parse final JSON: %s", task_id, e)
        diag = {"primary_cause": "other",
                "summary": f"PARSE_ERROR: {e}",
                "ui_struggles": []}
    diag["task_id"] = task_id
    diag["score"] = score
    diag["verdict"] = verdict
    out_json.write_text(json.dumps(diag, indent=2))
    logger.info("[%s] %s — %s", task_id, diag.get("primary_cause"),
                (diag.get("summary", "") or "")[:120])
    return diag


def main() -> int:
    ap = argparse.ArgumentParser(description="Per-trajectory diagnoser (chunked multi-turn)")
    ap.add_argument("--rollouts-dir", required=True, type=Path)
    ap.add_argument("--tasks-dir", required=True, type=Path)
    ap.add_argument("--app-name", required=True)
    ap.add_argument("--output-dir", required=True, type=Path)
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--chunk-size", type=int, default=10,
                    help="Screenshots per chunk / per turn")
    ap.add_argument("--task-list", type=str, default=None)
    ap.add_argument("--include-passes", action="store_true")
    args = ap.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="[%(asctime)s %(levelname)s %(name)s] %(message)s")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    allowed = None
    if args.task_list:
        allowed = {t.strip() for t in args.task_list.split(",") if t.strip()}

    candidates: list[Path] = []
    for d in sorted(args.rollouts_dir.iterdir()):
        if not d.is_dir():
            continue
        if allowed is not None and d.name not in allowed:
            continue
        result = _load_result(d)
        if result is None:
            logger.info("skip %s (no result.json)", d.name); continue
        score = float(result.get("score", 0.0) or 0.0)
        if not args.include_passes and score >= 0.65:
            logger.info("skip %s (passed score=%.3f)", d.name, score); continue
        candidates.append(d)

    if not candidates:
        logger.error("no trajectories to diagnose"); return 1
    logger.info("diagnosing %d trajectories (parallel=%d, model=%s, chunk=%d)",
                len(candidates), args.parallel, args.model, args.chunk_size)

    diagnoses: list[dict] = []
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        futures = {pool.submit(_diagnose_one, d, args.tasks_dir, args.app_name,
                               args.output_dir, args.model, args.chunk_size): d
                   for d in candidates}
        for fut in as_completed(futures):
            d = futures[fut]
            try:
                diagnoses.append(fut.result())
            except Exception as e:
                logger.error("[%s] diagnose failed: %s", d.name, e)
                diagnoses.append({"task_id": d.name, "primary_cause": "other",
                                  "summary": f"DIAGNOSE_ERROR: {e}",
                                  "ui_struggles": []})

    summary = {"n_tasks": len(diagnoses), "by_cause": {},
               "tasks": sorted(diagnoses, key=lambda x: x.get("task_id", ""))}
    for d in diagnoses:
        c = d.get("primary_cause", "other")
        summary["by_cause"][c] = summary["by_cause"].get(c, 0) + 1
    (args.output_dir / "diagnoses_summary.json").write_text(json.dumps(summary, indent=2))
    logger.info("by_cause: %s", summary["by_cause"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
