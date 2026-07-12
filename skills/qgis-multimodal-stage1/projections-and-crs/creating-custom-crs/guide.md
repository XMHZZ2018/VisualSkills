# Creating a Custom CRS (QGIS 3.44)

When none of the ~7,000 built-in coordinate reference systems fit your needs, QGIS lets you roll your own. You'll need a working knowledge of the PROJ projection library (or a WKT definition handy), but the mechanics are straightforward.

Open the custom CRS editor via **Settings > Custom CRS…**. This opens the **User Defined CRS** dialog, which lists any custom CRSs you've already created and gives you fields to define new ones. Everything you create here is stored in your personal QGIS user database alongside bookmarks and other settings.

See `fig01.png`.

To add a new CRS, click the **Add new CRS** button (the green plus icon at the top-right of the list). Give it a descriptive name — something you'll recognize later in the CRS selector.

Next, choose your format. You can enter either a **Proj String** or **WKT** definition. The recommendation is to store everything in WKT. If you only have a proj string, go ahead and paste it in with "Proj String" selected, then switch the format dropdown to **WKT (Recommended)** — QGIS will convert it for you automatically.

Enter your cartographic parameters in the **Parameters** text box. This is the actual CRS definition: the projection method, datum, ellipsoid, units, and any other relevant parameters. Once you've got them in, hit **Validate** to confirm QGIS can parse the definition without errors.

You can also sanity-check the results right in this dialog. In the **Test** section at the bottom, enter a known WGS 84 latitude/longitude pair and click **Calculate**. The transformed coordinates appear on the right — compare them against expected values to confirm your definition is producing correct output.

If you need to integrate an NTv2 grid-shift file, drop the `.gsb` file into your PROJ data folder (e.g., `C:\OSGeo4W64\share\proj` on Windows, or the `proj` folder under your user profile). Then add `+nadgrids=yourfile.gsb` to your Proj String parameters. This lets QGIS apply the grid-based transformation as part of your custom CRS.

Once everything looks good, click **OK**. Your new CRS will now appear under "User Defined CRS" in any CRS selector throughout QGIS — project settings, layer properties, processing tools, everywhere.
