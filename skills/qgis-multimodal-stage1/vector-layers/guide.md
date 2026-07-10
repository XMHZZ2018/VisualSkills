Here is the guide:

---

Manage vector layer appearance, inspect and edit feature attributes, and modify geometries using QGIS's Layer Properties, Attribute Table, and editing tools.

## Layer Properties Dialog

Open the Layer Properties dialog in any of these ways:
- **Double-click** the layer in the Layers panel
- **Right-click** the layer → **Properties…**
- **Layer menu → Layer Properties…**

The dialog contains many tabs across the top. The most commonly used are:

Read the screenshot `fig01.png` in this directory — it shows the Information tab icon (the blue "i"), which is the read-only summary tab showing source path, geometry type, CRS, feature count, and extent.

Read the screenshot `fig04.png` in this directory — it shows the Source tab icon (wrench), where you set layer name, encoding, CRS assignment, and use the Query Builder to filter features.

Read the screenshot `fig07.png` in this directory — it shows the Symbology tab icon (paintbrush), the entry point for all feature rendering: single symbol, categorized, graduated, or rule-based styles.

Read the screenshot `fig10.png` in this directory — it shows the Labels tab icon ("abc"), which opens the labeling configuration for single labels, rule-based labels, etc.

Read the screenshot `fig13.png` in this directory — it shows the Mask tab icon, used to configure label mask effects that punch through overlapping symbology.

### Key Layer Properties Workflows

**Change layer CRS** (reassign, not reproject):
1. Open Properties → **Source** tab
2. Click the CRS selector button next to the assigned CRS
3. Choose the correct CRS and click OK

**Filter features with Query Builder**:
1. Properties → **Source** tab → click **Query Builder** at the bottom
2. Double-click a field name, choose an operator, double-click a value
3. Click **Test** to verify the feature count, then **OK**
4. A filter icon appears next to the layer in the Layers panel — hover to see the active query

**Save/share styles**: Use the **Style** menu at the bottom of the dialog to export/import styles as `.qml` files or copy to clipboard.

---

## Attribute Table

### Opening the Attribute Table

Read the screenshot `fig02.png` in this directory — it shows the Open Attribute Table toolbar button (blue grid icon), found in the Attributes toolbar.

Open the attribute table via:
- **Layer menu → Open Attribute Table**
- Right-click layer → **Open Attribute Table**
- Click the toolbar button shown in `fig02.png`
- Keyboard: **F6** (all features), **Shift+F6** (selected only), **Ctrl+F6** (visible only)

Read the screenshot `fig11.png` in this directory — it shows the full Attribute Table window for a "regions" layer with 26 features, 4 selected (highlighted in blue), displaying id, name_2, and type_2 columns. The title bar shows total/filtered/selected counts. The toolbar runs across the top with editing, selection, and field calculator buttons.

### Attribute Table Toolbar — Key Buttons

Read the screenshot `fig14.png` in this directory — it shows the Toggle Editing pencil icon (**Ctrl+E**), which must be active before any edits are possible.

| Action | Shortcut |
|---|---|
| Toggle editing mode | Ctrl+E |
| Select all features | Ctrl+A |
| Invert selection | Ctrl+R |
| Deselect all | Ctrl+Shift+A |
| Filter/select by form | Ctrl+F |
| Pan map to selected | Ctrl+P |
| Zoom map to selected | Ctrl+J |
| Open field calculator | Ctrl+I |
| New field | Ctrl+W |

### Table View vs Form View

Switch between modes using the icons at the **bottom-right** of the attribute table window:
- **Table view**: all features as rows, all fields as columns. Right-click a column header to resize, hide, sort, or reorder columns.
- **Form view**: feature list on the left panel; attribute form for the selected feature on the right. Use arrow buttons at the bottom to step through features. Buttons at the bottom let you highlight, pan to, or zoom to the current feature in the map canvas.

### Editing Attributes

1. Click **Toggle Editing** (pencil icon, Ctrl+E) — the table border turns red/orange
2. Click any cell to edit its value directly
3. Use **Quick Field Calculation bar** (appears below toolbar in edit mode) to update many features at once with an expression
4. Click **Save Edits** to commit, or toggle editing off and confirm

**Delete features**: Select rows → click **Delete selected features** button.

**Add a new field**: Click **New field** (Ctrl+W) → set name, type, length → OK.

**Organize columns**: Click the **Organize columns** button (grid icon) in the toolbar to show/hide fields or drag-and-drop to reorder them for display (does not alter the datasource field order).

---

## Snapping and Geometry Editing

Before editing geometries on the canvas, enable snapping to ensure vertices align precisely.

Read the screenshot `fig03.png` in this directory — it shows the Enable Snapping magnet icon (red magnet), toggled via **View → Toolbars → Snapping Toolbar** or **S** key shortcut.

Snapping can be configured to snap to different geometry components:

Read the screenshot `fig06.png` in this directory — it shows the Snap to Vertex icon (four corner dots), which snaps the cursor to existing vertices.

Read the screenshot `fig09.png` in this directory — it shows the Snap to Segment icon (checkmark/line), which snaps to the nearest point along a line segment.

Read the screenshot `fig12.png` in this directory — it shows the Snap to Area icon (green oval), which snaps to polygon interiors.

Read the screenshot `fig15.png` in this directory — it shows the Snap to Centroid icon (concentric circles), which snaps to the geometric center of features.

### Basic Geometry Editing Workflow

1. Select the layer in the Layers panel
2. Enable snapping (press **S** or click the magnet icon)
3. Set snap mode (vertex, segment, area, or centroid) in the Snapping toolbar
4. Click **Toggle Editing** (pencil, Ctrl+E) on the layer
5. Use digitizing tools from the **Digitizing toolbar** (Add Feature, Move Feature, Node Tool, etc.)
6. While editing, a vertex handle appears when hovering near snappable geometry
7. Save edits with **Layer → Save Layer Edits** or toggle editing off and confirm

**Node Tool**: Select a feature, then use the Node Tool to drag individual vertices, insert new nodes (double-click on a segment), or delete nodes (select vertex → Delete key).