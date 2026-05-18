# Form Basics (LibreOffice Writer 7.3.7)

Forms in Writer let you create interactive documents — think questionnaires, data-entry sheets, or anything where a reader fills in fields rather than editing freely. A form has fixed sections (your questions and labels) and editable sections (check boxes, text fields, drop-down lists) where the recipient provides input. The typical workflow is simple: design the form, send it out, get it back filled in, and review the answers.

Forms are handy in three situations: distributing a simple document for people to complete and return, linking to a database so entered data is stored automatically, or viewing information already held in a database. If you just need a straightforward fill-and-return form with no database behind it, Writer alone is all you need — no need to involve LibreOffice Base.

**Creating the document.** Open a fresh document with **File > New > Text Document**. Before placing any controls, turn on the positioning grid so things line up nicely: go to **View > Grid and Helplines** on the Menu bar and select **Display Grid**. You may also want to enable **Snap to Grid** for precise placement.

**Opening the form toolbars.** You'll need two toolbars: Form Controls and Form Design. Bring them up via **View > Toolbars > Form Controls** and **View > Toolbars > Form Design**. The Form Controls toolbar has icons for every common control type — text boxes, check boxes, option buttons, list boxes, and more. You can dock these toolbars or leave them floating, and even switch them between vertical and horizontal layout by dragging a corner.
**Activating design mode.** Click the **Design Mode** icon on the Form Controls toolbar to toggle design mode on. With design mode active, you can insert and edit controls; with it off, the form behaves as it would for the end user (buttons click, check boxes toggle, etc.).

**Inserting controls.** Click a control icon on the toolbar, then click in your document where you want it and drag to size it. Controls display a fixed-size symbol followed by their type name (like **Check Box** or **Option Button**). The chosen control stays active, so you can stamp out several of the same type in a row without going back to the toolbar. When you're done inserting, click the **Select** icon on the Form Controls toolbar to return the pointer to normal.

Hold **Shift** while creating or resizing a control to keep it perfectly square or to maintain its proportions — a small trick that keeps things tidy.

**Configuring controls.** Once a control is placed, right-click it and select **Control** from the context menu to open its properties and customize how it looks and behaves.

---

## UI Reference  —  Table & Form Menus

_Scope: Design Mode toggle, form control types (Label through Navigation Bar), Control/Form Properties_

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

