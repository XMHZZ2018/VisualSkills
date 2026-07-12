# Adjusting Sharpness (GIMP 2.10)

When a photo comes out slightly soft — missed focus or camera shake — GIMP's **Unsharp Mask** is your go-to fix. Head to **Filters > Enhance > Sharpen (Unsharp Mask)**. The default **Radius** and **Amount** values are a solid starting point; bump either one up to strengthen the effect, but ease off before noise and edge halos creep in.

If sharpening introduces color fringing around high-contrast edges, decompose the image into HSV (**Colors > Components > Decompose**), run Unsharp Mask on the Value channel only, then recompose. Human eyes resolve luminance detail far better than color, so this keeps things natural.

For targeted touch-ups, grab the **Blur/Sharpen** tool from the Toolbox (set to Sharpen mode) and paint over the areas that need crispness. Use a light hand — overdoing it amplifies grain.

**Reducing noise** is the flip side. Grainy low-light shots respond well to **Filters > Enhance > Selective Gaussian Blur** with a radius of 1–2 pixels — it smooths flat areas while preserving edges. The **Despeckle** filter (**Filters > Enhance > Despeckle**) is another option; tweak its settings in the preview until grain fades without killing detail.

When an image is *too* sharp or crisp, apply a gentle **Filters > Blur > Blur** — repeat as needed until the softness feels right.
