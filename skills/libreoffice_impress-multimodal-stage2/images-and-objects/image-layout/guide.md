# Image Layout & Composition (LibreOffice Impress 7.3.7)

When you've got several images on a slide and need them to look intentional rather than scattered, Impress gives you a solid set of tools for alignment, grouping, rotation, and stacking.

**Aligning objects** requires at least two selected items — hold *Shift* and click each one, or drag a marquee around them. Then right-click and choose **Align Objects**, or find the same options under the **Align Objects** dropdown on the Line and Filling toolbar. You get six choices: **Left**, **Centered**, **Right** for horizontal alignment, and **Top**, **Center**, **Bottom** for vertical. You can also reach these via **View > Toolbars > Align Objects** if you want a persistent toolbar.

For precise placement, select an object and press *F4* to open the **Position and Size** dialog (also at **Format > Object and Shape > Position and Size**). The **Position** tab lets you type exact X and Y coordinates relative to a base point. Check **Keep ratio** in the **Size** section before changing width or height so your image doesn't get squished. You can also lock an object in place by ticking **Position** under the **Protect** section.

See `fig01.png`.

If you'd rather stay in the sidebar, expand the **Position and Size** panel under the **Properties** deck — it has the same X/Y, width/height, rotation, flip, and arrange controls all in one place.

**Grouping** is handy when you want multiple images to move and scale as one unit. Select the objects, then go to **Format > Group > Group** (or *Ctrl+Shift+G*). Need to tweak one piece inside the group? Double-click it or press *F3* to enter the group, make your edits, then press *Ctrl+F3* to exit back out. To break the group apart entirely, use **Format > Group > Ungroup** (*Ctrl+Alt+Shift+G*).

See `fig02.png`.

**Rotating** an object is quickest from the **Transformations** sub-toolbar — click the triangle next to **Transformations** on the Line and Filling toolbar, choose **Rotate**, and the selection handles turn into rotation grips. Drag a corner handle to spin the object freely; hold *Shift* while dragging to snap to 15-degree increments. You can also drag the pivot point to rotate around a different center. For an exact angle, open the **Position and Size** dialog (*F4*), switch to the **Rotation** tab, and type the degrees directly.

To **flip** an image, right-click it and choose **Flip > Vertically** or **Horizontally**, or use **Format > Flip** from the Menu bar. For more control over the flip axis, open the **Transformations** toolbar via **View > Toolbars > Transformations** and use the **Flip** tool to reposition the symmetry line before flipping.

**Arranging the stack order** matters when images overlap. Go to **Format > Arrange** and pick from **Bring to Front** (*Ctrl+Shift++*), **Bring Forward** (*Ctrl++*), **Send Backward** (*Ctrl+–*), or **Send to Back** (*Ctrl+Shift+–*). There's also **In Front of Object**, which swaps two selected objects' positions in the stack.

Finally, turn on **snap to grid** for consistent spacing — configure it under **Tools > Options > LibreOffice Impress > Grid**. Enable *Snap to grid* and set your preferred resolution. If the grid feels too rigid for a particular move, hold *Ctrl* while dragging to temporarily override snapping. For visual guidance while repositioning, enable helplines via **Tools > Options > LibreOffice Impress > View** and check *Helplines while moving*.

---

## UI Reference  —  Align and Distribute

_Scope: All 6 Align Objects commands (Left/Centered/Right/Top/Center/Bottom) and slide-reference toggle_

LibreOffice Impress provides alignment and distribution via two Format menu submenus, mirrored in the right-click context menu, and as optional floating toolbars.

Read the screenshot `ui-align-objects-submenu.png` in this directory.

## Align Objects (6 commands)

Available via Format > Align Objects, right-click > Align Objects, or the Align Objects floating toolbar (View > Toolbars > Align Objects):

- **Left** — align left edges
- **Centered** — center horizontally
- **Right** — align right edges
- **Top** — align top edges
- **Center** — center vertically
- **Bottom** — align bottom edges

The Align Objects toolbar includes a **Slide reference toggle** — when active, objects align relative to the slide boundaries instead of relative to each other.

## Distribute Selection (8 commands)

Available via Format > Distribute Selection or right-click > Distribute Selection. Requires 3+ selected objects.

- **Horizontally**: Left, Center, Spacing, Right — equalise horizontal spacing by edges, centers, or gaps
- **Vertically**: Top, Center, Spacing, Bottom — equalise vertical spacing by edges, centers, or gaps

An optional Distribute Selection floating toolbar is available via View > Toolbars > Distribute Selection.

---

## UI Reference  —  Format Menu

_Scope: Align Objects, Arrange, Group, Flip, Distribute Selection submenus_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

Read the screenshot `ui-format-menu.png` in this directory.

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

## UI Reference  —  Group and Ungroup Objects

_Scope: Group/Ungroup/Enter Group/Exit Group operations and shortcuts (Ctrl+Shift+G, F3, Ctrl+F3)_

Combines multiple drawing objects into a single logical unit that can be moved, resized, and transformed together. Supports entering group editing mode to modify individual members without ungrouping.

Read the screenshot `ui-group-menu.png` in this directory.

## Operations

| Action | Menu Path | Shortcut | Condition |
|---|---|---|---|
| **Group** | Format > Group > Group | Shift+Ctrl+G | 2+ drawing objects selected |
| **Ungroup** | Format > Group > Ungroup | Shift+Ctrl+Alt+G | Grouped object selected |
| **Enter Group** | Format > Group > Enter Group | F3 (or double-click) | Grouped object selected |
| **Exit Group** | Format > Group > Exit Group | Ctrl+F3 | Inside group editing mode |

All four are also available in the right-click context menu when applicable.

## Workflow States

1. **Multiple objects selected** — status bar shows "2 Shapes selected"; Group is available
2. **Group selected** — status bar shows "Group object selected"; Enter Group and Ungroup available; can move/resize/rotate the group as a whole
3. **Inside group editing** — selected member shows handles, other members appear dimmed; Exit Group available

## Constraints

- **Text placeholder frames** (title, content) cannot be grouped with drawing objects — produces error: "This function cannot be run with the selected objects."
- Minimum 2 objects required for grouping
- Escape inside group editing mode deselects the current member but does NOT exit group mode — use Ctrl+F3 or right-click > Exit Group

---

## UI Reference  —  Position and Size Dialog

_Scope: Position X/Y, Width/Height, Keep ratio, Protect Position, Rotation tab for precise angle_

A 3-tab modal dialog (opened via **F4** or Format > Text Box and Shape > Position and Size) providing precise numeric control over a selected object's position, size, rotation, slant, and corner radius.

Read the screenshot `ui-position-size-dialog.png` in this directory.

## Tab 1: Position and Size

- **Position X / Y** — coordinates in inches, with base point selector (3x3 grid of 9 anchor points)
- **Width / Height** — object dimensions with +/- spinners; Height greyed for text frames with "Fit height to text" enabled
- **Keep ratio** — maintain aspect ratio when resizing (greyed for text frames)
- **Size Base Point** — 3x3 grid controlling which anchor the object grows/shrinks from
- **Protect Position** — locks X/Y (auto-checks Protect Size and greys all fields)
- **Protect Size** — locks Width/Height independently
- **Fit width to text** / **Fit height to text** — auto-size to text content (text frames only; greyed for shapes)

## Tab 2: Rotation

- **Pivot Point X / Y** — rotation center coordinates with 3x3 snap selector
- **Rotation Angle** — degrees (0-360), positive = counter-clockwise
- **Rotation Dial** — interactive circular control linked to the angle field

## Tab 3: Slant & Corner Radius

- **Corner Radius** — rounding for rectangle corners (greyed for standard shapes)
- **Slant Angle** — horizontal shear in degrees
- **Control Point 1 / 2** — bezier control points (greyed for non-bezier shapes)

## Access

- **F4** key with an object selected
- Format > Text Box and Shape > Position and Size...
- Right-click on object > Position and Size...

---

## UI Reference  —  Tools Menu

_Scope: Options > LibreOffice Impress > Grid for snap-to-grid settings_

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

