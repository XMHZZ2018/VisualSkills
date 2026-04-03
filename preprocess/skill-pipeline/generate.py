"""Phase 3: Generate skills from taxonomy.

For each leaf topic:
  1. Download video + transcript
  2. Extract coarse frames (every 5-10s)
  3. Claude generates text skill from transcript + coarse frames
  4. For multimodal: Claude writes guide and identifies key time ranges
  5. Extract fine frames (every 1-2s) within those ranges
  6. Claude picks best frame per range → final guide with embedded PNGs

Usage:
    python3 preprocess/skill-pipeline/generate.py --domain chrome --mode text
    python3 preprocess/skill-pipeline/generate.py --domain chrome --mode multimodal
    python3 preprocess/skill-pipeline/generate.py --domain chrome --mode both
    python3 preprocess/skill-pipeline/generate.py --domain chrome --node safe-browsing
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import yt_dlp

from taxonomy import Taxonomy, TaxonomyNode

PIPELINE_DIR = Path(__file__).parent
DATA_DIR = PIPELINE_DIR / "data"
MMSKILLS_ROOT = PIPELINE_DIR.parent.parent


def _skills_dir(domain: str, modality: str) -> Path:
    """Return the skills directory for a domain and modality."""
    return MMSKILLS_ROOT / "skills" / f"{domain}-knowledge-{modality}"

MAX_VIDEO_DURATION = 20 * 60  # 20 minutes max

FINE_INTERVAL = 1    # seconds between fine frames
FINE_WINDOW = 3      # seconds before/after the key timestamp


def coarse_interval_for_duration(duration: float) -> int:
    """Adaptive coarse sampling rate based on video duration.

    Shorter videos get higher sampling rate (more frames per second).
    Keeps total coarse frames roughly in the 20-40 range.
    """
    if duration < 60:       # <1 min  → every 2s  (~30 frames)
        return 2
    elif duration < 120:    # <2 min  → every 3s  (~40 frames)
        return 3
    elif duration < 300:    # <5 min  → every 5s  (~60 frames max)
        return 5
    elif duration < 600:    # <10 min → every 10s (~60 frames max)
        return 10
    else:                   # 10-20 min → every 20s (~60 frames max)
        return 20


# ── Video + Transcript ───────────────────────────────────────────────────────

def download_video(video_id: str, output_dir: Path) -> Path | None:
    """Download video at ≤720p + subtitles. Skips videos over MAX_VIDEO_DURATION."""
    output_dir.mkdir(parents=True, exist_ok=True)
    video_path = output_dir / "video.mp4"

    if video_path.exists():
        return video_path

    url = f"https://www.youtube.com/watch?v={video_id}"

    # Check duration first without downloading
    try:
        with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
            info = ydl.extract_info(url, download=False)
            duration = info.get("duration", 0)
            if duration > MAX_VIDEO_DURATION:
                print(f"TOO LONG ({duration // 60}m{duration % 60}s > {MAX_VIDEO_DURATION // 60}m)")
                return None
    except Exception:
        pass  # proceed anyway, duration check is best-effort

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "merge_output_format": "mp4",
        "writeautomaticsub": True,
        "writesubtitles": True,
        "subtitleslangs": ["en"],
        "subtitlesformat": "vtt",
        "outtmpl": str(output_dir / "video"),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        # yt-dlp may output video.mp4 or video.webm etc.
        if not video_path.exists():
            for f in output_dir.glob("video.*"):
                if f.suffix in (".mp4", ".mkv", ".webm"):
                    f.rename(video_path)
                    break
        return video_path if video_path.exists() else None
    except Exception as e:
        print(f"    Failed to download: {e}")
        return None


def parse_transcript(output_dir: Path) -> list[dict]:
    """Parse VTT transcript into list of {timestamp_sec, timestamp_str, text}."""
    vtt_path = None
    for f in output_dir.glob("*.vtt"):
        vtt_path = f
        break
    if not vtt_path:
        return []

    text = vtt_path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"^WEBVTT\n.*?\n\n", "", text, flags=re.DOTALL)

    def ts_to_sec(ts: str) -> float:
        parts = ts.split(":")
        h, m = int(parts[0]), int(parts[1])
        s = float(parts[2])
        return h * 3600 + m * 60 + s

    entries = []
    current_time_str = None
    current_time_sec = 0.0
    current_text = []

    for line in text.strip().split("\n"):
        line = line.strip()
        ts_match = re.match(r"(\d{2}:\d{2}:\d{2}\.\d{3}) --> ", line)
        if ts_match:
            if current_text:
                clean = re.sub(r"<[^>]+>", "", " ".join(current_text)).strip()
                if clean:
                    entries.append({
                        "timestamp_sec": current_time_sec,
                        "timestamp_str": current_time_str,
                        "text": clean,
                    })
            ts_str = ts_match.group(1)
            current_time_str = ts_str[:8]
            current_time_sec = ts_to_sec(ts_str)
            current_text = []
        elif line and not re.match(r"^\d+$", line) and not line.startswith("NOTE"):
            current_text.append(line)

    if current_text:
        clean = re.sub(r"<[^>]+>", "", " ".join(current_text)).strip()
        if clean:
            entries.append({
                "timestamp_sec": current_time_sec,
                "timestamp_str": current_time_str,
                "text": clean,
            })

    # Deduplicate consecutive identical text
    deduped = []
    prev = None
    for e in entries:
        if e["text"] != prev:
            deduped.append(e)
            prev = e["text"]

    return deduped


def format_transcript(entries: list[dict]) -> str:
    """Format transcript entries as readable text with timestamps."""
    lines = []
    for e in entries:
        lines.append(f"[{e['timestamp_str']}] {e['text']}")
    return "\n".join(lines)


# ── Frame Extraction ─────────────────────────────────────────────────────────

def get_video_duration(video_path: Path) -> float:
    cap = cv2.VideoCapture(str(video_path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return total / fps if fps > 0 else 0


def extract_coarse_frames(video_path: Path, output_dir: Path) -> tuple[list[dict], int]:
    """Extract frames at adaptive coarse interval based on video duration.

    Returns (frames_list, interval_used).
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        return [], 0

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0

    interval = coarse_interval_for_duration(duration)

    frames = []
    ts = 0.0
    idx = 0

    while ts < duration:
        frame_num = int(ts * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        if not ret:
            break

        idx += 1
        filename = f"coarse_{idx:03d}_t{int(ts)}s.png"
        cv2.imwrite(str(output_dir / filename), frame)
        frames.append({
            "filename": filename,
            "timestamp_sec": ts,
        })
        ts += interval

    cap.release()
    return frames, interval


def extract_fine_frames(
    video_path: Path,
    key_timestamps: list[float],
    output_dir: Path,
) -> dict[float, list[dict]]:
    """Extract fine-grained frames around each key timestamp.

    For each key timestamp, extract frames every FINE_INTERVAL second
    within [ts - FINE_WINDOW, ts + FINE_WINDOW].

    Returns: {key_ts: [frame_info, ...]}
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        return {}

    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) / fps if fps > 0 else 0

    result = {}

    for key_ts in key_timestamps:
        start = max(0, key_ts - FINE_WINDOW)
        end = min(duration, key_ts + FINE_WINDOW)
        fine_frames = []
        ts = start
        idx = 0

        while ts <= end:
            frame_num = int(ts * fps)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            ret, frame = cap.read()
            if not ret:
                break

            idx += 1
            filename = f"fine_t{int(key_ts)}s_{idx:02d}_at{ts:.1f}s.png"
            cv2.imwrite(str(output_dir / filename), frame)
            fine_frames.append({
                "filename": filename,
                "timestamp_sec": ts,
            })
            ts += FINE_INTERVAL

        result[key_ts] = fine_frames

    cap.release()
    return result


# ── Claude Calls ─────────────────────────────────────────────────────────────

def call_claude(prompt: str, timeout: int = 120) -> str | None:
    """Call Claude CLI and return the text response."""
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--output-format", "json", "--model", "claude-sonnet-4-6"],
            capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return None
    if result.returncode != 0:
        return None

    try:
        response = json.loads(result.stdout)
    except (json.JSONDecodeError, TypeError):
        return None
    text = response.get("result", "")

    # Strip markdown fences if present
    text = re.sub(r"^```(?:markdown|md|json)?\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text)
    return text


TEXT_SKILL_PROMPT = """\
You are generating a step-by-step guide for a desktop application task.

Topic: {topic_name}
Description: {topic_description}
Category: {category_name}

Here is the transcript from a YouTube tutorial on this topic:

{transcript}

Generate a concise, actionable guide in Markdown. Rules:
- Title should be "# {topic_name}"
- Write numbered steps (1. 2. 3. ...)
- Each step: one clear action ("Click ...", "Navigate to ...", "Select ...")
- Include exact menu paths where relevant (e.g., Format > Character > Font Effects)
- Keep it under 30 lines
- No fluff, no introduction, no conclusion — just the steps

Output ONLY the markdown guide, nothing else.
"""

# Pass 1: Claude sees coarse frames + transcript, writes a draft guide
# and identifies which steps need a screenshot (with approximate timestamps)
MM_COARSE_PROMPT = """\
You are generating a step-by-step guide with screenshots for a desktop application task.

Topic: {topic_name}
Description: {topic_description}
Category: {category_name}

Transcript from a tutorial video:

{transcript}

I have coarse screenshots from the video (one every {coarse_interval}s):
{coarse_frame_list}

Write a guide AND identify which steps need a screenshot. For each step that
needs a visual reference, specify the approximate video timestamp (in seconds)
where the best screenshot would be.

Output JSON with this structure:
{{
  "guide_steps": [
    {{
      "step": 1,
      "text": "Right-click the slide and select Slide Properties",
      "needs_screenshot": true,
      "timestamp_sec": 15
    }},
    {{
      "step": 2,
      "text": "In the Background tab, select Color from the dropdown",
      "needs_screenshot": true,
      "timestamp_sec": 45
    }},
    {{
      "step": 3,
      "text": "Click OK to apply",
      "needs_screenshot": false,
      "timestamp_sec": null
    }}
  ]
}}

Rules:
- 4-8 steps total
- Be VERY selective with screenshots — at most 2-3 per guide
- ONLY include a screenshot for steps where the UI element is genuinely hard to \
find (e.g., a buried menu, a dialog box, a color picker). Do NOT screenshot \
obvious actions like "click OK", "select text", or "press Ctrl+A"
- Too many screenshots distract the reader — fewer is better
- Timestamps should match moments from the coarse frames / transcript
- Each step text: one clear action
- Include exact menu paths where relevant (e.g., Format > Character > Font Effects)

Output ONLY valid JSON.
"""

# Pass 2: For each key timestamp, Claude picks the best fine frame
MM_FINE_PICK_PROMPT = """\
I need the best screenshot for this step in a Chrome tutorial:

Step: "{step_text}"

I have {num_fine} fine-grained frames extracted around timestamp {key_ts}s
(every {fine_interval}s within ±{fine_window}s):
{fine_frame_list}

Which frame filename best illustrates this step? Pick ONE frame that:
- Shows the relevant UI element clearly (button, menu, setting)
- Is not blurry or in transition
- Best matches the step description

Output ONLY the filename, nothing else.
"""


def generate_text_skill(
    leaf: TaxonomyNode,
    category_name: str,
    transcript_text: str,
    output_dir: Path,
) -> bool:
    """Generate text skill guide from transcript."""
    guide_path = output_dir / "guide.md"
    if guide_path.exists():
        return True

    prompt = TEXT_SKILL_PROMPT.format(
        topic_name=leaf.name,
        topic_description=leaf.description,
        category_name=category_name,
        transcript=transcript_text[:8000],
    )

    text = call_claude(prompt)
    if not text:
        return False

    output_dir.mkdir(parents=True, exist_ok=True)
    guide_path.write_text(text.strip() + "\n")
    return True


def generate_multimodal_skill(
    leaf: TaxonomyNode,
    category_name: str,
    transcript_text: str,
    coarse_frames: list[dict],
    coarse_interval: int,
    video_path: Path,
    frames_dir: Path,
    output_dir: Path,
) -> bool:
    """Generate multimodal skill using coarse-to-fine frame selection.

    Pass 1: Claude sees coarse frames + transcript → draft guide + key timestamps
    Pass 2: Extract fine frames around key timestamps → Claude picks best per step
    Pass 3: Assemble final guide.md with embedded PNGs
    """
    guide_path = output_dir / "guide.md"
    if guide_path.exists():
        return True

    # ── Pass 1: Coarse — identify key timestamps ──
    coarse_list = "\n".join(
        f"  - {f['filename']} (t={int(f['timestamp_sec'])}s)"
        for f in coarse_frames
    )

    prompt = MM_COARSE_PROMPT.format(
        topic_name=leaf.name,
        topic_description=leaf.description,
        category_name=category_name,
        transcript=transcript_text[:8000],
        coarse_interval=coarse_interval,
        coarse_frame_list=coarse_list,
    )

    response_text = call_claude(prompt, timeout=180)
    if not response_text:
        print("    Pass 1 (coarse) failed")
        return False

    try:
        guide_data = json.loads(response_text)
    except json.JSONDecodeError:
        # Try to extract JSON from response
        json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if json_match:
            guide_data = json.loads(json_match.group())
        else:
            print("    Failed to parse Pass 1 response")
            return False

    steps = guide_data.get("guide_steps", [])
    if not steps:
        print("    No steps in Pass 1 response")
        return False

    # Collect key timestamps that need screenshots
    key_timestamps = []
    for step in steps:
        if step.get("needs_screenshot") and step.get("timestamp_sec") is not None:
            key_timestamps.append(float(step["timestamp_sec"]))

    print(f"    Pass 1: {len(steps)} steps, {len(key_timestamps)} need screenshots")

    # ── Pass 2: Fine — extract and pick best frames ──
    output_dir.mkdir(parents=True, exist_ok=True)
    fine_dir = frames_dir / "fine"

    if key_timestamps:
        fine_frames_map = extract_fine_frames(video_path, key_timestamps, fine_dir)
    else:
        fine_frames_map = {}

    # For each step that needs a screenshot, pick the best fine frame
    step_screenshots = {}  # step_num → filename in output_dir

    for step in steps:
        if not step.get("needs_screenshot") or step.get("timestamp_sec") is None:
            continue

        key_ts = float(step["timestamp_sec"])
        fine_frames = fine_frames_map.get(key_ts, [])

        if not fine_frames:
            # Fallback: use nearest coarse frame
            nearest = min(coarse_frames, key=lambda f: abs(f["timestamp_sec"] - key_ts))
            src = frames_dir / nearest["filename"]
            dst_name = f"step{step['step']:02d}.png"
            if src.exists():
                shutil.copy2(src, output_dir / dst_name)
                step_screenshots[step["step"]] = dst_name
            continue

        if len(fine_frames) == 1:
            chosen_filename = fine_frames[0]["filename"]
        else:
            # Ask Claude to pick the best fine frame
            fine_list = "\n".join(
                f"  - {f['filename']} (t={f['timestamp_sec']:.1f}s)"
                for f in fine_frames
            )
            pick_prompt = MM_FINE_PICK_PROMPT.format(
                step_text=step["text"],
                num_fine=len(fine_frames),
                key_ts=int(key_ts),
                fine_interval=FINE_INTERVAL,
                fine_window=FINE_WINDOW,
                fine_frame_list=fine_list,
            )
            pick_result = call_claude(pick_prompt, timeout=120)

            # Match returned filename to actual files
            chosen_filename = None
            if pick_result:
                pick_clean = pick_result.strip()
                for f in fine_frames:
                    if f["filename"] in pick_clean:
                        chosen_filename = f["filename"]
                        break

            if not chosen_filename:
                # Fallback: pick the frame closest to key_ts
                chosen_filename = min(
                    fine_frames, key=lambda f: abs(f["timestamp_sec"] - key_ts)
                )["filename"]

        # Copy chosen frame to output dir
        src = fine_dir / chosen_filename
        dst_name = f"step{step['step']:02d}.png"
        if src.exists():
            shutil.copy2(src, output_dir / dst_name)
            step_screenshots[step["step"]] = dst_name

    print(f"    Pass 2: selected {len(step_screenshots)} fine frames")

    # ── Pass 3: Assemble final guide.md ──
    guide_lines = [f"# {leaf.name}\n"]

    for step in steps:
        step_num = step["step"]
        guide_lines.append(f"{step_num}. {step['text']}")
        if step_num in step_screenshots:
            png = step_screenshots[step_num]
            guide_lines.append(f"\n   ![Step {step_num}]({png})\n")

    guide_path.write_text("\n".join(guide_lines).strip() + "\n")
    return True


# ── SKILL.md index generation ───────────────────────────────────────────────

def generate_skill_index(taxonomy: Taxonomy, skills_dir: Path, is_multimodal: bool = False) -> None:
    """Generate SKILL.md index file from taxonomy."""
    domain_title = taxonomy.domain.replace("-", " ").title()
    skill_name = f"{taxonomy.domain}-knowledge"
    mm_note = " with screenshots" if is_multimodal else ""
    lines = [
        "---",
        f"name: {skill_name}",
        f"description: Step-by-step{mm_note} guides for common {domain_title} tasks. Read the relevant guide before performing a {domain_title} browser task.",
        "---\n",
        f"# {domain_title} Knowledge\n",
        f"Step-by-step{mm_note} guides for common {domain_title} tasks. Find the relevant topic below and read its guide for detailed instructions.\n",
        "| Category | Topic | Guide |",
        "|----------|-------|-------|",
    ]

    for cat in taxonomy.root.children:
        for leaf in cat.leaves():
            guide_rel = f"{cat.id}/{leaf.id}/guide.md"
            guide_path = skills_dir / guide_rel
            status = "✓" if guide_path.exists() else "—"
            lines.append(f"| {cat.name} | {leaf.name} | [{status}]({guide_rel}) |")

    skills_dir.mkdir(parents=True, exist_ok=True)
    (skills_dir / "SKILL.md").write_text("\n".join(lines) + "\n")


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_video_id(leaf: TaxonomyNode) -> str | None:
    """Extract YouTube video ID from leaf's signals."""
    for sig in leaf.signals:
        if sig.startswith("youtube:"):
            vid = sig.split(":", 1)[1]
            if vid and vid != "broad-search":
                return vid
    return None


def get_category(taxonomy: Taxonomy, leaf: TaxonomyNode) -> TaxonomyNode | None:
    """Find the category (depth-1) node that contains this leaf."""
    for cat in taxonomy.root.children:
        if cat.find(leaf.id):
            return cat
    return None


# ── Per-leaf processing ──────────────────────────────────────────────────────

def process_leaf(
    leaf: TaxonomyNode,
    category: TaxonomyNode,
    taxonomy: Taxonomy,
    mode: str,
    data_dir: Path,
    domain: str = "chrome",
) -> None:
    """Process a single leaf node."""
    video_id = get_video_id(leaf)
    if not video_id:
        print(f"  SKIP (no video ID)")
        return

    leaf_data_dir = data_dir / "videos" / leaf.id

    # ── Download video + transcript ──
    print(f"  Downloading video + transcript...", end=" ", flush=True)
    video_path = download_video(video_id, leaf_data_dir)
    if not video_path:
        print("FAILED")
        return
    print("OK")

    # ── Parse transcript ──
    entries = parse_transcript(leaf_data_dir)
    if not entries:
        print(f"  No transcript found")
        return
    transcript_text = format_transcript(entries)
    print(f"  Transcript: {len(entries)} entries")

    # ── Extract coarse frames ──
    frames_dir = leaf_data_dir / "frames"
    coarse_frames, coarse_interval = extract_coarse_frames(video_path, frames_dir)
    print(f"  Coarse frames: {len(coarse_frames)} (every {coarse_interval}s)")

    # ── Generate text skill ──
    if mode in ("text", "both"):
        text_dir = _skills_dir(domain, "text") / category.id / leaf.id
        print(f"  Generating text skill...", end=" ", flush=True)
        ok = generate_text_skill(leaf, category.name, transcript_text, text_dir)
        print("OK" if ok else "FAILED")

    # ── Generate multimodal skill (coarse-to-fine) ──
    if mode in ("multimodal", "both"):
        mm_dir = _skills_dir(domain, "multimodal") / category.id / leaf.id
        print(f"  Generating multimodal skill (coarse→fine)...")
        ok = generate_multimodal_skill(
            leaf, category.name, transcript_text,
            coarse_frames, coarse_interval, video_path, frames_dir, mm_dir,
        )
        print(f"  Multimodal: {'OK' if ok else 'FAILED'}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate skills from taxonomy")
    parser.add_argument("--domain", required=True, help="Domain (e.g., 'chrome')")
    parser.add_argument("--mode", choices=["text", "multimodal", "both"], default="both",
                        help="What to generate")
    parser.add_argument("--node", help="Process only this leaf node ID")
    parser.add_argument("--taxonomy", help="Path to taxonomy.json")
    args = parser.parse_args()

    tax_path = Path(args.taxonomy) if args.taxonomy else DATA_DIR / args.domain / "taxonomy.json"
    if not tax_path.exists():
        print(f"Taxonomy not found: {tax_path}")
        print("Run discover.py first.")
        sys.exit(1)

    taxonomy = Taxonomy.load(tax_path)
    data_dir = DATA_DIR / args.domain

    # Determine which leaves to process
    if args.node:
        leaf = taxonomy.find(args.node)
        if not leaf or not leaf.is_leaf:
            print(f"Leaf node '{args.node}' not found")
            sys.exit(1)
        leaves = [leaf]
    else:
        leaves = taxonomy.leaves()

    print(f"Processing {len(leaves)} topics in mode '{args.mode}'")
    print(f"Taxonomy: {tax_path}")
    print()

    for i, leaf in enumerate(leaves, 1):
        category = get_category(taxonomy, leaf)
        if not category:
            print(f"[{i:2d}/{len(leaves)}] SKIP {leaf.id} (no category)")
            continue

        print(f"[{i:2d}/{len(leaves)}] {category.name} / {leaf.name}")
        try:
            process_leaf(leaf, category, taxonomy, args.mode, data_dir, domain=args.domain)
            leaf.skill_status = "generated"
        except Exception as e:
            print(f"  ERROR: {e}")
            leaf.skill_status = "none"
        print()

    # Save updated taxonomy
    taxonomy.save(tax_path)

    # Generate SKILL.md index files
    if args.mode in ("text", "both"):
        generate_skill_index(taxonomy, _skills_dir(args.domain, "text"), is_multimodal=False)
        print(f"Text SKILL.md updated")
    if args.mode in ("multimodal", "both"):
        generate_skill_index(taxonomy, _skills_dir(args.domain, "multimodal"), is_multimodal=True)
        print(f"Multimodal SKILL.md updated")

    print(f"\nDone. {len(leaves)} topics processed.")


if __name__ == "__main__":
    main()
