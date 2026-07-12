# Connecting to WMS/WMTS Services (QGIS 3.44)

Open the Data Source Manager with **Ctrl+L** and switch to the **WMS/WMTS** tab. You can also get there via **Layer > Add Layer > Add WMS/WMTS Layer...** from the menu bar.

Hit **New** to define a connection. Give it a recognizable **Name** and paste the server's base URL — just the host, no query parameters like `request=GetCapabilities`. For WMTS KVP services, append `?SERVICE=WMTS&REQUEST=GetCapabilities` to the URL. RESTful WMTS endpoints use the format `{BaseURL}/1.0.0/WMTSCapabilities.xml` instead.

If the server requires credentials, use the **Authentication** tab — preferably a stored authentication configuration rather than a plain username/password, since those travel with your project file in the clear.

Optionally tweak **WMS DPI-Mode**, **WMTS server-side tile pixel ratio**, or check **Ignore axis orientation** if the server misbehaves with coordinate order. Click **OK** to save.

Back in the main dialog, select your connection from the dropdown and press **Connect**. QGIS fetches the capabilities document and populates the layer tree. Pick one or more layers, choose an **Image encoding** (PNG for fidelity, JPEG for speed), and set the **CRS** if the default isn't what you need.

You can select multiple layers — they'll be merged into a single request by default. Toggle **Load as separate layers** if you'd rather keep them independent. Use the **Layer Order** tab to control draw priority, then click **Add** to drop the imagery onto your map canvas.

QGIS caches WMS tiles for 24 hours automatically, so reopening a project won't re-download everything. If you're behind a proxy, configure it under **Settings > Options > Network** before connecting.
