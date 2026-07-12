# Removing Unwanted Objects (GIMP 2.10)

Small sensor dust or hair on your lens? Use the **Despeckle** filter via **Filters > Enhance > Despeckle**. The key is to first make a tight selection around the speck — just the artifact plus a small margin. Despeckle needs that limited context to distinguish junk from real detail. Adjust the parameters while watching the preview, and if results are poor, undo, try a slightly different selection, and run it again. Each spot needs its own pass.

For larger distractions — a person in your beach shot, a power line across a landscape — reach for the **Clone** tool (keyboard shortcut **C**). Ctrl-click a clean area that has similar texture and color to what surrounds the unwanted object, then paint over the eyesore. The trick is picking a source region that blends naturally; work in short strokes and resample often to avoid obvious repetition.

When you need something smarter, try the **Heal** tool (**H**), which works like Clone but blends the sampled pixels with the surrounding tones and lighting of the destination. It's ideal for skin blemishes, wrinkles, or small imperfections where color continuity matters.

To remove an entire background, you'll want a precise selection first. Use the **Free Select** tool for simple shapes, **Intelligent Scissors** when the subject has complex but well-defined edges, or the **Foreground Select** tool to paint broad strokes marking foreground vs. background and let GIMP refine the boundary. Once your subject is selected, hit **Select > Invert** so the background is active instead. From there, fill it with a flat color using **Bucket Fill**, or desaturate it via **Colors > Desaturate** to keep your subject in color against a monochrome backdrop.

For truly stubborn removals, cut the object out, then use the third-party **Resynthesizer** plug-in to intelligently fill the gap with synthesized surrounding texture. Results vary, but when it works it's nearly invisible.
