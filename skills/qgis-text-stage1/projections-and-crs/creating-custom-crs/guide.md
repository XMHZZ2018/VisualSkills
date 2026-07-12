# Creating a Custom CRS (QGIS 3.44)

When none of the ~7,000 built-in coordinate reference systems fit your needs, you can define your own. Open the dialog via **Settings > Custom CRS…** — this stores your definitions in your personal QGIS user database alongside bookmarks and other custom data.

Hit the **Add new CRS** button (the green plus icon) to start a blank entry. Give it a descriptive name in the **Name** field — something you'll recognize later in the CRS selector.

Under **Definition**, pick your **Format**: either `WKT (Recommended)` or `Proj String`. If you only have a Proj string handy, paste it in, then switch the format dropdown to WKT — QGIS will convert it automatically. WKT is the preferred storage format going forward.

Type or paste your projection parameters into the **Parameters** box. These follow standard PROJ cartographic parameters (the same ones documented in the USGS Open-File Report 90-284 if you want the deep reference).

Click **Validate** to confirm QGIS can parse your definition as a valid projection. Fix any errors before proceeding.

To sanity-check the result, use the **Test** section at the bottom: enter a known WGS 84 latitude in **Latitude** and longitude in **Longitude**, click **Calculate**, and compare the output in the **Destination CRS** column against expected values in your new system.

Once satisfied, click **OK**. Your custom CRS now appears under "User Defined CRS" in any CRS selector throughout QGIS.

**NTv2 grids:** If your custom CRS requires an NTv2 transformation, drop the `.gsb` file into your Proj folder (e.g., `C:\OSGeo4W64\share\proj` on Windows) and append `+nadgrids=yourfile.gsb` to the Proj definition string.
