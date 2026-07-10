# Using Sections for Page Layout (LibreOffice Writer 7.3.7)

Sections in Writer let you treat a block of text differently from the rest of your document. Think of them as containers — you can use them to write-protect text, hide content, pull in content from another file, add columns to just part of a page, or give a region its own background and footnote style.

To create a section, place your cursor where you want it (or select existing text), then go to **Insert > Section**. The dialog that opens has five tabs: *Section*, *Columns*, *Indents*, *Area*, and *Footnotes/Endnotes*. Give the section a meaningful name in the **New Section** box — it shows up in the Navigator, so something descriptive helps. When you're happy with the settings, hit **Insert**.

See `fig01.png`.

If you want the section to pull in content from a separate file, check the **Link** option on the *Section* tab, click **Browse**, and pick the source document. You can even link to a specific section within that file using the *Section* drop-down. Writer can update linked sections automatically — configure that under **Tools > Options > LibreOffice Writer > General** in the *Update links when loading* area.

To keep people from editing a section's content, tick **Protect** in the *Write Protection* area. You can optionally add a password by also selecting **With password** — just be aware that a forgotten password can't easily be recovered. Protection only locks the content, not the section's formatting or attributes.

You can hide a section entirely by checking **Hide** in the *Hide* area. You can even make it conditional — enter a condition in the **With Condition** field using the same syntax as Writer's fields and formulas. This is great for producing different versions from a single source document (say, a student copy vs. a teacher copy of a test).

Need columns in just part of your page? The *Columns* tab lets you split the section into multiple columns. Check **Evenly distribute contents to all columns** if you want the text to balance out; leave it unchecked for newspaper-style flow where each column fills completely before the next one starts.

See `fig02.png`.

The *Indents* tab controls left and right margins for the section via the **Before section** and **After section** fields, with a handy preview on the right. The *Area* tab adds color or image backgrounds, and the *Footnotes/Endnotes* tab lets you restart numbering, change the format, or collect endnotes at the section's end instead of the document's end.

To edit or remove sections later, go to **Format > Sections**. Select a section from the list, change its name, link, protection, or hide settings, and click **OK**. To tweak column or formatting options, select the section and click **Options**. Clicking **Remove** doesn't delete the content — it just dissolves the section wrapper, merging the text back into the main document flow.

See `fig03.png`.

---

## UI Reference  —  Document Structure: Sections, Headers/Footers & Heading Numbering

_Scope: Insert Section dialog (all 5 tabs), Edit Sections dialog, section protection and linking_

These features control document organization beyond basic paragraph flow.

## Insert Section Dialog (Insert > Section...)

(see screenshot `ui-insert-section-dialog.png`)

Creates named, nestable document regions with independent formatting. **Tabs:** Section, Columns, Indents, Area, Footnotes/Endnotes.

**Section tab:**
- **Section name** field — auto-increments (Section1, Section2...). Section tree below shows existing sections for nesting.
- **Link** group — Link checkbox enables: File name field + Browse... button (import content from external file), DDE checkbox (Dynamic Data Exchange), Section dropdown (choose which section of the linked file).
- **Write Protection** — Protect checkbox (makes section read-only), With password checkbox (opens Enter Password sub-dialog, min 5 chars).
- **Hide** — Hide checkbox (makes section invisible), With Condition field (boolean expression for conditional hiding).
- **Properties** — Editable in read-only document checkbox.

**Columns tab:** Column count spinner (1-n), 5 preset layout icons, AutoWidth, per-column width/spacing spinners, separator line options (style, width, color, height, position).

**Indents tab:** Before section / After section indent spinners with preview.

**Area tab:** Background fill: None, Color (swatch grid + RGB/hex + Pick...), or Image (built-in textures, import, style/position/tiling controls).

**Footnotes/Endnotes tab:** Collect at end of text/section, restart numbering, custom format (before/after text + numbering style).

### Edit Sections Dialog (Format > Sections...)

Manages all document sections. Hierarchical section tree with state icons (lock = protected, arrow = hidden/linked). Controls mirror Insert Section but add **Options...** button (opens Columns/Indents/Background/Footnotes sub-dialog) and **Remove** button (no confirmation; reverted by Cancel).

## Headers & Footers

Headers/footers are enabled per page style via Insert > Header and Footer > Header/Footer > Default Page Style (toggle).

(see screenshot `ui-header-dropdown.png`)

**Inline editing:** Click the header/footer zone at the top/bottom of the page canvas. A dashed separator line and a label button ("Header/Footer (Default Page Style)") appear.

**Dropdown menu (▼ on label button):**
- Format Header/Footer... — opens Page Style dialog at Header/Footer tab
- Border and Background... — opens Border/Background dialog (Borders, Area, Transparency tabs)
- Delete Header/Footer... — confirmation dialog (irreversible)
- Insert Page Number — inserts page number field at cursor
- Insert Page Count — inserts total page count field at cursor

**Page Style Header/Footer tabs** (via Format Header/Footer... or right-click > Page Style...):
- Header/Footer on checkbox, Same content on left/right pages, Same content on first page
- Left/Right margins, Spacing (gap between header/footer and body), Height, AutoFit height
- More... button opens Border/Background sub-dialog

**Visibility:** Dashed lines and label button only appear when "Use header/footer menu" is enabled (Insert > Header and Footer) AND cursor is in the header/footer zone.

## Heading Numbering Dialog (Tools > Heading Numbering...)

(see screenshot `ui-heading-numbering-dialog.png`)

Configures automated numbering for heading levels 1-10. **Tabs:** Numbering, Position.

**Level selector** (left column): Click levels 1-10 individually, or "1 - 10" to edit all levels at once.

**Numbering tab:**
- **Number** dropdown — None, 1/2/3, A/B/C, a/b/c, I/II/III, i/ii/iii, ordinals, words, Cyrillic variants, symbols
- **Start at** spinner (default 1)
- **Paragraph style** dropdown — maps each level to a heading style (Level N → Heading N by default)
- **Character style** dropdown — applies a character style to the number portion only
- **Show sublevels** spinner — how many ancestor numbers to prepend (e.g., 2 on level 2 → "1.1")
- **Separator** Before/After fields — text around the number (e.g., "Chapter " before, "." after)
- **Preview panel** — live 10-level preview

**Position tab:**
- **Alignment** dropdown (Left/Centered/Right)
- **Aligned at** spinner — distance from left margin for the number
- **Followed by** dropdown — Tab stop (with Tab stop at spinner), Space, Nothing, or New Line
- **Indent at** spinner — body text indent for the heading
- **Default** button — resets position settings to built-in defaults

**Bottom bar:** Help, Load/Save (9 preset slots + Save As...), Reset, Cancel, OK.

---

## UI Reference  —  Insert Menu

_Scope: Section… command opening Insert Section dialog_

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

