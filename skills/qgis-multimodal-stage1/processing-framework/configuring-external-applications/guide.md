# Configuring External Applications (QGIS 3.44)

The Processing framework talks to external tools — GDAL, GRASS, R, LAStools, OTB — through algorithm providers. By default, providers that depend on software not bundled with QGIS are disabled; you switch them on once you've installed the underlying tool and pointed QGIS at it. After that, their algorithms show up in the Processing Toolbox and Model Designer just like native ones.

**Windows users** get the easiest path: the standalone QGIS installer bundles GRASS automatically. If you used OSGeo4W instead, just make sure you ticked GRASS during setup. Either way, no further configuration is needed.

Watch out for **file formats**. An external tool may not read every format QGIS can open. Vector layers get auto-converted (at the cost of extra time for large datasets), but raster formats like native GRASS layers won't even appear as valid inputs. Stick to well-known formats (GeoTIFF, Shapefile/GeoPackage) when feeding external providers, and check the Log panel if something fails silently.

If you have an active **feature selection** and the *Use only selected features* option is on, QGIS exports just those features before handing the layer off — expect longer run times on big layers.

All provider configuration lives under **Settings > Options > Processing tab > Providers**. GDAL is already active there. GRASS exposes options like using `r.external` instead of `r.in.gdal` for faster raster handling, and you can toggle console/command logging.

For **R**, install the *Processing R Provider* plugin, then set the R folder under **Providers > R** (Windows: point to `C:\Program Files\R\R-<version>`, not the binary itself; Linux: just ensure `R` is on your PATH). Example scripts like *Scatterplot* and *test_sf* verify your setup works. To get the full community script collection, grab the *QGIS Resource Sharing* plugin, reload repositories, and install the "QGIS R script collection." The scripts will appear grouped under R in the toolbox.

See `fig01.png`.

**LAStools** requires its own plugin from the official repository. Point **Providers > LAStools > LAStools folder** at your install directory. Linux users need Wine configured (default folder `/usr/bin`).

**OTB** (Orfeo ToolBox) is a remote-sensing image processing library installed separately. Under **Providers > OTB**, set the *OTB folder* to your install root and *OTB application folder* to `<install>/lib/otb/applications`. Optional tweaks include logger level (`INFO`/`WARNING`/`CRITICAL`/`DEBUG`), maximum RAM allocation, and paths to a geoid file or local SRTM tiles so elevation data doesn't need downloading at runtime.

Once any provider's paths are set and you click **OK**, its algorithms populate the toolbox immediately — no restart required (except for the Menus configuration, which does need a restart).
