# Connecting to ArcGIS REST Servers (QGIS 3.44)

QGIS can consume layers directly from ArcGIS REST endpoints — both MapServer (raster tiles) and FeatureServer (vector features). You don't need any plugins; the provider is built in.

To set up a connection, open the **Browser** panel, right-click the **ArcGIS REST Servers** entry, and choose **New Connection…**. Give it a name you'll recognize and paste the root URL of the service — something like `https://sampleserver6.arcgisonline.com/arcgis/rest/services`. Leave off any trailing `/MapServer` or `/FeatureServer` path; QGIS will discover the available services for you. If the server requires credentials, configure them under the **Authentication** tab (preferably using a stored authentication configuration rather than plain username/password, since those travel with the project file).

Once connected, expand the server node in the Browser panel to see the available MapServer and FeatureServer endpoints. Drag any layer straight onto the map canvas, or right-click and choose **Add Layer to Project**. For FeatureServer layers, QGIS automatically converts the ArcGIS symbology into native QGIS symbols, so your map should look much like the original web map right away.

FeatureServer layers can also be editable in QGIS — provided the service has editing enabled, your credentials grant write access, and the layer advertises Create, Update, or Delete capabilities. If those conditions are met, just toggle editing the same way you would for any vector layer. Keep in mind that each feature edit fires a separate network request, so bulk edits on hundreds of features will be slow.

After making edits — or if other users are working on the same service — hit **View > Refresh** (or press **F5**) to pull the latest state from the server. Refreshing before you start editing is a good habit when multiple people share the same layer, since ArcGIS REST services don't push live updates to QGIS.
