# Table Data and Operations (LibreOffice Writer 7.3.7)

Once you've got a table in your document, you can move between cells using the mouse, arrow keys, or **Tab**. The arrow keys nudge the cursor one character at a time, while **Tab** jumps to the next cell — and if you're in the last cell of the table, it automatically creates a new row. Use **Shift+Tab** to move backward. If you need a literal tab character inside a cell, press **Ctrl+Tab**.

For quick navigation, **Ctrl+Home** jumps to the beginning of the table and **Ctrl+End** to the end. If the cell has content, the first press goes to the start (or end) of that cell, and a second press takes you to the table boundary.

Sorting data works much like a spreadsheet. Select the cells you want sorted, then go to **Table > Sort** (or click the **Sort** icon on the Table toolbar). The Sort dialog lets you pick up to three keys, choose between columns or rows as the sort direction, and set each key to Numeric or Alphanumeric with Ascending or Descending order. Be sure to select all cells that could be affected — sorting just one column will rearrange that column alone and can mix up your rows.

The Sort dialog is titled "Sort" and contains a "Sort Criteria" section at the top with three sort keys (Key 1, Key 2, Key 3), each with a checkbox to enable it, a Column number spinner, a Key type dropdown (set to "Alphanumeric" by default), and Ascending/Descending radio buttons for Order. Below that, a "Direction" section offers radio buttons for "Columns" or "Rows" (Rows is selected by default), and a "Separator" section provides options for "Tabs" or a custom "Character" with a Select button. At the bottom left is a "Language" dropdown (set to "English (USA)") and a "Setting" section with a "Match case" checkbox, followed by Help, OK, and Cancel buttons.

Writer tables support basic spreadsheet-style formulas. Cells are referenced by a letter (column) and number (row), like `<C4>`. To enter a formula, click a cell and press **F2**, or go to **Table > Formula**, or click the **Sum** or **Formula** icon on the Table toolbar. The Formula Bar appears at the top. Type your formula (e.g., `=<B1>+<C2>`), then press **Enter** or click the green check mark. For summing a range, type something like `=sum<A2:A5>`. Unlike Calc, formulas in Writer tables do not auto-update when you insert or delete rows or columns — they do update when you change a cell value, though.

The Formula Bar appears above the document ruler, showing the cell reference "A1" on the left, followed by a formula function icon (with a dropdown arrow), a red X cancel button, and a green checkmark confirm button, then the formula input field displaying `=<B1>+<C2>`. Below in the table itself, cell A1 shows the formula text `=<B1>+<C2>` being entered, while other cells contain sample values such as 4 and 5.

You can protect individual cells from editing via **Table > Protect Cells** or the **Protect Cells** icon. To remove protection, use **Table > Unprotect Cells**, or press **Shift+Ctrl+T** to unprotect the entire table.

Adding a caption is easy: right-click the table and choose **Insert Caption**, or go to **Insert > Caption**. In the dialog, set the Category, Numbering, and type your caption text.

To split a table in two, place the cursor in the row that should become the top of the second table, then choose **Table > Split Table**. To merge two adjacent tables back together, delete the blank paragraph between them using the **Delete** key, select a cell in either table, and choose **Table > Merge Table**. Use **View > Formatting Marks** (Ctrl+F10) to see where those paragraph breaks are hiding.

Deleting a table is straightforward: right-click inside it and pick **Delete > Table**, or use **Table > Delete > Table**. To copy or move a table, select it, use **Ctrl+C** (or **Ctrl+X** to cut), click where you want it, and press **Ctrl+V**. If you need a paragraph before or after a table, position the cursor in the first (or last) cell and press **Alt+Enter**.

---

## UI Reference  —  Table & Form Menus

_Scope: Sort…, Edit Formula (F2), Protect/Unprotect Cells, Select, Delete_

The Table menu manages table creation and editing. The Form menu provides form controls and design tools. Most Table items are context-sensitive and greyed when the cursor is not in a table.

## Table Menu

The Table dropdown menu in the menu bar shows a vertical list of items in the following order: "Insert Table…" at the top, then submenus for "Insert", "Delete", "Select", and "Size", followed by a separator. Next come "Merge Cells", "Split Cells…", "Merge Table", and "Split Table…", then another separator with "Protect Cells" and "Unprotect Cells". After another separator are "AutoFormat Styles…", "Number Format…", and a "Number Recognition" checkbox toggle. Below that, "Header Rows Repeat Across Pages" and "Row to Break Across Pages" appear (partially truncated), followed by a "Convert" submenu, "Edit Formula", "Sort…", and finally "Properties…" at the bottom. Several items such as Merge Cells, Split Table, and Sort appear greyed out, indicating they are context-sensitive.

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
