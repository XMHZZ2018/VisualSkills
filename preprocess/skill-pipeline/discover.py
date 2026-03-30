"""Phase 1+2: Discover topics and organize into taxonomy.

Uses Claude's knowledge to draft an initial taxonomy for a domain,
then validates/enriches with YouTube search metadata.

Usage:
    python3 preprocess/skill-pipeline/discover.py --domain chrome
    python3 preprocess/skill-pipeline/discover.py --domain chrome --skip-youtube
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yt_dlp

from taxonomy import Taxonomy, TaxonomyNode

PIPELINE_DIR = Path(__file__).parent
DATA_DIR = PIPELINE_DIR / "data"

MAX_DEPTH = 3  # root=0, category=1, leaf=2

# ── Step 1: Claude drafts taxonomy ──────────────────────────────────────────

DRAFT_PROMPT = """\
You are building a knowledge taxonomy for the domain: "{domain}".

This taxonomy will be used to generate skills (step-by-step guides) that help
an AI agent perform desktop tasks in this domain.

Rules:
- Output a JSON tree with max depth 3 (root at depth 0, categories at depth 1, leaf topics at depth 2)
- Each leaf should be a single, actionable topic (something you could write a how-to guide for)
- Aim for 20-40 leaf topics — good coverage without being exhaustive
- Each node needs: "id" (slug), "name" (human-readable), "depth" (int)
- Each leaf also needs:
  - "description" (one sentence, what the guide would cover)
  - "search_queries" (array of 2-3 YouTube search query variants to find a tutorial for this topic — use different phrasings real users would type)
- Do NOT include "children", "signals", "skill_status", or "tasks" for leaves
- Internal nodes have "children" array

Output ONLY valid JSON, no markdown fences, no explanation.

Example structure:
{{
  "id": "{domain}",
  "name": "{domain_title}",
  "depth": 0,
  "children": [
    {{
      "id": "category-slug",
      "name": "Category Name",
      "depth": 1,
      "children": [
        {{
          "id": "topic-slug",
          "name": "Topic Name",
          "depth": 2,
          "description": "How to do X in {domain_title}",
          "search_queries": [
            "how to do X in {domain_title}",
            "{domain_title} X tutorial",
            "X {domain_title} step by step"
          ]
        }}
      ]
    }}
  ]
}}
"""


def draft_taxonomy_with_claude(domain: str) -> TaxonomyNode:
    """Use Claude to generate an initial taxonomy tree."""
    domain_title = domain.replace("-", " ").title()
    prompt = DRAFT_PROMPT.format(domain=domain, domain_title=domain_title)

    print(f"Asking Claude to draft taxonomy for '{domain}'...")
    result = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "json", "--model", "claude-sonnet-4-6"],
        capture_output=True, text=True, timeout=120,
    )

    if result.returncode != 0:
        print(f"Claude CLI failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    # Parse Claude's response — extract JSON from the result
    response = json.loads(result.stdout)
    text = response.get("result", result.stdout)

    # Try to extract JSON from the response
    # Claude may wrap it in markdown fences
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if json_match:
        tree_data = json.loads(json_match.group(1))
    else:
        # Try parsing the whole text as JSON
        tree_data = json.loads(text)

    root = TaxonomyNode.from_dict(tree_data)
    leaves = root.leaves()
    print(f"Claude drafted {len(leaves)} leaf topics across {len(root.children)} categories")
    return root


# ── Step 2: YouTube validation ──────────────────────────────────────────────

def search_youtube(query: str, max_results: int = 3) -> list[dict]:
    """Search YouTube and return video metadata (no download)."""
    ydl_opts = {"quiet": True, "no_warnings": True, "extract_flat": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
        results = []
        for entry in info.get("entries", []):
            if not entry:
                continue
            results.append({
                "title": entry.get("title", ""),
                "video_id": entry.get("id", ""),
                "duration": entry.get("duration"),
                "views": entry.get("view_count"),
                "channel": entry.get("channel") or entry.get("uploader", ""),
            })
        return results
    except Exception as e:
        print(f"  YouTube search failed: {e}")
        return []


def pick_best_video(all_results: list[dict]) -> dict | None:
    """Pick the best video from search results across multiple queries.

    Prefers: ≤10 min, highest view count, most relevant (earlier in results).
    """
    # Deduplicate by video_id
    seen = {}
    for r in all_results:
        vid = r.get("video_id")
        if vid and vid not in seen:
            seen[vid] = r

    candidates = list(seen.values())
    if not candidates:
        return None

    # Filter to ≤10 min
    short = [r for r in candidates if r.get("duration") and r["duration"] <= 600]
    pool = short if short else candidates

    # Sort by views (descending), take top
    pool.sort(key=lambda r: r.get("views") or 0, reverse=True)
    return pool[0]


def validate_with_youtube(root: TaxonomyNode, domain: str) -> list[str]:
    """For each leaf, search YouTube using multiple query variants and attach best signal.

    Also returns a list of new topics found on YouTube but missing from taxonomy.
    """
    leaves = root.leaves()
    domain_title = domain.replace("-", " ").title()
    new_topics = []

    print(f"\nValidating {len(leaves)} topics against YouTube...")

    for i, leaf in enumerate(leaves, 1):
        # Use search_queries if available, otherwise fall back to a default
        queries = leaf.search_queries
        if not queries:
            queries = [
                f"how to {leaf.name} in {domain_title}",
                f"{leaf.name} {domain_title} tutorial",
            ]

        print(f"  [{i:2d}/{len(leaves)}] {leaf.name} ({len(queries)} queries)...", end=" ", flush=True)

        # Search all query variants, collect all results
        all_results = []
        for q in queries:
            results = search_youtube(q)
            all_results.extend(results)

        best = pick_best_video(all_results)
        if best:
            leaf.signals.append(f"youtube:{best['video_id']}")
            dur = best.get("duration", 0)
            views = best.get("views") or 0
            print(f"✓ {best['title'][:50]}... ({dur // 60}m{dur % 60}s, {views:,} views)")
        else:
            print("✗ no videos")

    # Also do a few broad searches to find topics Claude may have missed
    broad_queries = [
        f"{domain_title} tips and tricks 2024",
        f"{domain_title} hidden features",
        f"{domain_title} settings you should change",
    ]

    existing_names = {leaf.name.lower() for leaf in leaves}

    print(f"\nBroad search for missed topics...")
    for query in broad_queries:
        results = search_youtube(query, max_results=5)
        for r in results:
            title = r["title"].lower()
            # Simple heuristic: if title mentions something not in our taxonomy
            # This is a rough signal — Claude will judge in the merge step
            if not any(name in title for name in existing_names):
                new_topics.append(r["title"])

    if new_topics:
        print(f"\nPotentially missed topics ({len(new_topics)}):")
        for t in new_topics[:10]:
            print(f"  - {t}")

    return new_topics


# ── Step 3: Merge new topics (if any) ──────────────────────────────────────

MERGE_PROMPT = """\
I have an existing taxonomy for "{domain}" and some potentially new topics
found on YouTube that might not be covered.

Current taxonomy leaves:
{existing_leaves}

Potentially new topics from YouTube:
{new_topics}

Which of these YouTube topics are genuinely new and should be added to the
taxonomy? For each one worth adding, provide:
- Which existing category (depth-1 node) it should go under
- A new leaf node with id, name, description

Rules:
- Only add topics that are genuinely missing (not already covered by an existing leaf)
- Max depth remains 3
- Output JSON array of additions, or empty array [] if nothing to add

Format:
[
  {{
    "parent_id": "existing-category-id",
    "node": {{
      "id": "new-topic-slug",
      "name": "New Topic Name",
      "depth": 2,
      "description": "What this topic covers"
    }}
  }}
]

Output ONLY valid JSON, no markdown fences.
"""


def merge_new_topics(root: TaxonomyNode, new_topics: list[str], domain: str) -> int:
    """Ask Claude to evaluate and merge new topics into the taxonomy."""
    if not new_topics:
        return 0

    existing_leaves = "\n".join(f"- {leaf.id}: {leaf.name}" for leaf in root.leaves())
    topics_str = "\n".join(f"- {t}" for t in new_topics[:20])

    prompt = MERGE_PROMPT.format(
        domain=domain,
        existing_leaves=existing_leaves,
        new_topics=topics_str,
    )

    print("\nAsking Claude to evaluate new topics...")
    result = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "json", "--model", "claude-sonnet-4-6"],
        capture_output=True, text=True, timeout=120,
    )

    if result.returncode != 0:
        print(f"Claude merge failed: {result.stderr}", file=sys.stderr)
        return 0

    response = json.loads(result.stdout)
    text = response.get("result", result.stdout)

    try:
        json_match = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", text, re.DOTALL)
        if json_match:
            additions = json.loads(json_match.group(1))
        else:
            # Try finding a JSON array in the text
            arr_match = re.search(r"\[.*\]", text, re.DOTALL)
            if arr_match:
                additions = json.loads(arr_match.group())
            else:
                additions = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        print(f"  Could not parse merge response, skipping")
        return 0

    added = 0
    for item in additions:
        parent = root.find(item["parent_id"])
        if parent and parent.depth < MAX_DEPTH - 1:
            new_node = TaxonomyNode.from_dict(item["node"])
            new_node.signals.append("youtube:broad-search")
            parent.children.append(new_node)
            print(f"  Added: {new_node.name} → {parent.name}")
            added += 1

    return added


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Discover and organize domain taxonomy")
    parser.add_argument("--domain", required=True, help="Domain name (e.g., 'chrome')")
    parser.add_argument("--skip-youtube", action="store_true", help="Skip YouTube validation")
    parser.add_argument("--output", help="Output path (default: data/<domain>/taxonomy.json)")
    args = parser.parse_args()

    domain = args.domain
    output_path = Path(args.output) if args.output else DATA_DIR / domain / "taxonomy.json"

    # Check if taxonomy already exists
    if output_path.exists():
        print(f"Taxonomy already exists at {output_path}")
        print("Loading existing taxonomy...")
        taxonomy = Taxonomy.load(output_path)
        taxonomy.print_tree()
        print(f"\n{len(taxonomy.leaves())} leaf topics")
        return

    # Step 1: Claude drafts taxonomy
    root = draft_taxonomy_with_claude(domain)
    print("\nDraft taxonomy:")
    print(root.pretty())

    # Step 2: YouTube validation
    if not args.skip_youtube:
        new_topics = validate_with_youtube(root, domain)

        # Step 3: Merge new topics
        added = merge_new_topics(root, new_topics, domain)
        if added:
            print(f"\nAdded {added} new topics from YouTube")
    else:
        print("\nSkipping YouTube validation")

    # Save
    taxonomy = Taxonomy(
        domain=domain,
        version=1,
        max_depth=MAX_DEPTH,
        root=root,
    )

    taxonomy.save(output_path)
    print(f"\nFinal taxonomy ({len(taxonomy.leaves())} leaves):")
    taxonomy.print_tree()
    print(f"\nSaved to {output_path}")


if __name__ == "__main__":
    main()
