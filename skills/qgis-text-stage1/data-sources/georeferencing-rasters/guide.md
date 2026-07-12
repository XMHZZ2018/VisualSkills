# Georeferencing Rasters (QGIS 3.44)

The Georeferencer assigns real-world coordinates to an unpositioned raster by matching Ground Control Points (GCPs) on the image to known locations. Open it via **Layer > Georeferencer**.

Load your raster with the **Open Raster** button in the toolbar. The image appears in the Georeferencer's working area, ready for you to start placing control points.

Switch to the **Add GCP Point** tool, click a recognizable spot on your raster, then either type coordinates manually (DMS, decimal degrees, or projected) or hit **From Map Canvas** to click the matching location on an already-georeferenced layer loaded in QGIS. The CRS is set automatically when picking from the canvas. Aim for at least four well-distributed points — more points yield a better fit.

Once your GCPs are placed, open **Transformation Settings**. Choose a transformation type: **Linear** or **Helmert** for well-made maps that just need positioning/rotation (these only write a world file); **Polynomial 1** for uniform shear; **Polynomial 2–3** for curved distortion; **Projective** for angled photographs; or **Thin Plate Spline** for warped or damaged sheets. Pick a resampling method — Nearest Neighbour preserves pixel values, while Cubic or Lanczos produce smoother visuals. Set your **Target CRS**, choose an output file path, and optionally enable **Load in project when done**.

Hit **Start Georeferencing**. QGIS writes a new GeoTIFF (or world file for Linear/Helmert) and, if you checked the option, loads it straight into your map canvas. Your GCPs are saved alongside the raster as a `.points` file, so you can reopen and refine them later.

Pro tip: use keyboard arrows to pan and the scroll wheel to zoom — saves constant tool-switching. The **Link Georeferencer to QGIS** / **Link QGIS to Georeferencer** buttons sync the two views so you can visually compare alignment as you work.
