# Layer Blend Modes (GIMP 2.10)

GIMP 2.10 offers 38 blend modes organized into seven groups. You set the mode via the **Mode** dropdown at the top of the **Layers** dialog — each layer can have its own mode, and effects stack cumulatively from bottom to top. The bottom layer's mode has no effect regardless of what you pick.

**Normal** is the default — the top layer simply covers what's below, governed by opacity. **Dissolve** scatters pixels randomly in semi-transparent areas, useful for textured edges.

**Lighten** modes brighten the result. **Screen** is the workhorse here — it inverts, multiplies, then inverts again, producing a washed-out glow. **Dodge** divides the lower layer by the inverse of the upper, pulling detail from shadows. **Addition** simply sums pixel values for a quick blast of brightness.

**Darken** modes do the opposite. **Multiply** is the classic — it multiplies pixel values together, so white is neutral and black crushes everything. **Burn** deepens shadows aggressively, while **Linear Burn** adds values then subtracts 1.0 for a slightly different darkening character.

**Contrast** modes push both ends. **Overlay** and **Soft Light** are your go-to options for boosting midtone contrast without blowing things out. **Hard Light** is more extreme, great for combining photos with punchy colors. **Vivid Light** cranks contrast hard in both highlights and shadows.

**Inversion** modes compare layers. **Difference** subtracts and takes the absolute value — identical layers produce pure black, making it perfect for alignment checks. **Grain Extract** and **Grain Merge** are a pair: extract pulls texture detail into a separate layer, merge applies it back.

**HSV Components** let you transplant individual color properties. **HSV Hue** takes hue from the top layer but keeps saturation and value from below — great for recoloring. **HSV Saturation** on a white layer desaturates the image entirely. **HSV Value** reveals detail in dark/light areas without shifting color.

**LCh Components** work like HSV modes but use the perceptually uniform CIELCh color space, producing more natural-looking results. **LCh Color** combines hue and chroma from the top layer with lightness from below — often preferable to HSL Color for color grading. **LCh Lightness** adjusts perceived brightness without the saturation shifts you sometimes get from HSV Value.
