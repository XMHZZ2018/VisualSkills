I have all the information needed. Here's the guide:

# Levels and Curves (GIMP 2.10)

Open Levels via **Colors → Levels…**. The dialog shows a histogram of your image's tonal distribution. Use the **Channel** dropdown to work on **Value** (overall brightness), individual **Red/Green/Blue** channels, or **Alpha** (transparency).

Under **Input Levels**, drag the black triangle right to deepen shadows, the white triangle left to brighten highlights, and the gray triangle to shift midtones. Alternatively, use the eyedropper buttons — the dark one picks your black point, the white one picks your white point — directly from the image.

**Output Levels** compresses the tonal range: slide the black handle up to lighten the darkest tones, or the white handle down to darken the brightest. This reduces contrast intentionally, useful for faded or matte looks.

For a quick fix on underexposed shots, drag the white input slider left until it meets the histogram data, then nudge the gamma slider left to open up midtones. Hit **Auto Input Levels** if you want GIMP to guess for you.

When you need finer control, open **Colors → Curves…** (or click **Edit these Settings as Curves** at the bottom of Levels). Curves maps input tones to output tones along a diagonal line — click anywhere on the curve to add a control point, then drag it up to brighten or down to darken that tonal range.

A classic S-curve — lifting the upper-midtone point and lowering the lower-midtone point — boosts contrast in the midtones while leaving extremes mostly alone. A steeper curve means more contrast in that range; a flatter curve means less.

You can Ctrl-click on the image canvas to place a point on the curve at exactly that pixel's value — handy for targeting a specific tone. Use **Shift**-click to add a point only in the active channel. Switch the curve type to **Free Hand** to draw arbitrary adjustments, then click **Smooth** to clean it up.

Both tools support **Preview** and **Split view** for real-time before/after comparison. When you're done, just click **OK** to apply.
