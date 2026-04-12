Now I have a clear picture of all the icons. Here is the guide:

---

Manage QGIS plugins via the Plugin Manager and automate tasks using the built-in Python console and code editor.

## Managing Plugins

### Opening the Plugin Manager

Go to **Plugins > Manage and Install Plugins…**

Read the screenshot `fig01.png` in this directory — it shows the Plugin Manager toolbar icon (a puzzle piece), which also appears in the Plugins toolbar as a shortcut.

The Plugin Manager dialog opens with a left panel of tabs and a right panel showing plugin details.

### Browsing and Installing Plugins

The upper tabs filter plugins by state:
- **All** — every plugin in enabled repositories
- **Installed** — active plugins (core + user-installed)
- **Not installed** — available but not yet installed
- **Upgradeable** — installed plugins with newer versions available
- **New** — recently published since your last update check
- **Invalid** — broken plugins (dependency errors, API mismatches)

Use the **Search** box at the top to filter by name, author, tag, or description. Select a plugin to see its metadata (version, rating, homepage, author) in the right panel. Then click **Install**, **Upgrade Plugin**, or **Uninstall Plugin** at the bottom.

To temporarily disable a plugin without uninstalling, uncheck the checkbox next to its name in the list.

To install from a ZIP file (e.g. downloaded directly from a plugin's GitHub repo), use the **Install from ZIP** tab and browse to the `.zip` file.

### Configuring Plugin Settings

Click the **Settings** tab at the bottom of the left panel.

Read the screenshot `fig03.png` in this directory — it shows the Settings tab gear icon used to navigate to repository and update configuration.

Key options in the Settings tab:

- Read the screenshot `fig05.png` in this directory — it shows the checkbox for **Check for Updates on Startup**, which triggers automatic update checks at most every 3 days.
- Read the screenshot `fig07.png` in this directory — it shows the checkbox for **Show also Experimental Plugins**, which reveals early-stage plugins not suitable for production.
- Read the screenshot `fig09.png` in this directory — it shows the checkbox for **Show also Deprecated Plugins**, which reveals unmaintained plugins (shown grayed out in the list).

To add a third-party plugin repository: click the **Add…** button (Read the screenshot `fig11.png` in this directory — it shows the green plus Add icon) and enter a name and URL (`http://` or `file://`).

To edit an existing repository entry, click Read the screenshot `fig13.png` in this directory — it shows the Edit (pencil) icon. To remove one entirely, click Read the screenshot `fig15.png` in this directory — it shows the red Remove icon.

---

## Python Console

### Opening the Console

- **Menu**: **Plugins > Python Console**
- **Keyboard**: `Ctrl + Alt + P`
- **Toolbar**: click the Python Console icon in the Plugins toolbar

Read the screenshot `fig02.png` in this directory — it shows the Python file/snake icon used to open the console from the toolbar.

### Console Layout

The console has three parts: a **toolbar** at top, an **output area** in the middle, and an **input area** (`>>>` prompt) at the bottom.

Read the screenshot `fig04.png` in this directory — it shows the full Python Console panel with output area displaying example `iface.mapCanvas()` and `layer.name()` calls, and the `>>>` input prompt at the bottom.

### Console Toolbar

| Button | Function |
|--------|----------|
| Read `fig06.png` — broom icon | **Clear Console**: wipes the output area |
| Read `fig08.png` — green play icon | **Run Command**: executes input (same as `Enter`) |
| Read `fig10.png` — editor icon | **Show Editor**: toggles the code editor panel |
| Read `fig12.png` — wrench icon | **Options…**: configure console properties (auto-completion, fonts, etc.) |
| Read `fig14.png` — help icon | **Help…**: links to Python Console help, PyQGIS API docs, PyQGIS Cookbook |

### Input Area Features

- **Code completion**: `Ctrl + Alt + Space` opens the auto-completion list
- **Command history**: `Up`/`Down` arrows browse previous commands; `Ctrl + Shift + Space` opens the full history dialog (double-click to re-run)
- **Run selected output**: select text in the output area and press `Ctrl + E` to re-execute it
- **Shell commands**: prefix with `!` to run shell commands (e.g. `!gdalinfo --version`); assign output to a variable with `var = !cmd`
- **Special commands**:
  - `?` — Python Console help
  - `_api` — open QGIS C++ API docs
  - `_pyqgis` — open QGIS Python API docs
  - `_cookbook` — open PyQGIS Cookbook

QGIS modules (`qgis.core`, `qgis.gui`, `processing`, etc.) and Qt modules are pre-imported. Access the QGIS interface object via `iface`:

```python
>>> mc = iface.mapCanvas()
>>> layer = mc.currentLayer()
>>> layer.name()
'airports'
```

---

## Code Editor

### Opening the Editor

Click the **Show Editor** button (Read the screenshot `fig10.png` in this directory — pencil/editor icon) in the console toolbar. The editor panel opens to the right of or above the console.

### Working in the Editor

- Open multiple scripts simultaneously — each in its own tab
- Add a new tab with the **New editor** button (Read the screenshot `fig11.png` in this directory — green plus icon)
- The editor supports syntax highlighting, auto-indentation, parenthesis insertion, code commenting (`Ctrl + :`), and syntax checking (`Ctrl + 4`)

### Key Editor Shortcuts

| Action | Shortcut |
|--------|----------|
| Run entire script | `Ctrl + Shift + E` |
| Run selected lines | `Ctrl + E` |
| Save script | `Ctrl + S` |
| Save as | `Ctrl + Shift + S` |
| Find/replace | `Ctrl + F` (use regex option for pattern matching) |
| Reformat code | `Ctrl + Alt + F` |
| Context help | `F1` |
| Toggle comment | `Ctrl + :` |
| Auto-completion | `Ctrl + Space` |

Running a script from the editor (`Ctrl + Shift + E`) executes the full file in the interactive console and produces a compiled `.pyc` file. Use **Run selected** (`Ctrl + E`) to test individual code blocks without running the whole script.