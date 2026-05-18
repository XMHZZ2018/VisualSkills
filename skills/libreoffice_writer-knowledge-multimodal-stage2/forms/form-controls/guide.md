# Form Controls Reference (LibreOffice Writer 7.3.7)

To start building a form, open the Form Controls toolbar via **View > Toolbars > Form Controls**, or go to **Form** on the Menu bar where you'll find the full list of controls and options. The toolbar gives you quick access to the most common controls, while the menu exposes everything, including sub-items under **More Fields** like Date Field, Time Field, Numerical Field, Currency Field, and Pattern Field.

See `fig01.png`.

When you first add a control, Writer enters **Design Mode** automatically—this is where you position and configure controls. To let users actually interact with the form, click the **Design Mode** icon again to toggle it off, then save the document.

The core controls cover most needs. A **Text Box** is your basic free-text input. **Check Box** gives you a simple on/off toggle. **Option Button** (radio button) works like a check box, but only one in a group can be selected at a time—group multiples by placing them inside a **Group Box**, which you can create easily with the Group Element wizard. **List Box** and **Combo Box** both present a list of choices; the difference is that a Combo Box also lets the user type a custom value. If the form isn't linked to a data source, turn wizards off, then type your list entries directly in the **List Entries** field on the General tab of the control's properties.

See `fig02.png`.

For specialized input, reach for **Formatted Field** (numeric formatting with min/max values), **Date Field**, **Time Field**, **Numerical Field**, or **Currency Field**. **Push Button** and **Image Button** can trigger macros—handy for validation or navigation logic. **Label** may look like plain text, but it can be linked to a macro so hovering or clicking does something useful. **File Selection** provides a browse dialog for picking files, and **Spin Button** lets users cycle through a number range.

Double-click any control to open its **Properties** dialog, which has three tabs: **General**, **Data**, and **Events**. For simple forms without a database, the General tab is usually all you need. The Form Design toolbar (**View > Toolbars > Form Design**) adds layout tools—**Align**, **Bring to Front/Send to Back**, **Activation Order** (the Tab key sequence), and **Form Navigator** for managing controls by name across the document.

---

## UI Reference  —  Table & Form Menus

_Scope: Full form control list, More Fields submenu, Control Properties, Form Navigator_

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

