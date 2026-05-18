# Navigating Documents (LibreOffice Writer 7.3.7)

Writer gives you several handy ways to jump around a document without endless scrolling. The two main tools are **Go to Page** and the **Navigator**, and once you know them, moving through even a huge document feels effortless.

**Go to Page** is the quickest way to land on a specific page. Open it with **Edit > Go to Page**, by pressing **Ctrl+G**, or simply by clicking the page number field on the Status Bar. A small dialog pops up showing the current page and the total page count — type your target page number, hit **OK**, and you're there. You can also use the *Go to Page* field at the top right of the Navigator for the same purpose.

The Go to Page dialog is a compact window titled "Go to Page" with a single input field labeled "Page:" pre-filled with the current page number (for example, 11), followed by the total page count (for example, "of 25"). Below the input field are two buttons: **OK** (highlighted as the default action) and **Cancel**.

The **Navigator** is the real powerhouse. It lives in the Sidebar — click the **Navigator** tab on the right, press **F5**, or go to **View > Navigator** on the Menu bar. It lists every heading, table, text frame, graphic, bookmark, and other object in your document in a collapsible tree. Click the little arrow next to a category to expand it, then double-click any item to jump straight to its location.

The Navigator panel is shown docked in the Sidebar, titled "Navigator" with a close button. At the top is a "Page" drop-down for the Navigate By selection, followed by Previous/Next arrow buttons and a page number field (showing "22") with minus and plus buttons. Below that are two rows of toolbar icons for functions such as Content Navigation View, copy/paste, set reminder, insert anchors, heading level display, and drag mode. The main area displays a collapsible tree listing document object categories — Headings (currently selected and highlighted in blue), Tables, Frames, Images, OLE objects, Bookmarks, Sections, Hyperlinks, and References — each with an expand arrow and a distinctive icon.

At the top of the Navigator you'll find a *Navigate By* drop-down list where you pick what type of object you want to step through — headings, bookmarks, tables, graphics, index entries, and more. Once you've chosen a type, use the **Previous** and **Next** icons (or buttons) to hop from one instance to the next throughout the document.

If you only care about one category — say, Headings — highlight it and click the **Content Navigation View** icon. This hides everything else so you can focus. Click it again to restore the full list. You can also adjust the number of heading levels displayed.

**Setting reminders** is a lesser-known gem. Click the **Set Reminder** icon in the Navigator to drop a bookmark at the cursor's current spot. You can set up to five reminders in a document (a sixth replaces the first). To revisit them, select **Reminder** in the *Navigate By* drop-down and click **Previous** or **Next**. They aren't visible in the text and aren't saved with the document — they're purely for your current editing session.

One practical tip: objects are much easier to find if you give them meaningful names when you create them. By default, Writer names things generically (Image1, Table1, etc.). You can rename an object later by right-clicking it in the Navigator and choosing **Rename**, or via **Image > Rename** in the context menu.

---

## UI Reference  —  Right Sidebar

_Scope: Navigator panel (Alt+4/F5): document structure tree, page navigation controls_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The screenshot shows a LibreOffice Writer window with an empty document. Along the far-right edge of the window is a narrow vertical strip of eight small icon buttons, highlighted with a red rectangle. The topmost button has a tooltip reading "Properties (Alt+1)." These icons sit between the document's scrollbar and the window border, and each one opens a different sidebar panel when clicked.

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
