# Exporting Map Output (QGIS 3.44)

QGIS gives you three ways to export what you see on the map canvas: as a raster image, as a PDF, or as a DXF file for CAD workflows. For full cartographic control you'd use the Print Layout, but these quick-export options are perfect when you just need a screenshot-quality output with georeferencing baked in.

To export the current map view, head to **Project > Import/Export** and pick either **Export Map to Image...** or **Export Map to PDF...**. Both open a dialog where you set the extent (defaults to the current view, but you can calculate from a layer or draw a custom rectangle on the canvas), the scale, the resolution, and the output dimensions in pixels. Adjusting one recalculates the others from center, and you can lock the aspect ratio to keep things proportional.

See `fig01.png`.

Below those basics, you'll find checkboxes for **Draw active decorations** (scale bar, north arrow, grid, title), **Draw annotations**, and **Append georeference information** — the last one writes a world file alongside your image (e.g. `.PNGW`) or embeds it directly into the PDF.

The PDF export adds a few extras: **Export RDF metadata** (title, author, date), **Create Geospatial PDF** with optional vector feature information embedded, **Simplify geometries to reduce output file size**, and a **Text export** setting that controls whether labels become editable text objects or outlines. There's also a **Rasterize map** toggle if you want a flat image inside the PDF wrapper.

See `fig02.png`.

Once you've dialed in the settings, hit **Save** to choose your file location and format. For images, you can also click **Copy to Clipboard** to paste the rendered map straight into another app like LibreOffice or GIMP.

For DXF export — useful when handing layers to CAD users — go to **Project > Import/Export > Export Project to DXF...**. This exports multiple layers into a single `.dxf` file. You pick the destination file, symbology mode, encoding, target CRS, and then check off which layers to include (or pull them from a map theme). Each layer can optionally be split into multiple DXF layers based on an attribute field's values. Additional options let you force 2D output, export only features in the current extent, control label export as MTEXT or TEXT elements, and set lines to zero-width for cleaner CAD editing.

See `fig03.png`.
