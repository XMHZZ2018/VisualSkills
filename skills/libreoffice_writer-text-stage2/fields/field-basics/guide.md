# Field Basics and Document Properties (LibreOffice Writer 7.3.7)

Fields let you insert dynamic data into your document — things like the current date, page count, author name, or a product title that might change later. They show up with a gray background on screen (unless you've turned that off via **View > Field Shadings**), and that shading won't appear in print or PDF export.

A few keyboard shortcuts are worth memorizing. **Ctrl+F2** opens the full Fields dialog, **Ctrl+F8** toggles field shading on and off, **Ctrl+F9** switches between showing field names and their values, and **F9** forces all fields to update.

For everyday inserts, you don't need the full dialog. Just go to **Insert > Page Number** or **Insert > Field** on the Menu bar and pick from the submenu — page number, page count, date, time, title, first author, subject, and more are all one click away.

The bottom portion of the Insert menu is shown with the **Field** item highlighted and its submenu expanded to the right. The submenu lists seven quick-insert options — Page Number, Page Count, Date, Time, Title, First Author, and Subject — followed by a separator and a **More Fields…** entry with the keyboard shortcut ⌘F2. Below the Field item in the main menu, Header and Footer, Envelope…, and Signature Line… are also visible.

When you need fields tied to your document's own metadata, head to **File > Properties**. This dialog has six tabs; the General and Statistics tabs are auto-populated by Writer. The ones you care about are **Description** and **Custom Properties**.

On the **Description** tab you'll find fields for Title, Subject, Keywords, and Comments. Fill these in and you can reference them anywhere in the document as fields. Change the value here once, and every reference updates automatically — handy when a draft title becomes a final one.

The Properties dialog for the document "WG7217-Fields_JHW" is shown with the **Description** tab selected. Six tabs run across the top: General, Description, Custom Properties, Security, Font, and Statistics. The Description tab displays four vertically stacked text fields labeled Title, Subject, Keywords, and Comments. The Title field is filled in with "Chapter 17 Fields", while the Subject, Keywords, and Comments fields are empty.

The **Custom Properties** tab is where it gets flexible. It may be blank in a new document, or pre-filled if you started from a template. Hit the **Add Property** button in the lower right to create a new row. Give it a name (there's a dropdown of common choices, or type your own), pick a type — Text, DateTime, Date, Duration, Number, or Yes/No — and set its value. For example, you might store a "Guide Name" as Text with the value "Writer Guide", or a "LibreOffice Version" set to "7.3".

The same Properties dialog is shown with the **Custom Properties** tab selected. The tab displays a table with three columns: Name, Type, and Value, plus a red X delete button at the end of each row. Two custom properties are defined: the first row has the name "Guide Name" with type "Text" and value "Writer Guide", and the second row has "LibreOffice Version" with type "Text" and value "7.2". Each name field has a dropdown arrow for selecting from predefined names, and each type field has a spinner control for cycling through the available types.

Once properties are defined, you can insert them as fields anywhere in the document through **Insert > Field > More Fields** (or **Ctrl+F2**). Whenever you update a property back in **File > Properties**, every field referencing it refreshes throughout the document. This makes Custom Properties ideal for information that appears in multiple places — project names, version numbers, client details — so you only ever maintain it in one spot.

---

## UI Reference  —  Insert Menu

_Scope: Field submenu (Page Number, Date, Time, Title, Author), Page Number…, More Fields (Ctrl+F2)_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert dropdown menu is shown fully expanded from the Writer menu bar. It lists items from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Several items have right-arrow indicators showing they expand into submenus.

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
