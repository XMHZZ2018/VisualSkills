# Setting Layer and Project CRS (QGIS 3.44)

Every layer and project in QGIS carries a Coordinate Reference System that tells QGIS how to map raw coordinates onto the Earth's surface. QGIS supports ~7,000 standard CRSs (identified by codes like `EPSG:4326` for WGS 84) and handles on-the-fly reprojection automatically — layers in different CRSs overlay correctly without manual conversion.

**Layer CRS.** When you load a layer, QGIS reads the CRS from metadata (e.g., a `.prj` file for Shapefiles). If it can't determine one, the behavior depends on your setting in **Settings → Options → CRS and Transforms → CRS Handling**. Under *CRS for Layers*, you can tell QGIS to leave unknown layers unreferenced, prompt you to pick a CRS, use the project CRS, or fall back to a default. To manually assign or fix a layer's CRS, select one or more layers in the Layers panel and press `Ctrl+Shift+C` (or right-click → **Set CRS of Layer(s)**), then choose the correct CRS. This doesn't reproject the data — it just tells QGIS how to interpret the existing coordinates.

**Project CRS.** The project CRS controls how the map canvas renders everything. Set it via **Project → Properties… → CRS** tab, or just click the CRS indicator in the bottom-right status bar. You can filter by name or EPSG code, browse the full list, or pick from recently used systems. The preview map shows the valid extent for whichever CRS you highlight. A quick shortcut: right-click any layer in the Layers panel and choose **Set Project CRS from Layer**.

**Default for new projects.** Under **Settings → Options → CRS and Transforms → CRS Handling**, the *CRS for Projects* section lets you either adopt the CRS of the first layer added or lock in a fixed default (e.g., `EPSG:4326`).

**Datum transformations.** When reprojecting between CRSs, multiple transformation paths may exist with varying accuracy. Under **Settings → Options → Transformations**, enable *Ask for datum transformation if several are available* to be prompted, or pre-configure preferred transformations for specific source/destination pairs. Project-specific overrides live in **Project → Properties… → Transformations**.
