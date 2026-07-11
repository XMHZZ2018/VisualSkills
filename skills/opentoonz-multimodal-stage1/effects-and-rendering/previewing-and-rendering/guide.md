# Previewing and Rendering (OpenToonz 1.7)

Before committing to a full render, you can preview your animation directly in the Viewer. Click the **Preview** button in the Viewer title bar to enter Preview mode — the current frame renders using the active camera, and as you scrub through frames the framebar color-codes progress: dark grey for rendered, light red for pending, light green for currently processing. If you only care about a specific region, activate **Define Sub-camera** in the bottom bar, drag out a box, then hit **Sub-camera Preview** to render just that area.

For a more configurable preview, open **Render > Preview Settings…** to set a different resolution, frame range, shrink factor, or resample balance — handy when you want fast feedback without waiting for full-res frames. Then launch it with **Render > Preview**, which opens a separate Flipbook window. You can freeze, clone, or compare previews by right-clicking inside that window.

See `fig01.png`.

The Flipbook itself is a versatile viewer — use the **Snapshot** and **Compare to Snapshot** buttons to overlay two frames with a draggable wipe, toggle channel display (R/G/B/Alpha), or check the **Histogram** for exposure issues. Link multiple open Flipbooks via **Play > Link Flipbooks** to scrub them in sync.

When you're ready for final output, open **Render > Output Settings…**. Here you choose the output camera and resolution, set the frame range and step, pick a file format (TIF sequences, MP4, MOV, WebM via FFmpeg, etc.), and configure resample balance, channel width, dedicated CPUs, and render tile size. The **Render** button at the bottom kicks off the process immediately.

See `fig02.png`.

For background rendering, use the Tasks pane (**Windows > Tasks**). Add scenes with **Add Render**, configure priority, frame range, and chunk size per task, then hit **Start**. Task icons turn yellow while running, green on success, red on failure. You can set dependencies between tasks so one waits for another to finish before starting.

See `fig03.png`.

To render with transparency — say, for compositing in another app — go to **Xsheet > Scene Settings…** and set **Camera BG Color** alpha to 0, then choose a format that supports alpha (TIF 32/64-bit, TGA 32-bit, or MOV with the Animation codec). For video formats you can also attach a **Clapperboard** via the Output Settings to prepend scene metadata as a static frame.
