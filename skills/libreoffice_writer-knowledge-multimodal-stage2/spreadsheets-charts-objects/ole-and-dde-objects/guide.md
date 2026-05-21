# OLE and DDE Objects (LibreOffice Writer 7.3.7)

OLE (Object Linking and Embedding) and DDE (Dynamic Data Exchange) both let you pull information from one application — say, a Calc spreadsheet — right into your Writer document. The key difference: a linked OLE object stays editable from both ends and keeps both documents in sync, while a DDE object acts more like a live mirror — changes flow from the source into Writer automatically, but you can't edit the DDE object directly inside Writer.

An **embedded** OLE object is a copy. There's no connection back to the source, so edits in either place stay independent. Embed when you want a self-contained document. A **linked** OLE object is a reference — change the original and the Writer copy updates too, but you need to keep the source file accessible and in the same location.

You can insert spreadsheets, charts, drawings, formulas, and presentations as OLE objects.

**Creating a new OLE object from scratch** is straightforward. Click where you want it, then go to **Insert > Object > OLE Object**. In the dialog that opens, keep **Create new** selected, pick the object type you want (spreadsheet, drawing, formula, etc.), and hit **OK**. Writer drops you straight into edit mode with the appropriate toolbars ready to go.

See `fig01.png`.

**Inserting an existing file as an OLE object** is just as easy. Open the same dialog via **Insert > Object > OLE Object**, but this time switch to **Create from file**. Click **Search** to browse for your file, then choose how you want it linked. If you want live syncing between the file and your document, check the **Link to file** option. If you'd rather show just an icon instead of the full content, tick **Display as icon**. Click **OK** and you're set.

See `fig02.png`.

**Editing an OLE object** is as simple as double-clicking it. Writer's toolbars swap out to match the embedded application — so if it's a Calc spreadsheet, you'll see Calc's menus and toolbars right inside your Writer window. Click outside the object to return to normal editing.

**DDE objects** work a bit differently. When a Calc spreadsheet is pasted as a DDE object, you can't edit it in Writer directly. But whenever the source Calc file is updated, those changes automatically appear in your Writer document. Use DDE when you want a read-only, always-current snapshot of external data.

On Windows, you'll also see a **Further Objects** option in the Object Type list, which lets you create OLE objects using other software compatible with OLE and LibreOffice.

---

## UI Reference  —  Insert Menu

_Scope: OLE Object > OLE Object… command for embedding/linking_

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

