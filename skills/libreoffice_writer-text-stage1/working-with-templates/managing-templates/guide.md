# Managing Templates (LibreOffice Writer 7.3.7)

You can only edit templates you created or imported — the ones bundled with LibreOffice are off limits. To edit one, open the Templates dialog via **File > Templates > Manage Templates**, find your template, right-click it, and hit **Edit**. It opens right in Writer like any other document; save your changes with **File > Save**.

If you've tweaked a template's styles, the next time you open a document based on that template you'll get a prompt. Choose **Update Styles** to pull the new styles into the document, or **Keep Old Styles** to leave it alone. Be aware that choosing **Keep Old Styles** detaches the document from its template entirely, even though the template is still listed under **File > Properties > General**.

To reassign a template to an existing document, the manual route works fine: open the Templates dialog, double-click the new template (a blank document opens with its styles), then **File > Save As** that new document. Now open your old document, select everything with **Edit > Select All**, copy it, click into the new document, paste, and save. Close the old file without saving.

To set a custom template as the default for new documents, open the Templates dialog, right-click the template you want, and select **Set as Default** from the context menu. An icon marks it as the default. From then on, **File > New** creates documents from that template.

See `fig01.png` for the default template icon badge.

To revert to Writer's built-in default, open the Templates dialog, click the **Manage** button in the upper right, and choose **Reset Default Text Document** from the drop-down.

See `fig02.png`.

Organizing your templates into categories keeps things tidy. Go to **File > Templates > Manage Templates**, click **Manage**, then **New Category** to create one. You can rename or delete categories you created (not the built-in ones) through the same **Manage** menu. To move a template between categories, right-click it, choose **Move**, pick the destination category, and click **OK**.

Renaming and deleting templates also happens via right-click in the Templates dialog — just select **Rename** or **Delete**. You can only do this with templates you created or imported; built-in and extension-installed templates are protected. To export a template to another location, right-click it, choose **Export**, and pick a destination folder.

You can also work with templates outside the Templates dialog. Double-clicking an .ott file in your file browser creates a new document from it, though that document won't be linked back to the template. And if you want to save any document as a template, use **File > Save As** and pick *ODF Text Document Template (.ott)* as the file type. To make it appear in the Templates dialog, either import it or place it in one of the template paths listed under **Tools > Options**.
