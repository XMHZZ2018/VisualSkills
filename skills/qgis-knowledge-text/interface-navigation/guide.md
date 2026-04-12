Core layout and navigation reference for the QGIS 3.44 graphical interface.

## GUI Layout Overview

QGIS has five main components:

1. **Menu Bar** — top of window, hierarchical menus (Project, Edit, View, Layer, etc.)
2. **Toolbars** — icon rows below the menu bar; dockable/movable
3. **Panels** — dockable side panes (Layers, Browser, Processing, etc.)
4. **Map View** — central canvas where layers render
5. **Status Bar** — bottom strip showing coordinates, scale, CRS, and progress

## Menu Bar Key Paths

### Project Menu
| Action | Shortcut |
|---|---|
| New project | `Ctrl+N` |
| Open project | `Ctrl+O` |
| Save | `Ctrl+S` |
| Save As | `Ctrl+Shift+S` |
| Project Properties | `Ctrl+Shift+P` |
| New Print Layout | `Ctrl+P` |
| Exit QGIS | `Ctrl+Q` |

Save to GeoPackage or PostgreSQL: **Project → Save to → GeoPackage…** / **PostgreSQL…**

### Edit Menu
Edit tools are **greyed out by default** — you must click **Toggle Editing** on the layer first (pencil icon in the Digitizing toolbar).

| Action | Shortcut |
|---|---|
| Undo | `Ctrl+Z` |
| Redo | `Ctrl+Shift+Z` |
| Select Features by Value | `F3` |
| Select Features by Expression | `Ctrl+F3` |
| Deselect All Features | `Ctrl+Alt+A` |
| Deselect from Current Layer | `Ctrl+Shift+A` |
| Select All Features | `Ctrl+A` |

### View Menu
- **New Map View** — `Ctrl+M` — opens a second 2D map canvas
- **Toggle Full Screen** — hides title bar, maximizes QGIS window
- **Toggle Panel Visibility** — show/hide all panels at once (useful for digitizing)
- **Toggle Map Only** — hides panels, toolbars, menus, and status bar; shows only the map canvas
- **View → Panels** — enable/disable individual panels (Browser, Layers, Processing Toolbox, etc.)

## The Browser Panel

**Open via**: View → Panels → Browser (or Browser (2) for a second instance)

The Browser panel is an expandable tree for finding and loading data. Click the arrow to expand nodes; use **Collapse All** button to reset.

### Top-Level Entries
- **Favorites** — pinned frequently-used folders; right-click a folder elsewhere to add
- **Spatial Bookmarks** — saved map extents, split into Project and User bookmarks
- **Project Home** — folder containing the current project file (change via Project → Properties → General → Project home)
- **Home / Drives** — OS file system starting from home directory and mounted drives
- **Database entries** — GeoPackage, SpatiaLite, PostgreSQL, MS SQL Server, Oracle, SAP HANA

### Adding Data from the Browser
1. Navigate to your file in the Browser tree
2. **Double-click** to add directly to the map, or
3. **Drag** the file onto the map canvas, or
4. Right-click → **Add Layer to Project**

### Searching the Browser
- Use the **Filter Browser** text box (funnel icon) at the top of the panel
- Click the **Options** dropdown next to the filter to set: Case Sensitive, Normal / Wildcard / Regular Expression matching

### Browser Context Menu (Files/Folders)
Right-click any folder to: Refresh, create New (Directory / GeoPackage / Shapefile), Hide from Browser, Set color (for visual organization), Open in Terminal, Open Directory in file manager.

### Properties Widget
Click the **Enable/disable properties widget** button (metadata icon) at the top of the Browser panel to show a preview pane at the bottom with layer metadata.

## Panels

Enable/disable panels via **View → Panels**. Key panels:
- **Layers** — layer stack and visibility toggles
- **Browser** / **Browser (2)** — file/database navigation
- **Processing Toolbox** — geoprocessing algorithms
- **Spatial Bookmarks** — saved extents

Panels can be dragged, docked to any edge, or floated as separate windows.

## Toolbars

Enable/disable via **View → Toolbars** or right-click any toolbar. Key toolbars:
- **Project** — New, Open, Save, Print Layout
- **Map Navigation** — Pan, Zoom In/Out, Zoom to Layer, etc.
- **Selection** — rectangle/polygon/freehand/radius select tools
- **Digitizing** — Toggle Editing, Add Feature, Undo/Redo
- **Attributes** — Identify Features, Open Attribute Table

## Common Navigation Workflows

### Zoom and Pan
- **Scroll wheel** — zoom in/out centered on cursor
- **Middle-click drag** — pan the map
- **Zoom to Layer**: right-click layer in Layers panel → Zoom to Layer
- **Zoom to Full Extent**: View → Zoom Full, or `Ctrl+Shift+F`

### Spatial Bookmarks
1. Navigate map to desired extent
2. View → New Spatial Bookmark… (or Browser panel → right-click Spatial Bookmarks)
3. Name it, assign to Project or User scope
4. To return: right-click bookmark in Browser → **Zoom to Bookmark**

### Reconfigure Keyboard Shortcuts
Settings → Keyboard Shortcuts — search any action and reassign its key.

### Interface Customization
Settings → Interface Customization — hide specific toolbars, panels, menu items, or Browser entries (e.g. uncheck `Browser → py` to hide Python scripts).

## Common Pitfalls

- **Edit tools are disabled**: You must enable editing mode (Toggle Editing / pencil icon) before any Edit menu geometry or attribute tools become active.
- **Browser shows nothing new**: Right-click the folder → **Refresh**, or check if the directory has monitoring disabled (network drives are not monitored by default).
- **Two Browser panels**: Open a second via View → Panels → Browser (2). Useful for drag-and-drop between deeply nested locations.
- **Project Home not set**: Until you save a project file, the Project Home entry does not appear in the Browser.
- **macOS difference**: Exit QGIS is under the **QGIS** application menu → Quit QGIS (`Cmd+Q`), not under Project.