# Saving and Protecting Documents (LibreOffice Writer 7.3.7)

You can save a document in Writer using several commands, and the differences matter. **File > Save** keeps the current filename and location. **File > Save As** (or Ctrl+Shift+S) lets you pick a new name, location, or file format. If you need to stash a copy while keeping the original open, use **File > Save a Copy** — the copy is saved but never opened. And **File > Save All** saves every open document in one go. For remote files, **File > Save Remote** stores the document on a remote server directly.

Writer can automatically save recovery copies at regular intervals. Head to **Tools > Options > Load/Save > General**, tick **Save AutoRecovery information every**, and set your preferred interval (the default is 10 minutes). While you're there, consider enabling **Always create backup copy** for an extra safety net.

If you need to share files with Microsoft Office users, go to **File > Save As** and pick a `.docx` format from the **File type** drop-down. Note that any changes you make from that point on will only appear in the Word version — you'd need to reopen the `.odt` original to keep working in ODF. To default to Word format permanently, go to **Tools > Options > Load/Save > General**, find **Default File Format and ODF Settings**, set **Document type** to *Text document*, and choose your preferred Word format under **Always save as**.

Writer offers two kinds of document protection: password-based and OpenPGP encryption. To password-protect a file, use **File > Save As** and tick the **Save with password** checkbox in the lower-left corner, then click **Save**.

See `fig01.png`.

A Set Password dialog appears with two sections. Enter a password in the **File Encryption Password** fields to fully lock the file — nobody opens it without the password. For a lighter touch, click **Options**, select **Open file read-only** under *File Sharing Password*, and optionally set a separate editing password so some people can read while others can also edit.

See `fig02.png`.

Be warned: LibreOffice uses strong encryption, so if you lose the password, the document is effectively gone. To change or remove a password later, open the document and go to **File > Properties > General**, then click **Change Password**.

For OpenPGP encryption, you'll need GPG software and a personal key pair already set up on your system. In the **Save As** dialog, select **Encrypt with GPG key** instead of (or alongside) the password option, click **Save**, and choose the recipient's public key from the list that appears. The recipient must have the corresponding private key to decrypt the file.

Writer can also open and save files on remote servers over FTP, WebDAV, Windows Share, SSH, or cloud services like Google Drive and Microsoft OneDrive. For details on setting up remote connections, see the *Getting Started Guide*.
