# Embedded Spreadsheets (LibreOffice Writer 7.3.7)

You can drop a fully functional Calc spreadsheet right inside a Writer document — handy for complex tables, calculations, or data you want to keep live. To insert one, go to **Insert > OLE Object** (see "Inserting a file as an OLE object" in your guide) or create a new one from scratch. You can also paste an existing Calc range as a linked OLE object or as a DDE link via **Edit > Paste Special > Paste Special**, choosing **Dynamic Data Exchange (DDE link)** in the Selection list. A DDE link keeps Writer in sync whenever the source Calc file changes.

See `fig01.png`.

Once the spreadsheet is in your document, it behaves like any other object — click it once to select it, then drag the green handles to resize, or drag the object itself to reposition it. Corner handles scale both dimensions at once; side handles stretch one axis only. Be careful not to accidentally double-click when you just want to move it.

Double-click the spreadsheet to enter edit mode. The toolbars swap to Calc's interface and you'll see the Formula Bar appear with the **Name Box**, **Function Wizard**, **Select Function** and **Formula** icons, plus an **Input Line** for entering data. You're essentially working in Calc at this point — navigate with arrow keys or Tab, type into cells, and use formulas just as you would in a standalone spreadsheet. When you're done editing, click anywhere outside the object to return to Writer.

If the embedded spreadsheet has multiple sheets, only the active sheet shows after you exit edit mode. To switch sheets, double-click back in and use the sheet tabs at the bottom. You can insert, rename, move, copy, or delete sheets by right-clicking a sheet tab or using the **Sheet** menu — for example, **Sheet > Insert Sheet** or **Sheet > Delete Sheet**.

To format cell data, select your cells, then right-click and choose **Format Cells** (or press **Ctrl+1**). Writer normally auto-detects data types, but if you need numbers treated as text — like phone numbers — prefix them with a single quote (`'`). For broader visual consistency, open the Styles deck in the Sidebar while in edit mode and apply styles to match your document's look, since Calc cell styles may not carry over cleanly into Writer.

You can insert or delete rows and columns through **Sheet > Insert Columns** or **Sheet > Insert Rows**, and remove them via **Sheet > Delete Rows** or **Sheet > Delete Columns**. To merge cells, select them and go to **Format > Merge Cells > Merge and Center Cells**. Splitting previously merged cells is done with **Format > Merge Cells > Split Cells**. Column widths and row heights can be adjusted by dragging the separators in the headers until the cursor becomes a double-headed arrow.

---

## UI Reference  —  Insert Menu

_Scope: OLE Object… for embedding Calc spreadsheets_

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

