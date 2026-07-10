# Image Layout & Composition (LibreOffice Impress 7.3.7)

When you've got several images on a slide and need them to look intentional rather than scattered, Impress gives you a solid set of tools for alignment, grouping, rotation, and stacking.

**Aligning objects** requires at least two selected items — hold *Shift* and click each one, or drag a marquee around them. Then right-click and choose **Align Objects**, or find the same options under the **Align Objects** dropdown on the Line and Filling toolbar. You get six choices: **Left**, **Centered**, **Right** for horizontal alignment, and **Top**, **Center**, **Bottom** for vertical. You can also reach these via **View > Toolbars > Align Objects** if you want a persistent toolbar.

For precise placement, select an object and press *F4* to open the **Position and Size** dialog (also at **Format > Object and Shape > Position and Size**). The **Position** tab lets you type exact X and Y coordinates relative to a base point. Check **Keep ratio** in the **Size** section before changing width or height so your image doesn't get squished. You can also lock an object in place by ticking **Position** under the **Protect** section.

The Position and Size dialog is shown with the "Position and Size" tab active (other tabs are "Rotation" and "Slant & Corner Radius"). The Position section has Position X set to 5.50 cm and Position Y set to 3.50 cm, each with minus/plus spinner buttons, and a base-point selector grid with nine anchor points to the right. Below that, the Size section shows Width at 6.00 cm and Height at 4.50 cm with their own spinners and base-point grid, and a checked "Keep ratio" checkbox. At the bottom left, a Protect section offers unchecked "Position" and "Size" checkboxes, and on the right an Adapt section offers greyed-out "Fit width to text" and "Fit height to text" options. The dialog footer has Help, Reset, Cancel, and OK buttons.

If you'd rather stay in the sidebar, expand the **Position and Size** panel under the **Properties** deck — it has the same X/Y, width/height, rotation, flip, and arrange controls all in one place.

**Grouping** is handy when you want multiple images to move and scale as one unit. Select the objects, then go to **Format > Group > Group** (or *Ctrl+Shift+G*). Need to tweak one piece inside the group? Double-click it or press *F3* to enter the group, make your edits, then press *Ctrl+F3* to exit back out. To break the group apart entirely, use **Format > Group > Ungroup** (*Ctrl+Alt+Shift+G*).

The slide canvas shows three overlapping shapes that have been selected as a group: a light-blue filled rectangle in the upper left, a red filled ellipse in the upper right partially overlapping the rectangle, and a dark-green filled diamond (rotated square) centered below and overlapping both. Small square selection handles appear around the bounding box of the entire group, indicating that all three objects are selected together as a single grouped unit.

**Rotating** an object is quickest from the **Transformations** sub-toolbar — click the triangle next to **Transformations** on the Line and Filling toolbar, choose **Rotate**, and the selection handles turn into rotation grips. Drag a corner handle to spin the object freely; hold *Shift* while dragging to snap to 15-degree increments. You can also drag the pivot point to rotate around a different center. For an exact angle, open the **Position and Size** dialog (*F4*), switch to the **Rotation** tab, and type the degrees directly.

To **flip** an image, right-click it and choose **Flip > Vertically** or **Horizontally**, or use **Format > Flip** from the Menu bar. For more control over the flip axis, open the **Transformations** toolbar via **View > Toolbars > Transformations** and use the **Flip** tool to reposition the symmetry line before flipping.

**Arranging the stack order** matters when images overlap. Go to **Format > Arrange** and pick from **Bring to Front** (*Ctrl+Shift++*), **Bring Forward** (*Ctrl++*), **Send Backward** (*Ctrl+–*), or **Send to Back** (*Ctrl+Shift+–*). There's also **In Front of Object**, which swaps two selected objects' positions in the stack.

Finally, turn on **snap to grid** for consistent spacing — configure it under **Tools > Options > LibreOffice Impress > Grid**. Enable *Snap to grid* and set your preferred resolution. If the grid feels too rigid for a particular move, hold *Ctrl* while dragging to temporarily override snapping. For visual guidance while repositioning, enable helplines via **Tools > Options > LibreOffice Impress > View** and check *Helplines while moving*.

---

## UI Reference  —  Drawing Toolbar

_Scope: Arrange and Object alignment dropdowns_

The second icon row provides drawing tools, shape creation, and quick formatting controls for objects on the slide canvas.

The Drawing toolbar is a single horizontal row of small icons. From left to right it includes: a Select arrow, a Zoom tool, then a series of drawing and shape tools — Connector, Line, Rectangle, Ellipse, Arrow, Freeform, Bezier Curves, Diamond/Shapes, Connector Points, Flowchart, Callout, Stars, and 3D Objects — many with small dropdown triangles indicating sub-menus. Toward the right end of the bar are an Area Fill Color picker (shown as a blue square icon with a dropdown), an Insert Image button, and finally Arrange and Object Alignment dropdown buttons.

## Elements

Row (left → right):

- **Select** (arrow) — Default selection/move tool
- **Zoom** — Zoom tool for canvas
- **Connector** (dropdown ▾) — Draw connector lines between objects
- **Line** (dropdown ▾) — Draw straight lines; dropdown for arrow styles
- **Rectangle** — Draw rectangles/squares
- **Ellipse** — Draw ellipses/circles
- **Arrow** (dropdown ▾) — Block arrows; dropdown for styles
- **Freeform** (dropdown ▾) — Freeform drawing tools
- **Bezier Curves** (dropdown ▾) — Curve drawing tools
- **Diamond** / **Shapes** (dropdown ▾) — Basic shapes palette
- **Connector Points** (dropdown ▾) — Connector shape types
- **Flowchart** (dropdown ▾) — Flowchart shape palette
- **Callout** (dropdown ▾) — Callout shapes palette
- **Stars** (dropdown ▾) — Stars and banners shapes
- **3D Objects** (dropdown ▾) — 3D shape primitives
- **Area Fill Color** (dropdown ▾) — Fill colour picker (blue square icon)
- **Insert Image** — Insert an image from file
- **Arrange** (dropdown ▾) — Object stacking order
- **Object alignment** (dropdown ▾) — Align objects on slide

---

## UI Reference  —  Format Menu

_Scope: Align Objects, Arrange, Group, Flip, Distribute Selection_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

The Format menu is shown open as a dropdown from the menu bar (with Insert, Format, Slide, and Slide Show tabs visible). The menu lists items top to bottom: Text, Spacing, Align Text (currently highlighted in blue), Lists, Clear Direct Formatting, Styles, Character…, Paragraph…, Bullets and Numbering…, Theme…, Table, Image, Text Box and Shape, a Shadow checkbox, Interaction…, Name…, Alt Text…, and the list continues below the visible area with Distribute Selection partially visible at the bottom.

## Elements

- **Text** `▸` — Text layout options
- **Spacing** `▸` — Line Spacing: 1 (Ctrl+1) / 1.5 (Ctrl+5) / 2 (Ctrl+2), Increase/Decrease Paragraph Spacing, Increase/Decrease Indent
- **Align Text** `▸` — Left (Ctrl+L), Center (Ctrl+E), Right (Ctrl+R), Justified (Ctrl+J), Top, Center, Bottom
- **Lists** `▸` — List formatting options
- **Clear Direct Formatting** (Shift+Ctrl+M) — Remove manual formatting
- **Styles** `▸` — Style application submenu
- **Character...** — Opens Character formatting dialog
- **Paragraph...** — Opens Paragraph formatting dialog
- **Bullets and Numbering...** — List style configuration dialog
- **Theme...** — Presentation theme settings
- **Table** `▸` — Table formatting options
- **Image** `▸` — Image adjustment options
- **Text Box and Shape** `▸` — Text box and shape formatting
- **Shadow** (checkbox) — Toggle drop shadow on selected object
- **Interaction...** — Configure click actions on objects
- **Name...** — Name the selected object
- **Alt Text...** — Set alternative text for accessibility
- **Distribute Selection** `▸` — Distribute objects evenly
- **Rotate** — Enter rotation mode for selected object
- **Flip** `▸` — Flip horizontally or vertically
- **Convert** `▸` — Convert object types
- **Align Objects** `▸` — Align objects relative to each other or the slide
- **Arrange** `▸` — Bring forward, send backward, etc.
- **Group** `▸` — Group, ungroup, enter/exit group

---

## UI Reference  —  Tools Menu

_Scope: Options > LibreOffice Impress > Grid for snap-to-grid settings_

The Tools menu provides spelling, language, autocorrect, macros, forms, extensions, customisation, and application-wide options.

The Tools menu is shown open as a dropdown from the menu bar (with Slide Show, Tools, and Window tabs visible). The entries listed top to bottom are: Spelling…, Automatic Spell Checking (with a check mark indicating it is enabled), Thesaurus… (greyed out), Language, AutoCorrect Options…, Redact, Auto-Redact, Minimize Presentation…, ImageMap (unchecked checkbox), Color Replacer (unchecked checkbox), Media Player (unchecked checkbox), Forms, and Macros. The menu continues below the visible area where additional entries such as Development Tools, Extensions, Customize, and Options would follow.

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
