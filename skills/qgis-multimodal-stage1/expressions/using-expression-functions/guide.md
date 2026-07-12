# Using Expression Functions (QGIS 3.44)

QGIS expressions are your Swiss Army knife for dynamic labeling, styling, field calculations, and filtering. You'll find the expression builder anywhere you see the small epsilon (ε) button — in the **Field Calculator**, **Select by Expression** dialog, layer symbology rules, and print layout item properties. The left panel of the builder organizes all available functions into categories you can expand and search.

**Geometry functions** let you interrogate and manipulate feature shapes on the fly. Use `$area` to get the area of the current feature, `buffer(@geometry, 500)` to create a 500-unit buffer, or `distance(geometry(@parent), @geometry)` to compute distance between features. Spatial predicates like `intersects()`, `contains()`, and `within()` return true/false and are essential for filtering in aggregate expressions or atlas setups.

**String functions** handle text manipulation directly in expressions. `upper("name")` and `lower("name")` change case, `concat('ID: ', "gid")` joins values (safely handling NULLs unlike the `||` operator), and `regexp_replace("field", '\\d+', '')` strips digits via regex. For padding and trimming, reach for `lpad()`, `rpad()`, `trim()`, `ltrim()`, and `rtrim()`.

**Math functions** cover the basics you'd expect: `round()`, `abs()`, `sqrt()`, plus trig functions (`sin`, `cos`, `atan2`) that work in radians. Convert with `degrees()` and `radians()`. The `clamp(min, value, max)` function is handy for keeping values in range, and `scale_linear()` remaps a value from one range to another — great for graduated symbology.

**Aggregate functions** are where things get powerful. They compute statistics across features without leaving the expression context. `sum("population", group_by:="state")` totals population per state. The cross-layer `aggregate()` function pulls data from a different layer entirely — for example, `aggregate('rail_stations', 'sum', "passengers", filter:=intersects(@geometry, geometry(@parent)))` sums passengers from stations that fall within the current polygon.

Variables, prefixed with `@`, give you dynamic context: `@project_crs`, `@map_scale`, `@atlas_feature`, `@row_number`. They change based on where the expression runs — the field calculator sees different variables than a print layout item. Use `var('my_custom_var')` or the `with_variable()` function to define your own for complex expressions that reuse computed values.
