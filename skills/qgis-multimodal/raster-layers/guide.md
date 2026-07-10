## Raster Layer Management in QGIS 3.44: properties, symbology, and analysis tools for raster data.

---

## Opening Layer Properties

Double-click a raster layer in the **Layers panel**, or right-click → **Properties**. The **Raster Layer Properties** dialog opens with multiple tabs across the left sidebar. You can also use the **Layer Styling Panel** (F7) for live preview of symbology changes without closing the dialog.

Read the screenshot `fig01.png` in this directory — it shows the Information tab icon, the first tab in the dialog sidebar.

---

## Layer Properties Tabs

### Information
Read-only summary of the layer: file path, provider, data type, CRS, band statistics, pixel size, compression, and extent. Use this tab to quickly verify what you've loaded without running any tools.

### Source
Read the screenshot `fig03.png` in this directory — it shows the Source tab icon.

The **Source** tab lets you:
- Rename the layer (display name in the Layers panel)
- View or reassign the **CRS** — click the projection button next to the CRS field to open the CRS Selector. Use this only to *correct* a wrongly assigned CRS, not to reproject data.
- Replace the layer's file path by editing the path field or pressing **…** to browse.

### Symbology
Read the screenshot `fig05.png` in this directory — it shows the Symbology tab icon.

The **Symbology** tab has three sections:

**Band rendering** — choose the renderer type from the dropdown:

| Renderer | When to use |
|---|---|
| Multiband color | Multi-band images (satellite, RGB) |
| Paletted/Unique values | Indexed palette or categorical rasters |
| Singleband gray | Single-band without palette (shaded relief) |
| Singleband pseudocolor | Continuous palette (elevation, temperature) |
| Single color | Uniform display regardless of pixel values |
| Hillshade | Derive hillshade from a single band |
| Contours | On-the-fly contour lines from a band |

**Min/Max Value Settings** — controls how QGIS stretches the color ramp. Options include *Cumulative count cut*, *Min/max*, and *Mean ± standard deviations*. Combined with a **Contrast enhancement** method (Stretch to MinMax, Clip to MinMax, etc.).

**Layer rendering** — overall blending mode and opacity for the layer.

**Resampling** — set zoom-in and zoom-out resampling methods (Nearest Neighbour, Bilinear, Cubic) to balance speed vs. quality.

### Transparency
Read the screenshot `fig07.png` in this directory — it shows the Transparency tab icon.

Set global **opacity** with the slider, or define **custom transparency** by adding pixel value ranges that should be rendered transparent. Useful for masking NoData regions or specific value ranges.

### Histogram
Read the screenshot `fig11.png` in this directory — it shows the Histogram tab icon.

Displays a value distribution histogram per band. Click **Compute Histogram** to populate it. Use the histogram to identify suitable Min/Max stretch values before configuring symbology.

### Rendering
Read the screenshot `fig12.png` in this directory — it shows the Rendering tab icon.

Controls scale-dependent visibility, map tips, and provider-level refresh settings.

### Temporal
Read the screenshot `fig13.png` in this directory — it shows the Temporal tab icon.

Configure time-based visibility for use with the **Temporal Controller** panel — set a fixed time range or link to a field/attribute.

### Pyramids
Read the screenshot `fig14.png` in this directory — it shows the Pyramids tab icon.

Build reduced-resolution overviews to speed up rendering at small scales. Select resolution levels, choose a resampling method, and click **Build Pyramids**. Note: building pyramids modifies the file on disk (or creates a sidecar `.ovr` file).

### Elevation
Read the screenshot `fig15.png` in this directory — it shows the Elevation tab icon.

Configure how the raster is used as a terrain source for 3D views and elevation profiles: set vertical scale, offset, and band to use for Z values.

---

## Raster Analysis: Raster Calculator

**Menu:** `Raster` → `Raster Calculator…`

Read the screenshot `fig02.png` in this directory — it shows the full Raster Calculator dialog with the Raster Bands list on the left, Result Layer settings on the right, an Operators grid, and the expression field at the bottom.

### Workflow

1. Open `Raster` → `Raster Calculator…`
2. In **Raster Bands**, double-click a layer/band to add it to the expression. Bands are referenced as `layername@bandnumber` (e.g., `elevation@1`).
3. Use the **Operators** buttons to insert arithmetic (`+`, `-`, `*`, `/`), trigonometric (`sin`, `cos`, `tan`), comparison (`=`, `!=`, `<`, `>=`), logical (`IF`, `AND`, `OR`), and statistical (`min`, `max`) operators.
4. In **Result Layer**:
   - Set **Output layer** path and **Output format** (e.g., GeoTIFF)
   - Or check **Create on-the-fly raster** to produce a virtual layer without writing to disk
   - Set the **Extent** using the extent selector (from layer, map canvas, bookmark, or manual coordinates)
   - Set **Resolution** (columns × rows); mismatched input layers are resampled via nearest neighbor
   - Check **Add result to project** to load the output automatically
5. Verify **Expression valid** shows at the bottom, then click **OK**.

### Expression Examples

**Meters to feet:**
```
"elevation@1" * 3.28
```

**Mask values below 0:**
```
("elevation@1" >= 0) * "elevation@1"
```

**Classify into two classes:**
```
("elevation@1" < 50) * 1 + ("elevation@1" >= 50) * 2
```

**Using IF syntax:**
```
if( elevation@1 < 50, 1, 2 )
```

---

## Raster Calculator Expression Dialog

**Menu:** `Raster` → `Raster Calculator Expression…` (also accessible from Processing algorithms *Raster calculator* and *Raster calculator (virtual)*)

Read the screenshot `fig10.png` in this directory — it shows the Raster Calculator Expression dialog: a Layers list on the left (showing loaded rasters), an Operators grid on the right, and the expression text box at the bottom with an example mask expression.

This variant is a standalone expression editor used within Processing. Layers are listed by name (without the `@band` suffix in the list, but referenced as `layername@bandnumber` in expressions). The operator set is the same as the main calculator. Click **Ok** to confirm the expression.

---

## Key Shortcuts & Tips

- **Layer Styling Panel** (F7): live-update symbology without reopening the dialog
- **Right-click layer → Export → Save As…**: export a virtual raster calculator result to a permanent file
- To view one band of a multiband raster in grayscale: use **Singleband gray** renderer and select the desired band — do not set other bands to "Not Set" in Multiband mode
- **Load Color Map from File**: in Paletted/Unique values renderer, click **…** (Advanced options) below the color table to import or export `.txt` color map files