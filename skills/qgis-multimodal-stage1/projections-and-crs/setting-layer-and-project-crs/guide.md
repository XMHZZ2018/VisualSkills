# Setting Layer and Project CRS (QGIS 3.44)

Every layer in QGIS carries (or should carry) a CRS that tells the software how its raw coordinates map onto the Earth's surface. When you load a layer, QGIS tries to detect the CRS automatically — for Shapefiles it reads the `.prj` sidecar file, for PostGIS layers it pulls the SRID from the database. If detection fails, what happens next depends on your settings.

Head to **Settings > Options… > CRS and Transforms > CRS Handling** to configure the fallback behavior. Under *CRS for Layers* you can tell QGIS to leave unrecognized layers as "unknown CRS," prompt you to pick one manually, adopt the project CRS, or apply a default you specify. The "prompt" option is safest when you're unsure — picking the wrong CRS will silently place your data in the wrong spot on the globe.

See `fig01.png`.

To assign or fix a CRS on layers that already exist in your project, select them in the **Layers** panel, then press **Ctrl+Shift+C** (or right-click and choose **Set CRS of layer(s)**). Pick the correct CRS and hit **OK**. This doesn't reproject the underlying data — it just tells QGIS how to interpret the coordinates.

The project CRS is separate: it controls how the map canvas reprojects everything for display. QGIS handles on-the-fly reprojection transparently, so layers in different CRSs still line up. To change the project CRS, go to **Project > Properties… > CRS**, use the filter to find your target system (e.g., type `32633` to find UTM zone 33N), and confirm with **OK**. You'll also see the current project CRS displayed in the lower-right corner of the status bar — clicking it opens the same dialog.

See `fig02.png`.

A quick shortcut: right-click any layer in the **Layers** panel and choose **Set project CRS from Layer** to instantly adopt that layer's CRS for the whole project.

New projects default to `EPSG:4326` (WGS 84). You can change this under **Settings > Options… > CRS and Transforms > CRS Handling** in the *CRS for Projects* section — set it to use the CRS of the first layer added, or pick a fixed default that suits your region.

The CRS selector dialog (which appears in both layer and project contexts) shows recently used systems at the top for fast access, a searchable list of all ~7,000 supported CRSs below, and a small map preview highlighting the valid area of use for whatever you've selected. If a CRS is grayed out or QGIS warns about accuracy, you may need to download additional transformation grid files — follow the prompt to install them into the `proj` folder under your user profile.

See `fig03.png`.
