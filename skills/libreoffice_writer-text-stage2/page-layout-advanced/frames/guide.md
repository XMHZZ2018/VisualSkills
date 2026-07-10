# Using Frames for Page Layout (LibreOffice Writer 7.3.7)

Frames are handy containers for text, tables, images, and other objects that you want to place precisely on a page. Think of them as independent boxes you can position anywhere — great for newsletters, flyers, or any document where the standard text flow isn't flexible enough. You can even link frames together so text flows from one to the next across pages, which is perfect for multi-column newsletter layouts.

To insert a frame, go to **Insert > Frame > Frame**. The Frame dialog opens, letting you set the size, position, and anchor type right away — or just click **OK** and tweak things later. If you already have text selected when you do this, that text gets pulled out of the normal flow and placed inside the new frame. For a more freehand approach, choose **Insert > Frame > Frame Interactively**, which lets you click and drag to draw the frame directly on the page.

The Frame dialog is shown with the *Type* tab selected. It contains a **Size** section at the top left with Width (set to 2.00 cm) and Height (at least 0.50 cm) fields, each with a "Relative to" dropdown (set to "Paragraph area"), AutoSize checkboxes, and a Keep ratio option. To the right is the **Anchor** section with four radio buttons: To page, To paragraph (currently selected), To character, and As character; beside it a small preview graphic shows the frame's position on a miniature page. Below is the **Position** section with Horizontal alignment (set to Center, relative to Paragraph area) and Vertical alignment (set to Top, relative to Paragraph text area), along with a "Mirror on even pages" checkbox and a "Keep inside text boundaries" checkbox. The dialog has tabs across the top for Type, Options, Wrap, Hyperlink, Borders, Area, Transparency, Columns, and Macro, with Help, Reset, Cancel, and OK buttons at the bottom.

Once a frame exists, click inside it to add content just like you would on the main page. To move or resize it, click the border to select it, then drag the green handles. Hold **Shift** while dragging a corner to keep the proportions locked. For precise control, right-click the frame and choose **Properties** to reopen the Frame dialog.

Anchoring determines how a frame behaves as surrounding content changes. **To Page** keeps the frame fixed at an absolute position — ideal for logos or headers. **To Paragraph** ties it to a specific paragraph so it moves along with the text. **To Character** is similar but anchors within the text sequence, while **As Character** treats the frame like an inline character, which is the safest choice for small icons or images that should stay in line with text. You set the anchor type on the *Type* tab of the Frame dialog or via the **Anchor** button on the Frame toolbar.

On the *Borders* tab, you can control the frame's border lines, padding, and shadow. If you want a borderless frame, pick the first preset (**Set No Borders**) under *Line Arrangement*.

The Frame dialog is shown with the *Borders* tab active. On the left is the **Line Arrangement** section with a row of five preset icons (the first, representing no borders, is a dashed-outline box; the others show various border configurations) and below them a **User-defined** preview area displaying the current border applied to a gray rectangle. On the right is the **Padding** section with spin boxes for Left, Right, Top, and Bottom (all set to 0.05 cm) and a checked "Synchronize" checkbox. The lower-left contains the **Line** section with a Style dropdown (showing a solid line), a Color dropdown (set to Black), and a Width field (0.05 pt). The lower-right holds the **Shadow Style** section with a Position row of five shadow-placement icons (the first, no shadow, is currently selected), a Color dropdown (Black), and a Distance field (0.10 cm).

To link frames so text overflows from one into another, select the first frame, click **Link Frames** on the Frame toolbar, then click the destination frame (which must be empty). A faint line appears between linked frames to confirm the connection. Text that doesn't fit in the first frame automatically continues in the next. Note that each frame can only link to one other frame — no branching. To break a link, select the frame and click **Unlink Frames**. The *Options* tab of the Frame dialog also shows the chain's previous and next links, and lets you rename frames for easier management.

Two frames are shown on the document canvas illustrating a linked-frame connection. The first frame (upper left) is selected, indicated by eight green square handles around its border, and contains a paragraph mark. A dotted diagonal line extends from the bottom-right handle of the first frame to the second frame (lower right), which is empty and displayed with a darker border. This dotted connector line visually represents the text-flow link between the two frames.

Keep your design simple: the fewer frames and anchor types you mix, the easier the document is to maintain. Use the Wrap page of the Frame dialog to control how body text flows around each frame, and consider the Frame toolbar (**View > Toolbars > Frame**) for quick access to common actions like wrap mode, alignment, and border toggles.

---

## UI Reference  —  Insert Menu

_Scope: Frame submenu: Frame Interactively, Frame… dialog_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown open in the LibreOffice Writer menu bar. It displays a vertical list of menu items from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Several items have a right-pointing arrow indicating submenus (More Breaks, Media, OLE Object, Shape, Frame, Formatting Mark, Footnote and Endnote, Table of Contents and Index, Field, Header and Footer). The Frame entry is where users access the Frame and Frame Interactively commands.

## Elements

- **Page Break** (Ctrl+Return) — Insert a manual page break at cursor.
- **More Breaks** (►) — Manual Row Break (Shift+Return), Column Break (Shift+Ctrl+Return), Manual Break… (dialog to choose break type and page style).
- **Image…** — Open file chooser to insert a raster or vector image.
- **Chart…** — Embed a chart OLE object.
- **Media** (►) — Gallery, Scan, Audio or Video…
- **OLE Object** (►) — Formula Object (Shift+Alt+E), QR and Barcode…, OLE Object…
- **Shape** (►) — 7 shape categories: Line, Basic Shapes, Block Arrows, Symbol Shapes, Stars and Banners, Callout Shapes, Flowchart — each opens a named-shape palette.
- **Section…** — Opens Insert Section dialog (tabs: Section, Columns, Indents, Area, Footnotes/Endnotes). Supports linked sections, write protection, and conditional hiding.
- **Text from File…** — Insert text from an external file.
- **Text Box** — Draw a floating text frame on the canvas.
- **Comment** (Ctrl+Alt+C) — Insert an annotation balloon.
- **Frame** (►) — Frame Interactively (draw) or Frame… (dialog).
- **Fontwork…** — Decorative text shapes gallery.
- **Hyperlink…** (Ctrl+K) — Hyperlink dialog with 4 type modes: Internet, Mail, Document, New Document.
- **Bookmark…** — Insert/manage bookmarks.
- **Cross-reference…** — Link to headings, bookmarks, figures, or other elements.
- **Special Character…** — Character picker dialog with search, font/block selectors, hex/decimal codes, favorites/recent.
- **Formatting Mark** (►) — No-break Space (Shift+Ctrl+Space), Non-breaking Hyphen, Soft Hyphen, Narrow No-break Space, Zero-width Space, Word Joiner.
- **Horizontal Line** — Insert a horizontal rule.
- **Footnote and Endnote** (►) — Insert Footnote, Endnote, or open the Footnote/Endnote dialog.
- **Table of Contents and Index** (►) — TOC/Index/Bibliography dialog, Index Entry, Bibliography Entry.
- **Page Number…** — Page number insertion dialog.
- **Field** (►) — Page Number, Page Count, Date/Time (fixed or variable), Title, Author, Subject, More Fields… (Ctrl+F2).
- **Header and Footer** (►) — Enable/disable headers and footers per page style.
- **Envelope…** — Envelope configuration dialog.
- **Signature Line…** — Digital-signature placeholder line.
