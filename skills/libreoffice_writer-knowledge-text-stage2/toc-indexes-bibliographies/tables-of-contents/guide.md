# Tables of Contents (LibreOffice Writer 7.3.7)

A table of contents (TOC) in Writer is built automatically from the headings in your document. When you change a heading's text or its page shifts, the TOC picks that up the next time you update it. The key requirement is consistent use of paragraph styles — apply **Heading 1** for chapter titles, **Heading 2** and **Heading 3** for subsections, and Writer takes care of the rest.

To insert a default TOC, click where you want it to appear and go to **Insert > Table of Contents and Index > Table of Contents, Index or Bibliography**. Leave the defaults and click **OK**. You'll get a gray-shaded block with clickable hyperlinks — the shading is just an on-screen reminder that the area is a field, and it won't print or export to PDF.

If headings aren't showing up, double-check that they're tagged with the right paragraph style. If an entire outline level is missing, verify the settings under **Tools > Chapter Numbering**. To turn off the gray background, head to **Tools > Options > LibreOffice > Application Colors** and deselect *Index and table shadings*.

When you add, delete, or move headings, the TOC goes stale. Right-click anywhere inside it and choose **Update Index** to refresh. Be sure **Edit > Track Changes > Show** is off before updating, or deleted headings may linger and page numbers can get confused.

The "Table of Contents, Index or Bibliography" dialog is shown with the **Type** tab selected. At the top, a "Type and Title" section has the Title field set to "Contents" and the Type dropdown set to "Table of Contents," with a "Protected against manual changes" checkbox enabled. Below that, the "Create Index or Table of Contents" section has a **For** dropdown set to "Entire document" and an **Evaluate up to level** spinner set to 3. The "Create From" section at the bottom offers three checkboxes — **Outline**, **Additional styles** (with an "Assign styles…" button beside it), and **Index marks** — all checked. Along the bottom of the dialog are **Help**, **Preview**, **OK**, **Close**, and **Reset** buttons. Five tabs run across the top: Type, Entries, Styles, Columns, and Background.

For deeper customization, right-click the TOC and select **Edit Index** to reopen the dialog. The **Type** tab controls the scope — you can build the TOC from the entire document or just the current chapter, and set how many outline levels to include with the **Evaluate up to level** field. Under *Create From*, the **Outline** option (default) pulls in styles linked to outline levels via **Tools > Chapter Numbering**, while **Additional styles** lets you fold in extra paragraph styles by clicking **Assign styles** and choosing the level for each one.

The **Entries** tab is where you fine-tune the structure line for each level — chapter number, entry text, tab stop, page number, and hyperlink markers are all represented by icons you can add, remove, or reorder. Pick a level on the left, then click in the white Structure field and use the buttons below to insert or swap elements. Hit **All** to copy the current structure to every level at once.

The dialog now shows the **Entries** tab selected, titled "Structure and Formatting." On the left is a Level list numbered 1 through 10, with level 1 currently highlighted. To the right, the Structure line displays a row of element tokens — LS (link start), E# (chapter number), E (entry text), T (tab stop), # (page number), and LE (link end) — separated by small editable gaps. Below the structure line are five buttons: **Chapter No.**, **Entry Text**, **Tab Stop**, **Page No.**, and **Hyperlink**, used to insert elements into the structure. A **Character style** dropdown is set to "\<None\>" with an **Edit…** button beside it. At the far right of the structure line is an **All** button that copies the current structure to all levels. Under the Format heading, a checkbox labeled "Tab position relative to paragraph style indent" is checked.

On the **Styles** tab you can assign a different paragraph style to each TOC level. Select the level, pick a style from the *Paragraph Styles* list, and click the **<** button to apply it. Use the **Background** tab if you want a colored or bitmap background behind the TOC — select **Color** or **Bitmap** from the row of buttons and configure as needed.

---

## UI Reference  —  Insert Menu

_Scope: Table of Contents and Index > TOC/Index/Bibliography dialog_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The screenshot shows the LibreOffice Writer **Insert** dropdown menu fully expanded. It is a single-column menu listing, from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), then a separator, followed by Hyperlink…, Bookmark…, Cross-reference…, then another separator, Special Character…, Formatting Mark, then a separator, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, then a final separator, Envelope…, and Signature Line…. Several entries have submenu arrows indicating flyout menus.

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
