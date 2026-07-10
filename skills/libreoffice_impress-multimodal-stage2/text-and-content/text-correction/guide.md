# Text Correction & Language (LibreOffice Impress 7.3.7)

When you're building a slide deck, typos sneak in fast. Impress has solid built-in spell checking to catch them. The quickest way to spot errors is to look for the red wavy underlines that appear as you type — right-click any flagged word and you'll get a list of suggested corrections. Pick one and you're done, or choose **Add to Dictionary** if the word is correct but just not recognized.

To run a full spell check across your presentation, hit **F7** or go to **Tools > Spelling**. This opens a dialog that walks you through each flagged word one at a time, offering suggestions you can accept, ignore, or use to add the word to your personal dictionary. It's especially handy when you've just pasted in a big block of text and want to clean it all up in one pass.

AutoCorrect is another time-saver — it silently fixes common typos as you type (think "teh" → "the"). You can review or customize these replacements under **Tools > AutoCorrect Options**. The **Replace** tab shows the full substitution table; add your own frequent typos here. If AutoCorrect ever "fixes" something you didn't want changed, just hit **Ctrl+Z** immediately to undo it.

For language and locale, Impress inherits the default language from your global LibreOffice settings. To change the default, open **Tools > Options**, expand **Language Settings**, and select **Languages**. The locale you pick here controls which dictionary is used for spell checking and which hyphenation rules apply.

Sometimes a single presentation mixes languages — maybe your title slides are in English but a few bullet points are in French. You don't need to change the global setting for that. Just select the specific text span, then go to **Format > Character** and open the **Fonts** tab. There's a **Language** dropdown that lets you assign a different language to just that selection. The spell checker will then use the right dictionary for each chunk of text.

If you notice spell check isn't catching errors at all, double-check that the text isn't accidentally marked as "None (Do not check spelling)" in that same **Format > Character** language dropdown. This is a surprisingly common gotcha, especially with pasted content.

For broader autocorrect behavior — like whether to capitalize the first letter of every sentence or fix accidental use of Caps Lock — check the **Options** and **Localized Options** tabs in **Tools > AutoCorrect Options**. These small tweaks keep your text clean without you having to think about it.

---

## UI Reference  —  Format Menu

_Scope: Character... dialog for language dropdown on Fonts tab_

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

## UI Reference  —  Standard Toolbar

_Scope: Spelling button for spell check_

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

_Scope: Spelling (F7), Automatic Spell Checking toggle, Language submenu, AutoCorrect Options 4-tab dialog_

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

