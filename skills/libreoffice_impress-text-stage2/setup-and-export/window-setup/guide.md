# Window Setup (LibreOffice Impress 7.3.7)

When you first launch Impress, the main window is split into three key areas: the Slides pane on the left, the Workspace in the center, and the Sidebar on the right. The Menu bar and toolbars sit across the top. If anything feels cluttered or missing, you can toggle each panel independently until the layout works for you.

The main Impress window is divided into three columns: on the far left, the Slides pane displays numbered slide thumbnails vertically; the large central Workspace shows the currently selected slide at editing size with horizontal and vertical rulers along its edges; and the Sidebar on the right provides property panels. Above all three areas sit the Menu bar and two rows of toolbars (Standard and Drawing), and a Status bar runs along the bottom of the window.

To show or hide the Slides pane, go to **View > Slides pane** on the Menu bar — or just click the X in its top-right corner to close it. You can also drag the **Hide/Show** marker on the left edge of the Workspace to collapse it without fully closing. The same trick works for the Sidebar: toggle it with **View > Sidebar** or press **Ctrl+F5**.

The Workspace defaults to **Normal** view, which is where you'll do most of your editing. Along the top of the Workspace you'll see tabs for **Normal**, **Outline**, **Notes**, and **Slide Sorter** — click any of them to switch. If those tabs aren't visible, turn them on via **View > Views Tab Bar**. Each view brings its own toolbar set, so if a toolbar you expect is missing after switching views, head to **View > Toolbars** and check the ones you need.

A close-up of the top-left portion of the Impress window shows the view-switching tab bar immediately above the slide editing canvas, with tabs labeled Normal, Outline, Notes, and Slide Sorter. The Normal tab is currently selected and highlighted. To the left, the Slides pane header is visible with its "Slides" label and a small X button in the top-right corner for closing the pane.

To maximize your editing area, click the **Hide/Show** marker in the vertical separator between the Workspace and the Slides pane or Sidebar. This collapses the panel without closing it — click the marker again to bring it back.

If the default toolbar-based interface doesn't suit you, Impress offers several UI variants. Open **View > User Interface** to see the options: **Standard Toolbar**, **Tabbed**, **Single Toolbar**, **Sidebar**, and more. Pick one, preview it on the right side of the dialog, then click **Apply to Impress** to change just Impress, or **Apply to All** for every LibreOffice module. Hit **Close** when you're done.

The "Select Your Preferred User Interface" dialog is displayed, listing UI layout options in a left-hand column: Standard Toolbar, Single Toolbar, Sidebar, Tabbed, Tabbed Compact, and Groupedbar Compact. The currently highlighted option shows a preview thumbnail on the right side of the dialog illustrating how that layout arranges menus, toolbars, and the editing area. At the bottom of the dialog are three buttons: "Apply to Impress" (to change only Impress), "Apply to All" (to change all LibreOffice modules), and "Close."

One last tip: if you want Impress to skip the template chooser on startup, go to **Tools > Options > LibreOffice Impress > General** and deselect *Start with Template Selection* under **New Document**. That way you'll land straight in a blank presentation, ready to work.

---

## UI Reference  —  Slides Panel

_Scope: Close Pane button, Hide/Show strip for panel visibility_

The Slides panel is a resizable left-side thumbnail strip showing all slides. Click to select/navigate, right-click for a context menu, drag to reorder.

The screenshot shows the Slides panel with several slide thumbnails listed vertically, and a right-click context menu open over one of them. The context menu displays items including Cut, Copy, Paste, New Slide, Duplicate Slide, Rename Slide, Hide Slide, a Layout submenu arrow, and Slide Properties at the bottom. The panel header at the top reads "Slides" with an X close button in its corner.

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

## UI Reference  —  Standard Toolbar

_Scope: Display Views toggles and Sidebar button_

The first icon row below the menu bar. Provides quick access to common file and editing operations.

The Standard Toolbar is a single horizontal row of icon buttons stretching across the top of the window, directly beneath the Menu bar. From left to right it shows: New (with dropdown arrow), Open (with dropdown arrow), Save, Email Document, Edit File, PDF export, Print, then clipboard icons for Cut/Copy/Paste, the Paint Format (clone formatting) brush, Undo/Redo arrows, Find & Replace, Spelling, a cluster of four small Display Views toggle buttons (Normal, Outline, Notes, Slide Sorter), the Presentation (start slideshow) button, Table/Chart/Text Box insertion icons, Hyperlink, the Sidebar toggle, and finally the Start Center button at the far right.

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

_Scope: Options (Alt+F12) for Impress General settings like template chooser_

The Tools menu provides spelling, language, autocorrect, macros, forms, extensions, customisation, and application-wide options.

The Tools dropdown menu is shown fully expanded. It lists, from top to bottom: Spelling... (F7), Automatic Spell Checking (Shift+F7) with a checkmark indicating it is enabled, Thesaurus... (Ctrl+F7) appearing greyed out, Language with a submenu arrow, AutoCorrect Options..., then a separator followed by Redact, Auto-Redact, and Minimize Presentation.... After another separator come three checkbox-style items — ImageMap, Color Replacer, and Media Player — then Forms with a submenu arrow and Macros with a submenu arrow. A final group contains Development Tools, XML Filter Settings..., Extensions... (Ctrl+Alt+E), Customize..., and Options... (Alt+F12) at the very bottom.

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

_Scope: Normal/Outline/Notes/Slide Sorter modes, Slide Pane/Sidebar/Status Bar/Rulers toggles, User Interface selector, Toolbars submenu, Zoom_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

The View dropdown menu is shown fully expanded. At the top is a group of radio-button editing modes: Normal (currently selected), Outline, Notes, Slide Sorter, Master Slide, Master Notes, and Master Handout. Below a separator, a series of checkbox toggles appears: Status Bar (checked), Slide Pane (checked), Views Tab Bar, Rulers with the shortcut Shift+Ctrl+R, Comments (checked), Sidebar (Ctrl+F5, checked), Color Bar, and Navigator (Shift+Ctrl+F5). Next come submenu items: User Interface..., Toolbars with a submenu arrow, Grid and Helplines with a submenu arrow, Snap Guides with a submenu arrow, and Color/Grayscale with a submenu arrow. A sidebar-panels group follows with Slide Layout, Slide Transition, Animation, Styles (F11), and Gallery. The menu ends with a Zoom submenu arrow at the bottom.

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
