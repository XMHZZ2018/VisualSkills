# ToonzScript (OpenToonz 1.7)

ToonzScript is OpenToonz's built-in scripting language, based on ECMAScript (so if you know JavaScript, you're mostly there). It lets you automate repetitive tasks — batch vectorizing, renumbering frames, rendering scenes — without clicking through menus over and over.

To run a saved script, go to **File > Script > Run Script...** and pick a `.js` file from `OpenToonz stuff/library/scripts/`. For quick one-off commands, open the interactive console via **File > Script > Open Script Console...** — you type a line, hit enter, and see results immediately. Use the Up/Down arrow keys to cycle through command history, and **Ctrl+Y** to kill a long-running operation.

Paths in strings need doubled backslashes (`C:\\tmp\\file.tif`) or just use forward slashes (`C:/tmp/file.tif`). Dragging a file into the console inserts its properly-escaped path automatically.

The core classes cover the full pipeline: `FilePath` for navigating directories, `Image` and `Level` for loading/saving artwork, `Scene` for manipulating xsheets (set cells, insert columns, load levels), `Transform` and `ImageBuilder` for geometric operations and compositing, `OutlineVectorizer` and `CenterlineVectorizer` for converting raster art to vectors, `Rasterizer` for the reverse, and `Renderer` for outputting final frames.

A typical workflow looks like this — load a level, process each frame, save the result:

```js
dir = "C:/OpenToonz stuff/SCRIPT IMAGES IN/";
a = new Level(dir + "toad3..tif");
b = new Level();
fids = a.getFrameIds();
t = new Transform();
for (i = 0; i < a.frameCount; i++) {
    ib = new ImageBuilder();
    b.setFrame(fids[i], ib.add(a.getFrame(fids[i]), t.rotate(360 / a.frameCount)).image);
}
b.save("C:/output/rotated..tif");
view(b);
```

Use `print()` to log progress, `view()` to preview images or levels in a flipbook, and `run("other.js")` to chain scripts together. The variable `ToonzVersion` gives you the current build if you need version-gated logic.
