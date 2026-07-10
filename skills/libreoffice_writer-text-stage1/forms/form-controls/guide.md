# Form Controls Reference (LibreOffice Writer 7.3.7)

To start building a form, open the Form Controls toolbar via **View > Toolbars > Form Controls**, or go to **Form** on the Menu bar where you'll find the full list of controls and options. The toolbar gives you quick access to the most common controls, while the menu exposes everything, including sub-items under **More Fields** like Date Field, Time Field, Numerical Field, Currency Field, and Pattern Field.

See `fig01.png`.

When you first add a control, Writer enters **Design Mode** automatically—this is where you position and configure controls. To let users actually interact with the form, click the **Design Mode** icon again to toggle it off, then save the document.

The core controls cover most needs. A **Text Box** is your basic free-text input. **Check Box** gives you a simple on/off toggle. **Option Button** (radio button) works like a check box, but only one in a group can be selected at a time—group multiples by placing them inside a **Group Box**, which you can create easily with the Group Element wizard. **List Box** and **Combo Box** both present a list of choices; the difference is that a Combo Box also lets the user type a custom value. If the form isn't linked to a data source, turn wizards off, then type your list entries directly in the **List Entries** field on the General tab of the control's properties.

See `fig02.png`.

For specialized input, reach for **Formatted Field** (numeric formatting with min/max values), **Date Field**, **Time Field**, **Numerical Field**, or **Currency Field**. **Push Button** and **Image Button** can trigger macros—handy for validation or navigation logic. **Label** may look like plain text, but it can be linked to a macro so hovering or clicking does something useful. **File Selection** provides a browse dialog for picking files, and **Spin Button** lets users cycle through a number range.

Double-click any control to open its **Properties** dialog, which has three tabs: **General**, **Data**, and **Events**. For simple forms without a database, the General tab is usually all you need. The Form Design toolbar (**View > Toolbars > Form Design**) adds layout tools—**Align**, **Bring to Front/Send to Back**, **Activation Order** (the Tab key sequence), and **Form Navigator** for managing controls by name across the document.
