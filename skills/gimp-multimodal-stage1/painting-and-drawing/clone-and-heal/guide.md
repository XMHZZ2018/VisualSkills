# Clone, Heal, and Perspective Clone (GIMP 2.10)

The Clone tool copies pixels from one spot to another using the current brush — think of it as a stamp you keep reloading from a source area. Activate it via **Tools > Paint Tools > Clone** or press **C**. Before you can paint, you need to set a source: hold **Ctrl** and click somewhere in any open image. The crosshair cursor confirms you're in source-selection mode. Once the source is set, paint on your target area and pixels flow from the source to your brush.

See `fig01.png`.

Under **Source** in Tool Options you can switch between **Image** (sampling from a layer) and **Pattern** (tiling a pattern). Enable **Sample merged** if you want to clone the composite of all visible layers — handy for non-destructive work on a separate transparent layer above your image.

The **Alignment** setting controls how the source tracks your brush. **None** resets the source origin with every stroke (good for repeated stamps). **Aligned** locks the offset after your first stroke so multiple passes blend seamlessly. **Registered** maps source and destination pixel-for-pixel across layers — perfect for painting filtered effects onto an original. **Fixed** always samples the exact same point no matter where you move.

The Heal tool is essentially a smarter clone. Open it with **Tools > Paint Tools > Heal** or press **H**. You set a source the same way (**Ctrl**-click), but when you paint, the tool blends the source texture into the surrounding colour and lighting of the destination. This makes it ideal for removing skin blemishes, dust spots, or small scratches — the repair blends rather than leaving obvious copied patches.

See `fig02.png`.

For Heal, choose a soft brush sized just a bit larger than the defect, sample from clean skin or background nearby, then click or drag over the blemish. Slight defects disappear in one click; for larger problems, build up with multiple light strokes rather than one heavy pass to avoid smearing.

Perspective Clone lets you clone while respecting vanishing-point geometry — useful for floors, walls, or any receding surface. Activate it via **Tools > Paint Tools > Perspective Clone**. The workflow has two modes, toggled in Tool Options: first select **Modify Perspective** and drag the corner handles to define your vanishing plane, then switch to **Perspective Clone** and Ctrl-click a source as usual. When you paint, the cloned content scales and skews to match the perspective grid you defined.

See `fig03.png`.

All three tools share common brush settings (size, opacity, hardness, dynamics) and respect layer boundaries. A pro tip: combine Clone with **Registered** alignment on a duplicated, filtered layer to create a "filter brush" — you selectively paint the filter effect only where you want it.
