# Working with List Styles (LibreOffice Writer 7.3.7)

List styles work hand-in-hand with paragraph styles to control indentation, alignment, and the bullet or numbering characters used for list items. You can define anything from a simple bulleted list to a complex multi-level nested outline. The big advantage over manually formatting lists with the **Toggle Ordered List** or **Toggle Unordered List** toolbar buttons is consistency — change the style once, and every list using it updates automatically.

To create a new list style, open the **Styles** deck in the sidebar, switch to the **List Styles** tab, right-click in the list, and choose **New Style**. The dialog that opens has six tabs beyond the usual **Organizer**: **Unordered**, **Ordered**, **Image**, **Outline**, **Position**, and **Customize**.

The **Unordered**, **Ordered**, and **Image** tabs offer predefined bullet and numbering formats. Just click the one you want — a thick border highlights your selection. The **Image** tab works the same way but uses small graphics instead of font characters.

The **Outline** tab gives you eight predefined nested-list layouts. Pick one as a starting point, then refine it with the **Position** and **Customize** tabs.

On the **Position** tab you dial in the spacing and alignment for each level. **Aligned at** sets how far the numbering symbol sits from the left margin. **Numbering alignment** (Left, Right, or Centered) controls how the symbol itself is justified at that position. **Numbering followed by** lets you choose a tab stop, a space, or nothing after the number. Finally, **Indent at** sets where the actual text of the list item begins. You can adjust these per level or select **1 – 10** to change all levels at once.

The "List Style: Untitled1" dialog is shown with the **Position** tab selected. On the left, under "Position and Spacing," there are fields for **Aligned at** (set to 0.64 cm), **Numbering alignment** (a dropdown set to "Left"), **Numbering followed by** (a dropdown set to "Tab stop"), **Tab stop at** (1.27 cm), and **Indent at** (1.27 cm). On the right side is a **Level** selector listing levels 1 through 10 plus a "1 – 10" option to select all levels at once, with level 1 currently highlighted. Below the fields is a **Preview** pane showing three progressively indented numbered items (each labeled "1.") to illustrate the spacing settings. The bottom of the dialog has **Help**, **Reset**, **Apply**, **OK**, and **Cancel** buttons.

The **Customize** tab is where you define what each level actually looks like. Select a level on the left (or **1 – 10** for all), then set the **Number** format, **Start at** value, **Character style**, and how many **Show sublevels** to display. The **Separator** fields let you add text before or after the number — handy for formats like "(1)" or "Section 1.2". Check **Consecutive numbering** at the bottom if you want numbering to continue across levels rather than restarting.

The "List Style: Untitled1" dialog is shown with the **Customize** tab selected. On the left is the **Level** selector listing levels 1 through 10 and "1 – 10," with level 1 highlighted in blue. In the center, under the "Numbering" heading, are fields for **Number** (a dropdown set to "1, 2, 3, …"), **Start at** (a spinner set to 1), **Character style** (a dropdown set to "None"), and **Show sublevels** (a spinner set to 1). Below those is a **Separator** section with **Before** (empty) and **After** (containing a period ".") text fields. At the bottom under "All Levels" is an unchecked **Consecutive numbering** checkbox. On the right side is a **Preview** pane displaying a multi-level numbered list where each level is progressively indented, all showing "1." as the numbering, with the first level's text block shown in black and the remaining levels in gray.

Once your list style is ready, apply it by assigning it to a paragraph style via the paragraph style's **Outline & List** tab, or by selecting text and double-clicking the list style in the Styles deck. For details on how list styles and paragraph styles interact in more advanced scenarios, see Chapter 12 of the Writer Guide.

---

## UI Reference  —  Right Sidebar

_Scope: Styles panel > List Styles category_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The LibreOffice Writer window is shown with an empty document. Along the far-right edge of the window is a narrow vertical strip containing eight small icon buttons stacked top to bottom — this is the collapsed sidebar. The topmost button is highlighted with a red rectangle and its tooltip reads "Properties (Alt+1)." The remaining seven buttons below it represent Styles, Gallery, Navigator, Page, Style Inspector, Manage Changes, and Accessibility Check, respectively. The main document area and standard toolbars (menu bar, formatting bar with font/size/style controls, and the standard toolbar) are visible to the left.

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
