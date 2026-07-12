# Printing Images (GIMP 2.10)

GIMP includes a built-in printing module that handles page setup, image positioning, and resolution — all with a live preview so you can check things before committing ink to paper.

**Setting print size without losing quality.** Pixels don't have a fixed real-world size; resolution is what bridges the gap. Most images default to 72 ppi, which produces huge, chunky prints. To fix this, open **Image → Print Size…** to reach the "Set Image Print Resolution" dialog. Pick a unit you like (inches, cm), set one dimension to your target, and GIMP adjusts the other proportionally. This changes only the metadata — no pixels are added or removed, so quality stays intact.

Keep an eye on the resolution numbers as you adjust dimensions. At 300 ppi or above, prints look sharp and pixels are invisible. Between 150–200 ppi things are still fine for casual viewing. Below 100 ppi you'll see visible blockiness — only acceptable for posters viewed from a distance.

The X and Y resolution fields are linked by default (indicated by the chain icon between them). Click the chain to unlink them if you need independent control, though for most work you'll want them locked together.

**Sending to the printer.** When you're ready to print, go to **File → Print** (or hit **Ctrl+P**). The Print dialog has tabs for General settings, Page Setup, Image Settings, Job, Image Quality, and Advanced options. Under Image Settings you can fine-tune the output size, adjust position offsets (Left, Right, Top, Bottom), and choose centering. The Preview pane on the right shows exactly where your image will land on the page.

See `fig01.png`.

Use **Print Preview** to do a final sanity check, then hit **Print** when you're satisfied. Note that the printer's own dpi (dots per ink) is separate from your image resolution — multiple printer dots make up each pixel, so don't confuse the two numbers.
