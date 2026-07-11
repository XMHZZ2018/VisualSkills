# Setup Fix Guide for CUA-World Environments

When adding a new software domain to CUA-World, the per-task `setup_task.sh` scripts often have common bugs that prevent Claude from starting work immediately. This guide documents the issues we found and fixed, so you can proactively check for them in any domain.

## Architecture Recap

```
Base Docker image (shared across all envs)
  └─ install_<software>.sh   (pre_start hook — installs the software)
  └─ setup_<software>.sh     (post_start hook — configures preferences, creates shortcuts)
  └─ tasks/<task>/setup_task.sh  (pre_task hook — creates data files, opens the software)
  └─ tasks/<task>/verifier.py    (post-task — checks the result)
```

All tasks in one domain share the same base + install + setup. The only per-task difference is `setup_task.sh`. Most bugs live there, but shared utilities in `task_utils.sh` affect all tasks.

## Common Issues and Fixes

### 1. Splash screen detected as ready (most critical)

**Symptom**: First 1-3 screenshots show a splash screen or loading bar instead of the actual application window. Claude wastes steps waiting for the software to finish opening.

**Root cause**: The `wait_for_ready()` function checks `wmctrl -l` for a window matching the app name, but many apps show a **splash screen** that also matches. For example:
- LibreOffice splash screen title: `"LibreOffice"`
- Actual document window title: `"myfile.ods — LibreOffice Calc"`

If you grep for `"LibreOffice"`, the splash matches and the function returns "ready" too early.

**Fix**: The readiness check must grep for a pattern that ONLY matches the actual document window, not the splash. Identify what's different between the splash title and the real window title, then match on that difference.

```bash
wait_for_app_ready() {
    local timeout=${1:-120}
    local elapsed=0

    # 1) Wait for process
    while [ $elapsed -lt 30 ]; do
        pgrep -f "$PROCESS_NAME" > /dev/null && break
        sleep 1; elapsed=$((elapsed + 1))
    done

    # 2) Wait for the ACTUAL document window (not splash screen).
    #    Use a pattern that distinguishes the real window from the splash.
    #    Examples:
    #      LibreOffice: splash = "LibreOffice", real = "file.ods — LibreOffice Calc"
    #        -> match on "(Calc|Untitled| — )"
    #      GIMP: splash = "GIMP", real = "image.png – GIMP"
    #        -> match on "( – |Untitled)"
    #    Always check wmctrl -l output for your app to identify the right pattern.
    while [ $elapsed -lt $timeout ]; do
        local wlist=$(DISPLAY=:1 wmctrl -l 2>/dev/null || true)
        if echo "$wlist" | grep -qiE "$DOCUMENT_WINDOW_PATTERN"; then
            sleep 3  # buffer for full render
            return 0
        fi
        sleep 1; elapsed=$((elapsed + 1))
    done
    return 1
}
```

**How to find the right pattern**: Launch the app manually inside a container, and run `wmctrl -l` repeatedly during loading. Note the title at each stage. Pick a pattern that only matches the final (document-open) stage.

### 2. Window not maximized

**Symptom**: Application window only covers part of the screen. Claude wastes actions or has trouble reading truncated content.

**Fix**: Use `wmctrl` to maximize after the window is ready:

```bash
maximize_window() {
    local wid=$(DISPLAY=:1 wmctrl -l | grep -i "$APP_NAME" | awk '{print $1; exit}')
    if [ -n "$wid" ]; then
        DISPLAY=:1 wmctrl -ia "$wid"          # activate
        sleep 0.3
        DISPLAY=:1 wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz
        sleep 0.5
    fi
}
```

**Common mistake**: Using `xdotool key F11` — this toggles **fullscreen** mode in many apps (which hides the menu bar), not maximize. Always use `wmctrl` instead.

### 3. Two grep patterns needed: broad for finding, specific for readiness

Window title grep patterns serve two different purposes — don't confuse them:

| Purpose | When to use | Pattern style | Example |
|---------|------------|---------------|---------|
| **Find/maximize window** (`get_window_id`, `maximize`) | After app is ready | Broad — match any state | `"LibreOffice"` |
| **Readiness check** (`wait_for_ready`) | During loading | Specific — exclude splash | `"(Calc\|Untitled\| — )"` |

Using the broad pattern for readiness checks is the #1 cause of the splash screen bug (Issue #1).

### 4. First-run dialogs and banners

**Symptom**: "What's new", "Tip of the Day", "Release Notes", license agreements, or other first-run dialogs appear and waste Claude's time or block interaction.

**Fix options** (try in order):
1. **Config file**: Set preferences in the app's config during `setup_<software>.sh` to suppress first-run dialogs. Look for settings like `ShowTipOfTheDay`, `ooSetupLastVersion`, `FirstRun`, etc.
2. **Pre-launch trick**: Launch the app once headlessly during `setup_<software>.sh` to trigger the "first run" state, then kill it. The actual per-task launch won't show the dialog.
3. **Dismiss via xdotool**: As a last resort, after maximize, click the close button or press Escape:
   ```bash
   su - ga -c "DISPLAY=:1 xdotool mousemove <X> <Y> click 1"
   ```
   Find the coordinates by taking a screenshot with the dialog visible.

### 5. File format triggers import dialog

**Symptom**: Opening a CSV, TSV, or other text file shows a "Text Import" dialog that blocks the application.

**Root cause**: The `setup_task.sh` creates a CSV file and opens it with the application. Many spreadsheet apps show an import dialog for CSV files.

**Fix options**:
1. **Convert to native format** during setup (preferred):
   ```bash
   libreoffice --headless --convert-to ods --outdir /home/ga/Documents file.csv
   ```
2. **Pre-configure import settings** in the app's config to auto-accept defaults.
3. **Use native format from the start** — have the setup script generate ODS/XLSX directly instead of CSV.

### 6. pip install fails on Ubuntu 24.04+

**Symptom**: `install_<software>.sh` fails with `externally-managed-environment` error.

**Root cause**: PEP 668 — Ubuntu 24.04 blocks system-wide pip installs by default.

**Fix**: Add `--break-system-packages` to all `pip3 install` commands:
```bash
pip3 install --break-system-packages --no-cache-dir <packages>
```

## Setup Script Structure

Every `setup_task.sh` should follow this pattern:

```bash
#!/bin/bash
source /workspace/scripts/task_utils.sh

# 1. Create data files
python3 << 'EOF'
# ... generate data files ...
EOF

# 2. Open in the application
su - ga -c "DISPLAY=:1 <app> <file> &"

# 3. Wait for ACTUAL document window (not splash)
wait_for_app_ready 120

# 4. Maximize
maximize_window

# 5. Dismiss any first-run dialogs (if needed)
```

## Cache Considerations

**Do NOT use `use_cache: true` for systemd/desktop environments.** Docker checkpoint/restore breaks the X11 display session — GDM doesn't restart properly after restore, so the container has no working display. All screenshot/interaction will fail silently.

Set `use_cache: false` in your eval config for any environment that uses a desktop (LibreOffice, GIMP, LibreCAD, diagrams.net, etc.). The extra ~1-2 min for `install_<software>.sh` on each run is worth having a working display.

If you already have a broken checkpoint, delete it:

```bash
docker rmi ga-checkpoint/<env_name>:0.1-pre_start
```

Note: Read-only mounted scripts (`setup_<software>.sh`, `task_utils.sh`) always reflect host changes regardless of cache — they are not part of the checkpoint.
