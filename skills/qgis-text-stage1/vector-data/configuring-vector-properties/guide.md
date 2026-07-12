Now I have a comprehensive understanding of the source material. Let me write the concise reference guide.

# Configuring Vector Layer Properties (QGIS 3.44)

Open the Layer Properties dialog by double-clicking a vector layer in the **Layers** panel, or right-clicking it and choosing **Properties...**. You can also reach it via **Layer > Layer Properties...** when the layer is selected.

**Symbology** is where you control how features look on the map. Pick a renderer from the dropdown at the top — **Single Symbol** applies one style to everything, **Categorized** splits features by discrete field values, **Graduated** bins a numeric field into classes, and **Rule-based** lets you write expression filters for full control. For point layers, you also get **Point Displacement**, **Point Cluster**, and **Heatmap** renderers. Hit **Classify** after choosing your field and color ramp to generate classes automatically.

Under **Layer rendering** (bottom of the Symbology tab), adjust overall **Opacity**, set **Blending mode** for compositing effects, enable **Draw Effects** for drop shadows or glows, and toggle **Control feature rendering order** to sort features by an attribute for z-ordering.

**Labels** are configured by switching the dropdown from **No Labels** to **Single Labels** (or **Rule-based Labeling** for conditional logic). Choose the field or expression for label text, then fine-tune font, buffer, placement, and rendering in the sub-tabs. Use the **Automated placement settings** button to manage collision resolution across all layers.

The **Rendering** tab controls **Scale dependent visibility** (min/max scales), **Simplify geometry** for performance at small scales, and **Force layer to render as raster** to keep PDF/SVG exports lightweight. You can also set a **Fixed reference scale** so symbol sizes stay consistent.

For **Metadata**, switch to the **Metadata** tab and fill in identification (title, abstract, keywords), access constraints, extent, contacts, and links. The read-only **Information** tab gives you a quick summary of CRS, feature count, storage format, and any custom properties already attached to the layer.

Use the **Style** menu at the bottom of the dialog to save, load, or switch between named styles — handy for toggling between different visual representations without recreating everything from scratch.
