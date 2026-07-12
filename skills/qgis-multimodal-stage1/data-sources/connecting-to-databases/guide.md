# Connecting to Databases (QGIS 3.44)

Everything starts from the Data Source Manager — open it with `Ctrl+L` or the toolbar icon. The left sidebar lists every supported source type, including dedicated tabs for PostgreSQL, SpatiaLite, Oracle, MS SQL Server, and SAP HANA. You can also right-click a database entry in the **Browser Panel** (`Ctrl+2`) and choose **New Connection** to get the same dialogs without leaving the tree view.

**PostgreSQL** is the most common case. Open the PostgreSQL tab and click **New** to create a connection. Fill in a friendly name, the host (use `localhost` if it's local), port (`5432` by default), and database name. Choose an SSL mode — "Prefer" is fine for most internal networks. For authentication, switch to the **Basic** tab and enter your username/password, or set up a stored authentication configuration for encrypted credential storage. Hit **Test Connection** to verify, then **OK** to save.

See `fig01.png`.

If you manage many PostgreSQL connections, consider a **pg_service.conf** file (`.pg_service.conf` on Linux/macOS). Define named services with host, port, dbname, and credentials — then just enter the service name in the connection dialog instead of repeating everything. QGIS resolves it automatically.

**SpatiaLite** is simpler — press `Ctrl+Shift+L` (or **Layer > Add Layer > Add SpatiaLite Layer**), click **New**, and browse to your `.sqlite` file. Once registered, the database appears in the dropdown for future sessions.

**Loading layers** from any connected database follows the same pattern: pick your connection from the dropdown and press **Connect**. QGIS populates a table of available layers grouped by schema, showing geometry type, SRID, and feature ID columns. Select the layer(s) you want — hold `Shift` or `Ctrl` for multiples — and click **Add**. If a layer shows a warning icon, you may need to manually specify its geometry type or primary key in the inline dropdowns before it becomes selectable.

See `fig02.png`.

For power users, the **DB Manager** plugin (**Database > DB Manager**) lets you run arbitrary SQL, preview tables, and drag results straight onto the map canvas. It works with all supported database types in one unified interface.
