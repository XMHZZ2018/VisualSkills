# Improving Photo Composition (GIMP 2.10)

When you snap a photo, the camera rarely frames things exactly as your eye saw them. GIMP gives you two main tools to fix that: rotation for straightening a tilted horizon, and cropping for tightening the frame around what matters.

**Straightening a tilted image.** Grab the Rotate tool from the Toolbox (or press **Shift+R**). In the Tool Options, make sure **Transform Layer** is selected and set the Transform Direction to **Backward (Corrective)**. Corrective mode lets you drag the grid to align with the crooked horizon rather than trying to guess the compensation angle — it feels much more intuitive. Click in the image, drag until the grid lines up with something that should be level, then hit **Enter**.
Avoid rotating twice to "fine-tune" — each rotation slightly blurs the image because pixels get resampled. If the first attempt isn't perfect, undo with **Ctrl+Z** and rotate again with a better angle. Enable the preview option in Tool Options so you can judge the correction before committing.

After rotation you'll have empty triangular gaps in the corners. The cleanest fix is to crop them away.

**Cropping for stronger composition.** Activate the Crop tool with **Shift+C** or click its Toolbox icon. Click and drag across the image to draw your crop rectangle, then press **Enter** to apply. Keep the "rule of thirds" in mind: placing your subject roughly one-third from each edge often gives images more visual energy than dead-center framing.

If **Delete cropped pixels** is unchecked in the Crop Tool Options, the outside pixels aren't destroyed — only the canvas boundary moves. That's handy if you think you might want to re-crop later, but for a final export you'll usually want it checked to keep the file lean.

Between these two moves — straighten, then crop — you can rescue most composition problems without touching anything else in the image.
