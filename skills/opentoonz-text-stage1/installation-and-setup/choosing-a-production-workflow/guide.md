# Choosing a Production Workflow (OpenToonz 1.7)

OpenToonz supports two main production workflows, and your choice depends on whether your animation originates on paper or entirely on screen.

## Traditional (Paper-Based) Workflow

Start by defining your hand-drawn animation levels in the Xsheet, then scan them into OpenToonz. Scanned images go through cleanup and auto-centering (using pegbar holes and field guide settings). Lineart drawings get prepped for painting. You can supplement scanned work with drawings made directly in OpenToonz — backgrounds, props, or utility masks for matte effects.

Create color models for reference, define a palette of styles, then paint your levels using index-linked palette styles. The big win here: editing a palette style automatically updates every line and fill that uses it, so you can adjust colors long after painting is done.

Once painted, expose everything in the Xsheet, animate with interpolated keys on cameras, columns, and pegbars, apply Special FX (blurs, lights, warps, gradients), and render — optionally distributing across a render farm via TCP/IP. Output formats include TIF, PNG, TGA, MP4, GIF, WebM, and Spritesheet.

## Paperless Workflow

The paperless path leans heavily on preproduction. Begin with concept development — a stable cast and limited settings make reusable libraries practical. Design characters with cutout animation in mind: plan pivot points that hide naturally under design features (a ribbon covering a ponytail joint, for instance).

Build a storyboard that doubles as an element inventory — every pose, prop, and background gets catalogued. From the storyboard, create an animatic in OpenToonz to lock timing and camera moves; this animatic can later be split into individual scene files.

Draw all elements directly in OpenToonz as library assets. Characters are decomposed into hierarchical skeleton components (head, torso, arms) that animators recombine. Store canonical turn-arounds and reference cycles (walk, run, jump) for reuse.

In the layout phase, load library assets into the Xsheet as Sub-Xsheets and arrange them per the animatic. Refine animation by adding key positions and tuning interpolation in the Function Editor. Apply Special FX, then render to your preferred format — the render farm handles batch processing across networked machines.
