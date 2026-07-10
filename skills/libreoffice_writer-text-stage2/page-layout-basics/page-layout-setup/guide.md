# Basic Page Layout and Margins (LibreOffice Writer 7.3.7)

Every page in Writer is governed by a page style. The *Default Page Style* is what you get out of the box, and it controls page size, orientation, margins, headers, footers, and more. You can modify it or create your own custom styles — but keep in mind that any changes to the Default Page Style apply only to the current document, not globally.

To get started, right-click anywhere on your page and select **Page Style** from the context menu. This opens the Page Style dialog, where most of the action happens. Head to the **Page** tab — here you'll find dropdowns for **Format** (Letter, A4, etc.), fields for **Width** and **Height**, and radio buttons to switch between **Portrait** and **Landscape** orientation.

The Page Style dialog is shown with its Page tab selected. On the left side, the Paper Format section displays a Format dropdown set to A4, Width of 21.00 cm, Height of 29.70 cm, and Portrait/Landscape radio buttons with Portrait selected; a page preview showing two facing pages appears to the right. Below that, the Margins section has spin-box fields for Inner (2.50 cm), Outer (1.80 cm), Top (2.00 cm), Bottom (2.00 cm), and Gutter (0.00 cm), while the Layout Settings section on the right offers dropdowns for Page layout (set to Mirrored), Page numbers (1, 2, 3, …), and Gutter position (Left), along with checkboxes for "Use page line-spacing" and "Background covers margins."

Down in the **Margins** section of that same tab, you can set **Inner** (or Left), **Outer** (or Right), **Top**, and **Bottom** margins to exact values. There's also a **Gutter** field — that's extra space added to the binding edge for documents you plan to print double-sided. You can either set the gutter explicitly or just leave it at zero and add the extra space to your inner margin manually. The **Layout Settings** area lets you choose mirrored margins for facing pages and configure page numbering. When you're happy, click **OK** to save.

If you just need a quick margin tweak, you can drag the margins directly on the rulers. The shaded gray areas at the edges of the horizontal and vertical rulers represent the margins — hover between the gray and white zones until the cursor becomes a double-headed arrow, then drag. It's fast, but not precise.

The screenshot shows the top-left corner of the Writer window where the horizontal and vertical rulers meet. On the horizontal ruler, a double-headed left-right arrow cursor is positioned at the boundary between the gray margin band and the white text area, with a tooltip reading "0.788 in." On the vertical ruler, a similar double-headed up-down arrow cursor sits at the margin boundary, also showing a "0.788 in" tooltip. Both drag points are highlighted with red boxes to indicate exactly where to click and drag to adjust the margins.

Be careful not to grab the small triangular arrows on the ruler — those control paragraph indents, not page margins. They sit right on top of each other, so aim for the margin boundary line itself.

For the quickest approach of all, open the **Page** deck in the Sidebar (on the right side of the Writer window). Under **Format**, you'll see a **Margins** dropdown with presets like None, Narrow, Moderate, Normal, Wide, and Mirrored. Pick one and you're done — though note that the Sidebar sets all four margins to the same value, so switch to the Page Style dialog if you need different margins on each side.

The Sidebar's Page panel is shown with the Format section expanded, displaying fields for Size (A4), Width (21.00 cm), Height (29.70 cm), and Orientation (Portrait). The Margins dropdown is open, revealing preset options: Custom (currently selected), None (highlighted in blue), Narrow, Moderate, Normal (1.90 cm), Normal (2.54 cm), Normal (3.18 cm), Wide, Mirrored, and Custom. Below the Format section, a collapsed Styles section is visible with fields for Number, Background, Layout, and Columns. To the right of the panel, a vertical strip of sidebar icon buttons is visible.

---

## UI Reference  —  Document Canvas, Rulers & Scrollbars

_Scope: Margin bands on horizontal/vertical rulers; drag to adjust page margins_

The main editing surface and its surrounding controls for navigation, measurement, and layout.

## Canvas

The white rectangular area represents the printable page, surrounded by a grey pasteboard.

**Mouse interactions:**
- **Click** — Place the text cursor.
- **Click-drag** — Select a range of text.
- **Double-click** — Select the word under the cursor.
- **Right-click** — Context menu with: Paste, Clone Formatting, Clear Direct Formatting, Character (►), Paragraph (►), List (►), Insert Comment, Page Style…
- **Right-click with selection** — Adds Cut and Copy to the context menu.

The **Character** submenu offers: Character…, No Character Style, Emphasis, Strong Emphasis, Quotation, Source Text.

## Horizontal Ruler

Visible by default (toggle: View > Rulers, Shift+Ctrl+R). Displays page margins as grey bands on each end, with the white writable area between them.

**Controls:**
- **Tab-type selector** (far left button) — Click to cycle: Left, Right, Center, Decimal tab stop, First-Line Indent, Hanging Indent.
- **First-line indent** (top triangle) — Drag to set first-line paragraph indent.
- **Left indent** (bottom-left triangle) — Drag to set left indent for wrapped lines.
- **Right indent** (right triangle) — Drag to set right indent.
- **Tab stops** — Click in the white area to add; drag to move; drag off the ruler to delete.
- **Right-click** — Change measurement units: Millimeter, Centimeter, Inch, Point, Pica, Char.
- **Double-click** — Opens the Paragraph dialog.

## Vertical Ruler

Not visible by default. Enable via View > Rulers > Vertical Ruler. Shows top/bottom margins as grey bands. Right-click to change units (Millimeter, Centimeter, Inch, Point, Pica, Line).

## Scrollbars

- **Vertical scrollbar** — Right edge, for vertical document navigation.
- **Horizontal scrollbar** — Bottom edge, for horizontal navigation.
- Toggle via View > Scrollbars (both enabled by default).

---

## UI Reference  —  Format Menu

_Scope: Page Style… (Shift+Alt+P)_

The Format menu controls text styling, paragraph formatting, page layout, and document-level formatting options.

The Format menu is shown open in the menu bar. It lists the following items from top to bottom: Text (with submenu arrow), Spacing (with submenu arrow), Align Text (with submenu arrow), Clone Formatting, Clear Direct Formatting, Spotlight (with submenu arrow), then a separator followed by Character…, Paragraph…, Lists (with submenu arrow), Bullets and Numbering…, Theme…, then another separator followed by Page Style…, Title Page…, Columns…, Watermark…, and the grayed-out Sections…. Below another separator are context-sensitive entries: Image, Text Box and Shape, Frame and Object, the grayed-out Name… and Alt Text…, then Anchor, Wrap, Arrange, Rotate or Flip, and Group.

## Elements

- **Text** (►) — 19 text style commands: Bold (Ctrl+B), Italic (Ctrl+I), Single/Double Underline, Strikethrough, Overline, Superscript (Shift+Ctrl+P), Subscript (Shift+Ctrl+B), Shadow, Outline Font Effect, Increase/Decrease Size (Ctrl+]/[), case transforms (UPPERCASE, lowercase, Cycle Case Shift+F3, Sentence case, Capitalize Every Word, tOGGLE cASE), Small Capitals (Shift+Ctrl+K).
- **Spacing** (►) — Line Spacing (1, 1.15, 1.5, 2), Increase/Decrease Paragraph Spacing, Increase/Decrease Indent.
- **Align Text** (►) — Left (Ctrl+L), Centered (Ctrl+E), Right (Ctrl+R), Justified (Ctrl+J).
- **Clone Formatting** — Paint formatting from selection to other text.
- **Clear Direct Formatting** (Ctrl+M) — Remove all manual formatting, revert to style defaults.
- **Spotlight** (►) — Highlight formatting in document: Character Direct Formatting, Paragraph Styles, Character Styles.
- **Character…** — Opens the Character dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Paragraph…** — Opens the Paragraph dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Lists** (►) — No List (Shift+Ctrl+F12), Unordered List (Shift+F12), Ordered List (F12), Demote/Promote Outline Level, Move Item Down/Up (Ctrl+Alt+Down/Up), Insert Unnumbered Entry, Restart Numbering, Add to List.
- **Bullets and Numbering…** — Full list formatting dialog.
- **Theme…** — Document theme settings.
- **Page Style…** (Shift+Alt+P) — Opens the Page Style dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Title Page…** — Add/configure title pages.
- **Columns…** — Multi-column page layout dialog.
- **Watermark…** — Insert or configure a watermark.
- Context-sensitive submenus (active when an object is selected): Image, Text Box and Shape, Frame and Object, Anchor, Wrap, Arrange, Rotate or Flip, Group.

---

## UI Reference  —  Key Formatting Dialogs

_Scope: Page Style dialog Page tab: paper format, margins, gutter, layout settings_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

The Find and Replace dialog is displayed with a "Find:" text field at the top (with a blue-highlighted empty input box), followed by "Match case" and "Whole words only" checkboxes. Below that is a "Replace:" text field. Three buttons appear in a row: "Find All," "Find Previous," and "Find Next." An expanded "Other options" section shows checkboxes for "Current selection only," "Comments," "Regular expressions," and partially visible options for "Replace backwards" and "Paragraph Styles" on the right side.

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is shown with four visible tabs: Font (currently selected), Font Effects, Position, and Hyperlink. The Font tab displays a Family field set to "Liberation Serif" with a scrollable font list below it (showing Liberation Serif highlighted in blue, followed by Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, Linux Libertine Initials O, Linux Libertine Mono O, and Linux Libertine O). Below the list are fields for Style (set to "Regular"), Size (set to "12 pt"), and Language (set to "English (USA)").

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is shown with the "Indents & Spacing" tab selected. Two rows of tabs are visible: the top row has Outline & List, Tabs, Drop Caps, and Borders; the bottom row has Indents & Spacing (active, with a blue underline) and Alignment. The Indent section contains spin-box fields for "Before text" (0.00″), "After text" (0.00″), and "First line" (0.00″), each with minus and plus buttons, and an "Automatic" checkbox. The Spacing section has "Above paragraph" (0.00″) and "Below paragraph" (0.00″) fields with plus/minus buttons, and a "Do not add space between paragraphs of the same style" checkbox. The Line Spacing section at the bottom shows a dropdown set to "Single."

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style: Default Page Style dialog is shown with the Organizer tab selected. Visible tabs across the top include Organizer (active), Page, Area, Transparency, Header, and Footer, with additional tabs partially visible. The Style section contains fields for Name ("Default Page Style"), Next style ("Default Page Style"), Inherit from (empty), and Category ("Custom Styles"). Below that, a Contains section displays a summary: "11.69 inch + From top 0.79 inch, From bottom 0.79 inch + Text direction left-to-right … Default Page Style + Not page line-spacing."

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

---

## UI Reference  —  Right Sidebar

_Scope: Page panel (Alt+5): size, orientation, margins_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The screenshot shows the full LibreOffice Writer window with an empty document. Along the far right edge of the window, a narrow vertical strip of eight small icon buttons is visible, highlighted by a red rectangle. A tooltip reading "Properties (Alt+1)" is shown next to the topmost button. The main area displays a blank white page with the horizontal ruler above it, the standard toolbar and formatting toolbar at the top, and the status bar at the bottom showing "Page 1 of 1," "Default Page Style," and "English (USA)."

## Panel Buttons (top to bottom)

- **Properties** (Alt+1) — Formatting panel with three collapsible sections:
  - *Style:* Paragraph style dropdown, Clone Formatting, Update/New Style buttons.
  - *Character:* Font family, size, Bold/Italic/Underline/Strikethrough, Font Color, Highlighting, Change Case, Super/Subscript.
  - *Paragraph:* Alignment, lists/indent toolbar, line spacing, above/below spacing fields, left/right/first-line indent.

- **Styles** (Alt+2 / F11) — Full style manager: category toolbar (Paragraph/Character/Frame/Page/List/Table Styles), hierarchical style list, Fill Format Mode, filter dropdown. See [Styles](styles.md).

- **Gallery** (Alt+3) — Clip-art browser: categories (Arrows, BPMN, Bullets, Diagrams, Flow chart, Icons), thumbnail grid, Icon/Detailed view, New… button.

- **Navigator** (Alt+4 / F5) — Document structure tree: Headings, Tables, Frames, Images, OLE objects, Bookmarks, Sections, Hyperlinks, References, Indexes, Comments, Drawing objects, Fields, Footnotes, Endnotes. Includes page navigation controls and drag-mode options.

- **Page** (Alt+5) — Page layout panel:
  - *Format:* Size (A4), Width/Height, Orientation (Portrait/Landscape), Margins.
  - *Styles:* Page number format, Background, Layout, Columns.
  - *Header/Footer:* Enable toggles, margins, spacing, same-content options.

- **Style Inspector** (Alt+6) — Two-column Properties/Value tree showing all applied styles: Paragraph Styles, Paragraph Direct Formatting, Character Styles, Character Direct Formatting (50+ properties per node).

- **Manage Changes** (Alt+7) — Two tabs:
  - *List:* Action/Author/Date/Comment table with Accept/Reject/Accept All/Reject All buttons.
  - *Filter:* Date range, Author, Action, Comment filters.

- **Accessibility Check** (Alt+8) — Runs an accessibility audit and lists issues by category, each with a Fix… button.
