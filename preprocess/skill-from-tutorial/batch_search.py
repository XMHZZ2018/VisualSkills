"""Batch search YouTube for all 20 Chrome task queries and save results."""

import json
import re
from pathlib import Path

import yt_dlp

ASSETS_DIR = Path(__file__).parent / "assets" / "searched"

QUERIES = [
    "how to make Bing default search engine in Chrome",
    "how to clear specific website cookies in Chrome",
    "how to restore last closed tab in Chrome",
    "how to save webpage as PDF in Chrome",
    "how to create desktop shortcut from Chrome",
    "how to create bookmark folder on bookmarks bar in Chrome",
    "how to bookmark a page to bookmarks bar in Chrome",
    "how to change Chrome profile name",
    "how to disable Chrome Refresh 2023 UI flags",
    "how to change default font size in Chrome",
    "how to change Chrome interface language",
    "how to auto delete browsing data when closing Chrome",
    "how to view saved passwords in Chrome",
    "how to install unpacked extension in Chrome developer mode",
    "how to disable dark mode in Chrome",
    "how to change number of Google search results per page",
    "how to remove startup page in Chrome",
    "how to enable Do Not Track in Chrome",
    "how to enable safe browsing in Chrome",
    "how to use Google Flights to find flights",
]


def slugify(query: str) -> str:
    """Convert query to directory slug."""
    # Remove "how to" prefix and "in Chrome" suffix for cleaner slugs
    s = query.lower()
    s = re.sub(r"^how to ", "", s)
    s = re.sub(r" in chrome.*$", "", s)
    s = re.sub(r" from chrome.*$", "", s)
    s = re.sub(r" on chrome.*$", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def search_youtube(query: str, max_results: int = 5) -> list[dict]:
    ydl_opts = {"quiet": True, "no_warnings": True, "extract_flat": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch{max_results}:{query} tutorial", download=False)

    results = []
    for entry in info.get("entries", []):
        if not entry:
            continue
        duration = entry.get("duration")
        results.append({
            "title": entry.get("title", ""),
            "url": entry.get("url") or f"https://www.youtube.com/watch?v={entry.get('id', '')}",
            "video_id": entry.get("id", ""),
            "duration": duration,
            "channel": entry.get("channel") or entry.get("uploader", ""),
            "view_count": entry.get("view_count"),
        })
    return results


def pick_best(results: list[dict]) -> dict | None:
    """Pick best video: duration ≤ 10min, ranked by relevance then views."""
    candidates = [r for r in results if r.get("duration") and r["duration"] <= 600]
    if not candidates:
        # Fallback: take shortest video
        candidates = sorted(results, key=lambda r: r.get("duration") or 9999)
        return candidates[0] if candidates else None
    # First result is most relevant (YouTube's ranking), use views as tiebreaker
    return candidates[0]


def format_duration(seconds: int | None) -> str:
    if not seconds:
        return "?"
    m, s = divmod(int(seconds), 60)
    return f"{m}:{s:02d}"


def main():
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    index_lines = ["# Search Index\n"]

    for i, query in enumerate(QUERIES, 1):
        slug = slugify(query)
        query_dir = ASSETS_DIR / slug
        results_file = query_dir / "search_results.md"

        # Skip if already searched
        if results_file.exists():
            print(f"[{i:2d}/20] SKIP {slug} (already searched)")
            index_lines.append(f"- [{slug}](./{slug}/search_results.md)")
            continue

        print(f"[{i:2d}/20] Searching: {query}")
        results = search_youtube(query)

        if not results:
            print(f"         No results found!")
            continue

        selected = pick_best(results)
        query_dir.mkdir(parents=True, exist_ok=True)

        # Write search_results.md
        md = f"# Search Results\n\n## Query\n{query}\n\n"
        md += "## Candidates (≤10 min)\n"
        md += "| # | Title | Channel | Duration | Views | URL |\n"
        md += "|---|-------|---------|----------|-------|-----|\n"
        for j, r in enumerate(results, 1):
            dur = format_duration(r["duration"])
            views = f"{r['view_count']:,}" if r.get("view_count") else "?"
            md += f"| {j} | {r['title']} | {r['channel']} | {dur} | {views} | {r['url']} |\n"

        if selected:
            md += f"\n## Selected\n**{selected['title']}** — top relevant result under 10 min\n"
            md += f"- URL: {selected['url']}\n"
            md += f"- Video ID: {selected['video_id']}\n"
            md += f"- Duration: {format_duration(selected['duration'])}\n"

        results_file.write_text(md)
        print(f"         Selected: {selected['title'][:60]}... ({format_duration(selected['duration'])})")

        index_lines.append(f"- [{slug}](./{slug}/search_results.md)")

    # Write index
    (ASSETS_DIR / "index.md").write_text("\n".join(index_lines) + "\n")
    print("\nDone! Index written to assets/searched/index.md")


if __name__ == "__main__":
    main()
