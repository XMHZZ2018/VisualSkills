# Blur, Sharpen, Smudge, Dodge, and Burn (GIMP 2.10)

These five paint tools let you make targeted, local adjustments by brushing directly over your image — no selections or filters required.

**Blur/Sharpen** lives at **Tools → Paint Tools → Blur/Sharpen** (or press **Shift+U**). Paint over an area to soften it (Blur) or increase local contrast (Sharpen). Hold **Ctrl** to flip between modes on the fly. The **Rate** slider controls how aggressively the effect builds with each stroke. Go easy with Sharpen — overdoing it creates ugly noise; for broader sharpening, reach for **Filters → Enhance → Unsharp Mask** instead.

**Smudge** (**Tools → Paint Tools → Smudge**, shortcut **S**) works like dragging your finger through wet paint. With **Flow** at 0.00 it pulls existing color along the stroke; raise Flow above zero and it blends the current foreground color in as you drag. The **Rate** slider controls how far the smudge carries. Enable **No erasing effect** to preserve transparency when smudging near edges — handy for filling gaps between color regions. Hold **Shift** and click to smudge in a straight line.

**Dodge/Burn** (**Tools → Paint Tools → Dodge / Burn**, shortcut **Shift+D**) lightens (Dodge) or darkens (Burn) tones under your brush, mimicking darkroom exposure control. Hold **Ctrl** to toggle between the two. Use the **Range** dropdown to restrict the effect to **Shadows**, **Midtones**, or **Highlights** only. The **Exposure** slider (0–100) sets the strength — start around 20–30 for subtle adjustments and build up gradually.

All three tools are incremental: repeated strokes over the same area compound the effect. Use **Opacity** to cap how much a single stroke can change, and **Rate** to control how fast it accumulates.
