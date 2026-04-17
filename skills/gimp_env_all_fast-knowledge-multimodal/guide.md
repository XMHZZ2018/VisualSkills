# Color Correction in GIMP 2.10 — Levels & Color Balance

## Overview

GIMP provides two key tools for color correction:

- **Colors > Levels** — adjust brightness, contrast, and per-channel tonal range
- **Colors > Color Balance** — shift color casts by adjusting complementary color pairs

Do NOT use Brightness/Contrast (Colors > Brightness-Contrast) — it applies a flat shift that clips highlights and shadows. Use Levels or Color Balance instead.

---

## Tool 1: Colors > Levels

The Levels tool controls the tonal range of an image through its histogram.

### Opening the dialog

Go to **Colors > Levels** from the menu bar. The "Adjust Color Levels" dialog appears.

Read the screenshot `levels-dialog-value.png` — it shows the Levels dialog with:
- **Channel** dropdown at top (set to "Value" for overall brightness)
- **Input Levels** section: a histogram showing the tonal distribution, with black-point slider (left), gamma/midtone slider (middle), and white-point slider (right)
- **Output Levels** section: two sliders controlling the output range
- **Preview** checkbox at bottom left

### Brightening an underexposed image (Value channel)

1. Open **Colors > Levels**.
2. Make sure **Channel** is set to **Value**.
3. Look at the histogram — if the data doesn't reach the right edge, the image is underexposed.
4. Drag the **white-point slider** (right side of Input Levels) leftward to where the histogram data ends. This stretches the tonal range to use the full brightness scale.
5. Drag the **gamma slider** (middle) slightly to the left to boost midtones.
6. Check **Preview** to see the effect on the canvas.
7. Click **OK** to apply.

Read the screenshot `levels-dialog-value-adjusted.png` — it shows the Levels dialog after adjusting the Value channel sliders, with the image visibly brighter.

### Per-channel color correction with Levels

The Levels tool can also fix color casts by adjusting individual R/G/B channels. Use the **Channel** dropdown to switch between Red, Green, and Blue.

Read the screenshot `levels-dialog-red-channel.png` — it shows the Levels dialog with Channel set to "Red". The Output Levels bar appears in red. Adjusting the red channel's output levels controls how much red is present in the image.

Read the screenshot `levels-dialog-green-channel.png` — it shows the Levels dialog with Channel set to "Green". The Output Levels bar appears in green.

For each channel:
- **Input Levels**: drag sliders to set the tonal range for that color
- **Output Levels**: constrain the output range to reduce or boost that color
  - Reducing the output maximum (dragging the right Output slider left) removes that color from highlights
  - Increasing the output minimum (dragging the left Output slider right) adds that color to shadows

**Example — fixing a warm (orange/yellow) cast:**
1. Switch Channel to **Red** — slightly reduce the Output Levels maximum to pull back excess red
2. Switch Channel to **Blue** — slightly increase the Output Levels minimum to add blue (counteracts yellow)
3. Toggle Preview on/off to compare before and after
4. Click **OK**

---

## Tool 2: Colors > Color Balance

The Color Balance tool adjusts complementary color pairs across shadows, midtones, and highlights separately.

### Opening the dialog

Go to **Colors > Color Balance** from the menu bar.

Read the screenshot `color-balance-dialog.png` — it shows the Color Balance dialog with:
- **Select Range to Adjust**: radio buttons for Shadows, Midtones (selected by default), Highlights
- **Adjust Color Levels**: three sliders for complementary color pairs:
  - **Cyan ↔ Red**
  - **Magenta ↔ Green**
  - **Yellow ↔ Blue**
- **Preserve luminosity** checkbox (keep this checked)
- **Reset Range** button to undo changes for the selected range

### Correcting a color cast

1. Open **Colors > Color Balance**.
2. Select the tonal range to adjust (start with **Midtones**).
3. Drag the sliders toward the color you want to add:
   - Image too warm (orange/yellow)? Drag toward **Cyan** and toward **Blue**
   - Image too cool (blue)? Drag toward **Red** and toward **Yellow**
   - Image too green? Drag toward **Magenta**
   - Image too magenta? Drag toward **Green**
4. Repeat for **Shadows** and **Highlights** if needed.
5. Check **Preview** to compare.
6. Click **OK** to apply.

**Tip:** Make small adjustments. Moving sliders too far introduces a new color cast. Work in increments and toggle Preview to check.

---

## Workflow summary

| Task | Tool | Menu path |
|------|------|-----------|
| Brighten an underexposed image | **Levels** (Value channel) | Colors > Levels |
| Fix a color cast quickly | **Color Balance** | Colors > Color Balance |
| Fix a color cast precisely | **Levels** (per-channel R/G/B) | Colors > Levels |

### Step-by-step for any color correction task:

1. Open the image in GIMP
2. First fix **exposure** — Colors > Levels, Value channel, adjust white-point and gamma
3. Then fix **color** — Colors > Color Balance (quick) or Colors > Levels per-channel (precise)
4. Enable **Preview** to verify each change
5. Click **OK** to apply
6. Export via **File > Export As**

---

## Filter: Neon Edges (Filters > Edge-Detect > Neon)

The Neon filter detects edges and renders them as bright, glowing colored lines on a black background — similar to neon signs.

### Before and after

Read the screenshot `neon-before.png` — it shows a sample image before applying the neon edges filter (a cityscape scene with buildings, mountains, and a tree).

Read the screenshot `neon-after.png` — it shows the same image after applying Filters > Edge-Detect > Neon. Notice:
- The background is **completely black**
- Object edges appear as **bright, vivid colored lines** (cyan, magenta, yellow, green, white)
- The effect is **dramatic** — the image should look entirely different from the original
- Windows and small details create bright spots against the dark background

### How to apply

1. Go to **Filters > Edge-Detect > Neon...**
2. In the Neon dialog:
   - **Radius**: controls edge thickness. Higher = thicker, brighter edges.
   - **Amount**: controls edge intensity. Higher = more vivid. The default can produce dim edges.
3. Enable **Preview** to check the result.
4. Compare the preview to the before/after reference images above. Adjust Radius and Amount until the result matches — edges should be bright and vivid, not faint.
5. Click **OK** to apply.

