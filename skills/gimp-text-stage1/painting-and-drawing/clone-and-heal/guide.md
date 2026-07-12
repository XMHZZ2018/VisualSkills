# Clone, Heal, and Perspective Clone (GIMP 2.10)

The **Clone** tool copies pixels from a source to your brush tip — great for patching damaged areas or painting with a pattern. Activate it via **Tools → Paint Tools → Clone** or press **C**. Before painting, hold **Ctrl** and click on the area you want to sample from; the cursor shows a crosshair to confirm source selection. Set **Source** to **Image** for pixel-based cloning or **Pattern** to tile a repeating fill.

The **Alignment** option controls how the source tracks your brush. **None** resets the source origin with every new stroke (good for stamping the same spot repeatedly). **Aligned** locks a fixed offset after your first stroke, so multiple passes mesh seamlessly. **Registered** maps each pixel 1:1 between source and destination layers — handy for "filter brush" effects where you paint a filtered copy back onto the original. **Fixed** always samples from the exact source point regardless of brush movement.

The **Heal** tool (**Tools → Paint Tools → Heal**, shortcut **H**) works like Clone but blends the sampled texture into the surrounding color and lighting of the destination. This makes it ideal for removing wrinkles, spots, or small blemishes — just **Ctrl**-click a clean area nearby, then paint over the defect. Unlike Clone, Heal won't leave obvious color seams at the edges of your strokes.

For surfaces with vanishing points — like a tiled floor or brick wall receding into the distance — use **Perspective Clone** (**Tools → Paint Tools → Perspective Clone**). It has two modes: first select **Modify Perspective** and drag the corner handles to match the scene's perspective plane, then switch to **Perspective Clone** and **Ctrl**-click your source. When you paint, the cloned pixels scale and skew to follow the perspective grid you defined.

All three tools share the standard brush options (size, opacity, hardness, dynamics). Enable **Sample Merged** on any of them to sample from all visible layers at once, letting you clone non-destructively onto a separate transparent layer above your image.
