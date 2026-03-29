"""Batch download selected YouTube videos for all queries."""

import json
import re
import subprocess
from pathlib import Path

ASSETS_DIR = Path(__file__).parent / "assets" / "searched"


def main():
    query_dirs = sorted(
        [d for d in ASSETS_DIR.iterdir() if d.is_dir() and (d / "search_results.md").exists()]
    )

    for i, query_dir in enumerate(query_dirs, 1):
        slug = query_dir.name

        # Skip if already downloaded
        if list(query_dir.glob("*.mp4")):
            print(f"[{i:2d}/{len(query_dirs)}] SKIP {slug} (video exists)")
            continue

        # Parse search_results.md for selected video URL and ID
        results_md = (query_dir / "search_results.md").read_text()
        url_match = re.search(r"- URL: (.+)", results_md)
        id_match = re.search(r"- Video ID: (.+)", results_md)

        if not url_match:
            print(f"[{i:2d}/{len(query_dirs)}] SKIP {slug} (no URL found)")
            continue

        url = url_match.group(1).strip()
        video_id = id_match.group(1).strip() if id_match else ""

        print(f"[{i:2d}/{len(query_dirs)}] Downloading: {slug}")
        print(f"         URL: {url}")

        output_path = query_dir / "video.mp4"
        cmd = [
            "yt-dlp",
            "--quiet", "--no-warnings",
            "-f", "best[height<=720][ext=mp4]/best[ext=mp4]/best",
            "-o", str(output_path),
            "--write-auto-subs", "--write-subs",
            "--sub-langs", "en",
            "--sub-format", "vtt",
            url,
        ]

        try:
            subprocess.run(cmd, timeout=120, capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            print(f"         TIMEOUT (file may still be usable)")

        # Check results
        if output_path.exists():
            size_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"         Done: {size_mb:.1f} MB")
        else:
            # yt-dlp may have added format extension
            mp4s = list(query_dir.glob("*.mp4"))
            if mp4s:
                size_mb = mp4s[0].stat().st_size / (1024 * 1024)
                print(f"         Done: {mp4s[0].name} ({size_mb:.1f} MB)")
            else:
                print(f"         FAILED: no mp4 found")

        # Check for subtitles
        vtts = list(query_dir.glob("*.vtt"))
        if vtts:
            print(f"         Subtitles: {vtts[0].name}")

    print("\nAll downloads complete.")


if __name__ == "__main__":
    main()
