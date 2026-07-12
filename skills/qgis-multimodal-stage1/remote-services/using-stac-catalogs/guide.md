# Using STAC Catalogs (QGIS 3.44)

STAC (SpatioTemporal Asset Catalog) is a standard way to organize and index spatial-temporal assets — satellite imagery, drone photos, sensor data — so you can search, preview, and load them directly in QGIS. There are two flavors: **static catalogs** (browsable JSON files, no search) and **STAC APIs** (searchable endpoints following the OGC API pattern).

To connect to a static catalog, right-click the **STAC** entry in the **Browser** panel and choose **New STAC Connection…**. Give it a name and the catalog URL, add authentication if needed, and hit **OK**. For a STAC API — which supports filtering and search — open the **Data Source Manager** instead (the **STAC** tab), click **New**, fill in the same fields, then press **Connect**.

See `fig01.png`.

Once connected, static catalogs appear as a tree under **STAC** in the Browser panel. Expand the catalog node to see its Collections, then drill into a Collection to find individual Items. Right-click any Item and choose **Details…** to inspect its metadata and coverage footprint. If an asset is cloud-optimized (like a COG), you can add it straight to your map canvas; otherwise use **Download Assets…** to save it locally first.

See `fig02.png`.

For STAC APIs, filtering happens through the Data Source Manager. Select your connection, click **Filters…**, and you can enable a **Spatial Extent** (bounding box or drawn area), a **Temporal Extent** (date or range), or restrict search to specific collections with **Only search within specific collections**. Apply the filters and matching items populate the results list. Toggle **Show Footprints** to see where each result lands on the map.

See `fig03.png`.

Right-click any result item for quick actions: **Zoom to Item**, **Pan to Item**, **Download Assets**, or **Details…**. Downloaded assets come with auxiliary files (thumbnails, style files) and can be loaded afterward with the standard **Layer > Add Layer > Add Raster Layer…** workflow.
