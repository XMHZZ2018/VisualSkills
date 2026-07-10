# Built-in Language Tools (LibreOffice Writer 7.3.7)

Writer has a handful of built-in language tools that make life easier when you're working with multilingual documents or just want spelling and grammar checks to target the right language. The key idea is simple: you can tag any chunk of text — a word, a paragraph, or the whole document — with a specific language, and Writer will use the matching dictionaries for spell-checking, hyphenation, and AutoCorrect.

The main hub for this is **Tools > Language** on the menu bar. It gives you three scopes to choose from: **For Selection** applies the language to whatever text you've highlighted, **For Paragraph** targets the paragraph where your cursor sits, and **For All Text** changes the language for the entire document, including anything you type going forward. If the language you need isn't listed in the submenu, just click **More...** to open the Character dialog and pick from the full list. There's also a handy **Reset to Default Language** option that snaps everything back to whatever you set in **Tools > Options**.

See `fig01.png`.

You can also set the default language for new documents (or just the current one) via **Tools > Options > Language Settings > Languages**. Under *Default Languages for Documents*, pick your Western, Asian, or Complex text layout language. Be careful here — changes apply to all future documents unless you tick the **For the current document only** checkbox.

See `fig02.png`.

If the spelling checker doesn't seem to work for a particular language, look for a checkmark symbol next to it in the language list. No checkmark means no dictionary is installed — you can grab one through **Tools > Language > More Dictionaries Online**.

Sometimes you don't want spell-checking at all for certain text — code snippets, URLs, that kind of thing. Set the language for those passages to **None (Do not check spelling)** and Writer will skip right over them.

For paragraph-level control, you can bake a language right into a paragraph style. Open the style, go to the **Font** tab, and set the **Language** dropdown. This is great when you have a document mixing, say, English and French body text — just create styles like "Text Body-EN" and "Text Body-FR" and apply them as needed.

See `fig03.png`.

Finally, the quickest way to check or change the language is right on the **Status bar** at the bottom of the window. It shows the current language next to the page style. Click it to get a menu where you can switch languages for the selection or paragraph, toggle off spell-checking, or reset to the default — all without diving into any dialogs.
