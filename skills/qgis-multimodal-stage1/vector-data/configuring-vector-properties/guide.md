# Configuring Vector Layer Properties (QGIS 3.44)

To open the Layer Properties dialog, double-click any vector layer in the **Layers** panel, or right-click it and choose **Properties…**. You can also go to **Layer > Layer Properties…** while the layer is selected. The dialog is organized into tabs along the left side — Information, Source, Symbology, Labels, Rendering, Metadata, and many more.

See `fig01.png`.

The **Source** tab is where you rename the layer (for display purposes only), verify or reassign the coordinate reference system, and point to a different file on disk if your data has moved. If you only want a subset of features visible, click **Query Builder** at the bottom — write a SQL-like WHERE clause (e.g., `"type" = 'residential'`) and only matching features will appear in the project.

Under **Symbology**, you pick how features are drawn. The renderer dropdown at the top gives you options: **Single Symbol** applies one look to everything, **Categorized** assigns a distinct symbol per unique value in a field, **Graduated** breaks a numeric field into classes with a color ramp or scaled sizes, and **Rule-based** lets you write arbitrary expressions for full control. For point layers you also get **Point Displacement**, **Point Cluster**, and **Heatmap** renderers. Choose a field or expression as the classification value, pick a color ramp, then hit **Classify** to generate classes automatically.

See `fig02.png`.

Below the renderer settings, the **Layer Rendering** section lets you adjust overall layer opacity, set blend modes (like Multiply or Screen), enable **Draw Effects** (drop shadows, blur, glow), and control feature rendering order with an expression-driven z-index.

The **Labels** tab controls text annotation on features. Select **Single Labels** from the dropdown, pick the attribute (or write an expression) for the label value, then configure font, size, color, buffer, background, shadow, placement, and rendering across the sub-tabs. For complex scenarios, switch to **Rule-based Labeling** to show different label styles depending on feature attributes or scale. The **Automated placement settings** button (top-right) configures project-wide collision resolution — how many candidate positions QGIS evaluates, whether truncated labels appear at map edges, and whether labels export as text or paths in PDF/SVG.

See `fig03.png`.

The **Rendering** tab sets scale-dependent visibility (so a layer disappears when you zoom too far in or out) and simplification options for faster drawing at small scales. Finally, the **Metadata** tab lets you fill in title, abstract, keywords, and contact information that travels with the layer — useful for data catalogs and WMS/WFS services published via QGIS Server.
