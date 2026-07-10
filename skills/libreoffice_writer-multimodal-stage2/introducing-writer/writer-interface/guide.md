# Writer Interface Overview (LibreOffice Writer 7.3.7)

When you first open Writer, the main window lays out everything you need in a familiar arrangement: the **Title bar** sits at the very top showing your document's filename (or "Untitled X" if you haven't saved yet), followed by the **Menu bar**, then one or more **toolbars**, your document workspace in the center, the **Sidebar** on the right, and the **Status bar** along the bottom.

See `fig01.png`.

The **Menu bar** is your gateway to nearly every command. Entries like **Close** and **Save** in the **File** menu act immediately, while items followed by three dots (like **Find…** in the **Edit** menu) open dialogs. A right-pointing arrow — as you'll see next to **Toolbars** and **Zoom** in the **View** menu — means there's a submenu waiting.

Right below the Menu bar you'll find the **Standard toolbar**, and beneath that the **Formatting toolbar**. The Formatting toolbar is context-sensitive: when your cursor is in text it shows font and paragraph controls, but select an image and it switches to graphic-related tools. If you'd rather consolidate things, **View > User Interface > Single Toolbar** merges them into one row. To toggle any toolbar on or off, go to **View > Toolbars** and check or uncheck its name.

The **Sidebar** normally lives on the right side of the window. If it's not visible, turn it on with **View > Sidebar**. It organizes its tools into decks — **Properties**, **Page**, **Styles**, **Gallery**, **Navigator**, and **Style Inspector** — each accessible by clicking its icon on the Tab bar. The Properties deck is probably where you'll spend the most time: its Character and Paragraph panels let you format text without hunting through menus, and some panels include a **More Options** button that opens the full dialog for deeper control. You can resize the Sidebar by dragging its left edge, collapse it to just its Tab bar, or undock it entirely via the **Sidebar Settings** drop-down.

See `fig02.png`.

Toolbars can be moved around freely. Docked toolbars show a small handle on their left edge — grab that handle and drag to undock the toolbar into a floating palette, or dock it to a different edge of the window. To lock a toolbar in place so it doesn't shift around, right-click it and select **Lock Toolbar Position**. You can also right-click any toolbar, choose **Visible Buttons**, and toggle individual icons on or off to tailor things to your workflow.

The horizontal **ruler** runs across the top of the workspace and is handy for adjusting margins and indents at a glance. The vertical ruler is hidden by default; bring it up via **View > Rulers > Vertical Ruler**, or press *Ctrl+Shift+R* to toggle both rulers at once.

The **Status bar** at the bottom packs a surprising amount of information into a single strip. On the left you'll see the document-changed indicator (click to save), the current page number (left-click to open **Go to Page**, right-click to jump to a bookmark), and a live word and character count. Further right you'll find the current **Page Style** (right-click to switch styles), the document **Language** (click to change it or choose **None** to skip spell-checking), and the **Insert/Overwrite** mode toggle. The far-right end holds the **View Layout** buttons and a **Zoom** slider for quick magnification changes.

See `fig03.png`.

---

## UI Reference  —  Document Canvas, Rulers & Scrollbars

_Scope: Canvas area, horizontal/vertical rulers, scrollbars as parts of the Writer window_

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

## UI Reference  —  Formatting Toolbar

_Scope: Formatting toolbar as second toolbar row below Standard toolbar_

The second toolbar row provides all character and paragraph formatting controls with split-button dropdowns.

Read the screenshot `ui-formatting-toolbar.png` in this directory.

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

_Scope: Sidebar overview: 8 panel buttons, Properties deck (Style/Character/Paragraph sections)_

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

## UI Reference  —  Edit, View, Window & Help Menus

_Scope: View: Toolbars submenu, Sidebar (Ctrl+F5), Rulers, Status Bar toggles_

These menus provide standard editing operations, display controls, window management, and help access.

## Edit Menu

(see screenshot `ui-edit-menu.png`)

- **Undo** (Ctrl+Z) / **Redo** (Ctrl+Y) / **Repeat** (Shift+Ctrl+Y)
- **Cut** (Ctrl+X) / **Copy** (Ctrl+C) / **Paste** (Ctrl+V) — standard clipboard operations.
- **Paste Special** (►) — Paste Unformatted Text (Shift+Ctrl+Alt+V), Paste Special… (Shift+Ctrl+V), Paste as Nested Table, Paste as Rows Above, Paste as Columns Before.
- **Select All** (Ctrl+A)
- **Selection Mode** (►) — Standard (default) or Block Area (Shift+Alt+F8) for column selection.
- **Find…** (Ctrl+F) — Opens the inline Find toolbar.
- **Find and Replace…** (Ctrl+H) — Opens the Find and Replace dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Go to Page…** (Ctrl+G) — Jump to a specific page number.
- **Track Changes** (►) — Record, Show, Manage, Accept/Reject individual or all changes, Compare/Merge documents.
- **Comment** (►) — Reply, Resolve, Delete comments and comment threads.
- **Reference** (►) — Insert Footnote/Endnote, Index Entry, Bibliography Entry.
- **Fields…** / **External Links…** / **OLE Object** (►) — Context-sensitive editing commands.
- **Exchange Database…** — Switch the document's database source.
- **Direct Cursor Mode** — Toggle: click anywhere on the page to place the cursor.
- **Edit Mode** (Shift+Ctrl+M) — Toggle between edit and read-only mode.

## View Menu

(see screenshot `ui-view-menu.png`)

- **Normal** / **Web** — Radio pair for print-layout vs web-layout editing view.
- **User Interface…** — Choose from 7 UI variants (Standard Toolbar, Tabbed, Single Toolbar, Sidebar, etc.).
- **Toolbars** (►) — Toggle ~27 available toolbars on/off. Includes Customize… and Lock Toolbars.
- **Status Bar** — Toggle status bar visibility.
- **Rulers** (►) — Toggle horizontal ruler (Shift+Ctrl+R) and vertical ruler.
- **Scrollbars** (►) — Toggle horizontal and vertical scrollbars.
- **Grid and Helplines** (►) — Display Grid, Snap to Grid, Helplines While Moving.
- **Formatting Marks** (Ctrl+F10) — Show/hide paragraph marks, spaces, tabs.
- **Text/Table/Section Boundaries**, **Images and Charts**, **Whitespace** — Visibility toggles (all on by default).
- **Show Tracked Changes** — Toggle track-change markup display.
- **Field Shadings** (Ctrl+F8) / **Field Names** (Ctrl+F9) / **Field Hidden Paragraphs** — Field display options.
- **Sidebar** (Ctrl+F5) — Toggle the right sidebar panel.
- **Styles** (F11) / **Gallery** — Quick access to sidebar panels.
- **Navigator** (F5) — Toggle the document structure navigator.
- **Data Sources** (Shift+Ctrl+F4) — Toggle the database data-source view.
- **Full Screen** (Shift+Ctrl+J) — Hide menus/toolbars for maximum editing area.
- **Zoom** (►) — Presets (Entire Page, Page Width, 50%–200%) and full Zoom & View Layout dialog.

## Window Menu

- **New Window** — Open a second window for the same document.
- **Close Window** (Ctrl+W) — Close the current window.
- Active document list — bullet marks the current window.

## Help Menu

- **LibreOffice Help** (F1), **What's This?**, **User Guides**
- **Show Tip of the Day**, **Search Commands** (Shift+Escape)
- **Get Help Online**, **Send Feedback**, **Restart in Safe Mode…**
- **Get Involved**, **Donate to LibreOffice**, **License Information**, **About LibreOffice**

---

## UI Reference  —  Standard Toolbar

_Scope: Standard toolbar as first toolbar row: overview of all icon buttons and separators_

The first toolbar row below the menu bar provides quick access to file operations, clipboard, editing, and insert commands.

Read the screenshot `ui-standard-toolbar.png` in this directory.

## Elements

Row (left → right):

- **New** (Ctrl+N, split-button ▼) — New document; dropdown lists all document types.
- **Open** (Ctrl+O) — Open file dialog.
- **Save** (Ctrl+S, split-button ▼) — Save; dropdown: Save As…, Export…, Save a Copy…, Save as Template…, Save Remote File…
- **Export Directly as PDF** — One-click PDF export.
- **Print** (Ctrl+P) — Print dialog.
- **Toggle Print Preview** (Shift+Ctrl+O)

| *(separator)* |

- **Cut** (Ctrl+X) / **Copy** (Ctrl+C) / **Paste** (Ctrl+V, split-button ▼)
- **Clone Formatting** — Paint-format brush; double-click for persistent mode.

| *(separator)* |

- **Undo** (Ctrl+Z, split-button ▼) / **Redo** (Ctrl+Y)

| *(separator)* |

- **Find and Replace** (Ctrl+H) — Opens Find & Replace dialog.
- **Check Spelling** (F7)
- **Toggle Formatting Marks** (Ctrl+F10) — Show/hide ¶ marks, spaces, tabs.

| *(separator)* |

- **Insert Table** (Ctrl+F12, split-button ▼) — Dialog or visual grid picker for row×column count.
- **Insert Image** — File picker for images.
- **Insert Chart** — Embed chart OLE object.
- **Insert Text Box** — Draw a text frame on canvas.
- **Insert Page Break** (Ctrl+Return)
- **Insert Field** (split-button ▼) — Page Number, Page Count, Date/Time, Title, Author, Subject, More Fields…
- **Insert Special Characters** (split-button ▼) — Full character picker or favorites quick-pick.

| *(separator)* |

- **Insert Hyperlink** (Ctrl+K) — Hyperlink dialog.
- **Insert Footnote** / **Insert Endnote**
- **Insert Bookmark** — Bookmark dialog.
- **Insert Cross-reference** — Cross-reference dialog.
- **Insert Comment** (Ctrl+Alt+C)
- **Show Track Changes Functions** — Toggle Track Changes toolbar.

| *(separator)* |

- **Insert Line** — Line-drawing mode; double-click for persistent mode.
- **Basic Shapes** (split-button ▼) — 4×6 shape palette.
- **Show Draw Functions** — Toggle Drawing toolbar.

---

## UI Reference  —  Status Bar

_Scope: Status bar overview: all segments (page number, word count, page style, language, zoom)_

The status bar runs across the bottom of the window. Every segment is interactive.

Read the screenshot `ui-status-bar.png` in this directory.

## Segments (left to right)

- **Page Number** ("Page 1 of 1") — Left-click opens Go to Page dialog (page number spinner). Right-click shows bookmark list.

- **Word / Character Count** ("0 words, 0 characters") — Left-click opens Word Count dialog showing Words, Characters (incl/excl spaces), Comments for both selection and whole document.

- **Page Style** ("Default Page Style") — Left-click opens the Page Style dialog (9 tabs: Organizer, Page, Area, Transparency, Header, Footer, Borders, Columns, Footnote). Right-click shows quick-change list of all page styles: Default Page Style, First Page, Left Page, Right Page, Envelope, Index, HTML, Footnote, Endnote, Landscape.

- **Language** ("English (USA)") — Click opens language popup: current language (checked), None (no spell-check), Reset to Default Language, More…, Set Language for Paragraph (►).

- **Selection Mode** — Click opens radio-button popup: Standard selection, Extending selection, Adding selection, Block selection.

- **View Layout buttons** — Three icons:
  - Single-page view (one page at a time)
  - Multiple-page view (pages side by side)
  - Book view (two-page spread)

- **Zoom controls** — Zoom Out (−) button, drag slider, Zoom In (+) button.

- **Zoom Percentage** ("100%") — Left-click opens Zoom & View Layout dialog (Optimal, Fit width and height, Fit width, 100%, Custom; View Layout: Automatic, Single page, Columns, Book mode). Right-click shows quick-pick presets: Entire Page, Page Width, Optimal View, 50%–200%.

