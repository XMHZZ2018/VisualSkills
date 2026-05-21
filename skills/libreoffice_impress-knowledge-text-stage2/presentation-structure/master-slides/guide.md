# Master Slides (LibreOffice Impress 7.3.7)

A master slide is basically a template that controls the default formatting for every slide built from it — think background, colors, fonts, logos, and text layout. A single presentation can use more than one master slide, so you're not locked into a single look throughout.

You'll find all your master slides in the **Master Slides** deck on the Sidebar. It's organized into three panels: **Used in This Presentation**, **Recently Used**, and **Available for Use**. Click the expand marker next to any panel name to browse thumbnails.

The Sidebar's Master Slides deck displays three collapsible panels stacked vertically. The top panel, "Used in This Presentation," shows thumbnails of master slides currently applied in the open file. Below it, "Recently Used" lists designs you've selected before, and "Available for Use" expands to reveal a scrollable grid of all built-in master slide thumbnails — each one previewing its background, color scheme, and text layout.

To apply a master slide to your work, right-click on the one you want in the *Used in This Presentation* section of the Master Slides deck. From the context menu, pick **Apply to All Slides** or **Apply to Selected Slides** — that's really all there is to it. Select specific slides in the Slides pane first if you only want to restyle a few of them.

If the built-in designs aren't enough, you can pull in master slides from other templates. Go to **Slide > Change Slide Master** to open the Available Master Slides dialog, then click **Load**. In the Load Master Slide dialog, choose a category on the left (like **Presentations**), pick a template on the right, and hit **OK**. The new designs will appear in the **Select a Slide Design** box. Pick the one you want, and click **OK** to apply it. Check **Exchange background page** to push the change to every slide, or leave it unchecked to target only your selection.

The Available Master Slides dialog shows a "Select a Slide Design" list box at the top displaying the names of loaded master slides. Below it is an "Exchange background page" checkbox. A **Load** button opens a secondary Load Master Slide dialog that has a Categories list on the left (including entries like "Presentations") and a Templates list on the right; selecting a template and clicking OK imports its master slide designs back into the main dialog. The dialog includes OK, Cancel, and Help buttons along the bottom.

To create your own master slide from scratch, open **View > Master Slide** to enter Master View. Click **New Master** on the Master View toolbar (or right-click in the Slides pane and choose **New Master**). Add your background, logos, text formatting, and whatever else you need, then click **Rename Master** to give it a meaningful name. When you're done, click **Close Master View** on the toolbar or go to **View > Normal** to get back to your regular editing.

To tweak an existing master slide's properties, stay in Master View, select the slide, and open **Slide > Slide Properties**. The dialog has **Slide**, **Background**, and **Transparency** tabs where you can adjust the paper format, background color or image, and more.

The Slide Properties dialog is a three-tabbed window with Slide, Background, and Transparency tabs. The Slide tab contains a Paper Format section with a format dropdown (set to a value like "Screen 16:9"), width and height spinners, orientation radio buttons for Portrait and Landscape, and margin spinners for Left, Right, Top, and Bottom. The Background tab offers buttons to choose None, Color, Gradient, Image, Pattern, or Hatch, with a preview area on the right. The Transparency tab provides radio buttons for No transparency, a percentage-based Transparency spinner, or a Gradient option with controls for type, center coordinates, angle, and start/end values. Help, Reset, Cancel, and OK buttons appear at the bottom of the dialog.

One thing to watch: any changes you make in Master View affect *every* slide using that master. If you've applied direct formatting to individual slides in Normal view (say, a custom bullet color), those overrides stick — master slide changes won't clobber them. To revert an object back to the master's style, select it and use **Format > Clear Direct Formatting**.

---

## UI Reference  —  Slide Menu

_Scope: Change Slide Master, New/Delete Master, Master Background/Objects toggles, Master Elements_

The Slide menu manages slide creation, duplication, deletion, layout, master slides, visibility, and transitions.

The Slide dropdown menu displays a vertical list of commands organized into logical groups separated by dividers. At the top are New Slide (with the Ctrl+M shortcut shown), Duplicate Slide, and Insert Slide from File. A Layout submenu arrow leads to layout choices. Below that are Delete Slide, Save Background Image, and Set Background Image entries. The middle section contains Slide Properties, Change Slide Master, New Master, Delete Master, and the checkmarked Master Background and Master Objects toggles, followed by Master Elements. Further down are Show Slide, Hide Slide, Rename Slide, and Jump to Last Edited Slide (Shift+Alt+F5). Move and Navigate submenus provide reordering options. The menu ends with Summary Slide, Expand Slide (both greyed out), and Slide Transition.

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

_Scope: Background and Transparency tabs used when editing master slide properties_

A multi-tab dialog for configuring slide dimensions, background, and transparency. Opened via Slide > Slide Properties or right-click > Slide Properties on a slide thumbnail.

The Slide Properties dialog window shows three tabs along the top: Slide, Background, and Transparency. In the visible Slide tab, the Paper Format section contains a Format dropdown (e.g., "Screen 16:9"), Width and Height spinners, and Portrait/Landscape radio buttons under Orientation. A Paper tray dropdown is set to "[From printer settings]". The Margins section provides Left, Right, Top, and Bottom spinners defaulting to 0.00". A Layout Settings area includes a slide numbers dropdown and checkboxes for "Fit object to paper format" (checked) and "Background covers margins" (unchecked). Along the bottom of the dialog are Help, Reset, Cancel, and OK buttons.

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

## UI Reference  —  View Menu

_Scope: Master Slide editing mode toggle_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

The View dropdown menu begins with a group of editing mode entries shown as radio-button items: Normal (currently selected), Outline, Notes, Slide Sorter, Master Slide, Master Notes, and Master Handout. Below a separator, checkbox toggles appear for Status Bar (checked), Slide Pane (checked), Views Tab Bar, Rulers (with Shift+Ctrl+R shortcut), and Comments (checked). Further down are Sidebar (Ctrl+F5, checked), Color Bar, and Navigator (Shift+Ctrl+F5). Submenus indicated by arrows include User Interface, Toolbars, Grid and Helplines, Snap Guides, and Color/Grayscale. Near the bottom, direct sidebar panel launchers list Slide Layout, Slide Transition, Animation, Styles (F11), and Gallery. The menu ends with a Zoom submenu for controlling the view magnification.

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
