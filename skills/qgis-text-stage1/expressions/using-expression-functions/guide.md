# Using Expression Functions (QGIS 3.44)

QGIS expressions live everywhere — labels, symbology rules, field calculator, print layouts. Open the expression builder from any context by clicking the expression button (the epsilon icon), and you'll find functions organized into categories in the middle panel.

**Geometry** functions are your spatial workhorse. Use `$area` and `$length` for the current feature's measurements, or `area(geometry)` and `length(geometry)` for arbitrary geometries. Spatial predicates like `intersects()`, `contains()`, `crosses()`, and `disjoint()` return true/false for topology tests. Transform shapes with `buffer()`, `centroid()`, `convex_hull()`, and `difference()`. Convert between formats using `geom_from_wkt()` and `geom_to_wkt()`.

**String** functions handle text manipulation. `upper()`, `lower()`, and `title()` change case. `concat('a', 'b')` joins strings (NULL-safe, unlike the `||` operator which returns NULL if either side is NULL). Use `regexp_replace()` and `regexp_substr()` for pattern matching, `left()` / `right()` / `substr()` for slicing, and `format_number()` to prettify numeric output in labels.

**Math** functions cover the basics — `abs()`, `sqrt()`, `round()`, trig functions (`sin`, `cos`, `tan` and their inverses), plus `floor()`, `ceil()`, and `clamp(min, value, max)` for bounding. `scale_linear()` remaps a value from one range to another, which is great for proportional symbology.

**Aggregate** functions pull summary statistics across features without leaving the expression. `sum("population")`, `mean("score")`, `count("id")` all operate on the current layer by default. Add `group_by` to partition results (e.g., `sum("passengers", group_by:="region")`), or use `filter` to restrict which features contribute. The powerful `aggregate()` function reaches into *other* layers — `aggregate('rail_stations', 'sum', "passengers", filter:=intersects(@geometry, geometry(@parent)))` sums passengers from stations that intersect the current feature.

All expressions support `NULL` handling, nested function calls, and variables like `@geometry` (current feature) and `@parent` (source feature in aggregates). The **Expression** tab's search bar and built-in help panel show syntax and examples for every function as you type.
