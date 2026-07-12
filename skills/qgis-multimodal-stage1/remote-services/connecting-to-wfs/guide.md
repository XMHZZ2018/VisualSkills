# Connecting to WFS Services (QGIS 3.44)

A WFS (Web Feature Service) layer in QGIS behaves like any other vector layer — you can identify features, select them, open the attribute table, and even edit geometries if the server supports WFS-T. QGIS handles WFS 1.0.0, 1.1.0, 2.0, and the newer OGC API - Features (OAPIF), with background downloading and on-disk caching built in.

To get started, open the Data Source Manager with **Ctrl+L** (or **Layer > Add Layer > Add WFS / OGC API - Features Layer...**) and switch to the **WFS / OGC API - Features** tab. Hit **New...** to create a connection. Give it a name, paste in the server URL (just the base URL — no `request=GetCapabilities` fragments), and optionally configure authentication. For OGC API - Features endpoints, provide the landing page URL instead.

See `fig01.png`.

Under **WFS Options**, you can auto-detect the server version with the **Detect** button, choose between GET and POST for requests, set a maximum feature count, and pick simple or complex feature mode. Complex mode uses the OGR GMLAS driver and exposes nested structures as JSON. If the server supports paging, enable **Feature paging** and set a page size — otherwise the server's default applies.

Once the connection is saved, select it from the **Server Connections** dropdown and click **Connect**. You'll see available layers listed below. Pick what you need, then optionally tick **Only request features overlapping the view extent** to limit downloads to your current map area. You can also change the layer's CRS or double-click a layer row to open the **SQL Query Composer** and build a filter using spatial predicates and SQL functions.

See `fig02.png`.

Click **Add** and the layer loads onto your canvas. Download progress shows in the lower-left corner. From here it's a normal vector layer — style it, query it, export it.

For WFS-T or OGC API - Features Part 4 services, toggle editing mode on the layer to create, modify, or delete features directly on the server. Keep in mind each edit fires a separate network request, so bulk edits on hundreds of features will be slow. Save your edits when done and they're committed upstream immediately.
