# Adjusting Sharpness (GIMP 2.10)

Photos sometimes come back soft — maybe the focus wasn't perfect, or the camera moved slightly during the shot. If the blur is moderate, GIMP can recover a surprising amount of detail. On the flip side, images shot in low light often pick up grain, and occasionally a photo is just too crisp and needs softening.

**Sharpening a fuzzy image** is best done with the Unsharp Mask filter. Head to **Filters > Enhance > Sharpen (Unsharp Mask)**. Despite the confusing name (borrowed from darkroom technique), it makes things sharper, not blurrier. You get two key parameters — **Radius** and **Amount**. Start with the defaults; they're reasonable for most photos. Bump either one up to strengthen the effect, but go easy — overdoing it amplifies noise and creates ugly halos along edges.

If sharpening introduces color fringing in high-contrast areas, try decomposing the image into HSV components via **Colors > Components > Decompose**, running the Unsharp Mask on the Value channel only, then recomposing with **Colors > Components > Compose**. Human vision is far more sensitive to brightness detail than color detail, so this sidesteps the distortion.

For selective touch-ups, grab the **Blur/Sharpen** tool from the Toolbox (set it to "Sharpen" mode in the tool options) and paint over just the areas that need crispening. Use a light hand — heavy strokes look unnatural.

**Reducing grain** from low-light or high-ISO shots works best with **Filters > Enhance > Selective Gaussian Blur**, radius set to 1 or 2 pixels. It smooths noise while preserving edges better than a plain blur. The **Despeckle** filter (**Filters > Enhance > Despeckle**) is another option — it has a live preview, so experiment with its settings until the grain fades without killing detail.

**Softening an overly crisp image** is the easy direction. Apply **Filters > Blur > Blur** once for a subtle effect, or repeat it a few times until the harshness backs off. Quick and predictable.
