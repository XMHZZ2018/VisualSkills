# Formatting Footnotes and Endnotes (LibreOffice Writer 7.3.7)

Footnotes sit at the bottom of the page where they're referenced; endnotes gather at the end of the document. Both are easy to insert, but you'll probably want to tweak how they look and where exactly they land on the page. Here's how.

## Footnote Location and the Separator Line

The placement of footnotes and the style of the separator line between them and the body text are controlled at the *page style* level. Since your document might use several page styles, you may need to adjust this on each one individually.

Open the page style dialog by going to **Format > Page** on the Menu bar (or right-click the page and choose **Page** from the context menu). Switch to the **Footnote** tab to see your options.

See `fig01.png`.

Under **Footnote Area**, the default **Not larger than page area** lets Writer calculate space automatically based on how many footnotes appear. If you'd rather cap it yourself, select **Maximum footnote height** and type in a value — any footnote content that doesn't fit will spill onto the next page.

The **Space to text** field controls the gap between your body text and the first footnote.

## Customizing the Separator Line

In the **Separator Line** section of that same tab, you can set the line's **Position** (left, center, or right), its **Style**, **Thickness**, **Color**, and **Length** (as a percentage of the page width). There's also a **Spacing to footnote contents** value that controls the gap between the line and the footnotes themselves.

Once everything looks right, click **OK** to save your changes. These settings apply to the current page style, so if your document uses multiple page styles, repeat the process for each one that carries footnotes.

---

## UI Reference  —  Document Structure: Sections, Headers/Footers & Heading Numbering

_Scope: Section Footnotes/Endnotes tab: collect at end, restart numbering, custom format_

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

