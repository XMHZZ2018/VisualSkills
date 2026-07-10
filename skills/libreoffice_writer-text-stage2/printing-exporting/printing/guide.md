# Printing Documents (LibreOffice Writer 7.3.7)

The fastest way to get ink on paper is the **Print Directly** icon on the Standard toolbar — one click and your entire document goes straight to the default printer with whatever settings are already in place. If the icon isn't showing, right-click the toolbar, choose **Visible Buttons**, and enable **Print Directly**. To pick or change your default printer, head to **File > Printer Settings** and make your selection in the Printer Setup dialog.

When you need more control, open the full Print dialog with **File > Print** (or *Ctrl+P*, *⌘+P* on macOS). On Windows and Linux you'll see a **General** tab where you choose the printer, page range, number of copies, paper size, and orientation. The **LibreOffice Writer** tab lets you fine-tune what actually prints — page backgrounds, images, hidden text, form controls, and comments. There's also a handy **Print text in black** checkbox if you want all text forced to black regardless of document colors.

The Print dialog on Windows and Linux has two tabs at the top — **General** and **LibreOffice Writer**. The left half of the dialog shows a page preview with dimensions displayed (e.g., 8.27 in × 11.69 in for A4). On the right, the **Printer** section shows the selected printer name and its status with a **Properties…** button. Below that, the **Range and Copies** section offers radio buttons for **All Pages**, **Pages** (with a text field for entering specific pages), and **Selection** (greyed out when nothing is selected), plus an **Include** drop-down set to "Odd and Even Pages" and an expandable **more** link. The **Page Layout** section beneath provides **Paper size** and **Orientation** drop-downs with its own **more** expander. Along the bottom are a **Preview** checkbox, page navigation controls, and **Help**, **More Options…**, **Print**, and **Cancel** buttons.

You're not limited to printing the whole document. In the **Range and Copies** section, select **Pages** and type individual pages (e.g., `1,3,7,11`) or ranges (`1-4`). If you highlight text or a graphic first and then open the Print dialog, the **Selection** option becomes active so you can print just that snippet. The preview pane on the left updates in real time so you always know what you're about to send.

To fit multiple pages on one sheet, click **More** on the **Page Layout** section (Windows/Linux) and choose from the **Pages per sheet** drop-down. You can also pick the print order — left-to-right then down, top-to-bottom then right, and so on. For brochure printing, select **Brochure** in the Page Layout area, print **Even pages** first, flip the stack back into the tray, then print **Odd pages**. If your printer supports duplex, just choose **All pages** and let the hardware handle it.

The expanded **Page Layout** section shows **Paper size** (set to A4 8.27in × 11.69in) and **Orientation** (set to Automatic) drop-downs at the top, followed by a **More** area that has been expanded. Inside, a **Pages per sheet** radio button is selected with a drop-down set to "4", and to its right a small diagram shows the resulting 2×2 grid numbered 1–4. Below that, the **Order** drop-down is open, revealing four choices: "Left to right, then down" (currently highlighted), "Top to bottom, then right", "Top to bottom, then left", and "Right to left, then down". A **Brochure** radio button appears at the bottom left as an alternative to Pages per sheet.

For black-and-white output on a color printer, you have a few routes. On Windows/Linux, click **Properties** in the Print dialog and set the printer itself to grayscale. On macOS, check **Print text in black** in the **Color** section of the LibreOffice Writer page. For a permanent global change, go to **Tools > Options > LibreOffice Writer > Print** and enable **Print text in black** or head to **Tools > Options > LibreOffice > Print** and select **Convert colors to grayscale**.

Before printing anything, it's worth previewing. Use **File > Print Preview** (or *Ctrl+Shift+O*) to get a read-only look at your pages with a dedicated toolbar that lets you toggle between **Single Page Preview**, **Two Pages Preview**, **Book Preview**, and **Multiple Pages Preview**. When you're happy, hit the **Print** icon right on that toolbar.

To print an envelope, go to **Insert > Envelope**. The *Envelope* tab is where you fill in or edit the addressee and sender info — Writer pulls your sender details from **Tools > Options > LibreOffice > User Data**. Switch to the *Format* tab to adjust positioning and envelope size, then the *Printer* tab to set orientation and tray. Click **Insert** to add it to your document, or **New Document** to create a standalone envelope.

The Envelope dialog has three tabs across the top: **Envelope** (currently selected), **Format**, and **Printer**. On the left side, an **Addressee** text area (currently empty) sits above a **Sender** section with a checkbox enabled and a pre-filled return address. On the right, a **Database** section provides drop-downs for selecting an address data source, table, and database field, with an arrow button to insert a field into the addressee area. Below the database fields, a small envelope preview graphic shows the relative placement of the sender block (upper-left) and addressee block (center-right). Along the bottom of the dialog are **Help**, **Insert**, **Reset**, **Cancel**, and **New Document** buttons.

---

## UI Reference  —  File Menu

_Scope: Print (Ctrl+P), Print Preview (Shift+Ctrl+O), Printer Settings_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

The File menu is an expanded drop-down from the menu bar, listing entries from top to bottom: New, Open…, Open Remote…, Recent Documents, Close, then a separator, followed by Wizards, Templates, Reload (greyed out), Versions…, then another separator with Save, Save As…, Save Remote…, Save a Copy…, Save All (greyed out), then Export…, Export As, Send, Preview in Web Browser, then a separator leading to Print Preview (with a checkbox icon), Print…, Printer Settings…, Properties…, Digital Signatures, and finally Exit LibreOffice. Keyboard shortcuts are shown to the right of several entries, such as Shift+Ctrl+O for Print Preview and Ctrl+P for Print.

## Elements

- **New** (►) — Create a new document of any type (Text, Spreadsheet, Presentation, Drawing, etc.). Ctrl+N for Text Document.
- **Open…** (Ctrl+O) — Open an existing file.
- **Open Remote…** — Open a file from a remote server.
- **Recent Documents** (►) — List of recently opened files.
- **Close** — Close the current document.
- **Wizards** (►) — Step-by-step creation wizards: Letter, Fax, Agenda, Document Converter, Address Data Source.
- **Templates** (►) — Edit Template, Save as Template, Manage Templates (Shift+Ctrl+N).
- **Reload** — Reload document from disk (greyed on unsaved documents).
- **Versions…** — Manage saved versions of the document.
- **Save** (Ctrl+S) — Save in current format.
- **Save As…** (Shift+Ctrl+S) — Save with a new name or format.
- **Save Remote…** — Save to a remote server.
- **Save a Copy…** — Save a copy without changing the working file.
- **Save All** — Save all open documents.
- **Export…** — Export in a non-native format.
- **Export As** (►) — Export as PDF (dialog or direct), Export as EPUB (dialog or direct).
- **Send** (►) — Email document in various formats (ODF, Word, PDF), send via Bluetooth, create Master/HTML document.
- **Preview in Web Browser** — Open document preview in default browser.
- **Print Preview** (Shift+Ctrl+O) — Toggle print-preview layout.
- **Print…** (Ctrl+P) — Open the Print dialog.
- **Printer Settings…** — Configure printer options.
- **Properties…** — Open the 6-tab document properties dialog (General, Description, Custom Properties, Security, Font, Statistics).
- **Digital Signatures** (►) — Digital Signatures…, Sign Existing PDF…
- **Exit LibreOffice** (Ctrl+Q) — Quit the entire suite.
