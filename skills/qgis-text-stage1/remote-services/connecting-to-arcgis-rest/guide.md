# Connecting to ArcGIS REST Servers (QGIS 3.44)

QGIS can consume ArcGIS REST services — MapServer, FeatureServer, ImageServer, and more — without any plugins. You set up a connection once, and then browse or load layers just like any other remote data source.

To create a connection, open **Layer > Data Source Manager** (or press `Ctrl+L`) and switch to the **ArcGIS REST Server** tab. Click **New**, give the connection a name, and paste the service endpoint URL — that's the base REST URL, not a specific layer endpoint. Add authentication credentials if the service requires them, then hit **OK**.

Once connected, select your connection from the dropdown and click **Connect** to fetch the available layers. Pick the ones you need and click **Add** to load them into your project. When loading from a FeatureServer, QGIS automatically converts ArcGIS symbology into native QGIS symbols, so your map should look the same as it does in ArcGIS web maps without manual restyling.

FeatureServer layers can be edited directly in QGIS — toggle editing as you would any vector layer — provided the service has editing enabled, your credentials allow write access, and the layer advertises Create, Update, or Delete capabilities. If any of those conditions aren't met, the layer stays read-only.

Because you're working against a live service, hit **View > Refresh** (or `F5`) to pull down the latest server-side changes before making edits, especially if multiple people are working on the same layer.
