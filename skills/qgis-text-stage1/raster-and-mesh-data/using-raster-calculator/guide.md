No inline image references in the markdown. I have everything I need from the text content. Here's the guide:

# Using the Raster Calculator (QGIS 3.44)

The Raster Calculator lets you do map algebra — pixel-by-pixel math across one or more raster layers — and write the result to a new layer. Open it from **Raster > Raster Calculator**.

The **Raster Bands** list on the left shows every loaded raster layer. Double-click a band to drop it into the expression box. Bands are referenced as `layer_name@band_number`, so the first band of a layer called `DEM` becomes `DEM@1`.

Build your expression using the operator buttons or just type directly. You get arithmetic (`+`, `-`, `*`, `sqrt`, `abs`, `ln`), trig (`sin`, `cos`, `tan`), comparisons (`=`, `!=`, `<`, `>=`), logical operators (`IF`, `AND`, `OR`), and stats (`min`, `max`). Comparisons return 1 (true) or 0 (false), which is handy for masking.

In the **Result layer** section, set your output path and format — or tick **Create on-the-fly raster** to get a virtual layer whose pixels are computed live without writing to disk. You can also constrain the **Spatial extent** and adjust the output **Resolution** (columns/rows). Check **Add result to project** to load the output into your layer panel automatically.

A few expression patterns worth memorizing: convert meters to feet with `"elevation@1" * 3.28`. Mask out negative values with `("elevation@1" >= 0) * "elevation@1"`. Classify into two bins with `if(elevation@1 < 50, 1, 2)`.
