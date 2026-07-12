# Layer Transparency and Alpha Channel (GIMP 2.10)

The alpha channel is what gives a layer the ability to be transparent. If your image has only a single background layer, it won't have one by default — you'll need to add it before any transparency tricks will work.

To add it, go to **Layer → Transparency → Add Alpha Channel**. You can also right-click the layer in the Layers dialog and pick **Add Alpha Channel** from the context menu. Once it's there, the checkerboard pattern shows through anywhere you erase or delete pixels.

If you want to get rid of transparency on a layer, use **Layer → Transparency → Remove Alpha Channel**. Any transparent areas get filled with whatever your current background color is in the Toolbox, so set that first if it matters.

**Color to Alpha** is incredibly handy for removing backgrounds. Hit **Layer → Transparency → Color to Alpha…**, pick the color you want gone (white is the default), and GIMP converts all instances of that color into transparency — with smooth partial transparency for pixels that are close to that color. Great for extracting objects from solid-colored backgrounds.

**Alpha to Selection** turns your layer's existing transparency into a selection. Opaque pixels become fully selected, transparent pixels become unselected, and translucent pixels become partially selected. Find it at **Layer → Transparency → Alpha to Selection**. This replaces your current selection entirely.

If you'd rather combine with an existing selection, the sibling commands — **Add to Selection**, **Subtract from Selection**, and **Intersect with Selection** — sit right below it in the same menu and let you union, subtract, or intersect the alpha-based selection with whatever you already have active.
