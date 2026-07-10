# Creating Tables (LibreOffice Writer 7.3.7)

Tables are a great way to organize data — think financial reports, catalogs, invoices, or even simple lists of names and addresses. They can also double as a page-layout tool when you need precise positioning of text and objects within your document.

All table-related commands live under **Table** on the Menu bar. When your cursor is inside a table, the Table toolbar appears automatically. You can also bring it up manually via **View > Toolbars > Table**. It gives you quick access to things like inserting and deleting rows/columns, merging and splitting cells, borders, alignment, number formats, and more. The Properties deck in the Sidebar also expands with a **Table** panel for adjusting row height, column width, and cell operations.

See `fig01.png`.

The fastest way to drop in a table is to click the **Insert Table** icon on the Standard toolbar. A little grid pops up — just drag to select how many rows and columns you want (up to 15 × 10) and click. Done.

See `fig02.png`.

For more control, open the Insert Table dialog instead: go to **Table > Insert Table**, press **Ctrl+F12**, or click **More Options** at the bottom of that drop-down grid. Here you can give the table a name (handy if you use the Navigator to jump between tables), set exact column and row counts, and configure options like repeating heading rows across pages or preventing the table from splitting over a page break. The *Styles* section at the bottom lets you pick from predefined table styles so you don't have to format everything by hand. When you're happy, hit **Insert** and Writer creates a table spanning the full text area width with equally sized columns.

See `fig03.png`.

You can nest tables too — just click inside a cell of an existing table and insert another one using any of the methods above. This is especially useful for complex page layouts.

There's also an AutoCorrect trick: type a sequence of plus signs and hyphens (like `+-----+-----+-----+`) and press Enter. Writer converts it into a table automatically, using the hyphens to determine column widths. You can toggle this behavior in **Tools > AutoCorrect > AutoCorrect Options** on the *Options* page.

If you already have text that should be a table — say, tab-separated or semicolon-separated data — select it and choose **Table > Convert > Text to Table**. Pick your separator type in the dialog, set any options, and click **OK**. The reverse works too: place your cursor in a table and use **Table > Convert > Table to Text** to flatten it back to plain text, which is great for exporting to other programs.

Finally, you can paste spreadsheet data directly. Open both documents, select the cells in your spreadsheet, copy with **Ctrl+C**, then switch to Writer and paste with **Ctrl+V**. You can also simply drag and drop the selection from the spreadsheet into your Writer document.

---

## UI Reference  —  Standard Toolbar

_Scope: Insert Table (Ctrl+F12) split-button with visual grid picker_

The first toolbar row below the menu bar provides quick access to file operations, clipboard, editing, and insert commands.

Read the screenshot `ui-standard-toolbar.png` in this directory.

## Elements

Row (left → right):

- **New** (Ctrl+N, split-button ▼) — New document; dropdown lists all document types.
- **Open** (Ctrl+O) — Open file dialog.
- **Save** (Ctrl+S, split-button ▼) — Save; dropdown: Save As…, Export…, Save a Copy…, Save as Template…, Save Remote File…
- **Export Directly as PDF** — One-click PDF export.
- **Print** (Ctrl+P) — Print dialog.
- **Toggle Print Preview** (Shift+Ctrl+O)

| *(separator)* |

- **Cut** (Ctrl+X) / **Copy** (Ctrl+C) / **Paste** (Ctrl+V, split-button ▼)
- **Clone Formatting** — Paint-format brush; double-click for persistent mode.

| *(separator)* |

- **Undo** (Ctrl+Z, split-button ▼) / **Redo** (Ctrl+Y)

| *(separator)* |

- **Find and Replace** (Ctrl+H) — Opens Find & Replace dialog.
- **Check Spelling** (F7)
- **Toggle Formatting Marks** (Ctrl+F10) — Show/hide ¶ marks, spaces, tabs.

| *(separator)* |

- **Insert Table** (Ctrl+F12, split-button ▼) — Dialog or visual grid picker for row×column count.
- **Insert Image** — File picker for images.
- **Insert Chart** — Embed chart OLE object.
- **Insert Text Box** — Draw a text frame on canvas.
- **Insert Page Break** (Ctrl+Return)
- **Insert Field** (split-button ▼) — Page Number, Page Count, Date/Time, Title, Author, Subject, More Fields…
- **Insert Special Characters** (split-button ▼) — Full character picker or favorites quick-pick.

| *(separator)* |

- **Insert Hyperlink** (Ctrl+K) — Hyperlink dialog.
- **Insert Footnote** / **Insert Endnote**
- **Insert Bookmark** — Bookmark dialog.
- **Insert Cross-reference** — Cross-reference dialog.
- **Insert Comment** (Ctrl+Alt+C)
- **Show Track Changes Functions** — Toggle Track Changes toolbar.

| *(separator)* |

- **Insert Line** — Line-drawing mode; double-click for persistent mode.
- **Basic Shapes** (split-button ▼) — 4×6 shape palette.
- **Show Draw Functions** — Toggle Drawing toolbar.

---

## UI Reference  —  Table & Form Menus

_Scope: Insert Table (Ctrl+F12), Insert rows/columns, Delete, Convert (Text to Table / Table to Text)_

The Table menu manages table creation and editing. The Form menu provides form controls and design tools. Most Table items are context-sensitive and greyed when the cursor is not in a table.

## Table Menu

(see screenshot `ui-table-menu.png`)

- **Insert Table…** (Ctrl+F12) — Opens the Insert Table dialog (name, columns, rows, heading options, table style presets).
- **Insert** (►) — Rows Above/Below, Rows…, Columns Before/After, Columns…
- **Delete** (►) — Rows, Columns, or entire Table.
- **Select** (►) — Cell, Row, Column, or Table.
- **Size** (►) — Row Height, Minimal/Optimal Row Height, Distribute Rows Evenly; Column Width, Minimal/Optimal Column Width, Distribute Columns Evenly.
- **Merge Cells** / **Split Cells…** / **Merge Table** / **Split Table…**
- **Protect Cells** / **Unprotect Cells**
- **AutoFormat Styles…** / **Number Format…**
- **Number Recognition** — Toggle checkbox.
- **Header Rows Repeat Across Pages** / **Row to Break Across Pages**
- **Convert** (►) — Text to Table…, Table to Text…
- **Edit Formula** (F2) / **Sort…** / **Properties…**

## Form Menu

- **Design Mode** (toggle, on by default) / **Control Wizards** (toggle, on by default)
- **Form controls:** Label, Text Box, Check Box, Option Button, List Box, Combo Box, Push Button, Image Button, Formatted Field, Group Box, Image Control, File Selection, Table Control, Navigation Bar.
- **More Fields** (►) — Date Field, Time Field, Numerical Field, Currency Field, Pattern Field.
- **Control Properties…** / **Form Properties…** / **Form Navigator…** / **Activation Order…**
- **Open in Design Mode** / **Automatic Control Focus** — toggles.
- **Content Controls** (►) — Word-compatible: Rich Text, Plain Text, Picture, Check Box, Combo Box, Drop-Down List, Date Control, Properties.

