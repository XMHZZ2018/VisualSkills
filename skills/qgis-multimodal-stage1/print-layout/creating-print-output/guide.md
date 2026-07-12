# Creating Print Output (QGIS 3.44)

Once your print layout looks good, you'll want to get it out of QGIS and into the real world. Open the **Layout** menu (or use the toolbar) and you've got four export paths: print directly, export as image, export as SVG, or export as PDF.

**Export as Image** — click the **Export as image** button, pick a format (PNG, TIFF, JPG, BMP, etc.) and a filename. Multi-page layouts automatically get a page number suffix appended (e.g., `map_2.png`). In the Image Export Options dialog, you can override the resolution, enable antialiasing, and toggle **Generate world file** if you need a georeferenced output with a sidecar `.tfw` or `.pnw`. The **Crop to content** checkbox trims the canvas to just your items — handy, but stick with PNG or TIFF since formats without transparency (JPG, BMP) will render the background as black.

See `fig01.png`.

**Export as SVG** — same flow, but you get vector-specific options. **Export map layers as SVG groups** keeps your layer names intact, which makes editing in Inkscape or Illustrator much easier. **Simplify geometries** is worth checking for large datasets — it strips vertices that are invisible at your export DPI, slashing file size. Watch the **Text export** setting: "Always export as text" keeps labels editable, while "outlines" converts them to paths (safer for fonts, but not searchable).

**Export as PDF** — the workhorse for print-ready output. All pages go into a single file. You can choose between **Lossy (JPEG)** and **Lossless** image compression — lossless is better for print shops but makes bigger files. Check **Create Geospatial PDF** if you want the output georeferenced and interactive. One gotcha: any layer with opacity below 100% forces rasterization of that layer, which can balloon file size.

See `fig02.png`.

**Atlas generation** turns a single layout into a map book. In the **Atlas** panel, enable **Generate an atlas**, then pick a **Coverage layer** — QGIS iterates through its features and produces one output per feature. Set a **Page name** field for meaningful filenames, apply a **Filter** expression to skip features you don't need, and control sort order. On your map item, enable **Controlled by atlas** so it zooms to each feature automatically.

Labels adapt to each atlas page when you wrap expressions in `[% ... %]` — for instance, `[% upper(CITY_NAME) %]` swaps in the current feature's city name. You can even use data-defined overrides to flip page orientation between portrait and landscape based on feature geometry, using an expression like `CASE WHEN bounds_width(@atlas_geometry) > bounds_height(@atlas_geometry) THEN 'Landscape' ELSE 'Portrait' END`.

See `fig03.png`.

To preview, hit **Atlas > Preview Atlas** and navigate features with the arrow buttons or the dropdown. When you're satisfied, export via **Atlas > Export Atlas as PDF** (single merged file if you checked **Single file export when possible**) or use the image/SVG variants, which write one file per feature per page into a folder you choose.
