# Configuring Project Properties (QGIS 3.44)

Open the dialog via **Project > Project Properties**. Everything here overrides the global settings from **Settings > Options**, so you can tailor each project without touching your defaults.

The **General** tab is where you land first. Set a project title, pick a selection color and background color for the canvas, and decide whether layer paths are saved as absolute or relative (relative is better if you share projects across machines). The Measurements section below that lets you choose an ellipsoid for distance/area calculations — leave it at WGS 84 for most work, or switch to "None/Planimetric" if you need raw cartesian values. You also select your preferred distance and area units here.

See `fig01.png`.

Head to the **CRS** tab to assign a coordinate reference system to the project. Layers are reprojected on-the-fly to match whatever you set here. If you're working with non-georeferenced data, tick "No CRS (or unknown/non-Earth projection)" and layers will draw from raw coordinates. For datum transformation specifics, switch to the **Transformations** tab — it lets you define preferred transformations for particular CRS pairs in this project.

The **Metadata** tab is straightforward: fill in a title, author, abstract, and keywords so the project is self-documenting. This metadata travels with the `.qgs`/`.qgz` file.

For controlling how new layers look, open the **Styles** tab. You can set default symbols for markers, lines, and fills, a default color ramp, and a text format for labels. Below that, configure symbol opacity and whether random colors are assigned to new layers. The Style Databases section lets you link external `.db` style libraries so everyone on the team shares the same symbology.

See `fig02.png`.

The **Colors** tab defines a project color palette. Named project colors are reusable via data-defined overrides — change the color once and every widget referencing it updates automatically.

Finally, the **Variables** tab lets you create custom project-level variables (accessible in expressions as `@my_variable`), and the **Data Sources** tab controls transaction modes, layer capabilities (identifiable, read-only, searchable, private), and performance options like trusting project metadata on load.
