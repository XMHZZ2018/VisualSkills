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

**Dialog layout (Value channel):** The dialog has a title bar reading "Adjust Color Levels". At the top is a **Channel** dropdown currently set to "Value". Below that is the **Input Levels** section containing a histogram — a mountain-shaped graph showing the tonal distribution of the image. The histogram data is clustered toward the left and center, trailing off before reaching the right edge (indicating the image is underexposed and lacking bright tones). Below the histogram are three triangular sliders: a black triangle on the far left (black-point, value 0), a gray triangle in the middle (gamma/midtone, value ~1.00), and a white triangle on the right (white-point, value 255). Below the Input Levels is the **Output Levels** section with a gradient bar from black to white and two sliders (left at 0, right at 255). At the bottom are checkboxes for "Preview" and buttons for "Reset", "Cancel", and "OK".

### Brightening an underexposed image (Value channel)

1. Open **Colors > Levels**.
2. Make sure **Channel** is set to **Value**.
3. Look at the histogram — if the data doesn't reach the right edge, the image is underexposed.
4. Drag the **white-point slider** (right side of Input Levels) leftward to where the histogram data ends. This stretches the tonal range to use the full brightness scale.
5. Drag the **gamma slider** (middle) slightly to the left to boost midtones.
6. Check **Preview** to see the effect on the canvas.
7. Click **OK** to apply.

**After adjustment:** When the white-point slider is dragged leftward to meet the histogram data and the gamma slider is shifted slightly left, the image becomes visibly brighter. The canvas behind the dialog shows improved exposure — previously dark areas become more visible while highlights remain intact.

### Per-channel color correction with Levels

The Levels tool can also fix color casts by adjusting individual R/G/B channels. Use the **Channel** dropdown to switch between Red, Green, and Blue.

**Red channel dialog:** When Channel is set to "Red", the histogram shows the red channel distribution. The **Output Levels** bar changes from a black-to-white gradient to a **black-to-red gradient**, making it visually clear you are controlling the red output range. Adjusting the red channel's output levels controls how much red is present in the image.

**Green channel dialog:** When Channel is set to "Green", the histogram shows the green channel distribution. The **Output Levels** bar changes to a **black-to-green gradient**. The layout is otherwise identical to the red channel view.

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

**Dialog layout:** The Color Balance dialog has a title bar reading "Color Balance". The top section is labeled **"Select Range to Adjust"** with three radio buttons: "Shadows", "Midtones" (selected by default), and "Highlights". Below that is the **"Adjust Color Levels"** section with three horizontal sliders, each representing a complementary color pair: **Cyan ↔ Red** (top slider), **Magenta ↔ Green** (middle slider), and **Yellow ↔ Blue** (bottom slider). Each slider has the cool color labeled on the left and the warm color on the right, with a numeric field showing the current value (0 = neutral). Below the sliders is a **"Preserve luminosity"** checkbox (checked by default — keep this checked) and a **"Reset Range"** button. At the bottom are "Preview" checkbox and "Reset", "Cancel", "OK" buttons.

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

**Before applying the filter:** The original image is a simple cityscape scene — a blue-to-teal gradient sky at the top, dark olive-green mountains in the background, and a green hillside in the foreground. There are four buildings of varying heights (gray and brown tones) with yellow-lit rectangular windows arranged in grids. On the right side stands a tree with a brown trunk and a round dark-green canopy. The overall image has soft, flat colors with gentle gradients.

**After applying the filter (Filters > Edge-Detect > Neon):** The image is dramatically transformed:
- The background is **completely black** — all flat-colored areas (sky, mountains, hillside) become solid black
- Object edges appear as **bright, vivid colored lines**: building outlines glow in **white and cyan**, the mountain ridgeline is a bright **white** line, the hillside edge is a vivid **green** diagonal line, and the tree canopy is outlined in **magenta and green** rings
- Building windows appear as **bright yellow/orange dots** against the black background, some with **red and cyan** accents on the window frames
- The overall effect is **dramatic and high-contrast** — it looks like a neon sign version of the scene, with only edges and bright details visible against total darkness
- The image looks **entirely different** from the original — no flat colors remain, only glowing edge lines

### How to apply

1. Go to **Filters > Edge-Detect > Neon...**
2. In the Neon dialog:
   - **Radius**: controls edge thickness. Higher = thicker, brighter edges.
   - **Amount**: controls edge intensity. Higher = more vivid. The default can produce dim edges.
3. Enable **Preview** to check the result.
4. Compare the preview to the before/after descriptions above. Adjust Radius and Amount until the result matches — edges should be bright and vivid, not faint. The background should be almost entirely black, with colorful glowing edge lines clearly visible.
5. Click **OK** to apply.
