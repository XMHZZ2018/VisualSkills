# Configuring Datum Transformations (QGIS 3.44)

QGIS reprojects layers on the fly whenever their CRS differs from the project CRS. When multiple transformation paths exist between two datums, you can control exactly which pipeline QGIS uses — and how it falls back if that pipeline isn't available.

Head to **Settings > Options > Transformations** tab. Under the *Default datum transformations* group, tick **Ask for datum transformation if several are available**. With this on, QGIS pops up a selection dialog any time it encounters a CRS pair with more than one valid transformation. If you check **Make default** when choosing, that selection carries forward to every new project you create.

Rather than waiting for the prompt, you can pre-configure preferred transformations. Click the **Add** button to open the *Select Datum Transformations* dialog. Pick a **Source CRS** and a **Destination CRS** using the dropdowns or the CRS-selector widget. The table below fills with every available transformation, showing accuracy (in metres) and the geographic area of use. Click any row to see the full scope, EPSG identifiers, and the underlying PROJ pipeline string in the details panel below.

See `fig01.png`.

Some transformations appear greyed out — these require an external grid-shift package you haven't installed yet. QGIS usually provides a download button right there; the downloaded `.gsb` or `.tif` file goes into the `proj` folder inside your active user profile directory.

Once you've found the right transformation, select it and optionally tick **Allow fallback transforms if preferred operation fails** so QGIS can gracefully degrade when the grid file is missing on another machine. Hit **OK** and the pair appears in the default datum transformations list. You can edit or remove entries later with the pencil and minus buttons.

These global defaults (set under **Settings > Options**) apply to all new projects. For project-specific overrides, open **Project > Properties… > CRS** tab and configure transformations there instead — those settings travel with the `.qgz` file and won't affect other projects.
