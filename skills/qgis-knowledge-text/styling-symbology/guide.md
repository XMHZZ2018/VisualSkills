Style Manager, Symbol Selector, and label settings are accessible from `Settings → Style Manager` or directly from Layer Properties.

## Opening Style Tools

- **Style Manager** (global library): `Settings → Style Manager` or the Style Manager button in the Project toolbar
- **Symbol Selector** (per-layer): `Layer → Properties → Symbology` tab, then click any symbol preview
- **Labels**: `Layer → Properties → Labels` tab

The Style Manager is **modeless** — it stays open while you work on the map.

## Style Manager Dialog

The dialog has three zones:
- **Left panel**: category tree (Favorites, All, Tags, Smart Groups) and a style database dropdown
- **Center**: tabbed preview grid of items (All / Marker / Line / Fill / Color ramp / Text format / Label settings / Legend Patch Shapes / 3D Symbols)
- **Bottom-left**: Import/Export button

### Switching Style Databases
Use the dropdown in the upper-left to switch between **Default** (shared across projects), **Project Styles** (project-specific), or any custom databases you've added.

### Adding / Editing Items
1. Select the appropriate tab (e.g., Marker for point symbols)
2. Click the **+ Add item** button, or right-click an existing item → **Edit Item**
3. Configure in the Symbol Selector dialog that opens
4. Click **Save Symbol** → give it a name, optional tags, choose destination database

### Organizing with Tags and Smart Groups
- **Tags**: right-click items → **Add to Tag** → pick or create a tag
- **Smart Groups**: click **Add Smart Group…** → enter a filter expression (e.g., name contains "road", has tag "water") — membership updates automatically
- To add/remove Favorites: right-click → **Add to Favorites** / **Remove from Favorites**

### Sharing Styles
**Export**: Import/Export dropdown → **Export Item(s)…** → select items → Export → saves as `.xml`

**Import**: Import/Export dropdown → **Import Item(s)** → point to `.xml` file or URL → optionally add tags or skip embedded tags → select items from preview → **Import**

**Browser panel shortcut**: drag a `.xml` style file onto the map canvas, or right-click it → **Import Style…**

## Symbol Selector Dialog

Opens when you click a symbol in Layer Properties → Symbology.

### Dialog Layout
- **Symbol tree** (left/top): shows stacked symbol layers; the combined result is previewed live
- **Layer settings** (right/bottom): parameters for the selected symbol layer
- **Library preview** (bottom): filterable thumbnail grid of saved symbols of the same type

### Building a Symbol
1. The top-level entry in the tree is the **symbol type** (Marker / Line / Fill) — set global **Unit**, **Opacity**, **Color**, and **Size** or **Width** here
2. Changing **Color** at the top level propagates to all unlocked sub-layers
3. Add symbol layers with the **+ (Add symbol layer)** button; stack multiple layers for complex symbols
4. Reorder layers with the up/down arrows; layers higher in the tree render on top
5. **Lock a layer's color** (padlock icon) to prevent it from inheriting global color changes
6. Toggle the **Enable symbol layer** checkbox to hide a layer without deleting it — useful for testing

### Common Symbol Layer Types

| Geometry | Layer Types |
|---|---|
| Point (Marker) | Simple marker, SVG marker, Font marker, Raster image marker, Ellipse marker, Filled marker |
| Line | Simple line, Marker line, Hashed line, Arrow |
| Polygon (Fill) | Simple fill, Gradient fill, Shapeburst fill, SVG fill, Pattern fill |

**Simple Marker** key properties: Shape, Size, Fill color, Stroke color/style/size, Rotation, Offset (X/Y), Anchor point, Join style, Cap style

### Advanced Symbol Options
Access via the **Advanced** dropdown button:
- **Clip features to canvas extent** (line/fill)
- **Force right-hand rule orientation** (fill) — fixes ring winding for consistent rendering without altering source geometry
- **Buffer settings…** (marker) — adds a halo around the marker for legibility
- **Symbol levels…** — controls render order across layers when using categorized/graduated symbology

### Saving to Library
Click **Save Symbol** (floppy disk icon in the symbol selector) → set name, destination database, and tags → optionally **Add to favorites**.

## Label Settings

Access via `Layer → Properties → Labels` tab.

- **Label with**: choose a field or write an expression
- **Text** sub-tab: font, size, color, bold/italic/underline
- **Formatting**: wrapping, case, spacing
- **Buffer**: white halo around text — set Size and Color; dramatically improves legibility
- **Background**: drawn shape behind label (rectangle, SVG, marker)
- **Shadow**: drop shadow for depth
- **Placement**: controls where labels appear relative to features (e.g., "Around Point", "Curved" for lines)
- **Rendering**: scale-based visibility, label priority, obstacle settings

Label formats can be saved as reusable **Text Formats** in the Style Manager (Text format tab) — these store font + buffer + shadow but not placement rules.

## Common Pitfalls

- **Color change doesn't affect all layers**: a locked color (padlock icon) on a symbol layer ignores global color changes — unlock it first
- **Style Manager changes don't auto-apply**: editing a symbol in Style Manager doesn't update layers already using it; you must re-apply the symbol to the layer
- **Data-defined override button is greyed out** in Style Manager — it only activates when the symbol is connected to a map layer via Layer Properties
- **Label buffer not showing**: Buffer is disabled by default; go to Labels → Buffer tab and check **Draw text buffer**
- **Symbols not visible at current scale**: check Labels → Rendering tab or Layer → Properties → Rendering for scale-dependent visibility settings