# Setting Up a Scene (OpenToonz 1.7)

Every new scene inherits settings from its parent project — camera size, frame rate, output options, and so on. This keeps your production consistent without manual setup each time. If you tweak settings for a particular scene, those changes save with the scene file and won't affect the rest of the project. To push your current scene's settings back as the new project defaults, go to **File > Project Management > Save Default Settings**.

## Working Units

Measurements throughout the interface can display as inches, millimeters, centimeters, fields, or pixels. Head to **File > Preferences… > Interface** and set the **Unit** dropdown for general measurements and **Camera Unit** for how camera dimensions are expressed. You can always override inline by typing a suffix like `cm`, `px`, or `fld` after a number — it converts automatically.

## Frame Rate

Open **Xsheet > Scene Settings…** and set the **Frame Rate** field to match your delivery format — 24 for film, 25 for PAL, 30 for NTSC. The current rate also shows in the Viewer's bottom bar. If you later need to render at a different rate without recompositing, use the **Stretch from FPS: To:** option in Output Settings rather than changing the scene itself.

See `fig01.png`.

## Camera Settings

Open the camera dialog via **Xsheet > Camera Settings…**. You'll see width and height (in your chosen camera unit), the resulting **A/R**, pixel resolution, and DPI — all interlinked. Change one value and the others update to stay consistent. Use the lock buttons to pin whichever dimension you want preserved. The **Use Current Level Settings** button auto-calculates a camera that exactly frames your selected level. Below the fields is a preset dropdown — pick a standard resolution or define your own with **Add**, and remove outdated ones with **Remove**.

See `fig02.png`.

## Color Calibration with 3D LUTs

For accurate color previsualization on your monitor, enable **Color Calibration using 3D Look-up Table** in **File > Preferences… > Interface**. Point the **3DLUT File** browser to your `.3dl` file (only this format is supported). After a restart, the Viewer, Flipbook, Palette, and Style Editor all display through the LUT — useful when targeting Rec. 709, DCI-P3, or Rec. 2020. Note that on non-Windows platforms, monitor auto-detection isn't available, and multiple monitors aren't yet supported.

See `fig03.png` for the viewer comparison without and with a 3D LUT applied.

## Memory Settings

Under **File > Preferences… > General**, the **Undo Memory Size (MB)** field caps how much RAM undo history can consume. Once the limit is hit, the oldest operations are discarded. If you work heavily with raster levels (scanned art, TLV files), enable **Minimize Raster Memory Fragmentation** in the same panel — it reserves a dedicated memory block for raster operations, preventing slowdowns from fragmentation over long sessions. Disable it if your project is mostly vector-based, since the reserved block would just sit idle. Both memory options require a restart to take effect.
