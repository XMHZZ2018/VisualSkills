# Search and Download

## Step 1: Search and select video

### 1a: Search YouTube

Use `search_youtube` with the query: `"$ARGUMENTS tutorial"`

### 1b: Filter by duration

From results, keep only videos with **duration ≤ 10 minutes**. Rank by relevance (title match to query, view count as tiebreaker).

### 1c: Select top 1

Pick the **best single video** based on:
- **Title**: how closely it matches the task description
- **View count**: higher is better (indicates quality)
- **Duration**: prefer concise videos that cover the task completely

### 1d: Log the selection

Write `preprocess/skill-from-tutorial/assets/searched/<query-slug>/search_results.md`:

```markdown
# Search Results

## Query
<original query>

## Candidates (≤10 min)
| # | Title | Channel | Duration | Views | URL |
|---|-------|---------|----------|-------|-----|
| 1 | ...   | ...     | ...      | ...   | ... |

## Selected
**<title>** — <why selected>
```

## Step 2: Download video

Use `download_youtube` for the selected video. Save to:

- `preprocess/skill-from-tutorial/assets/searched/<query-slug>/video.mp4`

Record the video ID and download path in `search_results.md`.
