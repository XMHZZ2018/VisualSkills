# Configuring Datum Transformations (QGIS 3.44)

QGIS reprojects layers on the fly, but when multiple transformation paths exist between two datums, you get to pick which pipeline to use. This matters for accuracy — the difference between a 1-meter and a 20-meter shift.

Open **Settings > Options** and navigate to the **CRS and Transforms > Coordinate Transforms** tab. Under **Default Datum Transformations**, tick **Ask for datum transformation if several are available**. With this enabled, QGIS will pop a dialog whenever it encounters an ambiguous source/destination CRS pair, letting you choose the best-fit operation on the spot. Tick **Make default** in that dialog to lock in your choice for future projects.

To predefine a transformation without waiting for the prompt, click the **Add** button in the same options panel. Set your **Source CRS** and **Destination CRS** using the dropdowns. A table appears listing every available pipeline — each row shows the transformation name, accuracy in meters, and geographic area of use. Click a row to inspect its scope, identifiers, and the underlying PROJ pipeline string. Greyed-out entries require an additional grid package; a download button will appear to fetch and install the missing grid into your user profile's `proj` folder.

Select your preferred transformation, optionally enable **Allow fallback transforms if preferred operation fails**, then click **OK**. The pair now appears in your default list and QGIS will use it automatically going forward. You can edit or remove entries from that list at any time.

These global defaults apply to every new project. For project-specific overrides, go to **Project > Properties… > CRS** and configure transformations there instead — those settings travel with the `.qgz` file and won't affect other projects.
