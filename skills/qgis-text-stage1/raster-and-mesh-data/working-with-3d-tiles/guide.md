The markdown file has no inline image references with paths — just figure captions. I have enough from the text content to write the guide.

# Working with 3D Tiles (QGIS 3.44)

3D Tiles stream large-scale 3D geospatial datasets using a hierarchical level-of-detail structure — think city-scale building models or terrain meshes that load progressively as you zoom in. QGIS 3.44 supports Cesium 3D Tiles (buildings/cities, including Google Photorealistic 3D Tiles) and Quantized Mesh (terrain elevation). Only tilesets in EPSG:4978 with explicit tiling are currently supported.

To add a 3D tile layer, go to **Layer > Add Layer > Add 3D Tiled Scene Layer** and point it at a local `tileset.json` or a remote service URL (Cesium Ion, Google, etc.).

Once loaded, open the layer's **Properties** dialog. Under **Symbology**, the default renderer shows the original texture. Switch to **Wireframe** if you want to inspect the mesh geometry instead — you can style the fill and line just like vector polygons. Enable **Use texture colors** for a fast averaged-color overview on large datasets. Tweak **Maximum error** to balance detail vs. performance: smaller values (0.1 mm) render more triangles, larger values (5 mm) speed things up with visible gaps. **Opacity** and **Blending mode** work the same as other layer types.

For 3D viewing, open **View > New 3D Map View**. In the layer's **3D View** properties, lower the **Maximum screen space error** to force higher-quality tiles sooner, or enable **Show bounding boxes** to debug tile loading. Under **Rendering**, set scale-dependent visibility so tiles only draw within a useful zoom range. The **Elevation** tab lets you apply a vertical **Scale** factor and **Offset** to adjust how Z values map to terrain height.
