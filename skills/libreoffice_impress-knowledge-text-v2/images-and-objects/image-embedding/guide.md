# Embedding Linked Images (LibreOffice Impress 7.3.7)

When you insert an image via **Insert > Image**, the Insert Image file browser includes an **Insert as Link** checkbox near the bottom left. If that box is checked, Impress stores only a reference to the file on disk rather than copying the image data into the presentation itself.

Visual reference: the Insert Image file browser with the Preview and Insert as Link checkboxes visible at the bottom left.

Linked images keep your file size down, which is handy when the same large image appears across multiple presentations or when the image only needs to be available at open time (like a holiday slideshow pulling from a local folder). But there's a catch — if you move the presentation to another computer or rename the source file, those links break and your images vanish.

For anything you plan to share or archive, embedding is the safer bet. Just make sure **Insert as Link** is *unchecked* when you insert the image through **Insert > Image**. The full image data gets written into the .odp file, so the presentation is self-contained and portable.

If an image file is especially large, linking rather than embedding can dramatically cut your presentation's file size. The tradeoff is portability: a linked presentation only works correctly when the original image files are accessible at their original paths.

To embed an image that was previously linked, remove the linked image from the slide and re-insert it via **Insert > Image** — this time leaving the **Insert as Link** checkbox unchecked. Navigate to the file, select it, optionally enable **Preview** to confirm the thumbnail, and click **Open**. The image lands on your slide with selection handles, fully embedded and ready to travel.
