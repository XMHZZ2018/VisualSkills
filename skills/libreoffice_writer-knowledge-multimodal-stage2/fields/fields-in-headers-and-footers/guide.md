# Fields in Headers and Footers (LibreOffice Writer 7.3.7)

Headers and footers really come alive when you drop fields into them — things like page numbers, dates, chapter titles, and document info that update automatically. No more manually typing "Page 3 of 12" on every page.

You can insert fields into headers or footers the same way you would anywhere else in your document. To add a page number, document title, author, creation date and time, current date and time, or total page count, head to **Insert > Field > [item]** on the Menu bar, or open Document Properties (see the guide's page 437) and choose the field you need from there.

If you want to insert a cross-reference to a bookmark, heading, or other item, use **Insert > Cross-reference** or go to **Insert > Field > More Fields > Cross-references** tab.

Here's a handy trick for chapter-based documents: if you've been using Heading 1 for your chapter titles, you can insert a Document field that automatically pulls in the current chapter's title. As you move from chapter to chapter, the header or footer updates on its own. Writer calls these chapter titles "Chapter names" in the Fields dialog. If you've used outline numbering on your Heading 1, you can also choose whether to include the chapter number, the name, or both. Set this up via **Insert > Field > More Fields > Document**.

You can even cross-reference other heading levels by specifying a value in the Level box on the Document tab of the Fields dialog. Level 1 corresponds to Heading 1, Level 2 to Heading 2, and so on — so you can pull in sub-chapter headings just as easily.

One more thing worth knowing: fields like "Chapter" and "Statistics" are especially useful during writing because they stay current as your document grows. Drop them into a footer early on and forget about them — they'll keep themselves accurate right through to your final draft.

---

## UI Reference  —  Document Structure: Sections, Headers/Footers & Heading Numbering

_Scope: Header/footer dropdown Insert Page Number/Count; inline header/footer editing zone_

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

_Scope: Field submenu, Header and Footer submenu for inserting fields_

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

