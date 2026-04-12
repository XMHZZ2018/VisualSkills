Manage raster layer display and analysis through the Layer Properties dialog and Raster menu tools.

## Opening Raster Layer Properties

- **Double-click** a raster layer in the Layers panel, or **right-click → Properties**
- The dialog has tabs: Information, Source, Symbology, Transparency, Labels, Histogram, Rendering, Temporal, Pyramids, Elevation, Metadata, Legend, Display, Attribute Tables, QGIS Server
- For faster styling without closing the dialog, use the **Layer Styling Panel** (F7) — it mirrors the Symbology and Transparency tabs with live preview

## Information & Source Tabs

**Information** (read-only): Shows layer path, CRS, band statistics, pixel size, compression, no-data values. Use this to quickly verify data type and extent.

**Source**: Change the display name or fix an incorrect CRS (click the projection button next to the CRS field). Use this only to *assign* a CRS, not to reproject — for reprojection use Raster → Projections → Warp.

## Symbology: Choosing a Renderer

**Layer Properties → Symbology → Band rendering → Render type dropdown**

| Data type | Recommended renderer |
|---|---|
| Satellite/aerial imagery (3+ bands) | Multiband color |
| Indexed palette (topo maps) | Paletted/Unique values |
| Single continuous band (DEM, rainfall) | Singleband pseudocolor |
| Grayscale/shaded relief | Singleband gray |
| Terrain visualization | Hillshade |
| On-the-fly isolines | Contours |

### Multiband Color
1. Set Red/Green/Blue band dropdowns to the appropriate bands
2. QGIS auto-fills Min/Max per band — override in **Min/Max Value Settings** if needed
3. Set **Contrast enhancement**: "Stretch to MinMax" works well for most imagery

> **Pitfall**: To view a single band of a multiband raster, don't set other bands to "Not Set" — switch the renderer to **Singleband gray** and pick your target band there.

### Singleband Pseudocolor
1. Select the band
2. Choose a color ramp from the dropdown
3. Set classification mode (Equal Interval, Quantile, etc.) and number of classes
4. Click **Classify** to generate the color map
5. Double-click any color swatch to change it; double-click a label to rename it

### Paletted/Unique Values
- Colors are auto-assigned from the embedded palette
- Double-click a color to change it; double-click a label to rename it
- Right-click selected rows to batch-change color, opacity, or label
- Use **Advanced options (...)** button to load/export color maps from file

### Hillshade
Select the elevation band, set Azimuth (light direction, default 315°) and Altitude (light angle, default 45°). Enable **Multidirectional** for softer shadows.

## Transparency Tab

Set global layer opacity with the **Global opacity** slider (0–100%). To mark specific pixel values as transparent, add rows to the **Custom Transparency Options** table with the pixel value(s) and transparency percentage.

> **Pitfall**: No-data values defined in the file are handled separately from custom transparency — check the Information tab to see what no-data value is embedded in the file.

## Resampling (under Symbology)

At the bottom of the Symbology tab under **Resampling**:
- **Zoomed in**: use Bilinear or Cubic for smooth appearance; Nearest Neighbor preserves discrete values (land cover classes)
- **Zoomed out**: use Average for cleaner downsampled display

## Raster Calculator

**Raster → Raster Calculator**

The dialog has two main sections:
- **Raster bands** list (left): all loaded rasters. Double-click to insert into the expression. Format: `layername@bandnumber` (e.g., `DEM@1`)
- **Result layer** section: set output path and format, or check **Create on-the-fly raster** for a virtual layer (no file written)

### Common expressions

```
# Convert meters to feet
"elevation@1" * 3.28

# Mask values below 0
("elevation@1" >= 0) * "elevation@1"

# Classify into two classes
("elevation@1" < 50) * 1 + ("elevation@1" >= 50) * 2

# Same using IF
if( "elevation@1" < 50, 1, 2 )
```

**Workflow**:
1. Open Raster → Raster Calculator
2. Double-click a band from the list to add it to the expression
3. Click operator buttons or type the expression manually
4. Set output path/format (or enable on-the-fly)
5. Check **Add result to project** to load it automatically
6. Click **OK**

> **Pitfall**: On-the-fly virtual rasters stay linked to source files — moving or deleting source rasters breaks them. Make them permanent via right-click → Export → Save As on the virtual layer.

## Pyramids Tab

For large rasters, pre-built pyramids improve rendering speed. In **Layer Properties → Pyramids**, select resolution levels and click **Build Pyramids**. Choose **Internal** (stored in the file, requires write access) or **External** (creates a `.ovr` sidecar file).

> **Pitfall**: Building pyramids modifies or creates files on disk. For read-only network files, use External pyramids.

## Histogram Tab

**Layer Properties → Histogram → Compute Histogram** — shows pixel value distribution per band. Useful for diagnosing contrast issues before adjusting Min/Max values in Symbology.