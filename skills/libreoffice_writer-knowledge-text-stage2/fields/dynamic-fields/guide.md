# Dynamic Fields and Numbering Sequences (LibreOffice Writer 7.3.7)

Fields in Writer are placeholders that update automatically — think of them as live references to information that might change over time. A project manager's name, a product title, or even your entire company name can be stored as a field. Update it once, and every instance in the document follows suit.

Writer gives you seven handy document properties — *Page Number*, *Page Count*, *Date*, *Time*, *Title*, *First Author*, and *Subject* — all available right from **Insert > Field**. Several of these pull their values from the Document Properties dialog. For richer metadata, head to the *DocInformation* and *Document* tabs of the Fields dialog by choosing **Insert > Field > More Fields** or pressing *Ctrl+F2*.

The Fields dialog is shown with the *DocInformation* tab selected. The left column, labeled **Type**, lists entries such as Comments, Created, Custom (expanded to reveal sub-items "Guide Name" and "LibreOffice Version"), Keywords, Last printed, Modified (currently highlighted), Revision number, Subject, Title, and Total editing time. The middle column, labeled **Select**, shows Author, Time, and Date (with Date currently selected). The right column, labeled **Format**, presents a long list of date format options such as "12/31/99", "12/31/1999", "Dec 31, 99", "Friday, December 31, 1999", "1999-12-31", and many others. At the bottom right of the dialog is an unchecked **Fixed content** checkbox, and the dialog has **Help**, **Close**, and **Insert** buttons along the bottom.

The *Custom* item in the *DocInformation* tab's Type list comes from the Custom Properties tab of **File > Properties**; it only shows up if you've actually defined custom properties. Some field values are pulled from **Tools > Options > LibreOffice** under the *User Data* page, so make sure that info is accurate. To insert any of these, pick your Type, choose a Select and Format option, then click **Insert**.

If a field should never change after insertion — say a creation date you want frozen — tick the **Fixed content** checkbox (bottom-right of the Fields dialog) when inserting it. You can always come back and uncheck it later if you change your mind.

## Saving Fields as AutoText

When you use the same fields repeatedly, AutoText saves you the trouble of re-inserting them manually. First, insert the field into your document, then select it and open **Tools > AutoText** (or press *Ctrl+F3*). Pick a group, give the entry a name and shortcut, then click the **AutoText** button and choose **New** — not **New (text only)**, which would strip the field and store plain text. Now just type the shortcut and press *F3* to drop the field in wherever you need it.

The AutoText dialog is shown with "Display remainder of name as suggestion while typing" checked at the top. The **Name** field contains "sample" and the **Shortcut** field contains "s". Below these fields is a group list showing "Business Cards, Work (3 ½ x 2)", "My AutoText" (currently highlighted), "Only for Templates", and "Standard", each with a disclosure triangle. A **Save Links Relative To** section at the bottom provides unchecked "File system" and "Internet" checkboxes. Along the bottom of the dialog are **Help**, **AutoText** (dropdown button, currently open to reveal **New**, **New (text only)**, and **Import…** options), **Categories…**, **Path…**, **Close**, and **Insert** buttons.

## Defining Custom Numbering Sequences

Sometimes built-in list styles don't cut it — maybe you need a "Step 1, Step 2, Step 3" sequence placed at arbitrary points in your text rather than as a formatted list. You can create your own using a number range variable field.

Place your cursor in a blank paragraph and open **Insert > Field > More Fields** (*Ctrl+F2*), then go to the *Variables* tab. Select **Number range** as the Type and **Arabic (1 2 3)** as the Format, and type a name (like "Step") in the Name field. Click **Insert** and a number field (starting at 1) appears in your document. Each additional click of **Insert** adds the next number in the sequence — 2, 3, 4, and so on.

Once you've seeded the sequence, you can delete the initial test fields; the "Step" variable remains available in the Select list of the Fields dialog for the rest of the session. For even faster access, save the field as an AutoText entry so you can drop in the next Step number with a quick shortcut and *F3*.

---

## UI Reference  —  Insert Menu

_Scope: Field > More Fields… (Ctrl+F2) Variables tab_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown expanded from the Writer menu bar. It is a single-column dropdown listing the following items from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Some items have submenu arrows indicating nested options, and separator lines divide the menu into logical groups.

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
