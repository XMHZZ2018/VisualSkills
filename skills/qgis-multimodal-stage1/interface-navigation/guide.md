Here is the multimodal guide:

---

Core reference for QGIS 3.44's five-part GUI, the Browser panel for data access, and the general interface tools that control layers and map display.

## The QGIS GUI Layout

QGIS has five main components arranged around a central map canvas.

Read the screenshot `fig01.png` in this directory — it shows the full QGIS interface with all five numbered components labeled: (1) Menu Bar at the top, (2) Toolbars below it, (3) Panels on the left (Browser and Layers) and right (Processing Toolbox), (4) Map View in the center, and (5) Status Bar at the bottom.

### Menu Bar
All functions are accessible through the hierarchical menu at the top. Key menus:
- **Project** — open, save, close, export projects
- **Edit** — select features, editing tools (requires Toggle Editing mode)
- **View** — map views, panels, toolbars, full-screen/map-only modes
- **Settings** — keyboard shortcuts, interface customization

Keyboard shortcuts can be reconfigured at **Settings › Keyboard Shortcuts**.

### Toolbars
Toolbars sit below the menu bar and provide one-click access to frequently used tools. Right-click any toolbar area to show/hide individual toolbars. The **Project toolbar** contains the most-used file operations.

### Panels
Panels (Browser, Layers, Processing Toolbox, etc.) dock to the sides of the map canvas. Show/hide all panels at once with **View › Toggle Panel Visibility**. A second instance of any panel can be opened via **View › Panels**.

### Status Bar
The bottom bar displays current coordinates, map scale, magnifier, and rotation. Click the coordinate display to change the CRS used for reporting.

### View Modes
- **Toggle Full Screen Mode** (`F11`) — hides the title bar
- **Toggle Panel Visibility** — hides/shows all docked panels for maximum canvas space
- **Toggle Map Only** — hides panels, toolbars, menus, and status bar; shows only the map canvas

---

## Project File Operations

All project file actions are under the **Project** menu and the **Project toolbar**.

| Action | Shortcut | Toolbar button |
|--------|----------|---------------|
| New project | `Ctrl+N` | Read the screenshot `fig04.png` in this directory — it shows the New (blank document) icon |
| Open project | `Ctrl+O` | Read the screenshot `fig07.png` in this directory — it shows the Open (folder) icon |
| Save | `Ctrl+S` | Read the screenshot `fig10.png` in this directory — it shows the Save (floppy disk) icon |
| Save As | `Ctrl+Shift+S` | Read the screenshot `fig13.png` in this directory — it shows the Save As icon |
| Project Properties | `Ctrl+Shift+P` | — |
| Exit QGIS | `Ctrl+Q` | — |

Projects can be saved to file (`.qgs` / `.qgz`), GeoPackage, PostgreSQL, or Oracle databases via **Project › Save to ›**.

---

## The Browser Panel

The Browser panel is the primary tool for finding and loading data into QGIS.

Read the screenshot `fig02.png` in this directory — it shows the full Browser panel with its top-level entries: Favorites, Spatial Bookmarks, Home, local drives (C:\\), and database connections (GeoPackage, SpatiaLite, PostgreSQL, SAP HANA, MS SQL Server, Oracle, WMS/WMTS, Cloud, WCS, WFS/OGC API, ArcGIS REST Servers).

### Opening the Browser
Go to **View › Panels › Browser** (or **Browser (2)** for a second instance). The panel typically docks on the left alongside the Layers panel.

### Navigating the Hierarchy

- Click Read the screenshot `fig05.png` in this directory — it shows the expand arrow (right-pointing triangle) — to expand a node
- Click Read the screenshot `fig08.png` in this directory — it shows the collapse arrow (downward triangle) — to collapse a branch
- Click Read the screenshot `fig11.png` in this directory — it shows the Collapse All button (arrow pointing up) — at the top of the panel to collapse all top-level entries at once

### Filtering the Browser

Read the screenshot `fig14.png` in this directory — it shows the Filter Browser funnel icon at the top of the panel.

Click the filter icon or type directly in the filter box to search by entry name across the entire hierarchy. Use the **Options** dropdown next to the filter box to set:
- Case-sensitive search
- Filter pattern: Normal, Wildcard(s), or Regular Expressions

### Adding Data to the Map
1. Navigate to a file or database layer in the Browser
2. **Double-click** the layer, **drag it onto the map canvas**, or select it and click **Add Selected Layers**
3. For databases: right-click the top-level entry › **Create a New Connection…**, fill in credentials, then expand the connection to browse tables

### Properties Widget
Click the Read the screenshot `fig09.png` in this directory — it shows the Enable/disable properties widget (eye with cursor) button — at the top of the Browser to toggle a metadata preview pane at the bottom of the panel. This shows CRS, extent, and field info for the selected item without loading it.

### Key Context Menu Actions (right-click any layer/file)
- **Add Layer to Project** — loads the layer into the map
- **Layer Properties…** — inspect metadata, CRS, fields
- **Export Layer** — save to a different format
- **Open with Data Source Manager…** — opens the full add-layer dialog
- **Manage ›** — rename or delete layers
- **Show in Files** — opens the OS file browser at that location

### Top-Level Entries Reference
- **Favorites** — pin frequently used folders; right-click folders and choose **Add as Favorite**
- **Spatial Bookmarks** — stored map extents, split into Project and User bookmarks; right-click to zoom, edit, or delete
- **Project Home** — the folder containing the current project file (customizable via **Project › Properties… › General › Project home**)
- **Home / drives** — OS file system; right-click a folder to create GeoPackage/Shapefile datasets, set folder icon color, or configure monitoring

---

## General Interface Tools

### Layer Styling Panel
Read the screenshot `fig03.png` in this directory — it shows the symbology (paint brush) icon used to open the Layer Styling panel, which provides a live-update panel for changing layer symbology without opening the full Layer Properties dialog.

Open it via **View › Panels › Layer Styling** or press `F7`. Changes apply in real time to the map canvas.

### Expression Filter
Read the screenshot `fig15.png` in this directory — it shows the expression filter icon (stylized "E"), used to filter features in the Layers panel or attribute tables using QGIS expressions.

### Layer Panel Presets
Read the screenshot `fig09.png` in this directory — it shows the Show Presets icon (eye with arrow), which manages layer visibility presets — saved snapshots of which layers are on/off — accessible from the top of the Layers panel.

### Controlling Panels and Toolbars via View Menu
- **View › Panels** — list of all available panels with checkboxes
- **View › Toolbars** — list of all toolbars; check/uncheck to show or hide
- **Settings › Interface Customization** — hide specific browser entries (e.g., uncheck `Browser › py` to remove Python scripts from the Browser panel)