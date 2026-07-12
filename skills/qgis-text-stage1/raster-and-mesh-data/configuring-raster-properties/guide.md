# Configuring Raster Layer Properties (QGIS 3.44)

Open the properties dialog by double-clicking a raster layer in the Layers panel, or right-click it and choose **Properties**. Everything lives in tabs along the left side.

**Band Rendering** — Under the **Symbology** tab, pick a render type that fits your data. Use *Multiband color* for satellite imagery (assigns bands to R/G/B channels), *Singleband gray* for simple elevation or relief maps, *Singleband pseudocolor* to apply a continuous color ramp to values like elevation, *Hillshade* for shaded relief from a DEM, or *Contours* for on-the-fly contour lines. Each renderer lets you set a contrast enhancement method and control min/max value mapping — try *Cumulative count cut* (2%–98%) to trim outliers without losing detail.

**Transparency** — Switch to the **Transparency** tab to drag the **Global Opacity** slider down and let underlying layers show through. You can also flag specific pixel values as no-data (they'll render transparent) or build a custom pixel list with per-value percent transparency for fine-grained control.

**Pyramids** — For large rasters that feel sluggish to pan, open the **Pyramids** tab. Select resolution levels from the list, choose an overview format (**External** is safest — it writes a `.ovr` sidecar rather than modifying your source file), pick a resampling method like *Average* or *Cubic*, then click **Build Pyramids**. Back up your raster first if you choose *Internal*, since that operation is irreversible.

**Histogram** — The **Histogram** tab plots the distribution of pixel values per band. Hit **Compute Histogram** to generate it, then use the **Prefs/Actions** dropdown to toggle individual band visibility, zoom to min/max markers, or update the layer's styling directly from the histogram's min/max fields.

**Resampling** — Still in **Symbology**, scroll to the Resampling section. Switch from *Nearest Neighbour* to *Bilinear* or *Cubic* to smooth pixelation when zoomed in. Enable **Early resampling** for tile-based layers to let the provider handle it at native resolution.
