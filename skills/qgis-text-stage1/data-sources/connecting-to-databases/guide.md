# Connecting to Databases (QGIS 3.44)

The fastest way to connect to a database is through the **Browser Panel** (**View › Panels › Browser** or `Ctrl+2`). Right-click the PostgreSQL, SpatiaLite, or MS SQL Server entry and choose **New Connection** to get started.

Alternatively, open the **Data Source Manager** with `Ctrl+L` and select the appropriate tab on the left — **PostgreSQL**, **SpatiaLite**, **MS SQL Server**, or **Oracle**. You can also reach PostgreSQL directly via **Layer › Add Layer › Add PostgreSQL Layer** (`Ctrl+Shift+D`).

For **PostgreSQL**, click **New** and fill in your host, port (default `5432`), database name, and authentication. You can reference a `pg_service.conf` file in the Service field to avoid repeating credentials. Hit **Test Connection** to verify, then **OK** to save.

For **SpatiaLite**, use **Layer › Add Layer › Add SpatiaLite Layer** (`Ctrl+Shift+L`). Click **New**, browse to your `.sqlite` file, and you're connected — no host/port needed.

Once a connection is saved, select it from the dropdown, press **Connect**, and the dialog lists available tables grouped by schema. Pick your layer(s) — hold `Shift` or `Ctrl` to multi-select — then click **Add** to load them onto the map canvas.

If a table shows a warning icon, you may need to manually set its geometry type in the **Spatial Type** column or assign a primary key under **Feature id** before it can be added.

For power users, the **DB Manager** plugin (**Plugins › Manage and Install Plugins**) lets you run SQL queries directly against any connected database and add the results as layers. Enable **Use estimated table metadata** in the connection settings if you're working with very large tables and initial loading feels slow.
