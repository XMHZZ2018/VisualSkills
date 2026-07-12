# Configuring Project Properties (QGIS 3.44)

Open **Project > Project Properties** to set options that override global defaults for the current project. Everything here travels with the `.qgs`/`.qgz` file.

In the **General** tab, give your project a title, set the project home folder, and pick your selection and background colors. The Measurements frame lets you choose the ellipsoid (e.g., WGS 84) and preferred units for distance and area — these control what the measure tool, field calculator, and identify results report.

The **Metadata** tab lets you fill in a structured metadata report — author, description, categories, links, and temporal/spatial extent — so the project is self-documenting and discoverable.

Under the **CRS** tab, assign the project's coordinate reference system. You can set it to "No CRS" for raw coordinate drawing, or pick any geographic, projected, or user-defined CRS. Layers added afterward get reprojected on-the-fly to match. If you need to control *how* reprojection happens between specific datums, switch to the **Transformations** tab and define preferred datum transformations there.

The **Styles** tab is where you set default symbols for new layers that lack a `.qml` style. Pick a default Marker, Line, Fill, Color Ramp, and Text Format. Under Symbol options you can set a default opacity and enable random fill colors so new layers don't all render identically. The Style Database section lets you attach shared `.db` style libraries to the project — all users who open the project get instant access to those symbols without importing them locally.
