# Generate Skills

## Step 5: Generate both text and multimodal skills

### 5a: Synthesize across all queries

Read all query summaries and transcripts from `preprocess/skill-from-tutorial/assets/searched/<query-slug>/`:
- `summary.md` — key moments with visual descriptions and timestamps
- `transcript.md` — full spoken transcript

Cross-reference across all queries to:
- Group queries by **topic area** (e.g., settings, bookmarks, extensions, privacy)
- Identify **shared navigation patterns** (e.g., opening Settings, accessing chrome://flags)
- Pick the **clearest explanation** of each procedure from its tutorial
- Identify **common pitfalls** mentioned across tutorials

### 5b: Generate text-only skill

Create `skills/os-world/text/chrome-knowledge/SKILL.md`:

```markdown
---
name: chrome-knowledge
description: Comprehensive guide for Chrome browser tasks — settings, bookmarks, extensions, privacy, downloads, and more
---

# Chrome Knowledge

Reference guide for performing common Chrome browser tasks.

## Topics

### Settings & Preferences
- [Change default search engine](#change-default-search-engine)
- [Set homepage](#set-homepage)
- ...

### Bookmarks & Tabs
- [Restore closed tabs](#restore-closed-tabs)
- [Manage bookmarks](#manage-bookmarks)
- ...

### Privacy & Security
- [Clear cookies and cache](#clear-cookies-and-cache)
- ...

---

## Change Default Search Engine

### Steps
1. Open Chrome Settings (⋮ → Settings, or `chrome://settings`)
2. Click "Search engine" in the left sidebar
3. ...

### Verification
...

---

## Clear Cookies and Cache
...
```

**Text-only guidelines:**
- Translate visual demonstrations into concrete text instructions
- Include specific UI element names, menu paths, button labels
- Include specific URLs (e.g., `chrome://settings/searchEngines`)
- Must be **self-contained** — no references to videos or external resources
- One section per query/task, ordered by topic area

### 5c: Generate multimodal skill

Create `skills/os-world/multimodal/chrome-knowledge/SKILL.md` as a **structured index** with sub-guides:

```markdown
---
name: chrome-knowledge
description: Comprehensive guide for Chrome browser tasks with visual references — settings, bookmarks, extensions, privacy, downloads, and more
---

# Chrome Knowledge

Visual reference guide for performing common Chrome browser tasks.

## Sub-Guides

| Topic | Guide | Description |
|-------|-------|-------------|
| Settings | [settings.md](./settings.md) | Default search engine, homepage, startup behavior, appearance |
| Bookmarks & Tabs | [bookmarks-tabs.md](./bookmarks-tabs.md) | Bookmark management, tab restore, tab groups |
| Privacy & Security | [privacy.md](./privacy.md) | Cookies, cache, browsing data, site permissions |
| Extensions | [extensions.md](./extensions.md) | Install, manage, remove extensions |
| Downloads | [downloads.md](./downloads.md) | Download settings, save locations |
```

**Why sub-guides:** A single SKILL.md with 20+ procedures and embedded screenshots would be too large. Claude reads SKILL.md first (the index), then reads the relevant sub-guide based on the task.

Each sub-guide (e.g., `settings.md`) contains:

```markdown
# Chrome Settings Guide

## Change Default Search Engine

### Steps

1. Open Chrome Settings (⋮ → Settings, or `chrome://settings`)

2. Click "Search engine" in the left sidebar. The page should look like this:

![Search engine settings page](./settings_search_engine.png)

3. Click the dropdown next to "Search engine used in the address bar"
4. Select the desired search engine

### Verification

The selected search engine now appears in the dropdown.

---

## Set Homepage
...
```

**Frame selection and placement:**
- Copy selected frames from `preprocess/skill-from-tutorial/assets/searched/<query-slug>/frames/` to `skills/os-world/multimodal/chrome-knowledge/`
- Rename frames descriptively (e.g., `settings_search_engine.png`, `clear_cookies_dialog.png`)
- Embed at key checkpoints where UI state is important to verify
- Typically 1-3 frames per procedure (navigation, target, verification)

**Frame selection criteria:**
- Shows the exact UI state the user should see at that step
- Text is legible
- No overlapping dialogs or irrelevant popups

### 5d: Register in marketplace.json

Add both skill paths to plugin marketplace files:
- `plugins/osworld-text/.claude-plugin/marketplace.json` → add `./skills/os-world/text/chrome-knowledge`
- `plugins/osworld-multimodal/.claude-plugin/marketplace.json` → add `./skills/os-world/multimodal/chrome-knowledge`

### 5e: Report

Output:
- Paths to both generated skill files
- Summary of what the skill covers (grouped by topic area)
- Number of queries synthesized and frames selected
- Total size of multimodal skill (SKILL.md + sub-guides + images)
