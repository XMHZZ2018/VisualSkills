# Managing the Gallery (LibreOffice Writer 7.3.7)

The Gallery lives in the Sidebar and holds clip art, arrows, diagrams, and other reusable graphics organized into themes. You can open it by clicking the **Gallery** icon in the Sidebar, or toggle it off with the Sidebar's **Hide** button. Like other Sidebar decks, it can float as its own window if you prefer. The Gallery supports both an Icon View and a Detailed View for browsing its contents.

The Gallery panel is shown in Detailed View within the Sidebar. The upper portion lists available themes — Arrows, BPMN, Bullets, Diagrams, Flow chart, and Icons — with the "Arrows" theme currently selected and highlighted. Below the theme list, the contents of the selected theme are displayed as a scrollable list of items, each showing a small thumbnail on the left and its name on the right (e.g., "curved-right-arrow", "curved-left-arrow", "180-degree-arrow", "curved-up-arrow", and so on). At the bottom of the panel are two view-toggle buttons for Icon View and Detailed View (with Detailed View currently active), and a **New…** button on the right for creating new themes.

Graphics are grouped by themes — Arrows, BPMN, Bullets, Diagrams, Flow Chart, Icons, People, and so on. Just click a theme on the left to see its contents on the right. The default themes that ship with LibreOffice are locked; you'll know them because right-clicking only offers **Properties** in the context menu.

To create your own theme, click the **New** button below the theme list. In the **Properties of New Theme** dialog, switch to the **General** tab and give your theme a name, then head over to the **Files** tab to start adding images.

The "Properties of My Theme" dialog is shown with the **Files** tab selected (alongside the **General** tab). It contains a **File type** drop-down at the top, currently set to "<All Files>" and displaying supported formats including .bmp, .dxf, .emf, .eps, .gif, .jpg, .jpeg, and more. To the right of the drop-down is a **Find Files…** button for browsing to a directory. Below the file type selector is a large empty file list area showing "<No Files>", and to its right are **Add** and **Add All** buttons for importing individual or all found files into the theme.

Adding objects to a custom theme is straightforward. Right-click the theme name, choose **Properties**, and open the **Files** tab. Hit **Find Files** to browse for a directory, enter the path or navigate to the folder, then click **Select** to search it. A list of found files appears, and you can filter by file type using the drop-down. Click **Add All** to grab everything, or pick individual files with **Add** (hold Shift or Ctrl to multi-select). To add a single file instead, click **Add** in the Properties dialog, which opens a file browser — find the image, select it, and click **Open**.

You can also grab additional gallery themes from the LibreOffice extensions site; they install automatically once downloaded.

When it's time to clean up, right-click an image inside a theme and choose **Delete** — confirm with **Yes** and it's removed from the Gallery (though the original file on disk stays untouched). To remove an entire custom theme, right-click it in the theme list and select **Delete**. Keep in mind you can't delete the built-in themes that came with LibreOffice.

---

## UI Reference  —  Right Sidebar

_Scope: Gallery panel (Alt+3): theme browser, thumbnail grid, New button_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The screenshot shows the full LibreOffice Writer window with an empty document open. Along the right edge of the window is a narrow vertical strip of sidebar icon buttons, highlighted with a red rectangle to indicate their location. The topmost button is labeled "Properties (Alt+1)" in a tooltip. Below it are additional icons for other sidebar panels including Styles, Gallery, Navigator, and more. The main document area occupies the center, with the standard menu bar (File, Edit, View, Insert, Format, Styles, Table, Form, Tools, Window, Help) and formatting toolbars at the top, and a status bar at the bottom showing page and word count information.

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
