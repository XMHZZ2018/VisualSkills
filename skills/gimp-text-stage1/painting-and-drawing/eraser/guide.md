# Erasing (GIMP 2.10)

The Eraser removes color from the current layer. What it reveals depends on context: if your layer has an alpha channel, you get transparency (the classic checkerboard). Without one — like a flattened Background layer — erasing paints with whatever your current background color is.

Activate it via **Tools > Paint Tools > Eraser**, click the eraser icon in the Toolbox, or just press **Shift+E**.

The **Opacity** slider controls erasure strength. Crank it to 100 for full removal; lower values produce partial transparency on alpha-enabled layers. If you need a clean, pixel-perfect erase with no soft edges, tick **Hard edge** in the Tool Options — otherwise sub-pixel brush placement leaves faint remnants even with a hard brush.

Hold **Ctrl** while clicking to pick a color — but unlike other tools, the Eraser samples into the *background* color, which makes sense since that's what non-alpha erasure reveals.

The real trick is **Anti Erase**: check it in Tool Options or hold **Alt** while painting. This *restores* previously erased pixels on an alpha layer. The RGB data never actually disappears when you erase — only the alpha drops to zero — so anti-erase bumps the alpha back up, making hidden content reappear. If your window manager grabs **Alt**, try **Alt+Shift** instead.

If you use a tablet, tap the stylus's reverse end on the Eraser icon once — GIMP remembers tool assignments per input device, so the back end stays an eraser permanently.

You can also erase into a floating selection to trim its shape, which is handy for quick compositing cleanups.
