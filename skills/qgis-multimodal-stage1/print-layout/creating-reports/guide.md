# Creating Reports (QGIS 3.44)

A report in QGIS is a multi-page document that goes beyond a simple print layout or atlas. Think of it as a structured narrative — header, repeating body sections driven by your data, and a footer — all stitched together into one exportable PDF, SVG, or set of images. You create one via **Project > New Report** or through **Project > Layout Manager** (choose "Empty Report" from the template dropdown).

The workspace looks like the familiar print layout designer, but with a **Report Organizer** panel on the left. This is where you manage the hierarchy of sections. Every report starts with a main section offering two toggles: **Include report header** and **Include report footer**. Enable either, click **Edit**, and you're dropped into a full layout canvas — add maps, labels, tables, pictures, whatever you need.

The real power comes from the **Add Section** button in the organizer. You get two choices: a **Static Layout Section** (a fixed page inserted wherever you like) and a **Field Group Section** (which iterates over features in a layer, one page per feature — essentially an atlas embedded inside your report). Pick a layer and a grouping field, and QGIS will generate a page for every unique value.

See `fig01.png`.

Field groups can be nested. Say you iterate over states, then add a child field group for populated places — QGIS will output each state's page followed by pages for every place within it, as long as both layers share a linking attribute (like `adm1name`). You can also stack sibling groups: airports after populated places, both under the same parent state group, producing a cleanly ordered hierarchy.

To include dynamic pictures (like a flag per state), add a picture item to the group body, then data-define the **Image Source** with an expression such as `concat(@project_folder, '/pictures/', upper("adm1name"), '_flag.png')`. For highlighting the current feature on a map, data-define your layer's style using `if($id = @atlas_featureid, 2.0, 0.1)` for line width or a similar conditional for fill colour.

See `fig02.png`.

When you're ready, go to **Report > Export Report as PDF…** (or Images/SVG). You'll get a single consolidated output: header first, then every iterated section in order, and the footer at the end. The combination of nested groups, headers/footers at each level, and the full layout toolset makes reports surprisingly flexible for automated, data-driven documents.
