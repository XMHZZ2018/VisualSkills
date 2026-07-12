# Working with Vector Tiles (QGIS 3.44)

Vector tiles deliver geographic data as pre-clipped, zoom-level-specific packets — far lighter than raster tiles and more efficient than shipping full vector datasets. They carry no built-in styling, so QGIS handles all the cartography on your end.

## Adding a Vector Tile Layer

Open **Layer > Data Source Manager** and switch to the **Vector Tile** tab. You can connect to remote XYZ sources (e.g., `http://example.com/{z}/{x}/{y}.pbf`), point to a local tile directory using a `file:///` XYZ template, or load an MBTiles file directly. If your tile service provides a Style URL, paste it in during connection setup — QGIS will pull symbology automatically once the layer loads.

## Styling with Rules

Double-click your vector tile layer to open **Layer Properties > Symbology**. Styling works through a rules list: each rule targets a specific sub-layer (like `landuse` or `roads`), a zoom range, and an optional filter expression. Hit **Add rule**, pick the geometry type (Marker, Line, or Fill), and configure its symbol. Toggle **Visible rules only** at the top to cut the list down to what's active at your current zoom — invaluable when you're debugging a busy stylesheet.

See `fig01.png`.

You can also import a MapBox GL JSON style file or a QML from the **Styles** menu at the bottom of the tab, which is the fastest way to get a polished look without building rules from scratch.

## Labels

The **Labels** tab follows the same rules-based approach. Add a labeling rule, bind it to a layer and zoom range, and configure placement and text style just like you would for any vector layer.

## Layer Rendering and Scale Visibility

Back in **Symbology**, the bottom section lets you dial **Opacity** and set a **Blending mode** across the whole tile layer. For coarser control, the **Rendering** tab offers scale-dependent visibility — set a min/max scale so the layer disappears when you zoom too far in or out.

## Source and Metadata

The **Source** tab shows the layer name, CRS, and (for `.mbtiles`/`.vtpk` files) lets you swap the underlying file path. The **Information** tab gives a read-only summary of zoom levels, CRS details, and any metadata attached to the source. Use the **Metadata** tab to author your own metadata report for the layer.
