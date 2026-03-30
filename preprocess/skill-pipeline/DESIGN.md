# Skill Pipeline v2 — Design

## Overview

Given a domain (e.g., "Chrome"), automatically discover what knowledge exists,
organize it into a taxonomy, generate skills, and evolve the taxonomy as new
tasks arrive.

```
  discover → organize → generate → evolve
                                     ↻ (loop back)
```

## Pipeline

### Phase 1: Discover

**Goal**: Collect raw topic signals from multiple sources for a domain.

**Sources** (3 sources, lightweight — metadata only, no video downloads):

| Source | What we fetch | Why |
|--------|--------------|-----|
| YouTube | Video titles, descriptions, view counts, duration | Rich how-to coverage, popularity signal |
| Google Support | Help article titles + section headings | Official feature taxonomy |
| Web search | Top "how to [domain]" article titles | Fills gaps YouTube/docs miss |

**How it works**:
1. Seed queries: `"Chrome settings tutorial"`, `"Chrome tips and tricks"`,
   `"Google Chrome how to"`, etc. (~10 seed queries per domain)
2. For each source, collect topic strings (titles/headings)
3. For YouTube: also save video ID, duration, view count (for Phase 3)
4. Output: `discovery.json` — flat list of raw topic signals with source metadata

```json
{
  "domain": "chrome",
  "signals": [
    {
      "text": "How to Enable Safe Browsing in Chrome",
      "source": "youtube",
      "meta": {"video_id": "abc123", "views": 50000, "duration": 180}
    },
    {
      "text": "Clear browsing data - Computer - Google Chrome Help",
      "source": "google_support",
      "meta": {"url": "https://support.google.com/chrome/answer/..."}
    },
    ...
  ]
}
```

**Implementation**: `discover.py --domain chrome`

---

### Phase 2: Organize

**Goal**: Cluster raw signals into a hierarchical taxonomy (max depth 3).

**How it works**:
1. Feed all signals from Phase 1 to Claude
2. Claude clusters, deduplicates, and organizes into a tree
3. Human reviews and adjusts (interactive)
4. Output: `taxonomy.json`

**Tree structure** (max depth 3: root → category → topic):

```
Chrome (root, depth 0)
├── Privacy & Security (depth 1)
│   ├── safe-browsing (depth 2, leaf)
│   ├── clear-browsing-data (leaf)
│   ├── do-not-track (leaf)
│   └── cookie-controls (leaf)
├── Appearance & Settings (depth 1)
│   ├── dark-mode (leaf)
│   ├── font-size (leaf)
│   ├── themes (leaf)
│   ├── default-search-engine (leaf)
│   └── language (leaf)
├── Bookmarks & Tabs (depth 1)
│   ├── add-bookmark (leaf)
│   ├── bookmark-folders (leaf)
│   ├── restore-closed-tab (leaf)
│   ├── tab-groups (leaf)
│   └── pin-tab (leaf)
├── Extensions (depth 1)
│   ├── install-from-store (leaf)
│   ├── install-unpacked (leaf)
│   └── manage-extensions (leaf)
├── Downloads & Files (depth 1)
│   ├── save-as-pdf (leaf)
│   ├── download-location (leaf)
│   └── desktop-shortcut (leaf)
├── Passwords & Autofill (depth 1)
│   ├── view-saved-passwords (leaf)
│   ├── autofill-settings (leaf)
│   └── payment-methods (leaf)
└── Google Services (depth 1)
    ├── sync-settings (leaf)
    ├── google-flights (leaf)
    └── google-translate (leaf)
```

**Depth constraint**: Max depth = 3 (root at 0, categories at 1, topics at 2).
When a SPLIT would exceed depth 3, widen the parent instead of deepening.

**taxonomy.json format**:

```json
{
  "domain": "chrome",
  "version": 1,
  "root": {
    "id": "chrome",
    "name": "Chrome",
    "children": [
      {
        "id": "settings",
        "name": "Settings",
        "children": [
          {
            "id": "privacy-security",
            "name": "Privacy & Security",
            "children": [
              {
                "id": "safe-browsing",
                "name": "Safe Browsing",
                "description": "Enable/configure Safe Browsing protection levels",
                "signals": ["youtube:abc123", "google_support:url1"],
                "skill_status": "none",
                "tasks": []
              }
            ]
          }
        ]
      }
    ]
  }
}
```

Each **leaf node** has:
- `id`: slug identifier
- `name`: human-readable name
- `description`: what this topic covers
- `signals`: references to discovery signals that mapped here
- `skill_status`: `"none"` | `"generated"` | `"refined"`
- `tasks`: list of OS World task IDs that map to this node (populated during Phase 4)

**Implementation**: `organize.py --domain chrome --input discovery.json`

---

### Phase 3: Generate

**Goal**: For each leaf node in the taxonomy, generate a skill (text + multimodal).

**How it works**:
1. Read taxonomy.json
2. For each leaf where `skill_status == "none"`:
   a. **Search** YouTube for the specific topic (fresh search, not reusing Phase 1)
      — Phase 1 gives breadth; Phase 3 needs the *best* tutorial per topic
   b. **Download** the best video
   c. **Extract** frames + transcript
   d. **Generate** skill (text guide.md + multimodal guide.md with screenshots)
3. Update `skill_status` to `"generated"` in taxonomy.json
4. Output: skill files in the standard directory structure

```
skills/os-world/text/chrome-knowledge/
├── SKILL.md                          # auto-generated index from taxonomy
├── privacy-security/
│   ├── safe-browsing/guide.md
│   ├── clear-browsing-data/guide.md
│   └── ...
├── appearance-settings/
│   ├── dark-mode/guide.md
│   └── ...
└── ...
```

The directory structure mirrors the taxonomy tree. SKILL.md is auto-generated
as an index table pointing to all leaf guides.

**Implementation**: `generate.py --domain chrome --taxonomy taxonomy.json`

Can also target specific nodes: `generate.py --node safe-browsing`

---

### Phase 4: Evolve

**Goal**: When new tasks arrive, classify them into the taxonomy and update
the tree as needed.

#### Algorithm: Incremental Taxonomy Evolution

Inspired by COBWEB (concept formation) — a tree where each new example is
classified top-down, and the tree adapts via 4 operations:

```
evolve(task, node):
    1. CLASSIFY: find best-matching leaf via top-down traversal
    2. EVALUATE: does the leaf's skill cover this task?
    3. ACT: based on the evaluation, do one of:
       - ABSORB:  task fits well → add task ID to node, optionally refine skill
       - CREATE:  task doesn't fit any child → add a new leaf node
       - SPLIT:   node has become too broad → split into sub-nodes
       - MERGE:   two sibling nodes are redundant → merge into one
    4. REGENERATE: if tree changed, regenerate affected skills
```

#### Operations in detail

**CLASSIFY** — Top-down traversal using Claude as semantic matcher:
```
Given node with children [A, B, C], ask Claude:
  "Which child best matches this task? Or none?"
Recurse into best match until reaching a leaf.
```

**ABSORB** — Task fits the leaf:
```
- Append task_id to leaf's tasks[]
- If task reveals a gap in the existing skill (e.g., the skill describes
  the GUI path but the task requires a specific flag/option not mentioned),
  refine the skill with additional detail
- skill_status → "refined"
```

**CREATE** — No existing leaf fits:
```
- Add a new leaf node under the most relevant parent
- Set skill_status = "none" (triggers Phase 3 for this node)
- Example: task "enable Chrome reading mode" → no leaf exists
  → create "reading-mode" under "Settings > Appearance"
```

**SPLIT** — A leaf has accumulated diverse tasks that need different skills:
```
- Replace leaf with child nodes (only if depth < max_depth)
- If already at max depth (3), widen the parent instead: add sibling leaves
- Redistribute existing tasks to new children
- Example: "privacy-security" leaf has tasks about safe browsing,
  cookie blocking, AND incognito mode → split into 3 sibling leaves
- Trigger condition: Claude judges that the node's tasks are
  internally dissimilar (or node.tasks > threshold, e.g., 5)
```

**MERGE** — Two siblings are too similar:
```
- Combine two leaf nodes into one
- Union their tasks, combine their skills
- Example: "add-bookmark" and "bookmarks-bar" → "bookmark-management"
- Trigger condition: Claude judges two siblings have high overlap
```

#### When to evolve

Three modes:

1. **On-demand**: `evolve.py --task "Enable reading mode in Chrome"`
   Process a single task description.

2. **Batch post-eval**: `evolve.py --eval-results workspaces/claude-opus-4-6/skill-multimodal/`
   After an evaluation run, process all tasks — especially failures — to
   identify taxonomy gaps.

3. **Continuous**: Feed tasks one-by-one, tree evolves incrementally.
   This is the COBWEB-style operation.

#### Evolution log

Every operation is logged for auditability:

```json
{
  "version": 2,
  "operations": [
    {
      "op": "CREATE",
      "parent": "settings.appearance",
      "new_node": "reading-mode",
      "reason": "Task 'enable reading mode' has no matching leaf",
      "task_id": "abc-123"
    },
    {
      "op": "SPLIT",
      "node": "privacy-security",
      "into": ["safe-browsing", "clear-data", "cookie-controls"],
      "reason": "Node accumulated 6 diverse tasks"
    }
  ]
}
```

---

## File layout

```
preprocess/skill-pipeline/
├── DESIGN.md              # This file
├── discover.py            # Phase 1: multi-source topic discovery
├── organize.py            # Phase 2: build taxonomy tree (interactive w/ Claude)
├── generate.py            # Phase 3: generate skills for leaf nodes
├── evolve.py              # Phase 4: classify tasks + adapt taxonomy
├── taxonomy.py            # Shared: taxonomy tree data structure + operations
└── data/
    └── <domain>/
        ├── discovery.json     # Phase 1 output
        ├── taxonomy.json      # Phase 2 output (living document)
        ├── evolution_log.json # Phase 4 audit trail
        └── videos/            # Phase 3 downloads (gitignored)
```

---

## Example walkthrough

### Initial build

```bash
# 1. Discover topics for Chrome
python3 preprocess/skill-pipeline/discover.py --domain chrome

# 2. Organize into taxonomy (Claude-assisted, interactive)
python3 preprocess/skill-pipeline/organize.py --domain chrome

# 3. Generate skills for all leaf nodes
python3 preprocess/skill-pipeline/generate.py --domain chrome

# 4. Run evaluation
python3 scripts/run-osworld/run.py --domain chrome --skill_mode multimodal
```

### Evolution after evaluation

```bash
# Feed evaluation results back into taxonomy
python3 preprocess/skill-pipeline/evolve.py \
    --domain chrome \
    --eval-results workspaces/claude-opus-4-6/skill-multimodal/chrome/

# Output:
#   ABSORB: 15 tasks matched existing leaves
#   CREATE: 2 new leaves (reading-mode, chrome-flags)
#   SPLIT:  1 node split (privacy → safe-browsing, clear-data, tracking)
#   taxonomy.json updated to version 2
#
# Generate skills for new/changed nodes:
python3 preprocess/skill-pipeline/generate.py --domain chrome --only-new
```

---

## Design decisions

**Why separate discover from generate video search?**
Phase 1 casts a wide net (breadth) to understand what topics exist.
Phase 3 does a focused search per topic (depth) to find the *best* tutorial.
A video that's great for discovering that "tab groups" is a topic might not
be the best tutorial for learning tab groups.

**Why COBWEB-style evolution?**
The 4 operations (absorb/create/split/merge) are exactly the right primitives
for maintaining a taxonomy that grows with new data. Unlike static clustering,
it handles:
- New topics that didn't exist at discovery time
- Topics that turn out to be too coarse or too fine-grained
- Redundancy that only becomes apparent after seeing tasks

**Why Claude as the semantic judge?**
Classification, split/merge decisions, and skill refinement all require
semantic understanding. Embedding similarity could work for classification,
but split/merge decisions need reasoning about what constitutes a coherent
topic. Claude is the natural fit.

**Why 3 levels max?**
Deeper trees make classification harder and skills too narrow.
Shallower trees make skills too broad to be useful.
3 levels balances specificity with manageability.
