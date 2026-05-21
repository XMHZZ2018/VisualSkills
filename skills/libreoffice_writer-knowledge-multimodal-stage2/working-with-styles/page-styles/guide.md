# Working with Page Styles (LibreOffice Writer 7.3.7)

Page styles in Writer control margins, page size, headers, footers, and columns — everything about the physical layout of your pages. Unlike paragraph or character styles, page styles can't be directly applied to content. Instead, every page inherits its look from an underlying page style, so when you tweak that style, all pages using it update at once. If you need individual pages to look different, you'll create separate page styles.

To get started, open the **Styles** deck and click the **Page Styles** icon. Right-click anywhere in the list and choose **New** to create a fresh style, or select an existing one and hit **Modify**. The Page Style dialog has nine tabs — the most important ones are Page, Header, Footer, Columns, and Borders.

On the **Page** tab, you'll set your paper size and orientation. Pick a predefined format from the **Paper Format** section, or choose **User** and type custom **Width** and **Height** values. Flip between **Portrait** and **Landscape** depending on your needs.

See `fig01.png`.

The **Margins** section on that same tab lets you dial in inner, outer, top, bottom, and gutter spacing. If you choose **Mirrored** in the **Page layout** dropdown under **Layout Settings**, the margin labels switch to Inner and Outer — perfect for book-style printing where left and right pages mirror each other. The **Gutter** margin adds extra binding space on the inner edge.

A common practice for printed layouts is asymmetrical margins: wider outer margins on the right-hand page, with the bottom margin larger than the top. If you're setting up a book, select a mirrored layout so the first chapter page uses the right-page settings, and the rest of the chapter uses a "mirrored" default style for both left and right pages. A mirrored page can carry different headers and footers, which is handy for alternating page numbers or chapter titles.

You can also define entirely separate page styles for left and right pages — say, a full-page photo on the left and two columns of text on the right. Just make sure the **Next Style** field on each style points to the correct following style so Writer cycles through them automatically.

Use the **Page numbers** dropdown to choose a numbering style (1, 2, 3 or i, ii, iii, etc.) that applies wherever you assign this page style. Combined with the **Header** and **Footer** tabs, you can insert fields like page number or chapter name into running headers or footers, giving each section of your document its own look without manual formatting.

---

## UI Reference  —  Right Sidebar

_Scope: Page panel: page number format, background, layout, columns, header/footer toggles_

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

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: Page Styles category in Styles panel toolbar_

LibreOffice Writer uses a style-based formatting system. The Styles menu provides quick-apply shortcuts, while the Styles panel (F11) offers full management.

Read the screenshot `ui-styles-menu.png` in this directory.

## Styles Menu

The menu has three radio-button sections for quick style application:

**Paragraph styles:**
- Body Text (Ctrl+0), Title, Subtitle, Heading 1 (Ctrl+1), Heading 2 (Ctrl+2), Heading 3 (Ctrl+3), Block Quotation, Preformatted Text

**Character styles:**
- No Character Style (default), Emphasis, Strong Emphasis, Quotation, Source Text

**List styles:**
- No List (Shift+Ctrl+F12), Bullet • List Style, Numbering 123/ABC/abc/IVX/ivx List Styles

**Management commands:**
- Edit Style… (Alt+P), Update Selected Style (Shift+Ctrl+F11), New Style from Selection (Shift+F11), Load Styles from Template, Manage Styles (F11)

## Styles Panel (F11 / Alt+2)

The Styles panel in the right sidebar provides full style management:

- **Category toolbar:** Paragraph Styles, Character Styles, Frame Styles, Page Styles, List Styles, Table Styles, Fill Format Mode, Styles actions ▼
- **Style list:** Hierarchical tree of all styles (Default Paragraph Style, Body Text, Caption, Heading, Index, etc.)
- **Right-click on a style:** New…, Edit Style…, Hide, Show, Delete…
- **Show Previews** / **Spotlight** checkboxes
- **Filter dropdown:** Hierarchical, All Styles, Hidden Styles, Applied Styles, Custom Styles, Automatic, Text/Document/List/Index/Special/HTML/Conditional Styles
- **Styles actions dropdown:** New Style from Selection, Update Selected Style, Load Styles from Template

