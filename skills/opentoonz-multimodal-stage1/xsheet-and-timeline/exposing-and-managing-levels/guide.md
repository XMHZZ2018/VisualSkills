# Exposing and Managing Levels (OpenToonz 1.7)

The Xsheet (or its horizontal sibling, the Timeline) is where you control what appears in your scene and when. Each column holds one layer of animation, and each row is a frame. To get artwork into those cells, you load and expose levels — animation sequences, single images, clips, or even other OpenToonz scenes nested as Sub-Xsheets.

**Loading levels via the File Browser.** Open the built-in browser panel (its tree on the left shows My Computer, Library, History, and your Projectroot) and simply drag files into the Xsheet, Timeline, or Scene Cast. Alternatively, use **Level > Load Level…** or right-click a cell and choose **Load Level…** — this gives you a dialog where you can also pick a subsequence frame range for video or image sequences. Image sequences named with a four-digit progressive number (e.g. `walk.0001.tif`, `walk.0002.tif`) are automatically recognized as a single animation level.

See `fig01.png`.

When loading files from outside your current project folders, OpenToonz asks whether to **Import** (copy into the project) or **Load** from the original path. Importing is strongly recommended — it keeps assets safe from accidental overwrites on save.

**The Scene Cast** stores every level you've loaded or created, whether it's currently exposed or not. Think of it as a library for the current scene. To put something on stage, select it in the Scene Cast and choose **Level > Expose in Xsheet**, or just drag it onto a cell. You can organize levels into folders, and anything highlighted in red has a broken file path that needs fixing.

See `fig02.png`.

**The Level Strip** lets you cherry-pick individual drawings from an animation level. Click any exposed cell to display its level in the strip, then select specific frames and drag them into the Xsheet wherever you need them. Handy for pulling out hold frames or reordering a cycle without touching the original file.

**Editing Level Settings.** Once a level is exposed, right-click it (or go to **Level > Level Settings…**) to open its properties panel. Here you can change the level's **Name**, redirect its **Path** to a different file, adjust **DPI** or physical dimensions, toggle **Premultiply** for images with alpha halos, enable **White As Transparent** for third-party lineart, or dial in a **Subsampling** factor for faster playback of heavy rasters. The **Use Camera DPI** button is a quick fix when a level matches camera pixel dimensions but not its DPI setting.

See `fig03.png`.

**Replacing a level** is straightforward: select the cells you want to swap, then use **Level > Replace Level…** and pick the new file. The exposure order and timing you've already set up stay intact — only the artwork changes. The original level stays in the Scene Cast if you need it back.

To keep things tidy, periodically run **Level > Remove All Unused Levels** to clear the Scene Cast of anything no longer referenced in the Xsheet. And remember: the **Expose Loaded Levels in Xsheet** toggle in **Preferences… > Loading** controls whether newly loaded levels go straight into columns or quietly wait in the Scene Cast for you to place them manually.
