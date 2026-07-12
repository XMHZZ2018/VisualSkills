# Layer Transparency and Alpha Channel (GIMP 2.10)

The alpha channel is what lets a layer have transparent or semi-transparent pixels. If your image is a single flat background layer, it won't have one by default — you need to add it before you can do anything involving transparency.

Everything lives under **Layer → Transparency**. That submenu is your one-stop shop for adding, removing, and converting alpha information.

See `fig01.png`.

**Adding an alpha channel** is the first thing to do when you want transparency on a background layer. Go to **Layer → Transparency → Add Alpha Channel**. You can also right-click the layer in the Layers dialog and pick **Add Alpha Channel** from the context menu. Once added, the eraser tool will actually erase to transparent instead of painting with the background color. Note that multi-layer images get an alpha channel automatically — this command is really for that initial single-layer case.

**Removing the alpha channel** does the opposite: any transparent areas get filled with the current background color from the Toolbox. Hit **Layer → Transparency → Remove Alpha Channel**. This is handy when you need to flatten transparency out of a specific layer without flattening the whole image. The command is greyed out if the layer never had an alpha channel to begin with.

**Color to Alpha** is one of GIMP's most useful tricks for isolating subjects. Open it via **Layer → Transparency → Color to Alpha…** and pick the color you want to vanish — typically white, for scanned line art or logos. GIMP converts that color (and shades close to it) into varying levels of transparency, preserving anti-aliased edges beautifully. The layer must already have an alpha channel for this to work.

**Alpha to Selection** lets you turn the current layer's transparency into a selection — opaque pixels become fully selected, transparent ones become unselected, and semi-transparent areas become partially selected. Access it through **Layer → Transparency → Alpha to Selection** or from the layer's right-click menu. This replaces your current selection entirely. If you'd rather combine it with an existing selection, use the sibling commands **Add to Selection**, **Subtract from Selection**, or **Intersect with Selection** in the same submenu.
