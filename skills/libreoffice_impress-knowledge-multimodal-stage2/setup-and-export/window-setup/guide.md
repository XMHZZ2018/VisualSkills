# Window Setup (LibreOffice Impress 7.3.7)

When you first launch Impress, the main window is split into three key areas: the Slides pane on the left, the Workspace in the center, and the Sidebar on the right. The Menu bar and toolbars sit across the top. If anything feels cluttered or missing, you can toggle each panel independently until the layout works for you.

See `fig01.png`.

To show or hide the Slides pane, go to **View > Slides pane** on the Menu bar — or just click the X in its top-right corner to close it. You can also drag the **Hide/Show** marker on the left edge of the Workspace to collapse it without fully closing. The same trick works for the Sidebar: toggle it with **View > Sidebar** or press **Ctrl+F5**.

The Workspace defaults to **Normal** view, which is where you'll do most of your editing. Along the top of the Workspace you'll see tabs for **Normal**, **Outline**, **Notes**, and **Slide Sorter** — click any of them to switch. If those tabs aren't visible, turn them on via **View > Views Tab Bar**. Each view brings its own toolbar set, so if a toolbar you expect is missing after switching views, head to **View > Toolbars** and check the ones you need.

See `fig02.png`.

To maximize your editing area, click the **Hide/Show** marker in the vertical separator between the Workspace and the Slides pane or Sidebar. This collapses the panel without closing it — click the marker again to bring it back.

If the default toolbar-based interface doesn't suit you, Impress offers several UI variants. Open **View > User Interface** to see the options: **Standard Toolbar**, **Tabbed**, **Single Toolbar**, **Sidebar**, and more. Pick one, preview it on the right side of the dialog, then click **Apply to Impress** to change just Impress, or **Apply to All** for every LibreOffice module. Hit **Close** when you're done.

See `fig03.png`.

One last tip: if you want Impress to skip the template chooser on startup, go to **Tools > Options > LibreOffice Impress > General** and deselect *Start with Template Selection* under **New Document**. That way you'll land straight in a blank presentation, ready to work.

---

## UI Reference  —  Slides Panel

_Scope: Close Pane button, Hide/Show strip for panel visibility control_

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

## UI Reference  —  Standard Toolbar

_Scope: Display Views toggles and Sidebar button_

The first icon row below the menu bar. Provides quick access to common file and editing operations.

Read the screenshot `ui-standard-toolbar.png` in this directory.

## Elements

Row (left → right):

- **New** (dropdown ▾) — Create a new document (dropdown lists all document types)
- **Open** (dropdown ▾) — Open an existing file; dropdown shows recent documents
- **Save** (dropdown ▾) — Save the current document
- **Email Document** — Send document via email
- **Edit File** — Toggle read-only / edit mode
- **PDF** — Export directly as PDF
- **Print** — Print the document
- **Cut** / **Copy** / **Paste** — Clipboard operations
- **Paint Format** (Clone Formatting) — Copy formatting to other objects
- **Undo** / **Redo** — Step through undo/redo history
- **Find & Replace** — Open Find and Replace dialog
- **Spelling** — Run the spelling checker
- **Display Views** — Normal, Outline, Notes, Slide Sorter mode toggles
- **Presentation** — Start slideshow (F5)
- **Table** / **Insert Chart** / **Insert Text Box** — Quick insertion tools
- **Hyperlink** — Insert or edit hyperlinks
- **Sidebar** — Toggle the Properties sidebar
- **Start Center** — Return to the LibreOffice Start Center

---

## UI Reference  —  Tools Menu

_Scope: Options > LibreOffice Impress > General for template chooser setting_

The Tools menu provides spelling, language, autocorrect, macros, forms, extensions, customisation, and application-wide options.

Read the screenshot `ui-tools-menu.png` in this directory.

## Elements

- **Spelling...** (F7) — Spelling & Grammar checker dialog
- **Automatic Spell Checking** (Shift+F7) ✓ — Toggle real-time underline spell checking
- **Thesaurus...** (Ctrl+F7) — Synonym lookup (greyed unless text is selected)
- **Language** `▸` — For All Text `▸` (language selection, None, Reset, More...), Hyphenation, More Dictionaries Online...
- **AutoCorrect Options...** — Dialog with 4 tabs: Replace, Exceptions, Options, Localized Options
- **Redact** — Activate redaction editing mode
- **Auto-Redact** — Apply automatic redaction rules
- **Minimize Presentation...** — Reduce file size
- **ImageMap** (checkbox) — Open/close the ImageMap editor
- **Color Replacer** (checkbox) — Open/close the Color Replacer tool
- **Media Player** (checkbox) — Open/close the Media Player panel
- **Forms** `▸` — Design Mode, Control Wizards, Control/Form Properties, Form Navigator, Activation Order, Add Field, Open in Design Mode, Automatic Control Focus
- **Macros** `▸` — Run Macro..., Edit Macros..., Organize Macros `▸`, Digital Signature..., Organize Dialogs...
- **Development Tools** (checkbox) — Open/close Development Tools panel
- **XML Filter Settings...** — XML Filter editor
- **Extensions...** (Ctrl+Alt+E) — Extension Manager
- **Customize...** — Customize dialog (tabs: Menus, Toolbars, Notebookbar, Context Menus, Keyboard, Events)
- **Options...** (Alt+F12) — Application settings tree (LibreOffice general, Load/Save, Languages, Impress-specific, Charts, Internet)

---

## UI Reference  —  View Menu

_Scope: Normal/Outline/Notes/Slide Sorter modes, Slide Pane/Sidebar/Rulers toggles, User Interface selector, Toolbars submenu, Zoom_

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

