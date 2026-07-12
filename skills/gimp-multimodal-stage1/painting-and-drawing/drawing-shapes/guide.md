# Drawing Simple Shapes and Lines (GIMP 2.10)

GIMP isn't a vector drawing program, but it handles basic shapes and lines just fine once you know the trick: you'll lean on the **Shift** key for lines, and selection tools for everything else.

## Straight Lines

Pick any brush-based tool — **Paintbrush**, **Pencil**, **Airbrush**, whatever suits you — and set your foreground color. Click once on the canvas to place a starting dot. Now hold **Shift** and move the mouse; you'll see a thin preview line stretching from that dot to your cursor. When the angle and length look right, click again to commit the stroke.

See `fig01.png`.

You can keep going — as long as **Shift** stays held, each new click extends another straight segment from the previous endpoint. Release **Shift** when you're done. The line inherits whatever brush size and opacity you've set in the tool options, so adjust those beforehand if you need something thicker or softer.

## Rectangles and Ellipses

For filled or outlined shapes, the workflow is: make a selection, then fill or stroke it. Grab the **Rectangle Select** tool (keyboard shortcut **R**) or **Ellipse Select** tool (**E**) and drag out your shape on the canvas.

To get a solid shape, choose your foreground color and hit **Edit > Fill with Foreground Color** (or just use the **Bucket Fill** tool inside the selection). For an outline instead, go to **Edit > Stroke Selection**, where you can pick the line width and style before confirming.

See `fig02.png`.

Once you're happy, remove the marching ants with **Select > None**. That's it — your shape is painted directly onto the layer.

## Tips

Hold **Shift** while dragging a selection to constrain it to a perfect square or circle. If you need a shape with rounded corners, check the **Rounded corners** option in the Rectangle Select tool options before drawing. For more complex vector shapes, GIMP's docs recommend a dedicated tool like Inkscape — but for quick rectangles, circles, and straight lines, selections plus stroke/fill get the job done fast.
