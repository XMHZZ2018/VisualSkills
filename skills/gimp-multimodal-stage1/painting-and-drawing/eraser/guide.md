# Erasing (GIMP 2.10)

The Eraser removes color from the current layer or selection. What it reveals depends on context: if your layer has an alpha channel, you get transparency (that classic checkerboard pattern). If it doesn't — like a flattened Background layer — erasing paints in whatever your current background color is, as shown in the Toolbox's color swatch.

Activate the Eraser through **Tools > Paint Tools > Eraser**, by clicking its icon in the Toolbox, or just hit **Shift+E**.

The **Opacity** slider works a bit counterintuitively here — higher opacity means *more* erasure, not less. At 100%, you wipe pixels completely; lower values give you a softer, partial erase that gradually builds transparency.

If you need a clean, total erase with no fuzzy edges, tick **Hard edge** in the Tool Options. Without it, sub-pixel brush placement can leave faint traces at stroke boundaries even with a hard brush selected.

See `fig01.png`.

Hold **Ctrl** while using the Eraser and it becomes a color picker — but unlike other tools, it grabs a *background* color rather than foreground. Handy for matching the erase color on non-transparent layers.

The **Anti Erase** option is the real hidden gem. Check it in Tool Options (or hold **Alt** on the fly) and you can *restore* previously erased pixels, even fully transparent ones. This works because erasing only touches the alpha channel — the RGB data is still hiding underneath. Anti-erase just brings the alpha back up so you can see it again. This only works on layers that have an alpha channel.

If **Alt** is grabbed by your window manager, try **Alt+Shift** instead.

One more trick: you can use the Eraser to reshape a floating selection by trimming its edges. And if you work with a tablet, assign the stylus's back end to the Eraser in the Toolbox — it'll stay assigned independently of what the tip uses.
