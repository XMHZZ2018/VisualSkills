Now I have all the source material. Let me write the guide.

# Configuring External Applications (QGIS 3.44)

The Processing framework extends QGIS by connecting to external tools like GDAL, GRASS, R, LAStools, and OTB. By default, algorithms relying on software not bundled with QGIS are disabled — you enable them under **Settings > Options > Processing tab > Providers**.

**Windows users** get the easiest path: the standalone installer ships GRASS pre-configured and ready to go. If you used OSGeo4W instead, just make sure you selected GRASS during installation.

**GDAL** is built in. Under **Providers > GDAL**, you can activate or deactivate its algorithms directly — no path configuration needed.

**GRASS** generally auto-detects its own installation. On Windows, point the GRASS connector to the correct folder only if auto-detection fails. On Linux, just confirm that typing `grass` in a terminal launches it. GRASS algorithms compute within a defined region — set it manually or let QGIS derive it from your input layers' extent.

**R** requires the **Processing R Provider** plugin. Once installed, configure the R folder under **Providers > R** in Processing settings. On Windows, point to the `R-<version>` folder (e.g., `C:\Program Files\R\R-4.x.x\`) — the folder, not the binary. On Linux, just ensure `R` is on your PATH. Grab community scripts via the **QGIS Resource Sharing** plugin (**Plugins > Resource Sharing > Resource Sharing**), then install the "QGIS R script collection."

**LAStools** needs a separate download from rapidlasso plus the LAStools plugin from the official repository. Configure it under **Providers > LAStools** by setting the **LAStools folder**. Linux users also need Wine installed and its folder specified (default `/usr/bin`).

**OTB (Orfeo ToolBox)** must be downloaded separately. Under **Providers > OTB**, set **OTB folder** to your install location and **OTB application folder** to `<install>/lib/otb/applications`. Optional tweaks include **Logger level** (INFO/WARNING/CRITICAL/DEBUG), **Maximum RAM**, and paths to a geoid file or local SRTM tiles.

A practical note on formats: external tools may not support every format QGIS can open. QGIS auto-converts vectors for you (at the cost of extra time for large layers), but rasters from GRASS databases won't even appear as available inputs. Stick to common formats like GeoPackage or Shapefile when things get weird, and check the log panel for clues.

If you're working with selections, be aware that passing only selected features forces QGIS to export a temporary copy — expect longer run times when selections are active and the **Use only selected features** option is on.
