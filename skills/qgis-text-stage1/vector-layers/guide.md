Manage vector layer appearance, attributes, and data through the Layer Properties dialog and Attribute Table.

## Opening Layer Properties

**Double-click** the layer in the Layers panel, or right-click → **Properties…**, or use **Layer → Layer Properties…**.

The dialog has tabs along the left side: Information, Source, Symbology, Labels, Fields, Attributes Form, Joins, Digitizing, and more.

### Key Tabs

- **Information** — Read-only summary: CRS, geometry type, feature count, file path, extent.
- **Source** — Rename the layer (display name only), change CRS assignment, set encoding, create spatial index, replace the data source path.
- **Fields** — View/manage field definitions.
- **Symbology** — Control rendering: Single Symbol, Categorized, Graduated, Rule-based (and more for points/polygons).
- **Digitizing** — Configure snapping and geometry validation behavior for editing.

### Setting a Feature Filter (Query Builder)

Access via **Source tab → Provider Feature Filter → Query Builder** button, or **Layer → Filter…**.

The dialog has three panels: **Fields** (left), **Values** (center), **Operators** (right), and a SQL expression box at the bottom.

1. Double-click a field name to add it to the expression.
2. Click **All** or **Sample** in Values to browse field values; double-click a value to insert it.
3. Use operator buttons (=, >, LIKE, AND, OR, NOT) to build the WHERE clause.
4. Click **Test** to verify — shows feature count matching the filter.
5. Click **OK** to apply. A filter icon appears next to the layer in the Layers panel.
6. To remove: open Query Builder → **Clear** → OK.

**Pitfall**: Filter syntax is provider-specific. DateTime filtering works in GeoPackage/PostGIS but not Shapefiles.

---

## Attribute Table

### Opening

- **F6** — open attribute table
- **Shift+F6** — open filtered to selected features
- **Ctrl+F6** — open filtered to visible map features
- Or: right-click layer → **Open Attribute Table**, or click the toolbar button in the Attributes toolbar

The title bar shows total feature count and current selection count.

### Table View vs Form View

Toggle between modes using icons at the **bottom-right** of the attribute table window.

- **Table view** — spreadsheet-style, one row per feature. Use `Shift+Mouse Wheel` to switch between horizontal/vertical scrolling.
- **Form view** — feature list on the left, attribute fields on the right. Navigate features with arrows at the bottom; pan/zoom to the active feature using the highlight/pan/zoom buttons.

Set default view at **Settings → Options → Data Sources**.

### Toolbar Quick Reference

| Action | Shortcut |
|---|---|
| Toggle editing mode | Ctrl+E |
| Save edits | (toolbar button) |
| Select all features | Ctrl+A |
| Invert selection | Ctrl+R |
| Deselect all | Ctrl+Shift+A |
| Filter/select by form | Ctrl+F |
| Select by expression | (toolbar button) |
| Pan map to selection | Ctrl+P |
| Zoom map to selection | Ctrl+J |
| Open field calculator | Ctrl+I |
| New field | Ctrl+W |
| Cut selected | Ctrl+X |
| Copy selected | Ctrl+C |
| Paste features | Ctrl+V |

### Configuring Columns

Right-click any **column header** to:
- **Set width…** or **Autosize** — resize that column
- **Hide column** — removes it from view (not from data)
- **Sort…** — sort by expression (supports multi-column sorting)
- **Organize columns…** — reorder, show/hide multiple fields at once via drag-and-drop

The **Organize columns** button (toolbar) opens a checklist dialog where you can show/hide fields, reorder by drag-and-drop, and add a virtual Actions column. **Pitfall**: reordering columns here only changes display order, not the underlying field order in the datasource.

### Editing Attributes

1. Enable edit mode: **Ctrl+E** or click the pencil icon.
2. Click a cell to edit inline, or use Form view for a cleaner interface.
3. To edit many features at once: click **Toggle multi edit mode** (toolbar) → change values → apply.
4. Use the **Quick Field Calculation bar** (appears below toolbar in edit mode) for fast expression-based updates to selected or all features.
5. Open the **Field Calculator** (**Ctrl+I**) for full expression-based field updates.
6. Save with the **Save Edits** button, or exit edit mode (Ctrl+E) and confirm save.

### Adding and Deleting Features (Attribute Table)

- **Add geometryless feature**: click the Add Feature dropdown → "Add feature via attribute table" (inserts blank row) or "Add feature via attribute form" (opens form dialog).
- **Delete features**: select rows → click **Delete selected features** button.

**Pitfall**: Deleting from the attribute table permanently removes features — there is no undo after saving edits.

---

## Common Pitfalls

- **CRS assignment vs reprojection**: Changing CRS in Source tab reassigns the CRS label (use only if wrong/missing). To actually reproject data, use **Processing → Reproject Layer** or **Save As** with a target CRS.
- **Filtered layers behave as if complete**: With a Query Builder filter active, selection, editing, and exports only operate on the filtered subset — the rest of the data is inaccessible until the filter is cleared.
- **Embedded layers are locked**: Layers embedded from external projects have read-only Layer Properties — edit in the source project.
- **Tool availability varies by format**: Some attribute table toolbar buttons (e.g., New Field, Delete Field) may be greyed out depending on the data format's capabilities via GDAL.