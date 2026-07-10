Manage QGIS plugins via the Plugin Manager and automate tasks using the built-in Python console and code editor.

## Managing Plugins

### Opening the Plugin Manager

**Plugins → Manage and Install Plugins...**

The dialog has tabs across the top and a detail panel on the right. A search bar at the top filters by name, author, tag, or description.

### Installing a Plugin

1. Go to **Plugins → Manage and Install Plugins...**
2. Click the **All** tab to browse available plugins
3. Select a plugin — metadata (description, author, ratings, links) appears on the right
4. Click **Install Plugin** at the bottom right

To install from a ZIP file (e.g., downloaded directly from GitHub):
1. Click the **Install from ZIP** tab
2. Use the file selector to locate the `.zip` file
3. Click **Install Plugin**

### Enabling/Disabling Plugins

In the **Installed** tab, each plugin has a checkbox on its left. Uncheck to temporarily deactivate without uninstalling.

### Upgrading Plugins

- **Upgradeable** tab shows plugins with available updates
- Select a plugin → click **Upgrade Plugin**, or use **Upgrade All** to update everything at once

### Adding External Repositories

1. Open Plugin Manager → **Settings** tab
2. In the "Plugin Repositories" section, click **Add...**
3. Enter a name and URL (`http://` or `file://` protocol)

### Settings Tab Options

| Option | Effect |
|---|---|
| Check for Updates on Startup | Auto-checks every 3 days |
| Show also Experimental Plugins | Reveals early-stage, unstable plugins |
| Show also Deprecated Plugins | Shows grayed-out unmaintained plugins |

**Pitfall:** Experimental plugins are hidden by default. If a plugin you know exists isn't showing up, enable "Show also Experimental Plugins" in the Settings tab.

---

## Python Console

### Opening the Console

- **Plugins → Python Console** or `Ctrl + Alt + P`
- Or click the **Python Console** button in the Plugins toolbar

The panel has a toolbar at top, output area in the middle, and input line at the bottom.

### Running Commands

Type in the input area at the bottom and press **Enter** (or the Run Command button). Modules pre-imported and ready to use: `qgis.core`, `qgis.gui`, `qgis.analysis`, `PyQt5`, `math`, `os`, `re`, `sys`.

### Key Console Shortcuts

| Shortcut | Action |
|---|---|
| `Enter` | Run command |
| `Up` / `Down` arrows | Browse command history |
| `Ctrl + Alt + Space` | Trigger autocomplete |
| `Ctrl + Shift + Space` | Show full command history dialog |
| `Ctrl + E` | Execute selected text from output area |

### Special Console Commands

```python
?              # Show Python Console help
_api           # Open QGIS C++ API docs
_pyqgis        # Open QGIS Python API docs
_cookbook      # Open PyQGIS Cookbook
!shell_cmd     # Run a shell command (e.g., !gdalinfo --version)
var = !cmd     # Capture shell command output into a variable
```

---

## Code Editor

### Opening the Editor

Click **Show Editor** in the console toolbar. It opens as a panel alongside the console, with tabs for multiple scripts.

### Key Editor Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + S` | Save script |
| `Ctrl + Shift + S` | Save as new file |
| `Ctrl + Shift + E` | Run entire script |
| `Ctrl + E` | Run selected lines only |
| `Ctrl + Space` | Autocomplete |
| `Ctrl + :` | Toggle comment on selected lines |
| `Ctrl + Alt + F` | Reformat code |
| `Ctrl + 4` | Check syntax |
| `F1` | Context help for selected object |
| `Ctrl + G` / `Shift + Ctrl + G` | Find next / previous |

### Common Workflow: Write and Run a Script

1. Open console (`Ctrl + Alt + P`), then click **Show Editor**
2. Click **New editor** (+ button) to open a blank tab
3. Write your script — autocomplete works for PyQGIS APIs
4. Press `Ctrl + 4` to check syntax before running
5. Press `Ctrl + Shift + E` to run the whole script, or select lines and press `Ctrl + E` to run a portion
6. Output appears in the interactive console panel below

### Common Pitfalls

- **Running a script creates a `.pyc` file** next to it — expected behavior, not an error.
- **Autocomplete requires the setting to be enabled**: Options... dialog in the console toolbar → Python settings.
- **Object Inspector** (class/function browser) requires enabling "Run and Debug" in Python settings before it appears.
- **Shell commands via `!`** run in a subprocess; while running, the input area switches to STDIN mode. Press `Ctrl + C` to kill a hung subprocess.
- **Command history** is saved to `console_history.txt` in your active user profile folder — useful for recovering lost one-liners.