# Positioning Images (LibreOffice Writer 7.3.7)

When you drop an image into a Writer document, four settings govern how it sits on the page: **arrangement**, **alignment**, **anchoring**, and **text wrapping**. Getting comfortable with these gives you full control over your layout.

**Anchoring** tells Writer what the image is attached to. Right-click the image and look under **Anchor** in the context menu. *To Page* locks the image at a fixed spot on the page — great for letterheads or newsletter layouts where the image shouldn't move as you edit text. *To Paragraph* ties the image to a specific paragraph so it travels with it; handy for icons beside paragraphs. *To Character* is similar but anchors to a specific character position. *As Character* treats the image like a letter in the text flow, which is perfect for small inline icons or sequential screenshots. You can set a default anchor type under **Tools > Options > LibreOffice Writer > Formatting Aids**.

**Alignment** controls where the image sits relative to its anchor point. For fine-grained control, open the image dialog's **Type** tab and use the **Position** options. Pick a horizontal reference (Left, Right, or Center relative to the page text area or entire page) and a vertical one (Top, Bottom, Center from the top edge). If you select **From left** or **From top**, you can type an exact distance.

See `fig01.png`.

**Arranging** matters when images overlap. Use **Format > Arrange** (or right-click and choose from the context menu) to shuffle the stacking order: **Bring to Front**, **Forward One**, **Back One**, or **Send to Back**. For drawing objects there's also **To Background / To Foreground**. Tip: press the *Tab* key to cycle through overlapping objects until you reach the one you want.

**Text wrapping** defines how surrounding text behaves around the image. The most common options — available on the **Wrap** tab of the image dialog or via right-click — include: *None* (text only above and below), *Parallel* (text on all four sides), *Optimal* (text flows around the image, but Writer prevents narrow columns less than 2 cm), and *Through* (image sits on top of the text, useful with transparency). *Before* and *After* restrict text to one side. Use the **Spacing** section on the Wrap tab to add breathing room between image and text. If you need text to hug an irregular shape, select **Contour** wrapping, then right-click and choose **Wrap > Edit Contour** to open the Contour Editor and draw around the region you want to keep clear.

See `fig02.png`.

Note: when an image is anchored *As Character*, wrapping options are disabled — you can only adjust spacing. And contour wrapping isn't available for frames, only for images and drawing objects.
