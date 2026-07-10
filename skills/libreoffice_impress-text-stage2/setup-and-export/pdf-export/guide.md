# PDF Export (LibreOffice Impress 7.3.7)

The fastest way to get a PDF out of Impress is the one-click method. Just click **Export Directly as PDF** on the Standard toolbar, or go to **File > Export As > Export Directly as PDF**. A file browser opens — pick your destination folder, give it a name, and hit **Save**. Done. This uses whatever PDF settings were last configured (or the defaults if you've never touched them).

If you need more control over the output — image quality, page range, structure tags — take the longer route via **File > Export as PDF**. This opens the PDF Options dialog, which has several tabs worth exploring.

The PDF Options dialog is shown open to the General tab. On the left side, the Range section offers radio buttons for All, Slides, and Selection, with a "View PDF after export" checkbox. Below that, the Images section provides radio buttons for Lossless compression and JPEG compression (with a quality percentage field), plus a "Reduce image resolution" checkbox with a DPI dropdown defaulting to 300 DPI. On the right side, General options include checkboxes for Hybrid PDF, Archival (PDF/A), Tagged PDF, and a Create PDF form option, while the Structure section has checkboxes for Export outlines, Comments as PDF annotations, and Export notes pages. The dialog has six tabs across the top (General, Initial View, User Interface, Links, Security, Digital Signatures) and Help, Cancel, and Export buttons at the bottom.

On the **General** tab, the *Range* section lets you export all slides, a specific set (enter slide numbers), or just the current selection. Check *View PDF after export* if you want the file to open automatically when it's done.

The *Images* section is where quality lives. Choose **Lossless compression** if image fidelity is critical, or stick with **JPEG compression** and dial the quality (default is 90%). You can also tick **Reduce image resolution** and set a DPI cap — 300 DPI is the default and works well for most print scenarios; drop it lower for screen-only documents to shrink file size.

On the right side of the General tab, the *General* options let you create a **Hybrid PDF** (which embeds the ODF source so the file can be re-opened and edited in LibreOffice), or produce a **PDF/A** archival-compliant file. You can also enable **Tagged PDF** to add document structure for accessibility, and toggle **Export outlines**, **comments**, or **notes pages** under the *Structure* section.

Once you're happy with the settings, click **Export**, choose your save location and filename, then click **Export** again to write the file. The format is locked to PDF — you can't change it in the file browser.

You can also email a PDF directly without saving it first. Head to **Format > Send > Email as PDF** — the same PDF Options dialog appears, and after you click **Send**, your default email client opens with the PDF already attached.

---

## UI Reference  —  File Menu

_Scope: Export As > Export as PDF, Export Directly as PDF, Send > Email as PDF_

The File menu provides all document lifecycle operations: creating, opening, saving, exporting, printing, and closing presentations.

The screenshot shows the File dropdown menu fully expanded in LibreOffice Impress. The menu lists items from top to bottom: New, Open, Open Remote, Recent Documents, Close, Wizards, Templates, Reload, Versions, then a separator before Save, Save As, Save Remote, Save a Copy, Save All, followed by Export, Export As (with a submenu arrow leading to "Export as PDF..." and "Export Directly as PDF"), and Send (with a submenu arrow leading to "Email Document..." and "Email as PDF..."). Further down are Preview in Web Browser, Print, Printer Settings, Properties, Digital Signatures, and finally Exit LibreOffice at the bottom. Keyboard shortcuts such as Ctrl+N, Ctrl+O, Ctrl+S, and Ctrl+P are shown alongside their respective items.

## Elements

- **New** `▸` — Submenu: Text Document, Spreadsheet, Presentation (Ctrl+N), Drawing, Formula, Database, HTML Document, XML Form Document, Labels, Business Cards, Master Document, Templates (Shift+Ctrl+N)
- **Open...** (Ctrl+O) — File chooser to open an existing document
- **Open Remote...** — Connect to and open a file from a cloud location
- **Recent Documents** `▸` — Submenu of recently opened files
- **Close** — Closes the current document
- **Wizards** `▸` — Document creation wizards
- **Templates** `▸` — Template management
- **Reload** — Reverts to last saved state (greyed for unsaved documents)
- **Versions...** — Manage saved document versions
- **Save** (Ctrl+S) — Save the current document
- **Save As...** (Shift+Ctrl+S) — Save with a new name or format
- **Save Remote...** — Save to a cloud location
- **Save a Copy...** — Save a copy without changing the active file path
- **Save All** — Save all open LibreOffice documents
- **Export...** — Export in various non-native formats
- **Export As** `▸` — **Export as PDF...** (opens PDF Options dialog) or **Export Directly as PDF**
- **Send** `▸` — **Email Document...** or **Email as PDF...**
- **Preview in Web Browser** — Export to HTML and open in browser
- **Print...** (Ctrl+P) — Opens Print dialog (General + LibreOffice Impress tabs)
- **Printer Settings...** — Select and configure the printer
- **Properties...** — Document metadata (tabs: General, Description, Custom Properties, Security, Font)
- **Digital Signatures** `▸` — **Digital Signatures...** or **Sign Existing PDF...**
- **Exit LibreOffice** (Ctrl+Q) — Close all LibreOffice windows

---

## UI Reference  —  PDF Options Dialog

_Scope: Entire dialog: General tab (range, images, compression), Initial View, Security, Digital Signatures tabs_

A 6-tab dialog for configuring PDF export. Opened via File > Export As > Export as PDF...

The screenshot shows the PDF Options dialog box with six tabs across the top: General, Initial View, User Interface, Links, Security, and Digital Signatures. The General tab is active and is divided into several grouped sections. On the left, the Range group contains radio buttons for "All," "Slides," and "Selection," along with a "View PDF after export" checkbox. Below that, the Images group has radio buttons for "Lossless compression" and "JPEG compression" with a quality percentage spinner, plus a "Reduce image resolution" checkbox paired with a DPI dropdown set to 300 DPI. On the right side, the General group offers checkboxes for Hybrid PDF, Archival (PDF/A) with a version dropdown, Universal Accessibility (PDF/UA), Tagged PDF (checked by default), and Create PDF form with a submit format dropdown. The Structure group below contains checkboxes for Export outlines, Comments as PDF annotations, Comments in margin, Export notes pages, Export hidden pages, and Use reference XObjects. At the bottom of the dialog are three buttons: Help, Cancel, and Export.

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

The screenshot shows a horizontal toolbar strip sitting directly beneath the menu bar in LibreOffice Impress. Reading left to right, the toolbar contains icon buttons for: New (with a dropdown arrow), Open (with a dropdown arrow), Save (with a dropdown arrow), Email Document, Edit File, a PDF export button (a small icon depicting a page with "PDF" on it) for one-click direct PDF export, Print, then clipboard operations (Cut, Copy, Paste), Paint Format (clone formatting), Undo and Redo, Find & Replace, Spelling, view mode toggles (Normal, Outline, Notes, Slide Sorter), a Presentation start button, quick-insert tools for Table, Chart, and Text Box, a Hyperlink button, a Sidebar toggle, and a Start Center button at the far right.

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
