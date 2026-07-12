The source file has no embedded images — just figure captions referencing the official docs. I have all the content I need from the STAC section (lines 830–933) to write the guide.

# Using STAC Catalogs (QGIS 3.44)

STAC (SpatioTemporal Asset Catalog) is a standard way to organize and index geospatial assets — satellite imagery, drone photos, sensor data — so you can search and load them directly in QGIS. There are two flavors: static catalogs (browsable JSON files, no search) and STAC APIs (dynamic, with full spatial/temporal querying).

To set up a connection, right-click the **STAC** entry in the **Browser** panel and choose **New STAC Connection…**. Give it a name, paste the catalog URL, add credentials if needed, and hit **OK**. For STAC APIs specifically, you can also go through **Layer > Data Source Manager > STAC** tab and click **New**.

Once connected, static catalogs appear as a tree under **STAC** in the Browser panel. Expand the node to see collections, then expand a collection to reveal individual items. Right-click any item and choose **Details…** to inspect its metadata and spatial footprint. If the asset is cloud-optimized (like a COG), you can add it straight to the map canvas; otherwise, use **Download Assets…** to save it locally first.

For STAC API connections, open the **Data Source Manager > STAC** tab, select your connection, and click **Filters…** to narrow results. You can enable **Spatial Extent** to restrict by bounding box, **Temporal Extent** to set a date range, and limit searches to specific collections. After applying filters, results appear in the main panel — toggle **Show Footprints** to visualize coverage on the map.

Right-click any result item to **Zoom to Item**, **Pan to Item**, view **Details…**, or **Download Assets**. Downloaded files include the primary dataset plus auxiliaries like thumbnails. Load them with the standard **Layer > Add Layer > Add Raster Layer…** workflow.
