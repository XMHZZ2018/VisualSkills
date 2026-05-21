# PDF Export (LibreOffice Impress 7.3.7)

The fastest way to get a PDF out of Impress is the one-click method. Just click **Export Directly as PDF** on the Standard toolbar, or go to **File > Export As > Export Directly as PDF**. A file browser opens — pick your destination folder, give it a name, and hit **Save**. Done. This uses whatever PDF settings were last configured (or the defaults if you've never touched them).

If you need more control over the output — image quality, page range, structure tags — take the longer route via **File > Export as PDF**. This opens the PDF Options dialog, which has several tabs worth exploring.

See `fig01.png`.

On the **General** tab, the *Range* section lets you export all slides, a specific set (enter slide numbers), or just the current selection. Check *View PDF after export* if you want the file to open automatically when it's done.

The *Images* section is where quality lives. Choose **Lossless compression** if image fidelity is critical, or stick with **JPEG compression** and dial the quality (default is 90%). You can also tick **Reduce image resolution** and set a DPI cap — 300 DPI is the default and works well for most print scenarios; drop it lower for screen-only documents to shrink file size.

On the right side of the General tab, the *General* options let you create a **Hybrid PDF** (which embeds the ODF source so the file can be re-opened and edited in LibreOffice), or produce a **PDF/A** archival-compliant file. You can also enable **Tagged PDF** to add document structure for accessibility, and toggle **Export outlines**, **comments**, or **notes pages** under the *Structure* section.

Once you're happy with the settings, click **Export**, choose your save location and filename, then click **Export** again to write the file. The format is locked to PDF — you can't change it in the file browser.

You can also email a PDF directly without saving it first. Head to **Format > Send > Email as PDF** — the same PDF Options dialog appears, and after you click **Send**, your default email client opens with the PDF already attached.

---

## UI Reference  —  File Menu

_Scope: Export As > Export as PDF, Export Directly as PDF, Send > Email as PDF_

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

## UI Reference  —  PDF Options Dialog

_Scope: All 6 tabs: General (Range, Images, Hybrid/PDF-A/Tagged), Initial View, User Interface, Links, Security, Digital Signatures_

A 6-tab dialog for configuring PDF export. Opened via File > Export As > Export as PDF...

Read the screenshot `ui-pdf-options-dialog.png` in this directory.

## Tabs

### General
- **Range**: All / Slides / Selection radio buttons; View PDF after export checkbox
- **Images**: Lossless compression / JPEG compression (quality % field); Reduce image resolution checkbox + DPI dropdown (300 DPI default)
- **Watermark**: Sign with watermark checkbox + text field
- **General** (right column): Hybrid PDF, Archival (PDF/A, ISO 19005) + version dropdown, Universal Accessibility (PDF/UA), Tagged PDF ✓, Create PDF form + Submit format dropdown
- **Structure**: Export outlines ✓, Comments as PDF annotations, Comments in margin, Export notes pages, Export hidden pages, Use reference XObjects

### Initial View
- **Panes**: Page only / Outline and page / Thumbnails and page; Open on page field
- **Magnification**: Default / Fit in window / Fit width / Fit visible / Zoom factor
- **Page Layout**: Default / Single page / Continuous / Continuous facing

### User Interface
PDF viewer UI configuration (toolbar, menu, window options)

### Links
Bookmark and URL handling settings

### Security
Password protection and permission controls

### Digital Signatures
Certificate-based signing options

Buttons: Help, Cancel, Export

---

## UI Reference  —  Standard Toolbar

_Scope: PDF one-click export button_

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

