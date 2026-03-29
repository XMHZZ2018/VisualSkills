# Extract and Summarize

## Step 3: Extract sparse frames and transcript

### 3a: Extract sparse frames (first pass)

Use `extract_frames` with the **default auto-interval** (not 1fps).
This gives ~1 frame per 10-20 seconds depending on video length — typically 6-15 frames.

Save frames to:
- `preprocess/skill-from-tutorial/assets/searched/<query-slug>/frames/`

### 3b: Extract transcript

The transcript was already downloaded by `download_youtube` (VTT subtitles).
Convert to markdown and save to:
- `preprocess/skill-from-tutorial/assets/searched/<query-slug>/transcript.md`

## Step 4: Summarize and identify key moments

### 4a: Read sparse frames + transcript

1. Read ALL sparse frames (only 6-15 images)
2. Read the transcript
3. Cross-reference to understand the full flow

### 4b: Write summary with key timestamps

Save to `preprocess/skill-from-tutorial/assets/searched/<query-slug>/summary.md`:

```markdown
# Video Summary: <title>

**Channel:** <channel>
**Duration:** <duration>
**URL:** <url>

## Key Moments

### 1. <description> (timestamp: Xs)
- What happened: <action taken>
- UI state: <what's visible>
- Frame: frame_NNNN_tXs.png (if a sparse frame captured this)
- **Needs precise frame: yes/no**

### 2. <description> (timestamp: Xs)
...
```

Focus on moments where:
- A **navigation action** was taken (clicked menu, opened settings page)
- A **target UI element** is visible (the setting to change, the button to click)
- A **verification state** is shown (confirmation, changed state)

### 4c: Extract precise frames (second pass, only if needed)

For key moments where the sparse frame doesn't clearly show the UI state,
use `extract_frame_at` targeted at that specific timestamp.

This is typically 3-5 additional frames, not hundreds.
