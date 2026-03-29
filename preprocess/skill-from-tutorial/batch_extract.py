"""Batch extract sparse frames and convert VTT transcripts to markdown."""

import json
import re
from pathlib import Path

import cv2

ASSETS_DIR = Path(__file__).parent / "assets" / "searched"


def extract_sparse_frames(video_path: Path, output_dir: Path) -> dict:
    """Extract frames at auto-interval based on duration."""
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        return {"error": f"Could not open {video_path}"}

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0

    # Auto-interval based on duration
    if duration < 120:
        interval = 10
    elif duration < 600:
        interval = 20
    else:
        interval = 40

    num_frames = max(1, int(duration / interval))
    num_frames = min(num_frames, 200)

    step = total_frames / num_frames if num_frames < total_frames else 1
    frame_indices = [int(i * step) for i in range(num_frames)]

    output_dir.mkdir(parents=True, exist_ok=True)
    paths = []

    for i, frame_idx in enumerate(frame_indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            continue
        timestamp = frame_idx / fps if fps > 0 else 0
        img_name = f"frame_{i+1:04d}_t{int(timestamp)}s.png"
        img_path = output_dir / img_name
        cv2.imwrite(str(img_path), frame)
        paths.append(img_name)

    cap.release()
    return {
        "num_frames": len(paths),
        "duration": round(duration, 1),
        "interval": interval,
        "frames": paths,
    }


def vtt_to_markdown(vtt_path: Path) -> str:
    """Convert VTT subtitle file to clean markdown transcript."""
    text = vtt_path.read_text(encoding="utf-8", errors="replace")

    # Remove VTT header
    text = re.sub(r"^WEBVTT\n.*?\n\n", "", text, flags=re.DOTALL)

    lines = []
    current_time = None
    current_text = []

    for line in text.strip().split("\n"):
        line = line.strip()
        # Timestamp line
        ts_match = re.match(r"(\d{2}:\d{2}:\d{2}\.\d{3}) --> ", line)
        if ts_match:
            # Save previous block
            if current_text:
                clean = " ".join(current_text)
                # Remove HTML tags
                clean = re.sub(r"<[^>]+>", "", clean)
                if clean.strip():
                    lines.append(f"**[{current_time}]** {clean.strip()}")
            current_time = ts_match.group(1)[:8]  # HH:MM:SS
            current_text = []
        elif line and not re.match(r"^\d+$", line) and not line.startswith("NOTE"):
            current_text.append(line)

    # Last block
    if current_text:
        clean = " ".join(current_text)
        clean = re.sub(r"<[^>]+>", "", clean)
        if clean.strip():
            lines.append(f"**[{current_time}]** {clean.strip()}")

    # Deduplicate consecutive identical lines (common in auto-subs)
    deduped = []
    prev = None
    for line in lines:
        # Extract just the text part for comparison
        text_part = re.sub(r"\*\*\[.*?\]\*\* ", "", line)
        if text_part != prev:
            deduped.append(line)
            prev = text_part

    return "# Transcript\n\n" + "\n\n".join(deduped) + "\n"


def main():
    query_dirs = sorted(
        [d for d in ASSETS_DIR.iterdir() if d.is_dir() and (d / "video.mp4").exists()]
    )

    for i, query_dir in enumerate(query_dirs, 1):
        slug = query_dir.name
        frames_dir = query_dir / "frames"
        transcript_file = query_dir / "transcript.md"

        # Extract frames
        if list(frames_dir.glob("frame_*.png")) if frames_dir.exists() else False:
            print(f"[{i:2d}/{len(query_dirs)}] SKIP frames {slug}")
        else:
            video_path = query_dir / "video.mp4"
            result = extract_sparse_frames(video_path, frames_dir)
            if "error" in result:
                print(f"[{i:2d}/{len(query_dirs)}] ERROR {slug}: {result['error']}")
            else:
                print(f"[{i:2d}/{len(query_dirs)}] Frames {slug}: {result['num_frames']} frames ({result['duration']}s, every {result['interval']}s)")

        # Convert transcript
        if transcript_file.exists():
            print(f"         SKIP transcript (exists)")
        else:
            vtts = list(query_dir.glob("*.vtt"))
            if vtts:
                md = vtt_to_markdown(vtts[0])
                transcript_file.write_text(md)
                line_count = len(md.strip().split("\n"))
                print(f"         Transcript: {line_count} lines")
            else:
                print(f"         No VTT found")

    print("\nAll extractions complete.")


if __name__ == "__main__":
    main()
