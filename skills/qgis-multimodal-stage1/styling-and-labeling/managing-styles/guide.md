# Managing the Style Library (QGIS 3.44)

The Style Manager is your central hub for symbols, color ramps, text formats, label settings, and legend patch shapes. Everything lives in a `symbology-style.db` file tied to your active user profile, so all projects under that profile share the same library. Open it from **Settings > Style Manager…**, the **Style Manager** button on the Project toolbar, or from any symbol picker inside layer properties.

At the top-left of the dialog you can switch between style databases — **Default** for the built-in library plus anything you've saved, or **Project Styles** for symbols scoped to the current project. You can also attach an existing `.db` file or create a fresh one.

See `fig01.png`.

Organize items using **Tags** (manual labels you attach yourself) or **Smart Groups** (dynamic filters based on name patterns or existing tags). Right-click any selection and choose **Add to Tag >** to file things away, or hit **Add Smart Group…** in the left panel to define filter rules. Both can coexist — they're just two lenses onto the same items.

Adding a new item is straightforward: click **Add item**, configure it in the builder that appears, and save. To tweak something later, select it and hit **Edit item**. Deleting is just **Remove item** — gone from your local database, but not from any exported files you've already shared.

To export, use the **Import/Export** drop-down at the bottom-left and pick **Export Item(s)…**. Select what you want (or filter by tag/group), then save as a single `.XML` file you can hand off to anyone. Symbols specifically can also go out as individual `.PNG` or `.SVG` files into a folder.

Importing works the other way: **Import/Export > Import Item(s)**, point it at an `.xml` file or URL, optionally tick **Add to favorites** and **Do not import embedded tags**, then pick the items you want from the preview and press **Import**. You can also just drag an `.xml` file from the Browser panel onto the map canvas for a quick import.

See `fig02.png`.

The online style repository at [hub.qgis.org/styles](https://hub.qgis.org/styles) is reachable via the **Browse Online Styles** button at the bottom of the dialog. Download any `.xml` bundle from there and import it using the same workflow.

For color ramps, switch to the **Color ramp** tab, click **Add item**, and pick a type — Gradient, Color presets, Random, ColorBrewer, or cpt-city (which ships hundreds of pre-built ramps). Gradient ramps let you double-click the preview bar to drop intermediate color stops, then fine-tune each stop's position, color model (RGB/HSL/HSV), and hue direction.

Legend patch shapes live under the **Legend Patch Shapes** tab. Add one by choosing Marker, Line, or Fill geometry, then define the shape as a WKT string. Toggle **Preserve aspect ratio** if needed, name it, tag it, and save — it's immediately available in your legend configuration.
