# Using Frames for Page Layout (LibreOffice Writer 7.3.7)

Frames are handy containers for text, tables, images, and other objects that you want to place precisely on a page. Think of them as independent boxes you can position anywhere — great for newsletters, flyers, or any document where the standard text flow isn't flexible enough. You can even link frames together so text flows from one to the next across pages, which is perfect for multi-column newsletter layouts.

To insert a frame, go to **Insert > Frame > Frame**. The Frame dialog opens, letting you set the size, position, and anchor type right away — or just click **OK** and tweak things later. If you already have text selected when you do this, that text gets pulled out of the normal flow and placed inside the new frame. For a more freehand approach, choose **Insert > Frame > Frame Interactively**, which lets you click and drag to draw the frame directly on the page.

See `fig01.png`.

Once a frame exists, click inside it to add content just like you would on the main page. To move or resize it, click the border to select it, then drag the green handles. Hold **Shift** while dragging a corner to keep the proportions locked. For precise control, right-click the frame and choose **Properties** to reopen the Frame dialog.

Anchoring determines how a frame behaves as surrounding content changes. **To Page** keeps the frame fixed at an absolute position — ideal for logos or headers. **To Paragraph** ties it to a specific paragraph so it moves along with the text. **To Character** is similar but anchors within the text sequence, while **As Character** treats the frame like an inline character, which is the safest choice for small icons or images that should stay in line with text. You set the anchor type on the *Type* tab of the Frame dialog or via the **Anchor** button on the Frame toolbar.

On the *Borders* tab, you can control the frame's border lines, padding, and shadow. If you want a borderless frame, pick the first preset (**Set No Borders**) under *Line Arrangement*.

See `fig02.png`.

To link frames so text overflows from one into another, select the first frame, click **Link Frames** on the Frame toolbar, then click the destination frame (which must be empty). A faint line appears between linked frames to confirm the connection. Text that doesn't fit in the first frame automatically continues in the next. Note that each frame can only link to one other frame — no branching. To break a link, select the frame and click **Unlink Frames**. The *Options* tab of the Frame dialog also shows the chain's previous and next links, and lets you rename frames for easier management.

See `fig03.png`.

Keep your design simple: the fewer frames and anchor types you mix, the easier the document is to maintain. Use the Wrap page of the Frame dialog to control how body text flows around each frame, and consider the Frame toolbar (**View > Toolbars > Frame**) for quick access to common actions like wrap mode, alignment, and border toggles.
