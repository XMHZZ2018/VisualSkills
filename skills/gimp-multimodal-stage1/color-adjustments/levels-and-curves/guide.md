# Levels and Curves (GIMP 2.10)

Open Levels via **Colors > Levels…** — you'll see a histogram of your image's tonal distribution with three sliders beneath it: black (shadows), gray (midtones), and white (highlights). The goal is simple: tell GIMP where black and white actually live in your image, and let it redistribute everything in between.

See `fig01.png`.

The **Channel** dropdown defaults to **Value**, which affects overall brightness. Switch to **Red**, **Green**, or **Blue** to fix a color cast — pulling back a dominant channel is often all you need. If your layer has transparency, the **Alpha** channel lets you reshape opacity the same way.

Drag the black input slider rightward until it meets the left edge of your histogram data — shadows deepen and contrast snaps into place. Do the same with the white slider from the right. The gray midtone slider shifts overall brightness without clipping: slide it left to brighten, right to darken. You can also use the eyedroppers in the **All Channels** section: pick a black point, a white point, and optionally a neutral gray directly from the image.

The **Output Levels** bar at the bottom does the opposite — it compresses your tonal range. Pulling the black output slider up lightens the darkest tones (useful for print-safe blacks), while pulling the white slider down tames blown highlights. Use this when you need to *reduce* contrast intentionally.

When Levels isn't precise enough, click **Edit these Settings as Curves** at the bottom of the dialog, or go directly to **Colors > Curves…**. Curves gives you a diagonal line on an input-vs-output grid. Click anywhere on that line to add a control point, then drag it up (brighter) or down (darker). The steeper a section of the curve, the more contrast that tonal range gets.

The classic S-curve — pulling shadows slightly down and highlights slightly up — boosts midtone contrast without blowing out the extremes. For color correction, switch to an individual channel and reshape just that curve. A gentle bump in the Red channel warms the image; pulling it down cools things toward cyan.

You can Ctrl-click on the image canvas while Curves is open to place a point at that pixel's exact tonal value — handy for targeting a specific area without guessing. Shift-click does the same but only for the active channel. Points can be toggled between **Smooth** and **Corner** types in the options below the grid, letting you create sharp transitions when needed.
