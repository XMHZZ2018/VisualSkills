# Defining a Different First Page (LibreOffice Writer 7.3.7)

Many documents — letters, memos, reports — need a first page that looks different from the rest. A letterhead might have a unique header, or a report's first page might skip the header and footer entirely. Writer gives you a few ways to pull this off.

**The simplest approach: one page style.** If you just need different headers or footers on the first page, you can stick with the Default page style. Right-click anywhere on the page, choose **Page Style**, then go to the **Header** or **Footer** tab. Turn on **Header on** (or **Footer on**), and deselect **Same content on first page**. You can optionally deselect **Same content on left and right pages** too. Now just type your first-page header or footer content on page one, and different content on any subsequent page — Writer keeps them independent.

See `fig01.png`.

**The more flexible approach: separate page styles.** Writer ships with a built-in *First Page* style and a *Default* style that work as a pair. The idea is that the First Page style automatically flows into the Default style for every page after it. To set this up, open the Page Style dialog for the First Page style, go to the **Organizer** tab, and set the **Next style** dropdown to **Default Style**. Now your first page uses one style, and everything after it switches automatically.

See `fig02.png`.

**The quick route: title pages.** If you want to convert existing pages into title pages (or insert new ones), head to **Format > Title Page**. This dialog lets you choose how many title pages to add, where to place them, and whether to restart page numbering afterward. You can also pick which page style to apply. It's especially handy for books or long documents where you need title, copyright, and decorative pages up front before the main content begins.

See `fig03.png`.

Between these three methods — toggling first-page content within one style, chaining two page styles together, or using the Title Page feature — you can handle just about any first-page scenario Writer throws at you.

---

## UI Reference  —  Document Structure: Sections, Headers/Footers & Heading Numbering

_Scope: Header/footer Same content on first page checkbox_

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

