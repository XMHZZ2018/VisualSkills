#!/usr/bin/env python3
"""Claude Code PreToolUse hook: enforce that every action tool call is
preceded by a <skill_check> block in the most recent assistant message.

Stdin payload (Claude Code PreToolUse format):
    {"tool_name": ..., "tool_input": ..., "transcript_path": ..., ...}

If the tool is an action tool and the last assistant message contains no
<skill_check>, exit code 2 → Claude Code blocks the call and feeds stderr
back to the model as the rejection reason.
"""
import json
import os
import sys

ACTION_TOOLS = {
    "mcp__gym-anything-controller__click",
    "mcp__gym-anything-controller__double_click",
    "mcp__gym-anything-controller__drag_to",
    "mcp__gym-anything-controller__hotkey",
    "mcp__gym-anything-controller__key_press",
    "mcp__gym-anything-controller__type_text",
    "mcp__gym-anything-controller__scroll",
    "mcp__osworld-controller__click",
    "mcp__osworld-controller__double_click",
    "mcp__osworld-controller__drag_to",
    "mcp__osworld-controller__hotkey",
    "mcp__osworld-controller__key_press",
    "mcp__osworld-controller__type_text",
    "mcp__osworld-controller__scroll",
}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    if data.get("tool_name") not in ACTION_TOOLS:
        sys.exit(0)

    transcript_path = data.get("transcript_path")
    if not transcript_path or not os.path.exists(transcript_path):
        sys.exit(0)

    # Walk the transcript and keep the text of the last assistant message.
    last_text = ""
    with open(transcript_path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if ev.get("type") != "assistant":
                continue
            msg_text_parts = []
            for c in ev.get("message", {}).get("content", []):
                t = c.get("type")
                if t == "thinking":
                    msg_text_parts.append(c.get("thinking", ""))
                elif t == "text":
                    msg_text_parts.append(c.get("text", ""))
            last_text = "".join(msg_text_parts)

    if "<skill_check>" in last_text:
        sys.exit(0)

    sys.stderr.write(
        "BLOCKED: action tool calls require a <skill_check> block in the "
        "immediately preceding assistant message. Output the block first "
        "(with relevant_guide, relevant_figure, already_loaded, reason) on "
        "its own line — using the exact <skill_check>...</skill_check> tag "
        "format — then retry the action.\n"
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
