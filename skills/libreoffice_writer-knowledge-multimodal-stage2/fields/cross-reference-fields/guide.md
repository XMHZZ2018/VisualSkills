# Automatic Cross-References (LibreOffice Writer 7.3.7)

Cross-references are one of those things you don't think about until your document shifts around — a heading moves, a figure gets renumbered — and suddenly all your "see page 12" callouts are wrong. Automatic cross-references fix that. Instead of typing static text, you insert a field that updates itself whenever you refresh fields or print.

To get started, place your cursor where you want the cross-reference to appear, then go to **Insert > Cross-reference** (or just press **Ctrl+F2** and click the **Cross-references** tab). You'll see a **Type** list on the left showing the kinds of items you can reference: headings, numbered paragraphs, figures, bookmarks, and more. Pick the type of item you're pointing at.

See `fig01.png`.

Once you select a type, the **Selection** list in the middle populates with all matching targets in your document — every heading, every figure caption, every bookmark. Click the one you want. Then, in the **Insert reference to** dropdown at the bottom, choose what information to pull in. For headings, **Reference** gives you the full heading text, while **Page** inserts the page number. For figures and tables, **Category and Number** (e.g., "Figure 6") is the most common choice, though **Caption Text** grabs the full caption instead. Hit **Insert** and you're done.

The format options are worth knowing. **Page** and **Chapter** return location info. **Above/Below** automatically writes "above" or "below" depending on the target's position relative to the reference — handy for phrases like "see the table below." For numbered paragraphs, **Number (full context)** includes parent numbering (like "2.4"), while **Number (no context)** gives just the item's own number ("4").

Sometimes the item you want to reference doesn't appear automatically in the Cross-references tab — maybe it's an illustration without a caption, or a bullet list item. In that case, you need to mark it as a target first. You can do this with a bookmark (**Insert > Bookmark**, give it a name, click **OK**) or by setting a reference. For a set reference, open **Insert > Cross-reference**, choose **Set Reference** in the **Type** list, type a name, select the text you want to target, and insert. After that, your target shows up in the Selection list and you can cross-reference it like anything else.

One practical tip: some people reach for hyperlinks instead of cross-references, but hyperlinks won't update their visible text when the target changes. Stick with cross-references for print documents — they stay current. The exception is HTML export, where cross-references don't convert to hyperlinks, so you'd need actual hyperlinks for web output.

---

## UI Reference  —  Insert Menu

_Scope: Cross-reference… dialog_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

Read the screenshot `ui-insert-menu.png` in this directory.

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

