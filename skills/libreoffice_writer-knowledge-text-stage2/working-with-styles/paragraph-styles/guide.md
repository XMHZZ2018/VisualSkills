# Working with Paragraph Styles (LibreOffice Writer 7.3.7)

Paragraph styles are where you control the overall shape and behavior of your text blocks — indentation, spacing, alignment, page breaks, and more. You'll find most of what you need by right-clicking a style in the **Styles** deck under the **Paragraph Styles** category and choosing **Modify**. You can also start from **Format > Paragraph...** for one-off tweaks, but styles are the way to go for consistency.

## Indents and Spacing

The **Indents & Spacing** tab is your go-to for controlling how a paragraph sits on the page. **Before text** sets the left indent, **After text** sets the right indent, and **First line** controls whether the opening line is indented (positive value) or hanging (negative value). Check **Automatic** if you want Writer to calculate the first-line indent based on font size automatically.

The Paragraph Style dialog is shown with the **Indents & Spacing** tab selected. On the left side, the **Indent** section contains three spin-box fields — "Before text," "After text," and "First line" — all set to 0.00 cm, with an unchecked **Automatic** checkbox below them. Below that is the **Spacing** section with "Above paragraph" (0.00 cm) and "Below paragraph" (0.11 cm) fields, plus an unchecked "Do not add space between paragraphs of the same style" checkbox. At the bottom, the **Line Spacing** section has a dropdown set to "Single" and an "Activate page line-spacing" checkbox. A preview pane on the right side of the dialog shows a schematic representation of the paragraph layout with gray bars representing text lines.

Below the indent fields you'll find **Spacing**, where you set the gap above and below the paragraph. A common trick is to add space above heading styles so they visually separate from the preceding body text without needing empty paragraphs. If two consecutive paragraphs share the same style, you can tick **Do not add space between paragraphs of the same style** to keep them snug.

For **Line Spacing**, the default is **Single**, but **1.15 lines** or **Proportional** at around 115% often reads better. If you're mixing font sizes in one paragraph, choose **Fixed** or **At least** to keep lines evenly spaced.

## Alignment

On the **Alignment** tab you pick between Left, Right, Center, and Justified. When using Justified, Writer lets you decide how to handle the last line — left-aligned is the default, but you can center or fully justify it too. There's also a **Text to Text** vertical alignment option here, handy when you mix font sizes on a single line; choose between Automatic, Base line, Top, Middle, or Bottom.

## Text Flow

The **Text Flow** tab handles hyphenation, page breaks, and widow/orphan control. Under **Hyphenation**, set the minimum characters before and after a break and the maximum consecutive hyphenated lines. In the **Breaks** section, you can force a paragraph to start on a new page — set *Type* to **Page**, *Position* to **Before**, and optionally pick a page style with **With Page Style**. This is the classic way to start each chapter on a fresh page.

The Paragraph Style dialog is shown with the **Text Flow** tab active, divided into three areas. On the left, the **Hyphenation** section has "Automatically" checked, "Don't hyphenate words in CAPS" unchecked, and three spin-box fields: "Characters at line end" (2), "Characters at line begin" (2), and "Maximum number of consecutive hyphens" (0). On the right, the **Breaks** section has "Insert" checked with Type set to "Page," Position set to "Before," the "With page style" checkbox enabled and set to "Default Page Style," and an unchecked "Page number" field. Along the bottom, the **Options** section lists four checkboxes: "Do not split paragraph" (unchecked/grayed out), "Keep with next paragraph" (unchecked), "Orphan control" (checked, set to 2 lines), and "Widow control" (checked, set to 2 lines).

Under **Options**, enable **Do not split paragraph** to prevent a paragraph from breaking across pages, or use **Orphan control** and **Widow control** (typically set to 2 or 3 lines) to avoid stranded lines at the top or bottom of a page.

## Outline Level and Lists

The **Outline & List** tab lets you assign an outline level to any paragraph style, which means it will appear in the Navigator and can be included in a table of contents generated via **Tools > Chapter Numbering**. You can also associate a list style here to get automatic numbering or bullets.

## A Few More Useful Tabs

The **Position** tab controls superscript/subscript settings and paragraph rotation — handy for rotated headings in narrow table columns (set rotation to 90 or 270 degrees). The **Drop Caps** tab on the Paragraph Style dialog lets you enable a large initial letter spanning multiple lines, great for a first-paragraph flourish. And on the **Area** tab, you can add a background color, gradient, or pattern to the entire paragraph area — a quick way to create callout blocks without resorting to frames.

The Paragraph Style dialog (titled "Paragraph Style: First Paragraph") is shown with the **Drop Caps** tab selected. In the **Settings** section, "Display drop caps" is checked, "Whole word" is unchecked, "Number of characters" is set to 1, "Lines" is set to 3, and "Space to text" is 0.00 cm. Below that, a **Contents** section provides a "Text" field containing the letter "A" and a "Character style" dropdown set to "[None]." On the right side of the dialog, a preview pane shows a large capital letter "A" spanning three lines of placeholder text, illustrating the drop-cap effect.

---

## UI Reference  —  Right Sidebar

_Scope: Styles panel > Paragraph Styles category, hierarchical tree_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The LibreOffice Writer window is shown with an empty document open. Along the far-right edge of the window, a narrow vertical toolbar displays eight small icon buttons stacked top to bottom — these are the collapsed sidebar panel selectors. The topmost button (highlighted with a red rectangle) is the **Properties** panel button, with its tooltip "Properties (Alt+1)" visible. The remaining seven buttons below it correspond to the other sidebar panels (Styles, Gallery, Navigator, Page, Style Inspector, Manage Changes, and Accessibility Check). The main document area, standard toolbars, and menu bar are visible to the left.

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
