# ToonzScript (OpenToonz 1.7)

ToonzScript is OpenToonz's built-in scripting language, based on ECMAScript (so if you know JavaScript, you're mostly there). It lets you automate repetitive tasks — batch vectorizing, renumbering frames, rendering scenes — by writing `.js` files or typing commands directly into a console.

To run a saved script, go to **File > Script > Run Script...** and browse for your `.js` file. Scripts live in `OpenToonz stuff/library/script/` by default, and the browser picks them up automatically. For quick one-off commands, open the interactive console via **File > Script > Open Script Console...** instead.

See `fig01.png`.

In the console, only the last paragraph is editable. Use the Up/Down arrow keys to cycle through command history — handy when you're iterating on a transform or tweaking vectorizer settings. Long-running operations won't block the UI, and you can interrupt them with **Ctrl+Y**. One path quirk: backslashes in strings must be doubled (`C:\\tmp\\file.tif`), or just use forward slashes — both work. Dragging a file into the console auto-inserts its escaped path.

The core classes give you building blocks for most automation jobs. `FilePath` handles path manipulation and existence checks. `Image` and `Level` let you load, save, and inspect drawings (TLV, PLI, or full-color). `Scene` gives full xsheet access — you can read cells, move them between columns, insert columns, and load or create levels programmatically. `Transform` and `ImageBuilder` handle geometric operations: rotate, scale, translate, and composite multiple images together.

For vectorization, you get two flavors: `OutlineVectorizer` and `CenterlineVectorizer`. Both accept raster or ToonzRaster input and spit out vector output. Configure attributes like `accuracy`, `despeckling`, and `maxColors`, then call `.vectorize()` on your image or level. The `Rasterizer` class does the reverse — vector to raster — with control over resolution and DPI. Set `.colorMapped = true` if you want ToonzRaster (TLV) output instead of plain raster.

The `Renderer` class renders entire scenes or selected frames/columns. Assign column and frame index arrays to `.columns` and `.frames` to render a subset, or leave them empty to render everything. A typical workflow: load a scene, configure the renderer, call `.renderScene()`, and save the resulting level.

Here's a taste of what a real script looks like — vectorizing a single image:

```js
dir = "C:\\OpenToonz stuff\\SCRIPT IMAGES IN\\";
a = new Image(dir + "drawing.0001.tif");
v = new OutlineVectorizer();
v.accuracy = 10;
v.maxColors = 10;
v.vectorize(a).save("C:\\output\\vec.pli");
```

And rotating every frame of a level into a spin animation:

```js
a = new Level("C:\\input\\walk..tif");
b = new Level();
t = new Transform();
fids = a.getFrameIds();
for (i = 0; i < a.frameCount; i++) {
    ib = new ImageBuilder();
    b.setFrame(fids[i], ib.add(a.getFrame(fids[i]), t.rotate(360 / a.frameCount)).image);
}
b.save("C:\\output\\rotated..tif");
view(b);
```

The `view()` command pops the result into a flipbook window so you can check your work without leaving the script workflow. Between `print()` for logging, `run()` for chaining scripts together, and the `ToonzVersion` variable for version checks, you have everything you need to build reliable automation pipelines.
