# Georeferencing Rasters (QGIS 3.44)

Open the Georeferencer from **Layer > Georeferencer**. The tool lives in its own dialog (or docked panel, if you prefer — toggle that under **Settings > Configure Georeferencer**). Load your unreferenced raster with the **Open Raster** button in the toolbar.

See `fig01.png`.

Now you need Ground Control Points — at least four, more is better. Activate the **Add GCP Point** tool, click a recognizable spot on the raster, and you'll get a coordinate entry dialog. You can type coordinates manually (DMS, decimal degrees, or projected), or hit **From Map Canvas** to click the matching location on an already-georeferenced layer loaded in the main QGIS window. The CRS gets set automatically when you pick from the canvas.

See `fig02.png`.

A handy trick: tick **Automatically hide georeferencer window** so the Georeferencer ducks out of the way while you click reference points on the main canvas. Use keyboard arrows to pan and the scroll wheel to zoom — saves constant tool-switching between Pan and Add GCP Point.

Your GCPs are saved to a sidecar `.points` file beside the raster, so you can reload and refine them later with **Load GCP Points** / **Save GCP Points As**.

Once you have enough points, open **Transformation Settings** (the wrench icon). Pick a transformation type: **Linear** or **Helmert** for well-made maps that just need positioning/rotation (these only write a world file, no pixel resampling). **Polynomial 1** handles shear; **Polynomial 2–3** corrects curvature but needs 6–10+ GCPs. **Thin Plate Spline** rubber-sheets badly distorted maps to force-fit every GCP exactly.

See `fig03.png`.

Choose a resampling method — Nearest Neighbour preserves original pixel values, Cubic or Lanczos look smoother. Set your **Target CRS**, pick an output path (defaults to `[filename]_modified.tif` in the same folder), and optionally enable **Set Target Resolution**, **Use 0 for transparency**, or **Load in project when done** so the result drops straight onto your map canvas.

Hit **Start Georeferencing** and QGIS writes your new GeoTIFF. Check the residual errors in the GCP table at the bottom of the dialog — high residuals on a single point usually mean a mis-click worth correcting.
