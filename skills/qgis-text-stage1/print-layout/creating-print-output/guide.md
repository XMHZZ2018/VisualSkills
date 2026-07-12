# Creating Print Output (QGIS 3.44)

Once your print layout is ready, open the **Layout** menu or toolbar to export. You've got four options: print directly, export as image, SVG, or PDF.

For images, click **Export as image**, pick your format (PNG, TIFF, JPG, etc.) and location. Multi-page layouts automatically append page numbers to the filename. In the export dialog, you can override resolution, enable antialiasing, and check **Generate world file** to produce a georeferenced output with an accompanying ESRI World File. The **Crop to content** option trims output to the bounding area of your items — use transparency-friendly formats like PNG or TIFF here since anything outside the page extent renders as black in JPG/BMP.

For SVG, click **Export as SVG**. Turn on **Export map layers as SVG groups** to keep layer names intact for easier editing in Inkscape or Illustrator. **Simplify geometries** is worth enabling to keep file sizes sane. Choose whether text exports as editable text or outlines under **Text export**.

For PDF, click **Export as PDF** — all pages go into a single file. You can pick **Lossy (JPEG)** or **Lossless** compression, enable **Create Geospatial PDF** for georeferenced output, and toggle **Simplify geometries**. Note that setting layer opacity below 100% forces rasterization, which can bloat your PDF.

To generate an atlas (automated map book), open the **Atlas** panel and enable **Generate an atlas**. Set your **Coverage layer** — each feature becomes one output page. Use **Filter with** to subset features and **Sort by** to control order. Labels support expressions between `[%` and `%]` delimiters (e.g., `[% upper(CITY_NAME) %]`) that update per feature. Preview with **Atlas > Preview Atlas**, then export via **Atlas > Export Atlas as PDF…** (single or multi-file) or **Export Atlas as Images…**.
