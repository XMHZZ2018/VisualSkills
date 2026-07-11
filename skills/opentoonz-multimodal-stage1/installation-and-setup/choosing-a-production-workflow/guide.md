# Choosing a Production Workflow (OpenToonz 1.7)

OpenToonz supports two main production workflows, and the one you pick shapes your entire pipeline. The choice boils down to whether your animation starts on paper or entirely on screen.

## Traditional (Paper-Based) Workflow

If your team draws on paper, the traditional pipeline is your path. You scan hand-drawn animation levels into OpenToonz, then run them through cleanup — auto-centering frames using pegbar holes and field guide settings. Once lineart is clean, drawings move into the **Ink & Painting** stage where you fill areas using palette styles linked by index. The beauty here is that changing a single palette style instantly updates every line and fill that references it, even after painting is done.

You build a **Color Model** as a reference for consistent painting across the production — this can be a drawing made in OpenToonz, a processed scan, or an image from external software. From there, all painted levels and imported assets land in the **Xsheet** for compositing: you layer columns, animate the camera and pegbars with interpolated keys, and apply Special FX (blurs, warps, gradients, etc.). Finally, you render — locally or across a network via the built-in **Render Farm** using TCP/IP.

See `fig01.png`.

## Paperless Workflow

Going fully digital front-loads more preproduction work but pays off with reusable asset libraries. You start with concept and graphic design — paying special attention to how character pivot points can be hidden under natural drawing features (a ribbon hiding a ponytail joint, for instance). The storyboard doubles as an asset inventory, listing every character pose, prop, and background needed per scene.

From the storyboard you build an **Animatic** in OpenToonz (or externally), importing scanned boards and roughing in timing and camera moves. Meanwhile, you draw all reusable elements — characters decomposed into skeleton parts (head, torso, arms), turn-around models, walk cycles — and store them in **Libraries**. During **Layout**, you load library elements into the Xsheet as Sub-Xsheets, place them per the animatic, and rough in key positions. The **Animation** phase refines those keys, tweaks poses, and dials in interpolation curves via the Function Editor. After applying **Special FX**, you render exactly as in the traditional path.

See `fig02.png`.

## Which Should You Choose?

Pick traditional if you already have paper drawings or prefer the tactile feel of hand-drawn animation. Pick paperless if you want cutout-style animation with heavy asset reuse across episodes — especially for series with a stable cast and recurring sets. Both pipelines converge at compositing and rendering, so you can even mix them within a single project.
