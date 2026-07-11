# Setting Up a Scene (OpenToonz 1.7)

Every new scene inherits settings from its parent project, keeping your production consistent. You can override any setting per-scene, and if you land on values you prefer going forward, lock them in with **File → Project Management → Save Default Settings**.

**Working units** live under **File → Preferences… → Interface**. Set **Unit** for general measurements (inches, mm, cm, fields, or pixels) and **Camera Unit** for how camera dimensions display. You can always override inline by typing a suffix like `cm`, `px`, or `fld` after a value — it converts automatically.

**Frame rate** is set in **Xsheet → Scene Settings…**. Use 24 for cinema, 25 for PAL, 30 for NTSC. The current FPS shows in the Viewer's bottom bar. If you need to deliver at a different rate later, use the **Stretch from FPS: To:** option in Output Settings rather than re-compositing.

**Camera size and resolution** are configured via **Xsheet → Camera Settings…**. You'll see fields for Width/Height (in your chosen Camera Unit), pixel resolution, DPI, and aspect ratio — changing one recalculates the others. Use the lock and radio buttons to pin whichever dimension matters most. The **Use Current Level Settings** button auto-fits the camera to your selected level. Save frequently-used setups with **Add** next to the presets dropdown.

**Color calibration** helps you preview accurate color on your monitor. Enable it in **File → Preferences… → Interface** by toggling **Color Calibration using 3D Look-up Table**, then point it at a `.3dl` file matched to your display. Restart OpenToonz afterward — the LUT then applies across the Viewer, Flipbook, Palette, and Style Editor.

**Memory tuning** keeps things responsive. Under **File → Preferences… → General**, set **Undo Memory Size (MB)** to cap how much RAM undo history consumes. If you work mostly with raster levels (scanned art), enable **Minimize Raster Memory Fragmentation** to reserve a dedicated memory block — but leave it off for vector-heavy projects so that memory isn't wasted. Both memory options require a restart.
