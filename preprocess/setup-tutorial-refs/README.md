---
name: setup-tutorial-refs
description: Search YouTube for tutorial videos on a topic, download the top 3, extract frames at 1fps, get transcripts, and write 10-second chunk summaries. Run this before skill-from-tutorial. Requires youtube-tutorial MCP server.
---

Search YouTube for tutorial videos, download the best ones, extract frames, and summarize.

## Usage

```
/mmskills:setup-tutorial-refs <topic description>
```

**Arguments:**
- `$ARGUMENTS` — description of what you want to learn (e.g., "clear Chrome cookies and site data")

## MCP Tools Available

- **`youtube-tutorial`**: `search_youtube`, `download_youtube`, `extract_frames`

## Workflow

Detailed instructions for each step are in the companion files:
- `preprocess/skill-from-tutorial/search-and-download.md` — Steps 1–2
- `preprocess/skill-from-tutorial/extract-and-summarize.md` — Steps 3–4

### Step 1: Search and select videos

Follow `preprocess/skill-from-tutorial/search-and-download.md` → Step 1.

### Step 2: Download top 3 videos

Follow `preprocess/skill-from-tutorial/search-and-download.md` → Step 2.

### Step 3: Extract frames and transcripts

Follow `preprocess/skill-from-tutorial/extract-and-summarize.md` → Step 3.

### Step 4: Summarize each video

Follow `preprocess/skill-from-tutorial/extract-and-summarize.md` → Step 4.

## Output

After completion, `preprocess/skill-from-tutorial/assets/searched/` contains:
- `search_results.md` — search log and selection reasoning
- `index.md` — overview of all 3 videos with links
- `video_1/`, `video_2/`, `video_3/` — each containing:
  - `frames/` — 1fps extracted frames
  - `transcript.md` — full transcript
  - `summary.md` — 10-second chunk summaries
