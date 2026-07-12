# Converting Selections to Paths and Channels (GIMP 2.10)

Selections in GIMP are transient — the moment you click elsewhere or start a new selection, they're gone. Saving them as channels or converting them to paths gives you durable, reusable outlines you can come back to any time.

**Saving a selection to a channel** is the quickest way to store it for later. Head to **Select → Save to Channel** and your current selection becomes a channel mask, visible in the Channels dialog. Think of it like a grayscale snapshot of your selection — white areas are selected, black areas aren't. You can reload it as a selection whenever you need it, even after closing and reopening the file.

**Converting a selection to a path** is handy when you want to refine the outline with precise control points. Go to **Select → To Path** and the marching ants become a vector path. Nothing visually changes on the canvas, but flip over to the Paths dialog and you'll see it sitting there. From that point you can grab the **Path tool** and drag anchor points around to fine-tune curves and corners — something you can't easily do with a raw selection.

For more control over how the conversion happens, access the command from the Paths dialog instead of the menu — it exposes advanced options that let you tweak the tracing algorithm's sensitivity.

**Going the other direction — path to selection — is just as simple.** Use **Select → From Path** or hit **Shift+V**. If your path isn't closed, GIMP connects the endpoints with a straight line and fills the resulting shape as a selection. The original path stays intact, so you can reuse it.
You can also click the **Path to Selection** button directly in the Paths dialog for a one-click conversion without touching the menu.

The practical workflow here: make a rough selection with any tool, convert it to a path for precision editing, then convert it back to a selection when you're ready to paint, fill, or mask. Save important selections to channels so you never lose them.
