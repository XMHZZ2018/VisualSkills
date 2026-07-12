# Using the Raster Calculator (QGIS 3.44)

The Raster Calculator lets you do map algebra — pixel-by-pixel math across one or more raster layers — and write the result to a new layer. Open it from **Raster > Raster Calculator**.

The dialog shows a **Raster bands** list on the left containing every raster layer currently loaded in your project. Double-click any band to drop it into the expression field. Bands are referenced as `layer_name@band_number`, so the first band of a layer called `DEM` becomes `DEM@1`.

See `fig01.png`.

Build your expression using the operator buttons or just type directly into the expression box. You get arithmetic (`+`, `-`, `*`, `sqrt`, `abs`, `ln`), trig (`sin`, `cos`, `tan`), comparisons (`=`, `!=`, `<`, `>=`), logical operators (`IF`, `AND`, `OR`), and basic stats (`min`, `max`). Comparisons return 1 for true and 0 for false, which makes them perfect for masking.

In the **Result layer** section, decide where the output goes. By default, it writes a new file to disk — pick a path and format. Alternatively, check **Create on-the-fly raster** to produce a virtual layer whose pixels are calculated dynamically from the source bands (no new file, but the source rasters must stay in place).

You can also set the output **Spatial extent** using the extent selector widget, and control **Resolution** by specifying column and row counts. If these differ from the input, values get resampled with nearest-neighbor. Toggle **Add result to project** to have the output appear in your layer panel automatically.

A few common recipes to get you started:

**Convert meters to feet** — straightforward multiplication:
```
"elevation@1" * 3.28
```

**Mask out values below zero** — the comparison acts as a 0/1 multiplier:
```
("elevation@1" >= 0) * "elevation@1"
```

**Classify into two elevation classes** — combine conditions or use `IF`:
```
("elevation@1" < 50) * 1 + ("elevation@1" >= 50) * 2
```
or equivalently: `if(elevation@1 < 50, 1, 2)`

That's really the core of it — load bands, write an expression, choose an output, and run. The Processing Toolbox also offers **Raster calculator** and **Raster calculator (virtual)** algorithms if you prefer working in a model or batch context.
