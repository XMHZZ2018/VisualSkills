# Create Presentation (LibreOffice Impress 7.3.7)

When you first launch Impress, it greets you with the **Select a Template** dialog. If you want a blank canvas instead, just hit **Cancel** and you'll land on an empty slide in the Workspace with the Slides pane on the left. If that template dialog annoys you, turn it off for good under **Tools > Options > LibreOffice Impress > General** — uncheck *Start with Template Selection* and it won't bother you again.

See `fig01.png`.

Your first slide uses the *Title Slide* layout by default, which gives you a title and subtitle placeholder. Click the *Click to add Title* or *Click to add Text* areas and start typing — Impress drops you straight into text editing mode. To pick a different layout, open the **Properties** deck on the Sidebar and look at the **Layouts** panel, or go to **Slide > Layout** on the Menu bar for a drop-down of all available options. Layouts range from a blank slide up to six content boxes for text, images, tables, and charts.

See `fig02.png`.

To add more slides, press *Ctrl+M*, or go to **Slide > New Slide**, or just right-click in the Slides pane and choose **New Slide**. Each new slide appears right after the one you have selected. If you need a copy of an existing slide instead, right-click it and pick **Duplicate Slide**.

For content beyond text, use the placeholders in your chosen layout — click the table, chart, or image icon inside a content box and Impress opens the appropriate insertion tool. You can also add objects manually through the **Insert** menu (e.g., **Insert > Image**, **Insert > Table**, **Insert > Chart**). To place free-form text anywhere on a slide, click **Insert Text Box** on the Standard or Drawing toolbar, then click on the slide where you want it.

If you already have an outline ready in a Writer document (formatted with heading paragraph styles), you can turn it into a presentation instantly. Open the document in Writer and go to **File > Send > Outline to Presentation**. Impress creates a new presentation with each top-level heading becoming its own slide. Alternatively, use **File > Send > AutoAbstract to Presentation** to control how many outline levels and paragraphs per level get pulled in.

See `fig03.png` for the Create AutoAbstract dialog.

Once your slides are in place, switch to **Slide Sorter** view to see the big picture. Drag slides around to reorder them, right-click to delete or hide ones you don't need yet, and review whether the flow makes sense. A good habit is to run the show at least once early — hit *F5* or go to **Slide Show > Start from First Slide** — so you can spot pacing issues, missing content, or slides that feel redundant before you spend time polishing.

To tweak a slide's background, right-click it, choose **Slide Properties**, select the **Background** tab, and pick from solid colors, gradients, bitmaps, patterns, or hatches. For a consistent look across all slides, work with master slides instead — find them in the **Master Slides** deck on the Sidebar. When you're happy with the structure, add transitions via the **Slide Transition** deck on the Sidebar, and animations through the **Animation** deck. Both are optional but can give your presentation a more polished feel.

---

## UI Reference  —  File Menu

_Scope: New > Presentation, Open, Templates submenu_

The File menu provides all document lifecycle operations: creating, opening, saving, exporting, printing, and closing presentations.

Read the screenshot `ui-file-menu.png` in this directory.

## Elements

- **New** (submenu) — create a new document: Presentation (Ctrl+N), Text Document, Spreadsheet, Drawing, Formula, Database, HTML Document, Templates (Shift+Ctrl+N), and more
- **Open...** (Ctrl+O) — open an existing file via file chooser
- **Open Remote...** — open from a cloud/remote location
- **Recent Documents** (submenu) — list of recently opened documents
- **Close** — close current document (prompts to save if unsaved)
- **Wizards** / **Templates** (submenus) — document creation wizards and template management
- **Reload** — revert to last saved state
- **Versions...** — manage saved document versions
- **Save** (Ctrl+S) — save current document
- **Save As...** (Shift+Ctrl+S) — save with a new name or format
- **Save Remote...** — save to a cloud location
- **Save a Copy...** — save a copy without changing the active file path
- **Save All** — save all open documents
- **Export...** — export to non-native formats
- **Export As** (submenu) — **Export as PDF...** (opens PDF Options dialog with 6 tabs: General, Initial View, User Interface, Links, Security, Digital Signatures) or **Export Directly as PDF**
- **Send** (submenu) — email document or email as PDF
- **Preview in Web Browser** — export to HTML and open in browser
- **Print...** (Ctrl+P) — opens the Print dialog (General and LibreOffice Impress tabs)
- **Printer Settings...** — configure printer
- **Properties...** — document metadata dialog (5 tabs: General, Description, Custom Properties, Security, Font)
- **Digital Signatures** (submenu) — manage document signatures or sign a PDF
- **Exit LibreOffice** (Ctrl+Q) — quit the application

---

## UI Reference  —  Insert Menu

_Scope: Image, Table, Chart entries for populating slide content_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

Read the screenshot `ui-insert-menu.png` in this directory.

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

_Scope: New Slide (Ctrl+M), Layout submenu (16 options), Slide Properties for background_

The Slide menu manages slide creation, duplication, deletion, layout, master slides, visibility, and transitions.

Read the screenshot `ui-slide-menu.png` in this directory.

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

_Scope: Background tab for slide background color/gradient/bitmap/pattern_

A multi-tab dialog for configuring slide dimensions, background, and transparency. Opened via Slide > Slide Properties or right-click > Slide Properties on a slide thumbnail.

Read the screenshot `ui-slide-properties-dialog.png` in this directory.

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

The Slides panel is a resizable left-side thumbnail strip showing all slides. It supports selection, navigation, reordering via drag-and-drop, and a rich right-click context menu for slide management.

Read the screenshot `ui-slides-panel.png` in this directory.
Read the screenshot `ui-slide-context-menu.png` in this directory.

## Panel Controls

- **Slides header label** — non-interactive "Slides" text at the top
- **Close Pane button** (X icon, top-right) — closes the panel entirely; restore via View > Slide Pane
- **Hide/Show strip** (thin vertical strip at right edge) — click to collapse/expand; drag to resize panel width
- **Slide thumbnails** — click to select and navigate; right-click for context menu; drag to reorder
- **Slide number badge** — 1-based number shown at top-left of each thumbnail
- **Hidden slide indicator** — diagonal hatched pattern overlays hidden slides

## Right-Click Context Menu

(see screenshot `ui-slide-context-menu.png`)

### Single-slide mode (8 items)
Copy, Paste, New Slide, Duplicate Slide, Rename Slide..., Hide Slide, Layout, Slide Properties...

### Multi-slide mode (12 items — adds Cut, Delete Slide, Navigate, Move)
- **Cut** (Ctrl+X) / **Copy** (Ctrl+C) / **Paste** (Ctrl+V)
- **New Slide** — insert blank slide after current
- **Duplicate Slide** — clone the selected slide
- **Rename Slide...** — opens a dialog with a Name text field
- **Hide Slide** / **Show Slide** — toggle visibility during slideshow
- **Delete Slide** — removes immediately (no confirmation; undo with Ctrl+Z)
- **Layout** (submenu) — 16 built-in layouts: Blank, Title Only, Title Slide, Title+Content, Centered Text, and more
- **Navigate** (submenu) — context-aware: To First/Previous/Next/Last Slide
- **Move** (submenu) — context-aware: Slide Up/Down/to Start/to End
- **Slide Properties...** — opens the 3-tab Slide Properties dialog

### Empty-area context menu
Right-clicking empty space below all thumbnails shows only: Paste, New Slide

---

## UI Reference  —  View Menu

_Scope: Normal and Slide Sorter views, Views Tab Bar toggle_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

Read the screenshot `ui-view-menu.png` in this directory.

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

