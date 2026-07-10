# Working with Character and Frame Styles (LibreOffice Writer 7.3.7)

Character styles override the formatting within a paragraph style. They apply to groups of characters — words, phrases, or even individual letters — rather than whole paragraphs. Reach for a character style whenever you want to change the appearance of part of a paragraph without affecting the rest. Common examples include **bold**, *italic*, colored words, or a different typeface.

Beyond simple formatting, character styles are handy for chapter numbers, page numbers, list numbers larger than surrounding text, and formatted hyperlinks. You can also assign a language to a character style so that, say, French words in an English document get spell-checked with the right dictionary.

## Creating a new character style

The Character Styles dialog looks a lot like the one for paragraph styles. Open the **Styles** deck in the Sidebar, right-click in the character styles list, and choose **New Style**. On the **Organizer** tab, name your style and set its hierarchical level. The **Font** tab lets you pick the font, style, and size — you can specify size as a percentage or point increase/decrease relative to the paragraph font, and you can set the language for correct spell-checking.

The **Font Effects** tab is where things get interesting: font color, underlining, relief, strikethrough, and more. If you frequently use hidden text, define a character style with the **Hidden** option marked — relief effects work nicely for drop caps or chapter-number emphasis too. Use the **Highlighting** tab to apply a colored background (same result as the **Highlight Color** tool on the Standard toolbar). The **Borders** tab adds a border and shadow, and the **Position** tab handles subscript, superscript, rotation, condensed, and expanded text.
Note that when rotating characters, you need to specify whether the rotated text fits within the line or is allowed to expand above and below it. This property is active only for character styles, not paragraph styles.

## Working with frame styles

Frames are containers for text or graphics. To keep their appearance consistent, define frame styles — for instance, photographs in a drop-shadowed border, line drawings in a plain border, or marginal notes without a border but with a shaded background. Writer ships with several predefined frame styles: **Frame**, **Formula**, **Graphics**, **Labels**, **Marginalia**, **OLE**, and **Watermark**. You can modify any of these or create new ones.
When you add an object to Writer, it's automatically wrapped in a frame of a predefined type. The frame controls placement on the page and interaction with surrounding elements. You can edit the frame by modifying its style or by applying a manual override. To format a frame manually, select **Insert > Frame** on the Menu bar — the dialog that opens contains all the settings available when frame styles are set up, plus a few that only appear when the frame is already inserted.

If you work with a mix of graphics, consider defining two related styles: one with a border for images on white backgrounds, and one without a border for everything else. Beyond that, the default frame styles generally cover most needs — you may just want to add a style or two for text frames.

---

## UI Reference  —  Right Sidebar

_Scope: Styles panel > Character Styles and Frame Styles categories_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The screenshot shows the LibreOffice Writer window with the collapsed sidebar visible as a narrow vertical strip of eight small icon buttons docked against the far-right edge of the window. The topmost button is highlighted and displays a tooltip reading "Properties (Alt+1)." A red rectangle is drawn around the top portion of this sidebar strip to call attention to its location. The main document area with its toolbars and horizontal ruler occupies the rest of the window to the left of the sidebar.

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
