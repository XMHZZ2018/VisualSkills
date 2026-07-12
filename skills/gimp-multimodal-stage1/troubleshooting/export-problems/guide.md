Neither page references any inline images, so the text content is the full source material. Here's the guide:

# Fixing Export Problems (GIMP 2.10)

Not every image format can carry everything your GIMP canvas holds. Two of the most common surprises hit when you export to JPEG or GIF — transparency vanishes or your colors shift. Both are format limitations, not bugs, and the fixes are straightforward once you know what's happening.

## Transparency Disappearing in JPEG

JPEG simply does not support transparency. When you export via **File > Export As** and choose `.jpg`, GIMP fills every transparent pixel with the current background color — usually white, sometimes black depending on your toolbox setting. The result looks like your carefully masked subject got pasted onto a flat slab of color.

The real fix is to pick a format that keeps alpha channels. Switch to **PNG** or **TIFF** instead — both handle transparency natively. If you absolutely must deliver a JPEG (say, for a web form that rejects other formats), flatten the image yourself first (**Image > Flatten Image**) so you can control what fills the transparent areas before the export bakes it in.

## Colors Shifting in GIF

GIF caps you at 256 colors total. When you export, GIMP automatically reduces your palette by merging similar colors together, and the result can look banded, washed out, or just wrong — especially on gradients or photographic content.

If you need more color depth, export as PNG instead; it gives you millions of colors with no quality loss. But if GIF is required (for animation or legacy reasons), convert manually first via **Image > Mode > Indexed**. That dialog lets you choose the dithering method, pick the palette size, and preview the damage before committing. Tweak those settings until the preview looks acceptable, then export — you'll get exactly the 256 colors you chose rather than whatever GIMP's automatic conversion decided.
