# Formatting Paragraphs (LibreOffice Writer 7.3.7)

Writer gives you two ways to format paragraphs: **styles** (recommended) and **direct formatting**. Styles bundle many settings under one name—font, indents, spacing, alignment—so you can apply them consistently and update everything at once. Direct formatting is quick for one-off tweaks, but it overrides styles and can't be removed by reapplying a style. To strip direct formatting, select the text and hit **Format > Clear Direct Formatting** (or just press *Ctrl+M*).

The fastest way to apply a paragraph style is the **Set Paragraph Style** drop-down at the left end of the Formatting toolbar, or use *Ctrl+1* through *Ctrl+5* for Heading 1–5. You can also browse styles in the **Paragraph** tab of the Styles deck on the Sidebar.

For alignment, the Formatting toolbar has buttons for **Left**, **Center**, **Right**, and **Justified**. Justified text spreads words to fill each line; the last line defaults to left-aligned, but you can change that in **Format > Paragraph…** on the **Alignment** tab—options include centered, justified, or even expanding a single trailing word to fill the line.

The Paragraph dialog is shown open to the Alignment tab, with the "Justified" radio button selected under Options. The "Last line" dropdown is expanded, revealing three choices: Start, Centered, and Justified (currently highlighted). Below that are an "Expand single word" checkbox, a "Snap to text grid (if active)" checkbox, a Text-to-text Alignment dropdown set to "Automatic," and a Properties section with a Text direction dropdown set to "Use superordinate object settings." A preview pane on the right side of the dialog shows lines of varying lengths illustrating the justified alignment effect.

**Line spacing** controls the distance between baselines within a paragraph. Click the line-spacing button on the Paragraph panel of the Sidebar to pick Single, 1.15, 1.5, Double, or a custom value (*Proportional*, *Fixed*, *At Least*, etc.). **Paragraph spacing**—the gap above and below—is set with the *Above Paragraph Spacing* and *Below Paragraph Spacing* fields on the same panel. As a rule, use either paragraph spacing or indentation to separate paragraphs visually, not both.

The Properties panel of the right Sidebar is shown with the Paragraph section expanded. At the top are four alignment buttons and list/indent controls. Below, on the left under "Spacing," there are fields for above-paragraph spacing (0.20 cm) and below-paragraph spacing (0.20 cm), with a line-spacing dropdown button whose popover is open displaying preset options—Spacing: 1, 1.15, 1.5, and 2—followed by a "Custom Value" section with a "Line Spacing" dropdown expanded to show choices: Single (selected), 1.15 Lines, 1.5 Lines, Double, Proportional, At least, Leading, and Fixed. On the right under "Indent," three fields show left indent (0.00 cm), right indent (0.00 cm), and first-line indent (0.00 cm).

For **indentation**, use the indent buttons on the toolbar or set precise values in the Paragraph dialog's **Indents & Spacing** tab. *Before Text* indents from the left margin, *After Text* from the right, and *First Line* indents just the opening line (the classic book-style indent). Switching to **Hanging Indent** does the opposite: the first line stays at the margin while subsequent lines are indented—handy for numbered paragraphs or lists with icons.

To work with **tab stops**, right-click a paragraph and choose **Paragraph**, then open the **Tabs** tab (or double-click the horizontal ruler). You can set the position, choose a type—**Left**, **Right**, **Center**, or **Decimal**—and pick a fill character like dots or dashes. Any custom tab stops you define will override the defaults. To change the default tab interval globally, head to **Tools > Options > LibreOffice Writer > General**.

The Paragraph dialog is shown open to the Tabs tab. On the left, a Position list displays two defined tab stops at 5.00 cm and 10.00 cm, with 5.00 cm currently selected (highlighted in blue). In the center, the Type section offers radio buttons for Left (selected), Right, Centered, and Decimal, each with a small alignment icon beside it, plus a Character field at the bottom for specifying a decimal character. On the right, the Fill Character section provides radio buttons for None (selected), dots, dashes, underscores, and a custom Character option with a text field. Along the right edge are three buttons: New, Delete all, and Delete.

The Paragraph dialog (**Format > Paragraph…**) has several other useful tabs. **Borders** lets you frame a paragraph with lines and shadows—great for callout boxes. **Text Flow** controls hyphenation, page breaks, and widow/orphan protection. **Drop Caps** creates an enlarged opening letter for a chapter feel. Explore these when you need them, but for anything you plan to reuse, define it in a paragraph style instead of applying it directly.

---

## UI Reference  —  Document Canvas, Rulers & Scrollbars

_Scope: Ruler indent triangles (first-line, left, right), tab stops, double-click opens Paragraph dialog_

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

_Scope: Paragraph…, Spacing submenu, Align Text submenu_

The Format menu controls text styling, paragraph formatting, page layout, and document-level formatting options.

The Format menu is shown open as a single-column dropdown. From top to bottom, the entries are: Text (with a submenu arrow), Spacing (with a submenu arrow), Align Text (with a submenu arrow), Clone Formatting, Clear Direct Formatting, Spotlight (with a submenu arrow), a separator, Character…, Paragraph…, Lists (with a submenu arrow), Bullets and Numbering…, Theme…, a separator, Page Style…, Title Page…, Comments… (greyed out), Columns…, Watermark…, Sections… (greyed out), a separator, then context-sensitive items: Image, Text Box and Shape, Frame and Object, Name… (greyed out), Alt Text… (greyed out), a separator, Anchor, Wrap, Arrange, Rotate or Flip, and Group.

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

_Scope: Paragraph dialog tabs: Indents & Spacing, Alignment, Text Flow, Tabs, Drop Caps_

These multi-tab dialogs provide detailed control over character formatting, paragraph layout, page styles, and search/replace.

## Find and Replace (Ctrl+H)

The Find and Replace dialog is a compact floating window titled "Find and Replace." At the top is a "Find:" label with a text input field. Below it are two checkboxes: "Match case" and "Whole words only." Next is a "Replace:" label with its own text field, followed by a row of three buttons: "Find All," "Find Previous," and "Find Next." An expandable "Other options" section is shown open, revealing checkboxes for "Current selection only," "Comments," "Regular expressions," along with partially visible options for "Replace backwards" and "Paragraph Styles" on the right side.

Opened via Edit > Find and Replace… or Ctrl+H.

- **Find** text field (with history dropdown)
- **Match case** / **Whole words only** checkboxes
- **Replace** text field (with history dropdown)
- **Buttons:** Find All, Find Previous, Find Next, Replace, Replace All
- **Other options** (collapsible): Current selection only, Comments, Regular expressions, Similarity search (with Similarities… button), Diacritic-sensitive, Replace backwards, Paragraph Styles
- **Attributes…** / **Format…** / **No Format** buttons for format-aware search

## Character Dialog (Format > Character…)

The Character dialog is shown open to the Font tab. It displays fields for Family (set to "Liberation Serif," highlighted in a scrollable list that also shows Linux Biolinum Keyboard O, Linux Biolinum O, Linux Libertine Display O, Linux Libertine Initials O, Linux Libertine Mono O, and Linux Libertine O), Style (set to "Regular"), Size (set to "12 pt"), and Language (set to "English (USA)"). Additional tabs visible along the top of the dialog are Font Effects, Position, and Hyperlink.

**Tabs:** Font, Font Effects, Position, Hyperlink, Highlighting, Borders

- **Font tab:** Family, Style (Regular/Bold/Italic/Bold Italic), Size, Language, Features… button, font preview.
- **Font Effects tab:** Font Color + Transparency, Overlining style+color, Strikethrough style, Underlining style+color+Individual words, Case dropdown, Relief, Hidden/Outline/Shadow checkboxes.
- **Position tab:** Normal/Superscript/Subscript radio + raise/lower %, Rotation (0°/90°/270°) + Scale width + Fit to line, Character spacing + Pair kerning.

## Paragraph Dialog (Format > Paragraph…)

The Paragraph dialog is shown open to the Indents & Spacing tab. Under the "Indent" heading are three fields with plus/minus buttons: "Before text" (0.00″), "After text" (0.00″), and "First line" (0.00″), along with an "Automatic" checkbox. Under the "Spacing" heading are "Above paragraph" (0.00″) and "Below paragraph" (0.00″) fields with plus/minus buttons, and a checkbox labeled "Do not add space between paragraphs of the same style." At the bottom, a "Line Spacing" dropdown is set to "Single." Additional tabs visible along the top include Outline & List, Tabs, Drop Caps, Borders, and Alignment.

**Tabs:** Indents & Spacing, Alignment, Text Flow, Outline & List, Tabs, Drop Caps, Borders, Area, Transparency

- **Indents & Spacing:** Before/After text indent, First line indent, Automatic; Spacing above/below paragraph; Line Spacing dropdown (Single/1.15/1.5/Double/Proportional/At least/Leading/Fixed); Activate page line-spacing.
- **Alignment:** Left/Center/Right/Justified radio; Last line dropdown; Expand single word; Text-to-text alignment; Text direction.
- **Text Flow:** Hyphenation settings, page/column breaks, orphan/widow control.
- **Tabs:** Tab stop position, type (Left/Right/Center/Decimal), fill character.

## Page Style Dialog (Format > Page Style…, Shift+Alt+P)

The Page Style dialog is shown open to the Organizer tab, titled "Page Style: Default Page Style." It contains fields for Name ("Default Page Style"), Next style ("Default Page Style"), Inherit from (empty), and Category ("Custom Styles"). Below is a "Contains" summary reading "11.69 inch + From top 0.79 inch, From bottom 0.79 inch + Text direction left-to-right… Default Page Style + Not page line-spacing." Tabs visible along the top include Organizer (selected), Page, Area, Transparency, Header, Footer, and partially visible Borders.

**Tabs:** Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote

- **Organizer:** Style name, Next style dropdown, Inherit from, Category, Contains description.
- **Page:** Paper format (size, width, height, portrait/landscape, paper tray), Margins (left/right/top/bottom/gutter), Layout settings (page layout, page numbers, gutter position).
- **Header/Footer:** Enable checkbox, margins, spacing, same content on left/right pages.
- **Columns:** Column count, width/spacing, separator line options.

---

## UI Reference  —  Formatting Toolbar

_Scope: Align Left/Center/Right/Justified, Increase/Decrease Indent, Line Spacing, Paragraph Spacing_

The second toolbar row provides all character and paragraph formatting controls with split-button dropdowns.

The Formatting toolbar is a single horizontal row of controls. From left to right it shows: a Paragraph Style dropdown displaying "Default Paragraph Style," two small style-update icons, a Font Name dropdown showing "Liberation Serif," a Font Size dropdown showing "12 pt," then buttons for Bold (B), Italic (I), Underline (U) with a split-button dropdown arrow, Strikethrough (S), Superscript (x²), and Subscript (x₂). Next come a Font Color button (A with a colored underline) and a Highlighting Color button, followed by four alignment buttons (Align Left, Center, Right, and Justified), then list toggle buttons, indent increase/decrease buttons, and finally line-spacing and paragraph-spacing controls at the right end.

## Elements

Row (left → right):

- **Paragraph Style** dropdown — Shows current style (e.g. "Default Paragraph Style"). Dropdown lists: Clear formatting, Default Paragraph Style, Body Text, Title, Subtitle, Heading 1–4, Block Quotation, Preformatted Text, More Styles…
- **Update Selected Style** (Shift+Ctrl+F11) — Update current style to match cursor formatting.
- **New Style from Selection** (Shift+F11) — Create a new style from current formatting.
- **Font Name** dropdown — Shows/changes the font (e.g. "Liberation Serif"). Lists all installed fonts rendered in their own typeface.
- **Font Size** dropdown — Shows/changes size in pt (6–48, plus custom values).

| *(separator)* |

- **Bold** (Ctrl+B) / **Italic** (Ctrl+I)
- **Underline** (Ctrl+U, split-button ▼) — Toggle; dropdown offers 11 underline styles (single, double, bold, dotted, dashed, wavy, etc.) plus More Options…
- **Strikethrough**
- **Superscript** (Shift+Ctrl+P) / **Subscript** (Shift+Ctrl+B)
- **Clear Direct Formatting** (Ctrl+M) — Eraser icon; removes all manual formatting.

| *(separator)* |

- **Font Color** (split-button ▼) — Applies current color; dropdown opens ~120-swatch color picker with Custom Color… option.
- **Character Highlighting Color** (split-button ▼) — Marker-pen highlight; dropdown opens color picker.

| *(separator)* |

- **Align Left** (Ctrl+L) / **Align Center** (Ctrl+E) / **Align Right** (Ctrl+R) / **Justified** (Ctrl+J)

| *(separator)* |

- **Toggle Unordered List** (Shift+F12, split-button ▼) — Bullet list; dropdown shows 8 bullet styles + Customize…
- **Toggle Ordered List** (F12, split-button ▼) — Numbered list; dropdown shows 8 numbering styles + Customize…
- **Select Outline Format** (split-button ▼) — Multi-level outline presets.
- **Increase Indent** / **Decrease Indent**

| *(separator)* |

- **Set Line Spacing** (split-button ▼) — Presets (1, 1.15, 1.5, 2) plus custom value editor.
- **Increase Paragraph Spacing** / **Decrease Paragraph Spacing**

---

## UI Reference  —  Right Sidebar

_Scope: Properties > Paragraph section: alignment, spacing, indent fields_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The full LibreOffice Writer window is shown with an empty document in the center and the right sidebar in its collapsed state. The sidebar appears as a narrow vertical strip along the far-right edge of the window, containing a column of small icon buttons. A red rectangle highlights the top icon, and a tooltip reading "Properties (Alt+1)" is displayed next to it, indicating the first panel button. Below the Properties icon, additional icons for Styles, Gallery, Navigator, Page, Style Inspector, Manage Changes, and Accessibility Check are visible as small buttons running down the strip.

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
