Manage QGIS global settings, project properties, and coordinate reference systems through the Settings and Project menus.

## Global Settings (Options)

**Settings → Options** (no default shortcut) opens the main preferences dialog with tabbed sections:

### General Tab
- **UI Theme**: "default", "Night Mapping", or "Blend of Gray" — requires restart
- **Open project on launch**: Choose Welcome Page, New, Most Recent, or a Specific project
- **Default paths**: Set to "Relative" (recommended) or "Absolute" for portability
- **Default project file format**: QGZ (embeds auxiliary data) vs QGS (plain text + separate .qgd file)
- **Embedded Python code**: Controls macro execution — set to "Ask" for safety

### System Tab
- Add custom **SVG paths**, **plugin paths**, and **documentation paths** here
- **Environment variables**: Enable "Use custom variables" to set/override env vars — useful for GRASS, SAGA, and debugging

### CRS and Transforms Tab
- **CRS for new projects**: Either inherit from first layer loaded, or set a fixed default
- **CRS for layers with no CRS**: Choose between Leave as unknown, Prompt, Use project CRS, or Use default layer CRS

---

## Settings Menu Quick Access

**Settings** menu provides direct shortcuts to:
- **Style Manager** — symbols, color ramps
- **Custom Projections** — create user-defined CRS
- **Keyboard Shortcuts** — view/reassign all shortcuts
- **Interface Customization** — hide toolbars, dialogs, menu items

---

## Project Properties

**Project → Properties** (or `Ctrl+Shift+P`) opens a tabbed dialog for per-project overrides:

### General Tab
- Set project title, default units (distance/area), and ellipsoid
- If you change the project CRS and want units to match, set **Map units** here

### CRS Tab
- Override the project CRS for this project only
- Shows a world map preview of the selected CRS extent
- Check **No CRS** to disable all projection handling (use for non-geographic maps like floor plans)

---

## Working with CRS

### Set/Change Project CRS
1. Open **Project → Properties → CRS** tab
2. In the Filter box, type an EPSG code (e.g., `4326`) or name (e.g., `UTM`)
3. Select the CRS from "Coordinate reference systems of the world" list
4. Click **OK** — all layers reproject on-the-fly to match

The current project CRS is always visible in the **status bar** (bottom-right corner). Click it to open the CRS selector directly.

**Shortcut**: Right-click any layer in the Layers panel → **Set project CRS from Layer**

### Assign CRS to a Layer
- Right-click the layer → **Set CRS** → **Set Layer CRS**
- Or select multiple layers and press `Ctrl+Shift+C`
- This changes how QGIS interprets coordinates — it does NOT reproject the data file itself

### Identify Layers with No CRS
Layers missing a CRS show a warning icon in the Layers panel. To fix: select them, press `Ctrl+Shift+C`, assign the correct CRS.

### CRS Selector Dialog
When the CRS selector opens (from any context):
- **Filter field** at top: search by EPSG code, name, or identifier
- **Recently used CRS** list: quick access to frequent picks
- **World list**: browse by Geographic / Projected / User-Defined categories
- **PROJ text** field (read-only): shows the underlying projection string

To remove a CRS from recent history: right-click it → **Remove selected CRS from recently used CRS**

---

## Common Pitfalls

- **Reprojection vs. reassignment**: "Set Layer CRS" only changes QGIS's interpretation — use **Vector → Data Management → Reproject Layer** to actually transform and save data in a new CRS
- **Units not updating after CRS change**: Go to **Project → Properties → General** and set distance/area units to "Map units" to sync with the new CRS
- **On-the-fly reprojection gaps**: If layers don't align visually, check that each layer has a correctly assigned CRS (not "unknown") before blaming the project CRS
- **QGS vs QGZ format**: QGS files are human-readable XML but auxiliary data (e.g., layer notes) goes to a separate .qgd file — both files must travel together. QGZ bundles everything but is binary
- **Options are profile-specific**: Changes in Settings → Options apply to your current user profile only, not system-wide