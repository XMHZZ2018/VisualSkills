# Printing Mailing Labels and Envelopes (LibreOffice Writer 7.3.7)

Labels are handy for printing address lists where each label holds a different address, but they also work for batch-printing identical labels — think return-address stickers or CD labels. Before you start, jot down the brand and type of your label sheets so you can match them in the dialog.

To get going, open **File > New > Labels**. On the **Labels** tab, pick your **Database** and **Table** from the drop-downs on the right, then select each address field (like FNAME, ADDRESS1, CITY, etc.) from the **Database field** list and click the left arrow to drop it into the **Label text** area. Add punctuation, spaces, and line breaks between fields until your label looks right.

The Labels dialog is shown with the Labels tab active. The left side contains an **Inscription** section with a **Label text** area populated with merge fields such as `<Addresses.Sheet1.0.FNAME>`, `<Addresses.Sheet1.0.SURNAME>`, `<Addresses.Sheet1.0.ADDRESS>`, `<Addresses.Sheet1.0.AD2>`, `<Addresses.Sheet1.0.CITY>`, `<Addresses.Sheet1.0.STATE>`, `<Addresses.Sheet1.0.PCODE>`, and `<Addresses.Sheet1.0.COUNTRY>`. On the right side are three drop-downs: **Database** set to "Addresses," **Table** set to "Sheet1," and **Database field** set to "COUNTRY," with a left-arrow button between them to insert fields into the label text. At the bottom, a **Format** section has **Continuous** and **Sheet** radio buttons (Sheet is selected), a **Brand** drop-down set to "Avery A4," and a **Type** drop-down with "J8160 Address" highlighted in blue, showing dimensions of 2.50" × 1.50" (3 × 7). Buttons along the bottom of the dialog include **Help**, **Reset**, **New Document**, and **Cancel**.

Down in the **Format** section, choose your label **Brand** and **Type** to match your physical sheets. If your labels aren't listed, select **[User]** in the Type box and flip to the **Format** tab to enter custom dimensions — horizontal pitch, vertical pitch, width, height, margins, columns, and rows. You can save a custom layout for reuse by clicking **Save** and giving it a name.

On the **Options** tab, make sure **Synchronize contents** is checked. This ensures edits you make to the first label propagate to all the others. Then hit **New Document**. You'll get a one-page document with a grid of label frames, each filled with your merge fields. The printed output expands to as many pages as your data requires.

The Labels dialog is shown with the **Options** tab selected. Under a **Distribute** heading, there are two radio buttons: **Entire page** (selected) and **Single label**, with **Column** and **Row** spinners both set to 1 next to the Single label option. Below the radio buttons, the **Synchronize contents** checkbox is checked.

A small **Synchronize Labels** button appears near the top-left of the screen. If you need to tweak formatting — change the font, fix punctuation, add a field — edit the upper-left label only, then click **Synchronize Labels** to push those changes to every label on the page.

When you're happy, go to **File > Print** and click **Yes** to confirm the mail merge. In the Mail Merge dialog you can print all records, or use Ctrl+click to cherry-pick individual ones. Click **OK** to send them to the printer (or choose **File** in the Output section to save to a file instead).

To edit a saved label file later, open it like any Writer document. You can right-click a label record, choose **Paragraph > Edit Style**, and adjust the font, size, or indents — but you can't regenerate labels from the source data without recreating the merge.

## Envelopes

For envelopes, go to **Insert > Envelope**. On the **Envelope** tab, drag your address fields from the database into the **Addressee** box, just like you did for labels. If your envelopes aren't pre-printed, check the **Sender** box and fill in your return address. Use the **Format** and **Printer** tabs to set envelope size and feed direction.

The Envelope dialog is displayed with the **Envelope** tab active and three tabs visible: Envelope, Format, and Printer. The upper-left area contains an **Addressee** text box filled with merge fields (`<Addresses.Sheet1.0.FNAME>` through `<Addresses.Sheet1.0.COUNTRY>`), and the upper-right has **Database**, **Table**, and **Database field** drop-downs set to "Addresses," "Sheet1," and "COUNTRY" respectively, with a left-arrow button for inserting fields. Below the addressee area, the **Sender** checkbox is checked, and the sender text box shows a sample return address ("Jean Hollis Weber, 123 Any Street, Some Town ZZ 0000, Australia"). To the right of the sender box is a graphical envelope preview showing the placement of the return address (upper-left, shaded) and the recipient address (center-right, shaded). Buttons along the bottom include **Help**, **Insert**, **Reset**, **New Document**, and **Cancel**.

Click **New Document** to create the envelope template. To merge and print, choose **File > Print**, confirm the merge, and select your records the same way as with labels.

---

## UI Reference  —  Insert Menu

_Scope: Envelope…_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown expanded from the LibreOffice Writer menu bar. It displays a single-column list of menu items from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Several items have submenu arrows, and some have checkbox icons to their left.

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
