# Editing and Cross-Referencing (LibreOffice Writer 7.3.7)

Once your master document is set up, you'll inevitably need to edit it — and eventually link pieces of it together with cross-references. Here's how both of those work.

**Editing the master document's appearance** comes down to one rule: make style changes in the *template*, not in the master document or any subdocument. When you reopen the master document after changing the template, Writer will ask whether to update links and apply changed styles — answer **Yes** to both prompts and everything cascades through.

You can't edit a subdocument's text directly inside the master document. Instead, double-click the subdocument in the Navigator (or just open the file separately). Edit it like any normal Writer document. If you change content, remember to manually update the table of contents, bibliography, and index from within the master document afterward.

**To add a subdocument**, re-insert it through the Navigator as you did during initial setup. To delete one, right-click its filename in the Navigator and choose **Delete**. If you rename a subdocument's file, the Navigator will show a broken link in red — right-click it, choose **Edit link**, point to the renamed file in the Edit Sections dialog, and click **OK**.

See `fig01.png` for the Edit Sections dialog.

**Cross-referencing between subdocuments** is more involved but entirely doable. The idea is to set a *target* in one subdocument and then insert a *reference* to that target from another. Note: this technique works correctly in the master document but may show an error if the subdocument is opened standalone.

Start by preparing the target. You can use bookmarks or set references. For a bookmark, select the target text and go to **Insert > Bookmark**, name it, and click **Insert**. For a set reference — which is more flexible since it works with headings and figure captions — open the target subdocument, click **Insert > Cross-Reference**, pick **Set Reference** in the *Type* list, highlight the heading or text you want to reference, give it a unique name in the *Name* box, and click **Insert**.

See `fig02.png` for the Fields dialog with Set Reference selected.

Now for the actual cross-reference. Open the master document, right-click the subdocument you want to insert the reference *into*, and choose **Edit**. Place your cursor where the reference should appear and go to **Insert > Cross Reference**. On the *Cross-references* tab, select **Insert Reference** in the *Type* list, choose **Reference** under *Insert reference to*, then find the target name you created earlier in the *Selection* list. Type that name into the *Name* field and click **Insert**.

See `fig03.png` for the Fields dialog with Insert Reference type and the target name selected.

That's it — Writer will resolve the reference when you view or print the master document, pulling in the correct chapter number, page number, or heading text from across subdocuments.
