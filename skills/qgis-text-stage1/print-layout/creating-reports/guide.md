Now I have all the source content. Let me write the reference guide.

# Creating Reports (QGIS 3.44)

A report is a multi-page document — think of it as an atlas on steroids, with headers, footers, and nested iterating sections that automatically generate pages for each feature in a layer.

Start one via **Project → New Report**, or use **Project → Layout Manager** and choose **Empty Report** from the template dropdown. You'll land in the familiar layout designer, but with a **Report Organizer** panel on the left.

The top-level report section offers **Include report header** and **Include report footer** — toggle either on, hit **Edit**, and design them like any print layout page (maps, labels, tables, pictures). Right-click the page to reach **Page properties** for size and orientation.

To add real content, click **Add Section** in the organizer. A **Static Layout Section** inserts a one-off page. A **Field Group Section** iterates over a layer's features, sorted by a chosen field — essentially an inline atlas. Set the layer and grouping field, enable **Include body**, then **Edit** the body to design what each feature's page looks like. Use `[% "field_name" %]` expressions in labels and check **Controlled by Report** on map items so they follow the current feature.

Nesting is where reports shine. Select an existing field group, hit **Add Field**, and add a child group. The child automatically filters to features matching the parent's grouping value (the child layer needs a matching attribute). You can also add sibling groups — they iterate consecutively under the same parent.

For dynamic images, add a picture item and data-define its **Image Source** with an expression like `concat(@project_folder, '/pics/', upper("adm1name"), '.png')`. To highlight the current feature on a map, data-define style properties using `if($id=@atlas_featureid, highlighted_value, default_value)`.

When you're done, export via **Report → Export Report as PDF…** (or Images/SVG). Every header, body iteration, and footer compiles into one structured document automatically.
