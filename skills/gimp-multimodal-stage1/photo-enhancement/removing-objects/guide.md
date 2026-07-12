# Removing Unwanted Objects (GIMP 2.10)

Images pick up all sorts of junk you didn't intend — dust specks on the lens, a stray telephone wire, a stranger walking through your otherwise perfect beach shot. GIMP gives you a handful of approaches depending on what you're dealing with.

**Small blemishes and dust spots** respond well to the Despeckle filter at **Filters > Enhance > Despeckle**. The key is to first draw a tight selection around just the speck and a small surrounding area — don't run it on the whole image or you'll get mush. With a small selection active, open Despeckle and adjust the parameters while watching the preview. If the artifact doesn't disappear cleanly, undo, draw a slightly different selection, and try again. Repeat per-speck if you have several.

**Larger unwanted objects** — people, wires, signs — are best handled with the **Clone tool** (keyboard shortcut **C**, or find it in the Toolbox). Clone works by painting pixels sampled from another region of your image over the offending area. Ctrl-click a clean source area that has similar texture and lighting, then paint over the thing you want gone. The trick is finding a source region that blends naturally; mismatched texture is immediately obvious. Work in short strokes, resample often, and zoom in. It feels clumsy at first, but with practice the results are surprisingly seamless.

For skin retouching or subtle blemishes, reach for the **Heal tool** (just below Clone in the Toolbox). It works like Clone but automatically blends the sampled texture with the surrounding color and lighting of the destination, making it ideal for wrinkles, acne, or small scars without leaving telltale patches.

**Removing or replacing an entire background** is a different workflow. You'll need to select the subject first, then invert the selection to target the background. GIMP offers several selection tools suited to different edge complexities: the **Free Select (Lasso)** for simple shapes, **Intelligent Scissors** for complex but high-contrast edges (it snaps to detected boundaries as you click around the subject), and the **Foreground Select tool** which lets you roughly mark foreground and background regions and refines automatically.

See `fig01.jpg` for the example subject before background removal.

Once you've isolated the subject, hit **Select > Invert** so the background is selected instead. From here you can fill it with a flat color using the **Bucket Fill tool**, desaturate it via **Colors > Desaturate** to create a color-subject-on-grayscale-background effect, or simply delete it to transparency (make sure your layer has an alpha channel first).

For flash photography red-eye, there's a dedicated filter at **Filters > Enhance > Red Eye Removal** — select the red area of the eye, run the filter, and tweak the threshold slider until the color looks natural.
