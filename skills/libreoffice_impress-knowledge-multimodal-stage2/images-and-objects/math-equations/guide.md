# Math Equations (LibreOffice Impress 7.3.7)

To drop a math formula onto a slide, head to **Insert > Object > Formula Object** on the Menu bar. This launches the built-in LibreOffice Math editor right inside Impress, letting you type markup for anything from simple fractions to complex integrals. You can also insert a formula as a general OLE object if you prefer that route.

While you're editing the formula, the Menu bar swaps in a **Math** menu with tools specific to equation creation and editing. You'll write your formula using Math's markup language — the *Math Guide* and the *Getting Started Guide* cover the full syntax if you need a deeper dive.

Pay attention to font sizing. Formulas look best when their text size roughly matches the surrounding slide content. To adjust, go to **Format > Font Size** on the Menu bar while the formula is active. If you need to change the typeface itself, use **Format > Fonts** instead.

One thing that catches people off guard: unlike in Writer, a formula in Impress is treated as a standalone object. It won't automatically align with text or other objects on the slide. You can grab it and move it around freely, just like any other shape — but you cannot resize it. The formula's dimensions are determined entirely by its content and font settings.

When you're done editing, just click anywhere outside the formula object to deselect it and return to the normal Impress editing mode. Double-click the formula again any time you need to make changes.

---

## UI Reference  —  Formula Editor (Math OLE Object)

_Scope: Entire formula editor: Command Window markup, Elements Panel categories, Format > Font Size/Fonts, preview area_

The LibreOffice Math formula editor, opened via Insert > OLE Object > Formula Object (Shift+Alt+E), embeds a mathematical formula as an OLE object on the slide.

Read the screenshot `ui-formula-editor.png` in this directory.

## Interface Zones

- **Formula Preview Area** (center) — live-rendered formula on the slide with selection handles
- **Command Window** (bottom pane) — plain-text markup editor (e.g., `a over b + sqrt{x^2 + y^2} = c`)
- **Elements Panel** (right sidebar) — category dropdown + clickable icon grid for inserting formula elements

## Elements Categories (10)

Unary/Binary Operators, Relations, Set Operations, Functions, Operators, Attributes, Brackets, Formats, Others, Examples

Key examples:
- **Functions**: sin, cos, tan, log, ln, exp, sqrt, nroot, absolute value, factorial
- **Operators**: lim, sum (Σ), product (Π), integral (∫), double/triple integrals, contour integrals
- **Brackets**: parentheses, square brackets, braces, angle brackets, ceiling/floor, matrix forms
- **Examples**: Euler's identity, Pythagorean theorem, Newton's 2nd law, E=mc², normal distribution

## Toolbar (in Math edit mode)

New (Ctrl+N), Zoom In/Out/100%/Show All, Formula Cursor toggle, Symbols... (Greek, Arabic, Special character sets)

## Key Menu Items

- Edit > Next Marker (F4) / Previous Marker (Shift+F4) — navigate placeholder arguments
- View > AutoUpdate Display — toggle live preview refresh
- Format > Text Mode — compact inline rendering
- Tools > Import Formula / Import MathML from Clipboard
- Right-click in Command Window — all element categories as submenus

---

## UI Reference  —  Insert Menu

_Scope: OLE Object > Formula Object (Shift+Alt+E)_

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

