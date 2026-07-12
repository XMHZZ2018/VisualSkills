# Connecting to WFS Services (QGIS 3.44)

A WFS layer in QGIS behaves like any other vector layer — you can identify features, select them, view the attribute table, and even edit them if the server supports WFS-T. QGIS handles WFS 1.0.0, 1.1.0, 2.0, and OGC API - Features, with background downloading, on-disk caching, and version autodetection built in.

To get started, open the Data Source Manager with **Ctrl+L** and switch to the **WFS / OGC API - Features** tab. Hit **New…** to create a connection. Give it a name, paste in the server URL (just the base URL — no `request=GetCapabilities` fragments), and optionally configure authentication. For OGC API - Features endpoints, provide the landing page URL.

Under **WFS Options**, you can press **Detect** to auto-identify the server version, choose between GET and POST for requests, set a max feature count, and pick a feature mode (Simple or Complex). Enable **Feature paging** with a page size if your server supports it — this keeps large datasets manageable.

Once the connection is saved, select it from the **Server Connections** dropdown and click **Connect**. The available layers appear in a list. Select one, optionally tick **Only request features overlapping the view extent** to limit downloads, and use **Change…** to pick a different CRS. Double-click a layer row to open the **SQL Query Composer** for advanced filtering with spatial predicates and SQL functions.

Click **Add** to load the layer. Download progress shows in the lower-left corner. For WFS-T or OGC API - Features Part 4 servers, toggle editing mode to create, modify, or delete features directly — though keep in mind each edit fires a network request, so bulk changes will be slow.
