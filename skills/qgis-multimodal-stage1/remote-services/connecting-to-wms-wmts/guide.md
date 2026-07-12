# Connecting to WMS/WMTS Services (QGIS 3.44)

A WMS server delivers pre-rendered map images on demand — you give it an extent and layers, it hands back a JPEG or PNG. WMTS is the tiled cousin: tiles are pre-generated on the server, so responses are faster since nothing needs to be rendered on the fly. QGIS handles both through the same interface.

To set up a new connection, open **Layer > Add Layer > Add WMS/WMTS Layer…** (or hit `Ctrl+L` and switch to the **WMS/WMTS** tab). You can also right-click the **WMS/WMTS** entry in the Browser panel and choose **New Connection…**.

Hit **New** and fill in a **Name** (just a label for the dropdown) and the **URL** — the base URL only, no `?request=GetCapabilities` fragments. If the server requires credentials, use the Authentication tab, though it's safer to store them as an Authentication configuration rather than plain username/password since those travel with the project file.

See `fig01.png`.

For WMTS specifically, the URL format depends on the interface type. A **KVP** service needs `?SERVICE=WMTS&REQUEST=GetCapabilities` appended to the base URL. A **RESTful** service uses the pattern `{BaseURL}/1.0.0/WMTSCapabilities.xml` — just paste that directly into the URL field.

Once connected, click **Connect** to fetch the server's capabilities. The layer tree shows available layers with their IDs, names, and styles. Pick one or more layers, choose an **Image encoding** (PNG for fidelity, JPEG for speed), and select a CRS if the default doesn't suit you. Multiple selected layers get merged server-side into a single combined layer unless you tick **Load as separate layers**.

See `fig02.png`.

Under **Options**, you can set a custom tile size, adjust the request step size to reduce label clipping at tile edges, or enable **Use contextual WMS Legend** so the legend only shows features visible at your current extent.

QGIS caches WMS tile responses for 24 hours automatically — reopening a project won't re-fetch tiles unless you explicitly hit **Connect** again. If you're behind a proxy, configure it under **Settings > Options > Network** before connecting.

For time-aware WMS/WMTS layers, the **Temporal** properties tab lets you control whether the layer tracks the temporal controller dynamically or displays a fixed time slice. You can pick from server-default dates, predefined ranges, or follow the project's temporal range.
