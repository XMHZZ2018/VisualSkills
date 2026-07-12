# Creating Keyboard Shortcuts (GIMP 2.10)

GIMP gives you two ways to assign keyboard shortcuts: a quick dynamic method right in the menus, and a dedicated dialog for more control. Both work well — pick whichever fits the moment.

**The quick way: dynamic shortcuts.** Head to **Edit > Preferences**, open the **Interface** section, and enable **Use dynamic keyboard shortcuts**. While you're there, check **Save keyboard shortcuts on exit** so nothing gets lost. Now you can assign a shortcut on the fly — just hover over any menu command so it highlights, hold still, and press your desired key combination. The shortcut appears immediately to the right of the command. Stick with **Ctrl+Alt+Key** combos for custom shortcuts to avoid colliding with built-in ones.

**The dedicated dialog.** Open it via **Edit > Keyboard Shortcuts…** (or from Preferences, click **Configure Keyboard Shortcuts…**). This dialog lets you assign shortcuts not just to menu commands but also to tools, filters, and other actions — no preference toggle needed.

See `fig01.png`.

The dialog lists action categories on the left — expand them with **+** to browse available commands. Use the **Search** field at the top if you already know what you're looking for. Each action shows its current shortcut or "Disabled" if none is set.

To assign a shortcut, click the action's row. The shortcut column changes to "New accelerator…" — now just press the key combination you want. If that combo is already taken, GIMP will tell you which action owns it and let you reassign or cancel.

See `fig02.png`.

To remove a shortcut, select the action and press **Backspace** to clear it.

At the bottom, the **Save keyboard shortcuts on exit** checkbox controls whether changes persist automatically. You can also hit **Save** to write changes immediately without closing the dialog, or **Close** to keep your changes active for the current session only.
