# Working with Page Styles (LibreOffice Writer 7.3.7)

Page styles in Writer control margins, page size, headers, footers, and columns — everything about the physical layout of your pages. Unlike paragraph or character styles, page styles can't be directly applied to content. Instead, every page inherits its look from an underlying page style, so when you tweak that style, all pages using it update at once. If you need individual pages to look different, you'll create separate page styles.

To get started, open the **Styles** deck and click the **Page Styles** icon. Right-click anywhere in the list and choose **New** to create a fresh style, or select an existing one and hit **Modify**. The Page Style dialog has nine tabs — the most important ones are Page, Header, Footer, Columns, and Borders.

On the **Page** tab, you'll set your paper size and orientation. Pick a predefined format from the **Paper Format** section, or choose **User** and type custom **Width** and **Height** values. Flip between **Portrait** and **Landscape** depending on your needs.

The "Page Style: Default Page Style" dialog is shown with the Page tab selected. Across the top are nine tabs: Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, and Footnote. The left side of the dialog contains the Paper Format section with a Format dropdown set to A4, Width of 21.00 cm, Height of 29.70 cm, and Orientation radio buttons with Portrait selected. Below that is the Margins section with fields for Inner (2.50 cm), Outer (1.80 cm), Top (2.00 cm), Bottom (2.00 cm), and Gutter (0.00 cm). The right side shows a two-page preview thumbnail, a Paper tray dropdown set to "[From printer settings]," and a Layout Settings section with Page layout set to Mirrored, Page numbers set to "1, 2, 3, …," a Reference Style dropdown, a "Use page line-spacing" checkbox, Gutter position set to Left, a "Gutter on right side of page" checkbox, and a checked "Background covers margins" checkbox.

The **Margins** section on that same tab lets you dial in inner, outer, top, bottom, and gutter spacing. If you choose **Mirrored** in the **Page layout** dropdown under **Layout Settings**, the margin labels switch to Inner and Outer — perfect for book-style printing where left and right pages mirror each other. The **Gutter** margin adds extra binding space on the inner edge.

A common practice for printed layouts is asymmetrical margins: wider outer margins on the right-hand page, with the bottom margin larger than the top. If you're setting up a book, select a mirrored layout so the first chapter page uses the right-page settings, and the rest of the chapter uses a "mirrored" default style for both left and right pages. A mirrored page can carry different headers and footers, which is handy for alternating page numbers or chapter titles.

You can also define entirely separate page styles for left and right pages — say, a full-page photo on the left and two columns of text on the right. Just make sure the **Next Style** field on each style points to the correct following style so Writer cycles through them automatically.

Use the **Page numbers** dropdown to choose a numbering style (1, 2, 3 or i, ii, iii, etc.) that applies wherever you assign this page style. Combined with the **Header** and **Footer** tabs, you can insert fields like page number or chapter name into running headers or footers, giving each section of your document its own look without manual formatting.

---

## UI Reference  —  Right Sidebar

_Scope: Page panel (Alt+5) and Styles > Page Styles category_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The LibreOffice Writer window is displayed with an empty document open. Along the far-right edge of the window is a narrow vertical strip containing eight small icon buttons stacked top to bottom; this strip is the collapsed sidebar, highlighted with a red rectangle. A tooltip reading "Properties (Alt+1)" is visible next to the topmost button, indicating that clicking it would open the Properties panel. The main document area, menu bar, toolbars, and status bar (showing "Default Page Style") are all visible in their standard positions.

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
