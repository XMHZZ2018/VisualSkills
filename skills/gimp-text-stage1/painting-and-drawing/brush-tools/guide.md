# Brush Tools (GIMP 2.10)

GIMP's brush tools live under **Tools → Paint Tools** and cover five ways to lay down color: **Pencil** (`N`), **Paintbrush** (`P`), **Airbrush** (`A`), **Ink** (`K`), and **MyPaint Brush** (`Y`). They all share the same brush library (except Ink, which uses its own nib system) and paint with the current foreground color.

The **Pencil** produces hard, aliased strokes with no feathering — ideal for pixel-art or icon work where every pixel must land exactly. The **Paintbrush** is the workhorse: anti-aliased, fuzzy-edged, and the one you'll reach for most. The **Airbrush** adds time-based buildup — hold it still and paint accumulates, controlled by its **Rate** and **Flow** sliders. **Ink** simulates a calligraphy pen whose nib shape, angle, and size you can tweak under its Adjustment and Type/Shape options. **MyPaint Brush** (added in 2.10.6) gives access to the huge MyPaint brush ecosystem; install new sets by dropping them into the folder shown at **Edit → Preferences → Folders → MyPaint Brushes**.

All these tools share common options in the Tool Options dock: **Mode**, **Opacity**, **Brush**, **Size**, **Spacing**, **Hardness**, **Force**, and **Dynamics**. Bump size precisely with arrow keys (±0.01) or Page Up/Down (±1.00). Enable **Apply Jitter** to scatter marks randomly, or **Smooth Stroke** to iron out wobbly mouse lines. **Lock brush size to view** keeps the brush visually constant as you zoom — great for iterative detail work.

Hold **Ctrl** with any brush tool to temporarily switch to the color picker. Hold **Shift** and click two points to paint a straight line between them. **Ctrl+Shift** constrains that line to 15° increments for perfect horizontals, verticals, or diagonals.

You can also apply any brush tool automatically: create a selection or path, then use **Edit → Stroke Selection** (or **Stroke Path**) and choose your paint tool — all current tool options apply to the stroke.
