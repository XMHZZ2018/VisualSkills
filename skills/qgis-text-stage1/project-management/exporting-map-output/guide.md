# Exporting Map Output (QGIS 3.44)

You can quickly export the current map canvas without building a full print layout. Head to **Project > Import/Export** and pick either **Export Map to Image…** or **Export Map to PDF…**.

Both options open a dialog where you set the **Extent** (current view, a layer's bounds, or draw a custom rectangle), choose a **Scale**, and adjust **Resolution** and output dimensions in pixels. The width/height lock keeps your aspect ratio if you resize one value.

Check **Draw active decorations** to include your scale bar, north arrow, or grid in the output. Enable **Draw annotations** if you want those exported too. **Append georeference information** writes a world file (`.pngw`, `.jpgw`, etc.) alongside your image, or embeds it directly into a PDF.

For PDF specifically, you get extra controls: **Export RDF metadata** (title, author, date), **Create Geospatial PDF** with optional vector feature information baked in, **Simplify geometries to reduce output file size**, and a **Text export** setting to render labels as text objects or outlines. You can also **Rasterize map** if you need a flattened result.

Once configured, hit **Save** to write the file — or use **Copy to Clipboard** (image export only) to paste directly into another app.

For DXF output, go to **Project > Import/Export > Export Project to DXF…**. This exports multiple vector layers at once into a single `.dxf` file. Pick your layers (or pull them from a map theme), set symbology mode, encoding, and target CRS. You can split features into DXF layers using a field value, and optionally limit export to the current map extent.
