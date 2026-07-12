# Joining and Relating Layers (QGIS 3.44)

QGIS gives you two main ways to connect data across layers: **joins** for simple one-to-one attribute lookups, and **relations** for richer one-to-many or many-to-many links. Both work without creating new layers — they extend your attribute table on the fly.

## Table Joins

A join appends fields from one layer onto another based on a shared attribute. Open the target layer's **Properties > Joins** tab and click **Add new join**. Pick the join layer, then choose matching fields in each layer (the join field and target field must share common values). Hit **OK** and the joined attributes appear in your target layer's attribute table immediately.

See `fig01.png`.

The join matches on the first feature it finds, so keep your join field values unique. You can limit which fields come across by enabling **Joined Fields** and picking a subset. A **Custom Field Name Prefix** avoids collisions when field names overlap. Enable **Cache join layer in virtual memory** for faster lookups on large datasets, and tick **Editable join layer** if you want to edit joined attributes directly from the target layer's table.

## Relations (One-to-Many)

When a parent feature has many children (regions with many airports, for example), you need a relation instead of a join. Go to **Project > Properties > Relations** tab and click **Add Relation**. Set the referenced (parent) layer and its primary key, then the referencing (child) layer and the foreign key field that points back to the parent.

See `fig02.png`.

Once defined, identify a parent feature and you'll see an embedded table of all its related children right in the feature form. From there you can add, link, unlink, or delete child features without switching layers.

See `fig03.png` for the feature form with related child records.

## Many-to-Many Relations

For N-M relationships (airports serving multiple airlines, airlines serving multiple airports), create a pivot table with foreign keys to both layers, then define two separate one-to-many relations — one from each main layer to the pivot table. PostgreSQL users can shortcut this with **Discover Relations** on the Relations tab. Set the correct cardinality in each layer's **Properties > Attributes Form** so the sub-form shows the linked layer rather than the raw pivot table.

## Polymorphic Relations

If multiple parent layers share a single child table (say, both `plants` and `animals` link to a `documents` table), use a polymorphic relation. Click the dropdown arrow beside **Add Relation** and choose **Add Polymorphic Relation**. You specify a "layer field" in the child table that identifies which parent layer each record belongs to, plus a layer expression (like `@layer_name`) to resolve it at runtime.

## Dataset-Stored Relationships

For layers from PostgreSQL, GeoPackage, or File Geodatabase, QGIS can detect relationships already defined at the database level. Use **Discover Relations** on the Relations tab, or right-click a database in the **Browser Panel** and choose **New relationship…** to create one directly. These persist in the dataset itself, not just the project file.
