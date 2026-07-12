# Managing the Style Library (QGIS 3.44)

All your symbols, color ramps, text formats, and label settings live in the Style Manager. Open it from **Settings > Style Manager…**, the **Style Manager** button on the Project toolbar, or from within any symbol configuration dialog.

At the top-left dropdown, pick which style database to work with — **Default** for your global library, **Project Styles** for project-scoped items, or any custom database you've added. Items are organized into **Favorites**, **Tags** (user-assigned labels), and **Smart Groups** (auto-populated by filter expressions like "name contains 'arrow'"). Tags and smart groups coexist — use whichever suits your workflow.

To add a new item, hit **Add item** and choose the type (symbol, color ramp, text format, etc.). Edit any existing item by selecting it and clicking **Edit item**. Right-clicking a selection lets you tag, copy, paste, or export items as PNG/SVG.

Sharing is handled through the **Import/Export** dropdown at the bottom-left. **Export Item(s)…** bundles your selection into a single `.XML` file you can hand off to anyone. To bring items in, use **Import Item(s)**, point it at an `.xml` file or URL, optionally add tags, preview what's available, and import what you need. You can also drag an `.xml` style file from the Browser panel straight onto the map canvas.

For community styles, click **Browse Online Styles** to reach the shared repository at hub.qgis.org/styles — download, unzip, and import the `.xml` file using any method above.

Color ramps get their own creation flow: under the **Color ramp** tab, **Add item** offers Gradient (with draggable color stops and HSL/HSV interpolation), Color presets, Random, ColorBrewer, or the massive cpt-city catalog. For legend patches, switch to the **Legend Patch Shapes** tab, pick your geometry type (Marker, Line, or Fill), and define the shape as a WKT string.
