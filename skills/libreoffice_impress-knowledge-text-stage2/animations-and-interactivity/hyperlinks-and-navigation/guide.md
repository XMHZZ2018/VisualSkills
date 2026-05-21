# Hyperlinks & Navigation (LibreOffice Impress 7.3.7)

Impress lets you wire up hyperlinks and interactive buttons so your audience can jump between slides, open web pages, or trigger actions with a click. Here's how it all works.

To insert a hyperlink, open the slide you want it on, then go to **Insert > Hyperlinks** (or just press **Ctrl+K**). The Hyperlink dialog pops up with four link types on the left: **Internet**, **Mail**, **Document**, and **New Document**. Pick the one that fits your need. For web links, choose **Internet**, set the protocol to Web or FTP, and fill in the **URL** and **Text** fields. For email, switch to **Mail** and enter the **Recipient** and **Subject**.

The Hyperlink dialog is a non-modal window with an icon bar on the left listing the four link types (Internet, Mail, Document, New Document). The main area on the right changes depending on the selected type; for Internet it shows a protocol dropdown (Web/FTP), a URL text field, and a Text field for the visible link label. At the bottom is a "Further Settings" section with a Form dropdown (letting you choose Text or Button), and the dialog has Apply, Close, and Help buttons along its lower edge.

The **Document** type is especially useful for slide-to-slide navigation within the same presentation. Leave the *Path* field blank (since you're staying in the same file), then click the **Target in Document** button to pick the exact slide you want to jump to. You can also just type the slide name directly into the *Target* field. Once everything looks right, hit **Apply** to drop the hyperlink onto your slide, then **Close** or **OK** to dismiss the dialog.

Down in the **Further Settings** area, the *Form* dropdown lets you present the link as plain text or as a button — handy if you want a visible clickable element rather than underlined text. The *Text* field controls what the user actually sees on the slide.

After a hyperlink lands on your slide, you'll want to reposition or resize it. Drag across the text to select it (don't click it directly or you'll activate the link). Once selected, right-click for formatting options, or drag the border to move it. For precise placement, use **Position and Size** from the context menu (or press **F4**).

If you'd rather have an object act as a navigation button — say a shape or image — Impress has a feature called Interactions. Switch to **View > Normal**, select any object on your slide, then right-click and choose **Interaction** (or go to **Format > Interaction**). In the Interaction dialog, set the *Action at mouse click* dropdown to something like "Go to page or object," then pick your target slide from the list. Click **OK** and you're done — during the slideshow, clicking that object jumps straight to the chosen slide.

The Interaction dialog is a compact window titled "Interaction" with a single dropdown labeled "Action at mouse click." This dropdown lists available click actions such as "No action," "Go to previous slide," "Go to next slide," "Go to first slide," "Go to last slide," "Go to page or object," "Go to document," "Play sound," "Run program," and "Run macro." When "Go to page or object" is selected, an additional field appears below the dropdown letting you choose the target slide by name. The dialog has OK, Cancel, and Help buttons at the bottom.

A couple of handy tips: if Impress keeps auto-converting URLs you type into hyperlinks and you don't want that, turn it off at **Tools > AutoCorrect Options > Options** and deselect **URL Recognition**. And if you want to change the color of all hyperlinks across your presentation, head to **Tools > Options > LibreOffice > Application Colors**, find *Unvisited links* and *Visited links*, and pick your preferred colors.

To test your navigation, start the slideshow with **F5** (from the first slide) or **Shift+F5** (from the current slide), then click your hyperlinks and interaction buttons to make sure they land where you expect.

---

## UI Reference  —  Format Menu

_Scope: Interaction... dialog entry for click actions on objects_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

The Format menu is shown expanded from the menu bar, displaying a vertical list of entries. Near the top are Text, Spacing, Align Text, and Lists submenus (each with a right-pointing arrow), followed by Clear Direct Formatting (Shift+Ctrl+M). Below that are Character..., Paragraph..., Bullets and Numbering..., Theme..., Table, Image, and Text Box and Shape submenus. Further down appear Shadow (as a toggle), Interaction..., Name..., and Alt Text.... The lower portion contains Distribute Selection, Rotate, Flip, Convert, Align Objects, Arrange, and Group — each with submenu arrows. The Interaction... entry is the key item here, providing access to the click-action configuration dialog for selected objects.

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

_Scope: Hyperlink... (Ctrl+K) opening Hyperlink dialog_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

The Insert menu is shown expanded from the menu bar, presenting a vertical list of insertion options. At the top are Image..., Audio or Video..., Chart..., and Table..., followed by Media and OLE Object submenus. Below those are Shape, Snap Guide..., Text Box (F2), Comment (Ctrl+Alt+C), and Fontwork.... The Hyperlink... entry appears mid-menu with its Ctrl+K shortcut displayed to the right. Continuing down are Special Character..., Formatting Mark, Slide Number, Field, Header and Footer..., and Form Control — several with submenu arrows indicating further options.

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

## UI Reference  —  Slide Show Menu

_Scope: Start from First/Current Slide (F5/Shift+F5) for testing navigation_

The Slide Show menu controls presentation playback, rehearsal timings, custom shows, and presentation settings.

The Slide Show menu is shown expanded from the menu bar with a short list of entries: Start from First Slide (F5), Start from Current Slide (Shift+F5), Rehearse Timings, Custom Slide Show..., and Slide Show Settings... at the bottom. Each entry is displayed on its own line with keyboard shortcuts shown right-aligned where applicable.

## Elements

- **Start from First Slide** (F5) — Launch full-screen presentation from slide 1
- **Start from Current Slide** (Shift+F5) — Launch from the currently selected slide
- **Rehearse Timings** — Run slideshow in rehearsal mode, recording per-slide timings
- **Custom Slide Show...** — Create, edit, copy, delete, or start named subsets of slides
- **Slide Show Settings...** — Opens the Slide Show Settings dialog (see below)

## Slide Show Settings Dialog

The Slide Show Settings dialog is a multi-section window. At the top left is the "Range" group with radio buttons for "All slides," "From:" (with a slide number spinner), and "Custom slide show" (with a dropdown). To the right is "Presentation Mode" with radio buttons for "Full screen," "In a window," and "Loop and repeat after" (with a time field in HH:MM:SS format), plus a "Show logo during pause" checkbox that is only active in loop mode. Below that is "Presentation Options" containing checkboxes for disabling automatic slide changes, changing slides by clicking on the background, mouse pointer visibility, mouse pointer as pen, enabling animated images, and keeping the presentation always on top. The lower portion has a "Display" section with a presentation display dropdown, presenter console setting, navigation bar toggle, and button size selector, as well as a "Remote Control" section with options to enable remote control, a download app link, and an insecure WiFi connections checkbox. OK, Cancel, and Help buttons appear at the bottom right.

### Range
- All slides (default) / From: Slide N / Custom slide show

### Presentation Mode
- Full screen (default) / In a window / Loop and repeat after HH:MM:SS
- Show logo during pause (only with Loop mode)

### Presentation Options
- Disable automatic change of slides
- Change slides by clicking on background ✓
- Mouse pointer visible / Mouse pointer as pen
- Enable animated images ✓
- Keep Presentation always on top

### Display
- Presentation display dropdown
- Presenter console: Full screen
- Show navigation bar, Buttons size (Automatic)

### Remote Control
- Enable remote control, Download App link, Enable insecure WiFi connections

---

## UI Reference  —  Standard Toolbar

_Scope: Hyperlink button for insert/edit_

The first icon row below the menu bar. Provides quick access to common file and editing operations.

The Standard toolbar is a single horizontal row of icon buttons stretching across the top of the Impress window, directly beneath the menu bar. From left to right it shows: New (with a dropdown arrow), Open (with dropdown), Save (with dropdown), Email Document, Edit File, PDF export, and Print buttons in the file operations group; then Cut, Copy, Paste, and Paint Format (clone formatting) for clipboard operations; Undo and Redo buttons; Find & Replace and Spelling; a set of view mode toggle buttons (Normal, Outline, Notes, Slide Sorter); a Presentation (play) button; quick-insert buttons for Table, Chart, and Text Box; the Hyperlink button for inserting or editing hyperlinks; a Sidebar toggle; and finally a Start Center button at the far right.

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

_Scope: AutoCorrect Options > Options tab for URL Recognition toggle_

The Tools menu provides spelling, language, autocorrect, macros, forms, extensions, customisation, and application-wide options.

The Tools menu is shown expanded from the menu bar as a vertical dropdown. At the top are Spelling... (F7) and Automatic Spell Checking (Shift+F7, shown with a checkmark indicating it is enabled), followed by Thesaurus... (Ctrl+F7, greyed out). Next is a Language submenu, then AutoCorrect Options... which opens the multi-tabbed autocorrect configuration dialog. Below that are Redact, Auto-Redact, Minimize Presentation..., and togglable panel entries for ImageMap, Color Replacer, and Media Player. Further down are a Forms submenu, a Macros submenu, and Development Tools. The bottom section lists XML Filter Settings..., Extensions... (Ctrl+Alt+E), Customize..., and finally Options... (Alt+F12) for accessing the full application settings tree.

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
