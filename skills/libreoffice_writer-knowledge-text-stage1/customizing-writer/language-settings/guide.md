# Language Settings (LibreOffice Writer 7.3.7)

Getting your language settings right affects spell checking, hyphenation, currency, date formats, and more. There are three things you'll typically want to configure: dictionaries, locale and language options, and spelling/grammar behavior.

LibreOffice ships with several language modules out of the box, each of which can include a spelling dictionary, a hyphenation dictionary, and a thesaurus. If you need additional languages, head to **Tools > More Dictionaries Online** on the Menu bar — this opens your browser with links to downloadable dictionary packs. Just follow the prompts to install what you need.

To adjust your locale and document language, open the Options dialog (click the expansion symbol by **Language Settings**) and choose **Languages**. On the right-hand side you'll find settings for your user interface language, the locale (which controls number formatting, currency, and date patterns), and the default language for documents. If you're working in a mixed-language environment — say, an English interface but German locale for numbering and currency — you can set these independently. To apply a language change only to the file you currently have open, tick **For the current document only**.

See `fig01.png`.

For Asian languages (Chinese, Japanese, Korean) or complex text layout languages (Hindi, Thai, Hebrew, Arabic), enable the corresponding checkboxes under **Enhanced Language Support**. This will add extra pages to the Language Settings section the next time you open the Options dialog.

Spelling and grammar options live under **Language Settings > Writing Aids**. If you want on-the-fly spell checking, make sure **Check spelling as you type** is selected — you can also toggle this from **Tools > Automatic Spell Checking** on the Menu bar. For grammar checking as you type, enable **Check grammar as you type** as well. If you work with technical documents full of uppercase words or part numbers, consider ticking **Check uppercase words** and **Check words with numbers** so the checker doesn't skip them. **Check special regions** extends checking into headers, footers, frames, and tables.

See `fig02.png`.

The Writing Aids page also shows your available language modules (like Hunspell SpellChecker, Lightproof grammar checker, and MyThes Thesaurus) and any user-defined dictionaries. You can create new custom dictionaries here, edit existing ones, or delete ones you no longer need — though system-installed dictionaries can't be removed. A handy tip: words you add via "Add to Dictionary" during a spell check go into the standard dictionary, while words you mark "Ignore All" land in the List of Ignored Words dictionary.

For sentence-level grammar checking, LibreOffice uses checkers that are enabled by default for your system language. To fine-tune what gets flagged, go to **Language Settings > English Sentence Checking**, select **English spelling dictionaries**, and click **Options** to review the available rules. After changing grammar settings, restart LibreOffice or reload the document for them to take effect.
