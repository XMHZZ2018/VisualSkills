# Creating Tables (LibreOffice Writer 7.3.7)

Tables are a great way to organize data — think financial reports, catalogs, invoices, or even simple lists of names and addresses. They can also double as a page-layout tool when you need precise positioning of text and objects within your document.

All table-related commands live under **Table** on the Menu bar. When your cursor is inside a table, the Table toolbar appears automatically. You can also bring it up manually via **View > Toolbars > Table**. It gives you quick access to things like inserting and deleting rows/columns, merging and splitting cells, borders, alignment, number formats, and more. The Properties deck in the Sidebar also expands with a **Table** panel for adjusting row height, column width, and cell operations.

The Table toolbar is a floating toolbar labeled "Table" containing 32 numbered icon buttons arranged in two rows. The icons provide quick access to functions such as inserting and deleting rows and columns, merging and splitting cells, setting borders, adjusting alignment, toggling number formats (percent, decimal), inserting images, sorting, protecting cells, and invoking the formula bar. The toolbar can be closed or collapsed using the dropdown arrow and X button in its top-right corner.

The fastest way to drop in a table is to click the **Insert Table** icon on the Standard toolbar. A little grid pops up — just drag to select how many rows and columns you want (up to 15 × 10) and click. Done.

Clicking the Insert Table icon on the Standard toolbar opens a dropdown panel titled "Table" that displays a visual grid of cells. As you drag across the grid, cells highlight in blue and a label such as "5 x 4" appears indicating the selected number of columns by rows. At the bottom of the dropdown is a **More Options…** button that opens the full Insert Table dialog instead.

For more control, open the Insert Table dialog instead: go to **Table > Insert Table**, press **Ctrl+F12**, or click **More Options** at the bottom of that drop-down grid. Here you can give the table a name (handy if you use the Navigator to jump between tables), set exact column and row counts, and configure options like repeating heading rows across pages or preventing the table from splitting over a page break. The *Styles* section at the bottom lets you pick from predefined table styles so you don't have to format everything by hand. When you're happy, hit **Insert** and Writer creates a table spanning the full text area width with equally sized columns.

The Insert Table dialog has a title bar reading "Insert Table" and is divided into several sections. The **General** section at the top contains a Name field (showing "Table2"), and spin boxes for Columns (set to 2) and Rows (set to 2). Below that, the **Options** section has a checked "Heading" checkbox with a nested checked "Repeat heading rows on new pages" option and a "Heading rows" spin box set to 1, plus an unchecked "Don't split table over pages" checkbox. The **Styles** section at the bottom shows a scrollable list of predefined table styles (including None, Default Table Style, Academic, Box List Blue, Box List Green, Box List Red, Box List Yellow, Elegant, and others) with a live preview table to the right displaying sample data with column headers Jan, Feb, Mar, Sum and row labels North, Mid, South, Sum. The dialog has Help, Cancel, and a blue Insert button along the bottom.

You can nest tables too — just click inside a cell of an existing table and insert another one using any of the methods above. This is especially useful for complex page layouts.

There's also an AutoCorrect trick: type a sequence of plus signs and hyphens (like `+-----+-----+-----+`) and press Enter. Writer converts it into a table automatically, using the hyphens to determine column widths. You can toggle this behavior in **Tools > AutoCorrect > AutoCorrect Options** on the *Options* page.

If you already have text that should be a table — say, tab-separated or semicolon-separated data — select it and choose **Table > Convert > Text to Table**. Pick your separator type in the dialog, set any options, and click **OK**. The reverse works too: place your cursor in a table and use **Table > Convert > Table to Text** to flatten it back to plain text, which is great for exporting to other programs.

Finally, you can paste spreadsheet data directly. Open both documents, select the cells in your spreadsheet, copy with **Ctrl+C**, then switch to Writer and paste with **Ctrl+V**. You can also simply drag and drop the selection from the spreadsheet into your Writer document.

---

## UI Reference  —  Table & Form Menus

_Scope: Insert Table (Ctrl+F12), Insert rows/columns, Delete, Convert Text↔Table_

The Table menu manages table creation and editing. The Form menu provides form controls and design tools. Most Table items are context-sensitive and greyed when the cursor is not in a table.

## Table Menu

The Table menu dropdown shows a vertical list of menu items in the following order: Insert Table…, Insert (with a submenu arrow), Delete (with a submenu arrow), Select (with a submenu arrow), Size (with a submenu arrow), then a separator followed by Merge Cells, Split Cells…, Merge Table, and Split Table…. After another separator are Protect Cells and Unprotect Cells, then AutoFormat Styles… and Number Format…. A Number Recognition item with an unchecked checkbox follows, along with the greyed-out items Header Rows Repeat Across Pages and Row to Break Across Pages. The bottom section contains Convert (with a submenu arrow), Edit Formula, the greyed-out Sort…, and Properties…. Several items appear greyed out, indicating the cursor is not currently inside a table.

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
