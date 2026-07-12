# Joining and Relating Layers (QGIS 3.44)

A **join** appends attributes from one layer to another based on a shared field (one-to-one). Open the target layer's **Properties › Joins** tab, hit **Add new join**, pick the join layer, then match a Join field to a Target field. All attributes from the first matching feature get appended. Keep your key fields unique — duplicates on the join side just grab the first match.

Fine-tune joins with options like **Cache join layer in virtual memory** for speed, **Joined Fields** to limit which columns come across, and **Custom Field Name Prefix** to avoid name collisions. Enable **Editable join layer** if you want to edit joined values directly from the target's attribute table, and toggle **Upsert on edit** or **Delete cascade** for automatic sync.

**Relations** handle one-to-many and many-to-many links — they're project-level, configured at **Project › Properties › Relations**. Click **Add Relation**, set the Referenced (parent) layer with its primary key, and the Referencing (child) layer with its foreign key field. Choose *Association* or *Composition* strength depending on whether child features should cascade-delete with parents.

Once a 1-N relation exists, the parent feature's form automatically shows a sub-table of related children. From there you can digitize new child features, link/unlink existing ones, or delete them — all without leaving the parent form.

For **many-to-many**, create a pivot table with foreign keys pointing to both layers, then define two 1-N relations through that pivot. For PostgreSQL, use **Discover Relations** to auto-detect them. Enable **transaction groups** in **Project Properties › Data Sources** so edits stay consistent across all three tables.

**Polymorphic relations** let a single child table reference multiple parent layers — add a "layer field" column that identifies which parent each row belongs to, then configure via **Add Polymorphic Relation** with a layer expression like `@layer_name`. QGIS also supports **dataset-stored relationships** (PostgreSQL, GeoPackage, FGDB) — right-click a database in the Browser Panel and choose **New relationship** to define them at the data source level.
