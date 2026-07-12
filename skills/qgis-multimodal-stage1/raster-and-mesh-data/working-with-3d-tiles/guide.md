# Working with 3D Tiles (QGIS 3.44)

3D Tiles are a streaming format for rendering large-scale 3D geospatial datasets — think city-scale building models or terrain meshes. QGIS 3.44 supports Cesium 3D Tiles (buildings, photorealistic cities from Google or Cesium Ion) and Quantized Mesh tiles (terrain elevation). Keep in mind that only tilesets using EPSG:4978 and explicit tiling are currently supported, and only the Batched 3D Model (`b3dm`) and glTF 2.0 tile formats work so far.

To add a 3D tile layer, use **Layer > Add Layer > Add 3D Tiled Scene Service** and point it at your tileset URL or local `tileset.json`. Once loaded, open the layer's properties by double-clicking it in the **Layers** panel.

Under **Symbology**, the default renderer shows the tiles with their original texture. Switch the drop-down to **Wireframe** if you want to inspect the underlying mesh geometry — you can style the fill and lines just like vector polygons. Enable **Use texture colors** for a quick averaged-color overview of large datasets without full texture rendering. The **Maximum error** slider controls detail level: smaller values (e.g., 0.1 mm) mean crisper detail but heavier rendering; larger values trade fidelity for speed. You'll also find **Opacity** and **Blending mode** controls here for compositing the layer with others.

See `fig01.png`.

The **3D View** tab governs how tiles behave in a 3D map. **Maximum screen space error** sets when tiles swap to higher or lower detail — lower values load finer tiles sooner. Toggle **Show bounding boxes** on when debugging tile loading issues. To actually see your data in 3D, open **View > New 3D Map View**.

See `fig02.png`.

In the **Rendering** tab, set **Scale dependent visibility** to restrict the layer to a min/max scale range — handy when 3D tiles clutter a zoomed-out 2D overview. The **Elevation** tab lets you apply a vertical **Scale** factor and **Offset** to adjust how Z values are interpreted, useful when your tileset's vertical datum doesn't align with your project terrain.

The **Source** tab is where you rename the layer and verify or override its CRS if it was incorrectly declared. **Information** gives a read-only summary (provider URL, zoom levels, extent, CRS details), and **Metadata** lets you attach descriptive metadata to the layer for cataloging.
