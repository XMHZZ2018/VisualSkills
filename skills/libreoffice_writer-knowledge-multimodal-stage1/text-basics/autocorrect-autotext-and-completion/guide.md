# AutoCorrect, Word Completion, and AutoText (LibreOffice Writer 7.3.7)

Writer's AutoCorrect feature ships with a big list of common misspellings, typos, and special-character codes that it fixes on the fly as you type. It's on by default. If it ever gets in your way, you can disable it entirely by unchecking **Tools > AutoCorrect > While Typing**.

To customize what gets corrected, open **Tools > AutoCorrect > AutoCorrect Options** and head to the **Replace** tab. You'll see two columns — the typo on the left, its replacement on the right. Delete any pair you don't want by selecting it and clicking **Delete**, or add your own by typing into the **Replace** and **With** boxes and clicking **New**. This is also handy for inserting special characters: for instance, typing `:smiling:` can auto-replace with ☺.

See `fig01.png`.

Word Completion is a separate feature that watches what you type and offers to finish long words for you. Once you've typed a word at least twice in a document, Writer will suggest it in future — just press **Enter** to accept or keep typing to ignore. You can turn it off via **Tools > AutoCorrect > AutoCorrect Options**, then the **Word Completion** tab, where you uncheck **Enable word completion**. On that same tab you can tweak the minimum word length, the maximum number of remembered words, the acceptance key (choose from **Enter**, **End**, **Tab**, or **Space bar**), and whether completions appear inline or as a hover tip via **Show as tip**.

See `fig02.png`.

AutoText lets you store reusable chunks — text, tables, graphics, fields — and recall them with a short abbreviation. To create one, type and select the content in your document, then go to **Tools > AutoText** (or press **Ctrl+F3**). Give it a name, adjust the suggested shortcut if you like, pick a category such as *My AutoText*, then click the **AutoText** button and choose **New** (to keep original formatting) or **New (text only)**. Close the dialog and you're set.

To insert an AutoText entry later, just type its shortcut and press **F3** — the full content drops right in. If you want a printable list of all your entries, navigate to **Tools > Macros > Organize Macros > Basic**, expand **Gimmicks** under *Macro From*, select **AutoText**, and click **Run**.
