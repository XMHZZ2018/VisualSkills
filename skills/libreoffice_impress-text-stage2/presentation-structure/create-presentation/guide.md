# Create Presentation (LibreOffice Impress 7.3.7)

When you first launch Impress, it greets you with the **Select a Template** dialog. If you want a blank canvas instead, just hit **Cancel** and you'll land on an empty slide in the Workspace with the Slides pane on the left. If that template dialog annoys you, turn it off for good under **Tools > Options > LibreOffice Impress > General** — uncheck *Start with Template Selection* and it won't bother you again.

The Impress workspace shows the main editing canvas in the center displaying a blank Title Slide with "Click to add Title" and "Click to add Text" placeholders. On the left, the Slides panel displays a numbered thumbnail of the current slide, and the Properties sidebar is visible on the right with the Layouts panel showing a grid of available slide layout options.

Your first slide uses the *Title Slide* layout by default, which gives you a title and subtitle placeholder. Click the *Click to add Title* or *Click to add Text* areas and start typing — Impress drops you straight into text editing mode. To pick a different layout, open the **Properties** deck on the Sidebar and look at the **Layouts** panel, or go to **Slide > Layout** on the Menu bar for a drop-down of all available options. Layouts range from a blank slide up to six content boxes for text, images, tables, and charts.

The Layouts panel in the Properties sidebar displays a grid of 16 layout thumbnails, each representing a different arrangement of title, text, and content placeholders. The currently selected layout is highlighted, and hovering over a thumbnail shows a tooltip with the layout name such as "Blank Slide," "Title Only," "Title Content," or "Title and 2 Content."

To add more slides, press *Ctrl+M*, or go to **Slide > New Slide**, or just right-click in the Slides pane and choose **New Slide**. Each new slide appears right after the one you have selected. If you need a copy of an existing slide instead, right-click it and pick **Duplicate Slide**.

For content beyond text, use the placeholders in your chosen layout — click the table, chart, or image icon inside a content box and Impress opens the appropriate insertion tool. You can also add objects manually through the **Insert** menu (e.g., **Insert > Image**, **Insert > Table**, **Insert > Chart**). To place free-form text anywhere on a slide, click **Insert Text Box** on the Standard or Drawing toolbar, then click on the slide where you want it.

If you already have an outline ready in a Writer document (formatted with heading paragraph styles), you can turn it into a presentation instantly. Open the document in Writer and go to **File > Send > Outline to Presentation**. Impress creates a new presentation with each top-level heading becoming its own slide. Alternatively, use **File > Send > AutoAbstract to Presentation** to control how many outline levels and paragraphs per level get pulled in.

The Create AutoAbstract dialog is a small modal window with two spinner controls: one labeled "Included Outline Levels" to select how many heading levels to include, and one labeled "Subpoints per Level" to control the number of paragraphs pulled in per outline level. The dialog has OK, Cancel, and Help buttons at the bottom.

Once your slides are in place, switch to **Slide Sorter** view to see the big picture. Drag slides around to reorder them, right-click to delete or hide ones you don't need yet, and review whether the flow makes sense. A good habit is to run the show at least once early — hit *F5* or go to **Slide Show > Start from First Slide** — so you can spot pacing issues, missing content, or slides that feel redundant before you spend time polishing.

To tweak a slide's background, right-click it, choose **Slide Properties**, select the **Background** tab, and pick from solid colors, gradients, bitmaps, patterns, or hatches. For a consistent look across all slides, work with master slides instead — find them in the **Master Slides** deck on the Sidebar. When you're happy with the structure, add transitions via the **Slide Transition** deck on the Sidebar, and animations through the **Animation** deck. Both are optional but can give your presentation a more polished feel.

---

## UI Reference  —  File Menu

_Scope: New > Presentation, Templates submenu_

The File menu provides all document lifecycle operations: creating, opening, saving, exporting, printing, and closing presentations.

The File menu is shown fully expanded, listing entries from top to bottom: New (with a right-arrow indicating a submenu for document types including Presentation), Open, Open Remote, Recent Documents, Close, Wizards, Templates, Reload, Versions, Save, Save As, Save Remote, Save a Copy, Save All, Export, Export As (with a submenu for PDF export), Send, Preview in Web Browser, Print, Printer Settings, Properties, Digital Signatures, and Exit LibreOffice. Keyboard shortcuts such as Ctrl+N, Ctrl+O, Ctrl+S, Ctrl+P, and Ctrl+Q are shown beside their respective entries.

## Elements

- **New** `▸` — Submenu: Text Document, Spreadsheet, Presentation (Ctrl+N), Drawing, Formula, Database, HTML Document, XML Form Document, Labels, Business Cards, Master Document, Templates (Shift+Ctrl+N)
- **Open...** (Ctrl+O) — File chooser to open an existing document
- **Open Remote...** — Connect to and open a file from a cloud location
- **Recent Documents** `▸` — Submenu of recently opened files
- **Close** — Closes the current document
- **Wizards** `▸` — Document creation wizards
- **Templates** `▸` — Template management
- **Reload** — Reverts to last saved state (greyed for unsaved documents)
- **Versions...** — Manage saved document versions
- **Save** (Ctrl+S) — Save the current document
- **Save As...** (Shift+Ctrl+S) — Save with a new name or format
- **Save Remote...** — Save to a cloud location
- **Save a Copy...** — Save a copy without changing the active file path
- **Save All** — Save all open LibreOffice documents
- **Export...** — Export in various non-native formats
- **Export As** `▸` — **Export as PDF...** (opens PDF Options dialog) or **Export Directly as PDF**
- **Send** `▸` — **Email Document...** or **Email as PDF...**
- **Preview in Web Browser** — Export to HTML and open in browser
- **Print...** (Ctrl+P) — Opens Print dialog (General + LibreOffice Impress tabs)
- **Printer Settings...** — Select and configure the printer
- **Properties...** — Document metadata (tabs: General, Description, Custom Properties, Security, Font)
- **Digital Signatures** `▸` — **Digital Signatures...** or **Sign Existing PDF...**
- **Exit LibreOffice** (Ctrl+Q) — Close all LibreOffice windows

---

## UI Reference  —  Insert Menu

_Scope: Image, Table, Chart entries for slide content population_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

The Insert menu is shown fully expanded with entries listed from top to bottom: Image, Audio or Video, Chart, Table, Media (with a submenu arrow), OLE Object (with a submenu arrow), Shape (with a submenu arrow), Snap Guide, Text Box (with shortcut F2), Comment (Ctrl+Alt+C), Fontwork, Hyperlink (Ctrl+K), Special Character, Formatting Mark (with a submenu arrow), Slide Number, Field (with a submenu arrow), Header and Footer, and Form Control (with a submenu arrow). Some entries like Special Character appear greyed out, indicating they are only available when editing a text frame.

## Elements

- **Image...** — File chooser dialog with preview and link-to-file options
- **Audio or Video...** — File chooser for media files
- **Chart...** — Inserts an editable default column chart as an embedded OLE object
- **Table...** — Opens Insert Table dialog (columns/rows spinners, default 5×2)
- **Media** `▸` — Gallery, Photo Album, Scan `▸`, Animated Image...
- **OLE Object** `▸` — Formula Object (Shift+Alt+E), QR and Barcode..., OLE Object...
- **Shape** `▸` — Shape category submenu
- **Snap Guide...** — Insert a snap guideline
- **Text Box** (F2) — Draw a text frame on the slide
- **Comment** (Ctrl+Alt+C) — Insert a yellow sticky-note comment
- **Fontwork...** — Decorative text effects gallery
- **Hyperlink...** (Ctrl+K) — Opens non-modal Hyperlink dialog with four link types: Internet, Mail, Document, New Document
- **Special Character...** — Character picker with search, font/block filters, favourites (greyed unless editing a text frame)
- **Formatting Mark** `▸` — Non-printing formatting marks
- **Slide Number** — Insert slide-number field at cursor
- **Field** `▸` — Date, time, and other field types
- **Header and Footer...** — Dialog with Slides and Notes and Handouts tabs for date/time, footer text, slide/page numbers, and "do not show on first slide" option
- **Form Control** `▸` — Form control insertion

---

## UI Reference  —  Slide Menu

_Scope: New Slide, Layout submenu (16 options), Slide Properties for background_

The Slide menu manages slide creation, duplication, deletion, layout, master slides, visibility, and transitions.

The Slide menu is shown fully expanded with entries from top to bottom: New Slide (Ctrl+M), Duplicate Slide, Insert Slide from File, Layout (with a submenu arrow leading to 16 layout options), Delete Slide, Save Background Image, Set Background Image, Slide Properties, Change Slide Master, New Master, Delete Master, Master Background (checked), Master Objects (checked), Master Elements, Show Slide, Hide Slide, Rename Slide, Jump to Last Edited Slide (Shift+Alt+F5), Move (with a submenu arrow), Navigate (with a submenu arrow), Summary Slide, Expand Slide, and Slide Transition. Several entries such as Delete Slide and Save Background Image appear greyed out depending on context.

## Elements

- **New Slide** (Ctrl+M) — Insert a blank slide after the current one
- **Duplicate Slide** — Create an identical copy of the current slide
- **Insert Slide from File...** — Import slides from another presentation
- **Layout** `▸` — 16 layout options: Blank Slide, Title Only, Title Slide, Title Content, Centered Text, Title and 2 Content, Title Content and 2 Content, Title 2 Content and Content, Title Content over Content, Title 2 Content over Content, Title 4 Content, Title 6 Content, Vertical Title Vertical Text, Vertical Title Text Chart, Title Vertical Text, Title 2 Vertical Text Clipart
- **Delete Slide** — Remove the selected slide (only available with 2+ slides)
- **Save Background Image...** — Save slide background (greyed unless custom background set)
- **Set Background Image...** — Set a background image for the slide
- **Slide Properties...** — Opens Slide Properties dialog (Slide, Background, Transparency tabs)
- **Change Slide Master...** — Change the master slide template
- **New Master** / **Delete Master** — Create or remove master slides
- **Master Background** ✓ / **Master Objects** ✓ — Toggle master background/objects visibility
- **Master Elements...** — Edit master slide elements
- **Show Slide** / **Hide Slide** — Toggle slide visibility during slideshow
- **Rename Slide...** — Rename the slide (opens dialog with name field)
- **Jump to Last Edited Slide** (Shift+Alt+F5) — Navigate to last edited slide
- **Move** `▸` — Slide to Start, Slide Up, Slide Down, Slide to End (context-sensitive)
- **Navigate** `▸` — To First/Previous/Next/Last Slide (context-sensitive)
- **Summary Slide** / **Expand Slide** — (greyed in normal conditions)
- **Slide Transition** — Opens the Slide Transition sidebar panel

---

## UI Reference  —  Slide Properties Dialog

_Scope: Background tab for slide background color/gradient/image_

A multi-tab dialog for configuring slide dimensions, background, and transparency. Opened via Slide > Slide Properties or right-click > Slide Properties on a slide thumbnail.

The Slide Properties dialog is a modal window with three tabs along the top: Slide, Background, and Transparency. The Slide tab is active, showing a Paper Format section with a format dropdown set to "Screen 16:9" and width/height spinners, an Orientation section with Landscape selected, a Margins section with Left, Right, Top, and Bottom spinners all set to 0.00", and a Layout Settings section with a slide numbering dropdown. At the bottom of the dialog are Help, Reset, Cancel, and OK buttons.

## Tabs

### Slide Tab
- **Paper Format**: Format dropdown (e.g., "Screen 16:9"), Width/Height spinners
- **Orientation**: Portrait / Landscape radio buttons
- **Paper tray**: Dropdown ([From printer settings])
- **Margins**: Left, Right, Top, Bottom spinners (default 0.00")
- **Layout Settings**: Slide numbers dropdown (1, 2, 3, ...)
- **Fit object to paper format** ✓
- **Background covers margins** (unchecked)

### Background Tab
- **None** (default) / **Color** / **Gradient** / **Image** / **Pattern** / **Hatch** buttons
- Preview area on the right

### Transparency Tab
- **No transparency** (default) / **Transparency** (50% spinner) / **Gradient** (Type, Center X/Y, Angle, Start/End value)
- Preview area on the right

Buttons: Help, Reset, Cancel, OK

---

## UI Reference  —  Slides Panel

_Scope: New Slide and Layout submenu in context menu_

The Slides panel is a resizable left-side thumbnail strip showing all slides. Click to select/navigate, right-click for a context menu, drag to reorder.

The Slides panel is shown on the left side of the Impress window with a single slide thumbnail labeled "1." A right-click context menu is open over the thumbnail, displaying entries: Copy, Paste, New Slide, Duplicate Slide, Rename Slide, Hide Slide, Layout (with a submenu arrow), and Slide Properties. The panel header reads "Slides" with a close button (X) at the top-right corner of the panel.

## Panel Controls

- **Slides header label** — Non-interactive "Slides" text at top of panel
- **Close Pane button** (X) — Closes the panel entirely; restore via View > Slide Pane
- **Hide/Show strip** — Thin vertical strip at right edge; click to collapse to ~6px, click again to restore; drag to resize panel width
- **Slide thumbnails** — Numbered thumbnails; click to select, drag to reorder; hidden slides show a diagonal hatched overlay

## Right-Click Context Menu

When only 1 slide exists:
- Copy, Paste, New Slide, Duplicate Slide, Rename Slide..., Hide Slide, Layout `▸`, Slide Properties...

With 2+ slides (additional items):
- Cut, Delete Slide, Navigate `▸`, Move `▸`

### Layout Submenu
16 layout options: Blank Slide, Title Only, Title Slide, Title Content, Centered Text, Title and 2 Content, Title Content and 2 Content, Title 2 Content and Content, Title Content over Content, Title 2 Content over Content, Title 4 Content, Title 6 Content, Vertical Title Vertical Text, Vertical Title Text Chart, Title Vertical Text, Title 2 Vertical Text Clipart

### Navigate Submenu (context-sensitive)
- First slide: To Next Slide, To Last Slide
- Last slide: To First Slide, To Previous Slide
- Middle slides: all four options

### Move Submenu (context-sensitive)
- First slide: Slide Down, Slide to End
- Last slide: Slide to Start, Slide Up
- Middle slides: all four options

---

## UI Reference  —  View Menu

_Scope: Normal and Slide Sorter views, Views Tab Bar toggle_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

The View menu is shown fully expanded, organized into sections. At the top are the editing mode entries: Normal (currently selected), Outline, Notes, Slide Sorter, Master Slide, Master Notes, and Master Handout. Below that are UI toggle entries with checkmarks indicating active state: Status Bar (checked), Slide Pane (checked), Views Tab Bar, Rulers, Comments (checked), Sidebar (checked), Color Bar, and Navigator. Further down are submenus for User Interface, Toolbars, Grid and Helplines, Snap Guides, and Color/Grayscale. The bottom section lists sidebar panel shortcuts: Slide Layout, Slide Transition, Animation, Styles (F11), Gallery, and Zoom options.

## Elements

### Editing Modes (radio buttons)
- **Normal** — Default slide editing mode with canvas, slides panel, and properties sidebar
- **Outline** — Text-only outline editor; toolbar switches to outline navigation tools
- **Notes** — Portrait layout with slide thumbnail + speaker notes area
- **Slide Sorter** — Grid of all slide thumbnails for reordering
- **Master Slide** — Edit the master slide template (title, outline levels, date/footer/number areas)
- **Master Notes** / **Master Handout** — Edit notes/handout master layouts

### UI Toggles (checkboxes)
- **Status Bar** ✓ — Toggle the bottom status bar
- **Slide Pane** ✓ — Toggle the left slide thumbnail panel
- **Views Tab Bar** — Tab bar with Normal/Outline/Notes/Slide Sorter tabs
- **Rulers** (Shift+Ctrl+R) — Horizontal and vertical rulers along the canvas
- **Comments** ✓ — Show/hide comment annotations
- **Sidebar** (Ctrl+F5) ✓ — Properties sidebar on the right
- **Color Bar** — Colour swatch bar at the bottom
- **Navigator** (Shift+Ctrl+F5) — Floating navigation panel

### Submenus
- **User Interface...** — UI mode selector
- **Toolbars** `▸` — Checklist of 30+ toolbars; enabled by default: Drawing, Presentation, Standard
- **Grid and Helplines** `▸` — Grid and guideline display options
- **Snap Guides** `▸` — Snap guide settings
- **Color/Grayscale** `▸` — Switch between Color, Grayscale, Black & White display

### Sidebar Panels
- **Slide Layout** / **Slide Transition** / **Animation** — Open the corresponding sidebar panel directly
- **Styles** (F11) — Opens the Styles panel
- **Gallery** — Opens the Gallery panel

### Zoom
- **Zoom** `▸` — Entire Page, Page Width, Optimal View, 50%–200%, Zoom & Pan, custom Zoom dialog
