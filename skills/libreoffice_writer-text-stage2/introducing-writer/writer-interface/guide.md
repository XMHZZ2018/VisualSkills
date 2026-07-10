# Writer Interface Overview (LibreOffice Writer 7.3.7)

When you first open Writer, the main window lays out everything you need in a familiar arrangement: the **Title bar** sits at the very top showing your document's filename (or "Untitled X" if you haven't saved yet), followed by the **Menu bar**, then one or more **toolbars**, your document workspace in the center, the **Sidebar** on the right, and the **Status bar** along the bottom.

The main Writer window shows "Untitled 2 – LibreOffice Writer" in the Title bar at the top, with the Menu bar (File, Edit, View, Insert, Format, Styles, Table, Form, Tools, Window, Help) directly below it. Beneath the Menu bar are two rows of toolbars: the Standard toolbar with common action icons and the Formatting toolbar with a paragraph style dropdown, font name and size selectors, and buttons for bold, italic, underline, strikethrough, superscript, subscript, font color, alignment, and list controls. The document editing area occupies the center with a horizontal ruler above it, and the Properties deck of the Sidebar is open on the right showing Style, Character, and Paragraph panels. The Status bar runs along the bottom, displaying "Page 1 of 1", "0 words, 0 characters", "Default Page Style", "English (USA)", and zoom controls at the far right set to 90%.

The **Menu bar** is your gateway to nearly every command. Entries like **Close** and **Save** in the **File** menu act immediately, while items followed by three dots (like **Find…** in the **Edit** menu) open dialogs. A right-pointing arrow — as you'll see next to **Toolbars** and **Zoom** in the **View** menu — means there's a submenu waiting.

Right below the Menu bar you'll find the **Standard toolbar**, and beneath that the **Formatting toolbar**. The Formatting toolbar is context-sensitive: when your cursor is in text it shows font and paragraph controls, but select an image and it switches to graphic-related tools. If you'd rather consolidate things, **View > User Interface > Single Toolbar** merges them into one row. To toggle any toolbar on or off, go to **View > Toolbars** and check or uncheck its name.

The **Sidebar** normally lives on the right side of the window. If it's not visible, turn it on with **View > Sidebar**. It organizes its tools into decks — **Properties**, **Page**, **Styles**, **Gallery**, **Navigator**, and **Style Inspector** — each accessible by clicking its icon on the Tab bar. The Properties deck is probably where you'll spend the most time: its Character and Paragraph panels let you format text without hunting through menus, and some panels include a **More Options** button that opens the full dialog for deeper control. You can resize the Sidebar by dragging its left edge, collapse it to just its Tab bar, or undock it entirely via the **Sidebar Settings** drop-down.

The Sidebar's Properties deck is shown in detail with annotated labels pointing to its key components. At the top is the Title bar reading "Properties" with a close button and a Sidebar Settings menu icon. Below it, the Style panel contains a "Text Body" paragraph style dropdown with Clone Formatting and style-management buttons. The Character panel follows, with a font family dropdown ("Liberation Sans"), font size selector ("11 pt"), and buttons for Bold, Italic, Underline, Strikethrough, Shadow, Font Color, Highlighting, Change Case, Superscript, and Subscript. The Paragraph panel is next, offering alignment buttons (left, center, right, justified), list and indent controls, and numeric Spacing (above/below) and Indent (before text, after text, first line) fields in centimeters. A "More Options" button is circled at the top-right corner of the Paragraph panel header, indicating it opens the full Paragraph dialog. On the left edge a Hide/show button is circled, which collapses or expands the sidebar. The vertical Tab bar on the right side shows icons for each deck (Properties, Styles, Gallery, Navigator, Page, Style Inspector, and more).

Toolbars can be moved around freely. Docked toolbars show a small handle on their left edge — grab that handle and drag to undock the toolbar into a floating palette, or dock it to a different edge of the window. To lock a toolbar in place so it doesn't shift around, right-click it and select **Lock Toolbar Position**. You can also right-click any toolbar, choose **Visible Buttons**, and toggle individual icons on or off to tailor things to your workflow.

The horizontal **ruler** runs across the top of the workspace and is handy for adjusting margins and indents at a glance. The vertical ruler is hidden by default; bring it up via **View > Rulers > Vertical Ruler**, or press *Ctrl+Shift+R* to toggle both rulers at once.

The **Status bar** at the bottom packs a surprising amount of information into a single strip. On the left you'll see the document-changed indicator (click to save), the current page number (left-click to open **Go to Page**, right-click to jump to a bookmark), and a live word and character count. Further right you'll find the current **Page Style** (right-click to switch styles), the document **Language** (click to change it or choose **None** to skip spell-checking), and the **Insert/Overwrite** mode toggle. The far-right end holds the **View Layout** buttons and a **Zoom** slider for quick magnification changes.

The right-hand portion of the Status bar is shown close-up with labeled annotations pointing to each element from left to right: the Insert mode indicator (showing "Insert"), the Selection mode toggle, the Digital signature icon, Object info (displaying "Numbering 1 : Level 1"), the View layout buttons (three small icons for Single Page, Multiple Pages, and Book view), the Zoom slider (a horizontal track with minus and plus buttons at either end), and the Zoom factor percentage (showing "120%").

---

## UI Reference  —  Right Sidebar

_Scope: Properties panel (Alt+1): Style/Character/Paragraph sections; sidebar icon strip overview_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The Writer window is shown with an empty document and the sidebar collapsed to its narrow Tab bar along the right edge. A red rectangle highlights the topmost icon button on the Tab bar, and a tooltip reading "Properties (Alt+1)" is visible next to it. Below that icon, the remaining sidebar deck icons are arranged vertically: Styles, Gallery, Navigator, Page, Style Inspector, Manage Changes, and Accessibility Check. The main window behind it shows the Menu bar, Standard and Formatting toolbars, horizontal ruler, and the Status bar at the bottom displaying "Page 1 of 1", "0 words, 0 characters", "Default Page Style", and "English (USA)" with zoom at 100%.

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
