# Configuring Raster Layer Properties (QGIS 3.44)

To open the properties dialog, double-click a raster layer in the Layers panel (or right-click and choose **Properties**). The dialog has tabs running down the left side — Symbology, Transparency, Histogram, Pyramids, and more. You can also tweak many of these settings live via the **Layer Styling Panel** (no OK/Apply round-trip needed).

**Band Rendering** lives under the **Symbology** tab. Pick a render type from the dropdown at the top: *Multiband color* maps bands to RGB channels, *Singleband pseudocolor* applies a continuous color ramp to elevation or similar data, *Singleband gray* gives you a simple grayscale, *Hillshade* generates relief shading from a DEM, and *Contours* draws isolines on the fly. For satellite imagery, Multiband color is usually auto-detected; for a DEM you'll likely switch to Singleband pseudocolor, choose a color ramp, set interpolation to Linear, and hit **Classify**.

See `fig01.png`.

Under **Min/Max Value Settings** (collapsed by default within Symbology), control how pixel value extremes affect the stretch. "Cumulative count cut" at 2%–98% is a good default that clips outliers. You can also choose "Mean +/- standard deviation" if a few extreme pixels are blowing out your display.

The **Transparency** tab has three sections. **Global Opacity** is a simple slider — drag it down to let underlying layers bleed through (great for overlaying a hillshade beneath a classified layer). Below that, set **No Data Value** so those pixels render as transparent (or pick a custom color). The **Custom Transparency Options** table lets you specify pixel value ranges and assign a percent-transparent to each — handy for hiding specific value bands without reclassifying.

See `fig02.png`.

The **Histogram** tab shows the distribution of values across all bands. Click **Compute Histogram** to generate it. Use the **Prefs/Actions** menu to toggle individual band visibility, zoom to min/max markers, or update the symbology min/max directly from the histogram — a quick way to refine your stretch without switching tabs.

**Pyramids** improve performance for large rasters by building reduced-resolution overviews. In the **Pyramids** tab, select resolution levels from the list, choose a resampling method (Average or Cubic are common choices for continuous data, Nearest Neighbour for classified), pick an overview format — **External** writes a `.ovr` sidecar file and leaves your original untouched, while **Internal** embeds them in the raster itself (irreversible). Click **Build Pyramids** when ready. You'll need write access to the directory containing the raster.

See `fig03.png`.

For **Resampling** (bottom of the Symbology tab), switch from "Nearest neighbour" to "Bilinear" or "Cubic" if your raster looks blocky when zoomed in. Enable **Early resampling** for tile-based layers — it lets the provider handle the downsampling at its native resolution, producing smoother zoomed-in views.
