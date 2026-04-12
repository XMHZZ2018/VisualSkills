Here is the multimodal skill guide:

---

Configure QGIS global preferences, project coordinate reference systems, and CRS handling behavior through the Settings menu and Project Properties dialog.

## Settings Menu Overview

All major configuration tools live under **Settings** in the menu bar:

- **Style Manager…** — create/manage symbols, styles, color ramps
- **Custom Projections…** — define your own CRS
- **Keyboard Shortcuts…** — reassign or add shortcuts
- **Interface Customization…** — hide dialogs and tools you don't need
- **Options…** — global preferences saved to your user profile

Read the screenshot `fig01.png` in this directory — it shows the Style Manager toolbar icon as it appears in the Settings menu entry.  
Read the screenshot `fig03.png` in this directory — it shows the Custom Projections globe icon used in the Settings menu.  
Read the screenshot `fig05.png` in this directory — it shows the Keyboard Shortcuts icon in the Settings menu.  
Read the screenshot `fig07.png` in this directory — it shows the Interface Customization icon in the Settings menu.

## Options Dialog

Open via **Settings › Options…** (wrench icon). Changes are saved to the active user profile and apply to all new projects.

Read the screenshot `fig15.png` in this directory — it shows the full General Settings tab of the Options dialog, with sections for Override System Locale, Application (style, theme, icon size, font), and Project Files.

### General Settings Tab

Key settings under **Application**:
- **Style** (restart required) — widget look; depends on OS
- **UI theme** (restart required) — `default`, `Night Mapping`, or `Blend of Gray`
- **Icon size** and **Font**

Key settings under **Project Files**:
- **Open project on launch** — choose `Welcome Page`, `New`, `Most recent`, or `Specific`
- **Create new project from default project** — set via *Set Current Project as Default*; saved templates appear in **Project › New From Template**
- **Default paths** — `Absolute` or `Relative` (can be overridden per project)
- **Default project file format** — `QGZ` (archive, embeds auxiliary data) or `QGS` (plain text, auxiliary data in separate `.qgd` file)
- **Enable macros** — controls embedded Python code execution; recommended to keep at `Ask`

### System Settings Tab

- **SVG paths** — add directories for custom SVG symbols
- **Plugin paths** — add directories for C++ plugins
- **Documentation paths** — override which help URL opens when clicking Help buttons in dialogs
- **Environment** — view and set custom environment variables (useful for GRASS/Processing tools); enable with *Use custom variables*

## CRS and Transforms Settings

Navigate to **Settings › Options… › CRS and Transforms › CRS Handling**.

Read the screenshot `fig04.png` in this directory — it shows the full CRS Handling tab, with separate sections for "CRS for Projects" (default CRS dropdown set to EPSG:4326 - WGS 84) and "CRS for Layers" (radio buttons for behavior when a layer has no CRS).

### Setting the Default Project CRS

Under **CRS for Projects**, choose how new projects get their CRS:
1. **Use CRS from first layer added** — project CRS matches the first loaded layer
2. **Use a default CRS** — always starts from a fixed CRS (default: EPSG:4326 WGS 84)

### Handling Layers With No CRS

Under **CRS for Layers**, set what happens when a layer is loaded without CRS information:

- **Leave as unknown CRS** — no prompt; layer gets a warning icon in the Layers panel (Read the screenshot `fig08.png` in this directory — it shows the `indicatorNoCRS` question-mark badge that appears next to unassigned layers). Useful when bulk-loading layers.
- **Prompt for CRS** — opens the CRS Selector dialog immediately on load
- **Use project CRS** — silently assigns the current project CRS
- **Use default layer CRS** — uses the fallback CRS set in the combobox above

Read the screenshot `fig06.png` in this directory — it shows the filled radio button indicating the currently selected option.

## Project CRS

The project CRS controls how all layers are rendered together via on-the-fly reprojection.

**To set the project CRS:**
1. Go to **Project › Properties… › CRS tab**
2. Search by EPSG code, name, or identifier in the Filter box
3. Select from the tree (Geographic, Projected, or User-defined)
4. Click **OK** — the status bar (bottom-right) updates to show the active CRS

**Shortcut — assign from a layer:**
- Right-click any layer in the Layers panel → **Set project CRS from Layer**

**To disable projection entirely** (e.g., for game maps or microscopy):
- Check **No CRS (or unknown/non-Earth projection)** — all coordinates treated as flat 2D Cartesian; ellipsoid and units become unavailable

> If you change the project CRS and want distance/area units to update accordingly, go to **Project › Properties… › General tab** and set **Map units** to match.

## Assigning CRS to Layers

**To assign/fix CRS on multiple layers at once:**
1. Select the layers in the Layers panel
2. Press `Ctrl+Shift+C` (or right-click → **Set CRS of layer(s)**, or **Layer › Set CRS of layer(s)**)
3. Find and select the correct CRS
4. Click **OK** — verify in the layer's **Source** tab under Layer Properties

> This changes only how QGIS interprets coordinates in the current project — it does not modify the source data files.

## CRS Selector Dialog

Used whenever QGIS prompts you to pick a CRS. Contains:
- **Filter** — type an EPSG code (e.g., `4326`), authority:code (e.g., `EPSG:3857`), or name
- **Recently used CRS** — quick access to frequently used systems; right-click to remove entries or clear all
- **Coordinate reference systems of the world** — full tree of ~7,000 CRSs grouped by type (Geographic, Projected, User-defined)
- **PROJ text** — read-only PROJ string for the selected CRS
- A map preview showing the CRS's coverage extent on Earth

Common CRSs to know: `EPSG:4326` (WGS 84, global lat/lon), `EPSG:3857` (Web Mercator, used by online maps).

## Custom Projections

Go to **Settings › Custom Projections…** to define a CRS not in the standard database. Custom CRSs are stored in your user profile's CRS database and appear in the CRS Selector under the *User Defined* node.

Read the screenshot `fig03.png` in this directory — it shows the globe icon for the Custom Projections menu entry, distinguishable from the wrench icon used for Options.