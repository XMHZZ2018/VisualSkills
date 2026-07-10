# Extensions and Macros (LibreOffice Writer 7.3.7)

LibreOffice lets you hook macros into events — things like opening a document, pressing a key, or moving the mouse. A common use is assigning the "open document" event to a macro that runs setup tasks automatically whenever you open a particular file. To wire this up, head to the **Events** tab of the **Customize** dialog. (For a deeper dive on writing macros themselves, check out Chapter 13 of the *Getting Started Guide*.)

## Adding functionality with extensions

Extensions are add-on packages you install into LibreOffice to get new capabilities. They can include template sets, spelling dictionaries, clipart galleries, macros, and dialog libraries. Some extensions add entirely new top-level menus, submenus, or toolbar icons, and they may bring their own settings panels accessible through the Extension Manager.

A handful of extensions ship bundled with LibreOffice and are baked into the program — those can only be removed by changing install options. Everything else comes from external sources. The official free repository lives at the LibreOffice extensions site. Some third-party extensions are free, others cost money, so check licenses before you grab one.

## Installing an extension

Download the extension file to any folder on your machine (the usual convention is a folder called *Download*). Then open **Tools > Extension Manager** from the menu bar. In the Extension Manager dialog, click **Get more extensions online** to browse the repository — a browser window opens where you can find and download what you need.
Once the file is saved locally, go back to the Extension Manager and click **Add**. Find and select the extension file, then click **Open**. You may be prompted to accept a license agreement. After installation completes, the extension appears in the Extension Manager list.

If your extension isn't from the official repository, just skip the online browsing step — download it yourself, then pick up from the **Add** button as described above.

## Updating extensions

To check for newer versions of your installed extensions, click the **Check for Updates** button in the Extension Manager dialog. LibreOffice will look for available updates and walk you through applying them.

## Resetting keyboard shortcuts

If you've reassigned shortcut keys and want to start fresh, open the **Customize** dialog and click the **Reset** button. This restores all keyboard shortcuts to their defaults immediately — no confirmation dialog, so use it deliberately.
