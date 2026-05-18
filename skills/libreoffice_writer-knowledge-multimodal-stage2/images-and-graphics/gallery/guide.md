# Managing the Gallery (LibreOffice Writer 7.3.7)

The Gallery lives in the Sidebar and holds clip art, arrows, diagrams, and other reusable graphics organized into themes. You can open it by clicking the **Gallery** icon in the Sidebar, or toggle it off with the Sidebar's **Hide** button. Like other Sidebar decks, it can float as its own window if you prefer. The Gallery supports both an Icon View and a Detailed View for browsing its contents.

See `fig01.png`.

Graphics are grouped by themes — Arrows, BPMN, Bullets, Diagrams, Flow Chart, Icons, People, and so on. Just click a theme on the left to see its contents on the right. The default themes that ship with LibreOffice are locked; you'll know them because right-clicking only offers **Properties** in the context menu.

To create your own theme, click the **New** button below the theme list. In the **Properties of New Theme** dialog, switch to the **General** tab and give your theme a name, then head over to the **Files** tab to start adding images.

See `fig02.png`.

Adding objects to a custom theme is straightforward. Right-click the theme name, choose **Properties**, and open the **Files** tab. Hit **Find Files** to browse for a directory, enter the path or navigate to the folder, then click **Select** to search it. A list of found files appears, and you can filter by file type using the drop-down. Click **Add All** to grab everything, or pick individual files with **Add** (hold Shift or Ctrl to multi-select). To add a single file instead, click **Add** in the Properties dialog, which opens a file browser — find the image, select it, and click **Open**.

You can also grab additional gallery themes from the LibreOffice extensions site; they install automatically once downloaded.

When it's time to clean up, right-click an image inside a theme and choose **Delete** — confirm with **Yes** and it's removed from the Gallery (though the original file on disk stays untouched). To remove an entire custom theme, right-click it in the theme list and select **Delete**. Keep in mind you can't delete the built-in themes that came with LibreOffice.

---

## UI Reference  —  Right Sidebar

_Scope: Gallery panel (Alt+3): theme browser, thumbnail grid, New button_

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

