# Text Box Formatting (LibreOffice Impress 7.3.7)

Every piece of text on an Impress slide lives inside a text box, so knowing how to style them is essential — especially when you want something like a code block or a callout to stand out visually. Here's how to work with fonts, backgrounds, and borders to get the look you need.

**Creating a text box** is straightforward: click **Insert Text Box** on the Standard or Drawing toolbar, then either click the slide for a single-line box that grows as you type, or click and drag to define a fixed-width area where text wraps automatically. You can also just press *F2* to drop a horizontal text box onto the current slide.

Once you're inside a text box, the **Text Formatting** toolbar appears automatically, giving you quick access to font family, size, bold, italic, underline, and more. For finer control, select your text and go to **Format** on the Menu bar — options like **Character** and **Paragraph** open dialogs where you can set exact font properties, spacing, and alignment. You can also tweak these from the **Character** and **Paragraph** panels in the Properties deck on the Sidebar.

To give a text box a **background fill** — great for making code blocks or highlighted content pop — right-click the text box border and choose the **Area** option, or expand the **Area** panel in the Properties Sidebar. From there you can pick a solid color, gradient, hatching, or bitmap. A light gray fill with a monospace font, for instance, instantly signals "code" to your audience.

**Adding a border** makes the box's edges visible. The quickest way is via the **Line and Filling** toolbar: select the text box, then set **Line Style**, **Line Width**, and **Line Color** directly on the toolbar. If it's not visible, enable it through **View > Toolbars > Line and Filling**. For more options — like transparency or corner rounding — right-click the border, select **Line**, and use the Line dialog's full set of controls under the **Line** tab. Set the style, color, width, and pick a **Corner Style** such as "Rounded" for a softer look. For rounded corners to be clearly visible, keep the line width above about 0.35 cm.

The Line dialog is a tabbed window with the "Line" tab selected, presenting dropdown menus and fields for Style (e.g., solid, dashed), Color, Width, and Transparency arranged in the upper portion, along with a Corner Style dropdown set to "Rounded" and a separate Corner Radius field. The lower area includes Arrow Styles sections for start and end line caps, each with their own width fields, and a preview strip at the bottom showing the currently configured line appearance.

You can also manage borders from the **Line** panel in the Properties Sidebar, which exposes the same line style, width, color, and transparency settings in a more compact form.

For **precise positioning and sizing**, press *F4* or go to **Format > Object and Shape > Position and Size**. The dialog lets you enter exact coordinates, dimensions, and even lock the position or size to prevent accidental changes. Check **Fit width to text** or **Fit height to text** under the Adapt section if you want the box to resize dynamically as content changes.

When you're building something like a styled code block, the recipe is simple: create a text box, set a monospace font (via the Text Formatting toolbar), apply a subtle background color (via **Area**), add a thin border with rounded corners (via the **Line** dialog or toolbar), and adjust internal spacing through **Format > Paragraph**. Direct formatting like this overrides any applied style, so it works even on AutoLayout boxes — just keep in mind that Impress leans more on manual formatting than Writer does, since Presentation Styles are fairly restrictive and don't support character-level styling.

---

## UI Reference  —  Format Menu

_Scope: Character, Paragraph, Text Box and Shape submenus_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

The Format menu is shown fully expanded as a vertical dropdown list. At the top are text-related entries — Text, Spacing, Align Text, Lists, Clear Direct Formatting, and Styles — followed by dialog-opening items such as Character, Paragraph, Bullets and Numbering, and Theme. The middle section contains object-oriented entries including Table, Image, Text Box and Shape, a Shadow toggle checkbox, and Interaction and Name/Alt Text items. The lower portion lists spatial operations: Distribute Selection, Rotate, Flip, Convert, Align Objects, Arrange, and Group, several of which display right-arrow indicators for submenus. Keyboard shortcuts such as Ctrl+L, Ctrl+E, and Shift+Ctrl+M are shown alongside their respective items.

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

## UI Reference  —  Insert Menu

_Scope: Text Box (F2) insertion entry_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

The Insert menu is displayed as a long vertical dropdown. It begins with media-related items — Image, Audio or Video, Chart, and Table — followed by a Media submenu and OLE Object submenu. Below those are Shape, Snap Guide, and the Text Box entry (with the shortcut F2 shown to its right). Further down are Comment (Ctrl+Alt+C), Fontwork, Hyperlink (Ctrl+K), Special Character, and Formatting Mark. The bottom section contains field-insertion items: Slide Number, Field, Header and Footer, and Form Control. Many entries show right-arrow submenu indicators, and separator lines group related items visually.

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

## UI Reference  —  Standard Toolbar

_Scope: Insert Text Box button_

The first icon row below the menu bar. Provides quick access to common file and editing operations.

The Standard toolbar appears as a single horizontal row of icon buttons directly beneath the menu bar. From left to right it shows: New, Open, and Save (each with small dropdown arrows), followed by Email Document, Edit File toggle, a PDF export button, and Print. Next come the Cut, Copy, and Paste clipboard buttons, then the Paint Format (clone formatting) brush icon. Undo and Redo arrows follow, then Find & Replace and Spelling. The middle-right area contains view-mode toggle buttons (Normal, Outline, Notes, Slide Sorter) and a Presentation (slideshow) button. Toward the right end are quick-insert tools for Table, Chart, and Text Box, a Hyperlink button, the Sidebar toggle, and finally a Start Center button. The Text Box button is identifiable by its small icon depicting a text frame with a letter "A" inside it.

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
