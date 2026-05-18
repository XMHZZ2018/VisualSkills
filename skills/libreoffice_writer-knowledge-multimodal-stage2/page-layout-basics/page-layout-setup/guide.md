# Basic Page Layout and Margins (LibreOffice Writer 7.3.7)

Every page in Writer is governed by a page style. The *Default Page Style* is what you get out of the box, and it controls page size, orientation, margins, headers, footers, and more. You can modify it or create your own custom styles — but keep in mind that any changes to the Default Page Style apply only to the current document, not globally.

To get started, right-click anywhere on your page and select **Page Style** from the context menu. This opens the Page Style dialog, where most of the action happens. Head to the **Page** tab — here you'll find dropdowns for **Format** (Letter, A4, etc.), fields for **Width** and **Height**, and radio buttons to switch between **Portrait** and **Landscape** orientation.

See `fig01.png`.

Down in the **Margins** section of that same tab, you can set **Inner** (or Left), **Outer** (or Right), **Top**, and **Bottom** margins to exact values. There's also a **Gutter** field — that's extra space added to the binding edge for documents you plan to print double-sided. You can either set the gutter explicitly or just leave it at zero and add the extra space to your inner margin manually. The **Layout Settings** area lets you choose mirrored margins for facing pages and configure page numbering. When you're happy, click **OK** to save.

If you just need a quick margin tweak, you can drag the margins directly on the rulers. The shaded gray areas at the edges of the horizontal and vertical rulers represent the margins — hover between the gray and white zones until the cursor becomes a double-headed arrow, then drag. It's fast, but not precise.

See `fig02.png`.

Be careful not to grab the small triangular arrows on the ruler — those control paragraph indents, not page margins. They sit right on top of each other, so aim for the margin boundary line itself.

For the quickest approach of all, open the **Page** deck in the Sidebar (on the right side of the Writer window). Under **Format**, you'll see a **Margins** dropdown with presets like None, Narrow, Moderate, Normal, Wide, and Mirrored. Pick one and you're done — though note that the Sidebar sets all four margins to the same value, so switch to the Page Style dialog if you need different margins on each side.

See `fig03.png`.

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

Read the screenshot `ui-format-menu.png` in this directory.

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

(see screenshot `ui-find-replace-dialog.png`)

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

(see screenshot `ui-character-dialog.png`)

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

(see screenshot `ui-paragraph-dialog.png`)

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

(see screenshot `ui-page-style-dialog.png`)

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

---

## UI Reference  —  Right Sidebar

_Scope: Page panel (Alt+5): size, orientation, margins_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

Read the screenshot `ui-right-sidebar-location.png` in this directory.

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

