# Previewing and Rendering (OpenToonz 1.7)

Before committing to a full render, you can preview your animation directly in the Viewer or in a separate Flipbook window. Toggle preview mode with the **Preview** button in the Viewer title bar — the framebar color-codes progress: dark grey for rendered frames, light red for pending, light green for the frame currently computing.

To speed things up, define a **Sub-camera** (smaller than the full camera frame) using the **Define Sub-camera** button in the Viewer bottom bar. Only that region renders during preview, saving significant time on complex scenes.

For a standalone preview window with its own settings, go to **Render > Preview Settings…** to configure resolution, frame range, shrink, and step independently of your final output. Then hit **Render > Preview** to open the Flipbook. You can freeze, clone, or compare previews by right-clicking inside the window. Caching an effect node in the FX Schematic (right-click a node > **Cache FX**) stores its compositing result in memory so subsequent previews skip recomputation.

When you're ready for final output, open **Render > Output Settings…**. Set your camera, frame range, file format (TIF, PNG, MP4, MOV, etc.), save location, channel width, and resample balance. MP4 and WebM require FFmpeg installed separately. For transparent backgrounds, set the alpha of **Camera BG Color** to 0 in **Xsheet > Scene Settings…** and choose a format that supports alpha (TIF 32/64-bit, TGA 32-bit, or MOV with Animation codec).

Kick off the render with **Render > Render**. For background processing, use the Tasks pane — add scenes via **Add Render**, configure priority and dependencies, then hit **Start**. Tasks can be split into chunks for render-farm distribution via the **Frames Per Chunk** property. Task status is color-coded: grey (waiting), yellow (running), green (done), red (failed).
