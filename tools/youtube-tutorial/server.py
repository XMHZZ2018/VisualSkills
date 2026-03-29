"""
youtube-tutorial MCP server

Provides tools to search YouTube, download videos, and extract frames
for building text-based skills from video tutorials.
"""

import json
import math
import os
import subprocess
from pathlib import Path

import cv2
import yt_dlp
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("youtube-tutorial")


@mcp.tool()
def search_youtube(
    query: str,
    max_results: int = 5,
) -> str:
    """Search YouTube for tutorial videos and return metadata.

    Args:
        query: Search query (e.g., "how to use pytest fixtures tutorial")
        max_results: Maximum number of results to return (default 5)

    Returns:
        JSON list of video results with title, url, duration, channel, and description.
    """
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)

    results = []
    for entry in info.get("entries", []):
        if not entry:
            continue
        results.append({
            "title": entry.get("title", ""),
            "url": entry.get("url") or f"https://www.youtube.com/watch?v={entry.get('id', '')}",
            "video_id": entry.get("id", ""),
            "duration": entry.get("duration"),
            "duration_str": _format_duration(entry.get("duration")),
            "channel": entry.get("channel") or entry.get("uploader", ""),
            "view_count": entry.get("view_count"),
            "description": (entry.get("description") or "")[:500],
        })

    return json.dumps(results, indent=2)


@mcp.tool()
def download_youtube(
    url: str,
    output_dir: str = "/tmp/mmskills_tutorial",
) -> str:
    """Download a YouTube video to a local directory.

    Downloads the best quality video up to 720p to keep file sizes reasonable.

    Args:
        url: YouTube video URL (e.g., "https://www.youtube.com/watch?v=...")
        output_dir: Directory to save the video (default: /tmp/mmskills_tutorial)

    Returns:
        JSON with path, title, duration, and file size.
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    # Try to extract video ID from URL without network call
    video_id = ""
    if "v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]

    # Skip download if file already exists
    existing = [f for f in out.iterdir() if video_id and video_id in f.name and f.suffix == ".mp4"] if video_id else []
    if existing:
        filepath = existing[0]
        # Parse title from filename instead of fetching metadata
        info = {"id": video_id, "title": filepath.stem.rsplit("_", 1)[0], "duration": None}
    else:
        # Use subprocess with timeout to avoid hanging
        outtmpl = str(out / "%(title).80s_%(id)s.%(ext)s")
        cmd = [
            "yt-dlp",
            "--quiet", "--no-warnings",
            "-f", "best[height<=720][ext=mp4]/best[ext=mp4]/best",
            "-o", outtmpl,
            "--write-auto-subs", "--write-subs",
            "--sub-langs", "en",
            "--sub-format", "vtt",
            url,
        ]
        try:
            subprocess.run(cmd, timeout=120, capture_output=True)
        except subprocess.TimeoutExpired:
            pass  # File is likely already written

        # Find the downloaded file
        filepath = None
        for f in out.iterdir():
            if video_id in f.name and f.suffix == ".mp4":
                filepath = f
                break
        if filepath is None:
            filepath = out / f"video_{video_id}.mp4"

        info = {"id": video_id, "title": filepath.stem.rsplit("_", 1)[0] if filepath.exists() else "", "duration": None}

    filepath = Path(filepath)
    size_mb = filepath.stat().st_size / (1024 * 1024) if filepath.exists() else 0

    # Find subtitles (downloaded alongside video)
    transcript_path = None
    existing_vtt = [f for f in out.iterdir() if f.suffix == ".vtt"]
    if existing_vtt:
        transcript_path = str(existing_vtt[0].resolve())

    return json.dumps({
        "path": str(filepath.resolve()),
        "title": info.get("title", ""),
        "duration": info.get("duration"),
        "duration_str": _format_duration(info.get("duration")),
        "size_mb": round(size_mb, 1),
        "transcript_path": transcript_path,
    }, indent=2)


@mcp.tool()
def extract_frames(
    video_path: str,
    output_dir: str,
    num_frames: int | None = None,
    prefix: str = "frame",
) -> str:
    """Extract frames from a video at uniform intervals.

    Automatically determines the number of frames based on video duration
    if num_frames is not specified:
      - < 2 min: 1 frame every 10 seconds
      - 2-10 min: 1 frame every 20 seconds
      - 10-30 min: 1 frame every 40 seconds
      - 30-60 min: 1 frame every 60 seconds
      - > 60 min: 1 frame every 90 seconds

    Args:
        video_path: Path to the video file
        output_dir: Directory to save extracted frame images
        num_frames: Number of frames to extract (default: auto based on duration)
        prefix: Filename prefix for frames (default: "frame")

    Returns:
        JSON with list of frame paths, total frames extracted, and video duration.
    """
    video_path = Path(video_path)
    if not video_path.exists():
        return json.dumps({"error": f"Video not found: {video_path}"})

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        return json.dumps({"error": f"Could not open video: {video_path}"})

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0

    if num_frames is None:
        if duration < 120:
            interval = 10
        elif duration < 600:
            interval = 20
        elif duration < 1800:
            interval = 40
        elif duration < 3600:
            interval = 60
        else:
            interval = 90
        num_frames = max(1, int(duration / interval))

    # Cap at a reasonable maximum
    num_frames = min(num_frames, 200)

    # Calculate frame indices to extract
    if num_frames >= total_frames:
        frame_indices = list(range(total_frames))
    else:
        step = total_frames / num_frames
        frame_indices = [int(i * step) for i in range(num_frames)]

    image_paths = []
    timestamps = []

    for i, frame_idx in enumerate(frame_indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            continue

        timestamp = frame_idx / fps if fps > 0 else 0
        img_name = f"{prefix}_{i + 1:04d}_t{int(timestamp)}s.png"
        img_path = out / img_name
        cv2.imwrite(str(img_path), frame)
        image_paths.append(str(img_path.resolve()))
        timestamps.append(round(timestamp, 1))

    cap.release()

    return json.dumps({
        "frames": image_paths,
        "num_frames": len(image_paths),
        "video_duration": round(duration, 1),
        "video_duration_str": _format_duration(int(duration)),
        "fps": round(fps, 2),
        "timestamps": timestamps,
    }, indent=2)


@mcp.tool()
def extract_frame_at(
    video_path: str,
    output_dir: str,
    timestamps: list[float],
    prefix: str = "keyframe",
) -> str:
    """Extract frames at specific timestamps from a video.

    Use this for the second pass — after identifying key moments from
    sparse frames and transcripts, extract precise frames at those timestamps.

    Args:
        video_path: Path to the video file
        output_dir: Directory to save extracted frame images
        timestamps: List of timestamps in seconds to extract frames at
        prefix: Filename prefix for frames (default: "keyframe")

    Returns:
        JSON with list of frame paths and their timestamps.
    """
    video_path = Path(video_path)
    if not video_path.exists():
        return json.dumps({"error": f"Video not found: {video_path}"})

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        return json.dumps({"error": f"Could not open video: {video_path}"})

    fps = cap.get(cv2.CAP_PROP_FPS)
    image_paths = []
    actual_timestamps = []

    for ts in timestamps:
        frame_idx = int(ts * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            continue

        img_name = f"{prefix}_t{int(ts)}s.png"
        img_path = out / img_name
        cv2.imwrite(str(img_path), frame)
        image_paths.append(str(img_path.resolve()))
        actual_timestamps.append(round(ts, 1))

    cap.release()

    return json.dumps({
        "frames": image_paths,
        "num_frames": len(image_paths),
        "timestamps": actual_timestamps,
    }, indent=2)


def _format_duration(seconds):
    """Format seconds into human-readable duration."""
    if not seconds:
        return "unknown"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}h{m:02d}m{s:02d}s"
    return f"{m}m{s:02d}s"


if __name__ == "__main__":
    mcp.run()
