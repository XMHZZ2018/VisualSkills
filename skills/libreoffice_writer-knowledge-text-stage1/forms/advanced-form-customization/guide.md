# Advanced Form Customization (LibreOffice Writer 7.3.7)

Once you've built a basic form, the real power comes from wiring up macros, locking down permissions, and fine-tuning how each control looks and behaves. Here's how to take your forms further.

## Linking Macros to Form Controls

Any form control — text boxes, buttons, checkboxes — can trigger a macro in response to an event like a keystroke, mouse click, or focus change. First, write your macro (see the Getting Started Guide, Chapter 13 for the basics). Then, make sure you're in design mode, right-click the control, and choose **Control Properties** from the context menu. Switch to the **Events** tab, where you'll see a list of available events such as *Changed*, *Key pressed*, *Mouse moved*, and more.

See `fig01.png`.

Click the browse button next to any event to open the **Assign Action** dialog. Hit the **Macro** button, pick your macro from the Macro Selector, and confirm with **OK**. You can assign different macros to different events on the same control. If you need to attach macros to the form itself (rather than a single control), right-click the form control, select **Form Properties**, and use its **Events** tab instead.

See `fig02.png`.

## Read-Only Documents and Database Permissions

When your form is finished and you want users to interact with it without altering the layout, go to **File > Properties > Security** and select **Open file read-only**. The form still works — users can browse and enter data — but the document structure stays locked.

By default, a database connection lets users add, edit, and delete records freely. To tighten that up, right-click a form control in design mode, choose **Form Properties**, and open the **Data** tab. You'll find toggles for *Allow additions*, *Allow modifications*, *Allow deletions*, and *Add data only* — set each to **Yes** or **No** as needed. To protect an individual field (say, a stock quantity you don't want edited), right-click that specific control, select **Control** from the context menu, go to the *General* tab, and set *Read-only* to **Yes**.

See `fig03.png`.

## Form Control Formatting Options

You can customize the appearance and behavior of any control through its **Control Properties** dialog (right-click the control in design mode, *General* tab). Set a label in the *Label* box, choose whether the control prints with the document via the *Print* option, and use the *Font* setting to control typeface and size for fields. For text boxes, setting a *maximum text length* that matches the database field's limit prevents frustrating data-entry errors. You can also set default values, configure password-masking characters, add help text, and style controls with background colors, 3-D effects, scroll bars, and borders.
