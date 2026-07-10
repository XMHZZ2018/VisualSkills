"""MCP server that exposes the libreoffice_writer skill via atomic topic loads.

Tools:
    load_topic(topic)  — return guide.md text + every adjacent figXX.png as one tool_result.
    list_topics()      — return all topic paths in this skill.

`topic` is a relative path from the skill root, e.g.
    "page-layout-basics/page-numbering"

Stdio MCP server, intended to be registered in mcp_config.json.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from mcp.server.fastmcp import FastMCP, Image

SKILL_ROOT = Path(__file__).resolve().parent.parent

# Figure references in guide.md are uniformly backtick-wrapped like `fig01.png`.
FIG_REF_RE = re.compile(r"`(fig\d+\.(?:png|jpe?g))`", re.IGNORECASE)


def _img(path: Path) -> Image:
    suffix = path.suffix.lstrip(".").lower()
    fmt = "jpeg" if suffix in ("jpg", "jpeg") else "png"
    return Image(data=path.read_bytes(), format=fmt)

mcp = FastMCP("writer-skill")


def _all_topics() -> list[str]:
    topics: list[str] = []
    for root, _dirs, files in os.walk(SKILL_ROOT, followlinks=True):
        if "guide.md" in files:
            rel = Path(root).relative_to(SKILL_ROOT)
            topics.append(str(rel))
    return sorted(topics)


@mcp.tool()
def list_topics() -> str:
    """List every topic path available in this skill.

    Each line is a topic path that can be passed to load_topic.
    """
    return "\n".join(_all_topics())


@mcp.tool()
def load_topic(topic: str) -> list:
    """Atomically load a topic's guide.md plus every adjacent figure image.

    Args:
        topic: relative path from the skill root, e.g.
            "page-layout-basics/page-numbering".

    Returns guide.md prose interleaved with the referenced figures, so each
    figure is delivered immediately after the sentence that mentions it
    (figures are referenced in the guide as `fig01.png` etc.). Any figures in
    the folder that are not referenced in the guide are appended at the end.
    Prefer this over Read for any *.md file inside this skill — it removes
    the need to issue separate Read calls for the figures.
    """
    topic = topic.strip().strip("/")
    # Reject path-escape attempts without resolving symlinks (each topic dir
    # is itself a symlink to the underlying mm-v1 skill, so .resolve() would
    # land outside SKILL_ROOT for every valid call).
    if ".." in Path(topic).parts:
        return [f"ERROR: topic path '{topic}' must not contain '..'."]
    folder = SKILL_ROOT / topic
    if not folder.is_dir():
        return [
            f"ERROR: topic '{topic}' not found. "
            f"Call list_topics() to see all valid topic paths."
        ]
    guide = folder / "guide.md"
    if not guide.exists():
        return [f"ERROR: no guide.md in topic '{topic}'."]

    text = guide.read_text(encoding="utf-8")
    figures = sorted(
        list(folder.glob("*.png"))
        + list(folder.glob("*.jpg"))
        + list(folder.glob("*.jpeg"))
    )
    fig_by_name = {f.name.lower(): f for f in figures}

    parts: list = []
    header = f"# {topic}/guide.md\n\n"
    cursor = 0
    emitted: set[str] = set()
    for m in FIG_REF_RE.finditer(text):
        chunk = text[cursor : m.end()]
        if cursor == 0:
            chunk = header + chunk
        parts.append(chunk)
        cursor = m.end()
        name = m.group(1).lower()
        fig = fig_by_name.get(name)
        if fig is not None and name not in emitted:
            parts.append(_img(fig))
            emitted.add(name)
    tail = text[cursor:]
    if cursor == 0:
        tail = header + tail
    if tail:
        parts.append(tail)
    # Fallback: any figures in the folder not referenced in the guide get
    # appended at the end so the agent still sees them.
    for fig in figures:
        if fig.name.lower() not in emitted:
            parts.append(_img(fig))
    return parts


if __name__ == "__main__":
    mcp.run()
