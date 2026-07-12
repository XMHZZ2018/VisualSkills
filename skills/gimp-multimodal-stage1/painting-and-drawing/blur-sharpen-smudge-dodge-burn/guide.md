# Blur, Sharpen, Smudge, Dodge, and Burn (GIMP 2.10)

The Blur/Sharpen tool uses your current brush to locally soften or crisp up detail. Activate it via **Tools > Paint Tools > Blur/Sharpen** or press **Shift+U**. By default it blurs — blending each pixel with its neighbors to tone down anything that pops too much. Switch to Sharpen mode by holding **Ctrl** while painting, or flip the **Convolve Type** radio button in Tool Options. Go easy on Sharpen; overdoing it creates ugly noise. For large-area work, you're better off with a filter like **Filters > Enhance > Unsharp Mask**.

See `fig01.png`.

Both modes are incremental — each pass over the same area deepens the effect. The **Rate** slider controls how aggressively the effect builds, while **Opacity** caps what a single stroke can achieve no matter how many passes you make.

The **Smudge** tool (press **S**) simulates dragging wet paint with your finger. With **Flow** at 0.00 (the default), it picks up whatever color it crosses and pushes it along your stroke. Raise Flow above zero and it instead paints with the current foreground color, blending it into the surface as you go. The **Rate** slider here acts like "smudge length" — higher values carry color farther. Enable **No erasing effect** if you want to smudge across transparent areas without eating into the alpha channel, which is handy for bridging two color regions. Hold **Shift** and click to smudge in straight lines; add **Ctrl** to constrain angles to 15° steps.

The **Dodge/Burn** tool (**Shift+D**) lightens or darkens tones, like overexposing or underexposing a photographic print. Hold **Ctrl** to toggle between the two on the fly. Under Tool Options, the **Range** menu lets you restrict the effect to Shadows, Midtones, or Highlights — so you can brighten just the light tones without blowing out the darks. The **Exposure** slider (default 50) controls how strong the shift is per stroke.

All three tools share the standard paint-tool options — brush shape, size, dynamics, jitter, smooth stroke — so you can fine-tune how they interact with your canvas just like any other brush-based tool.
