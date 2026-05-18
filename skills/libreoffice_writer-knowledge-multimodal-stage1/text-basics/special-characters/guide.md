# Inserting Special Characters (LibreOffice Writer 7.3.7)

Sometimes you need characters that don't live on your keyboard — things like ©, ¼, ñ, or €. To insert them, place your cursor where the character should go, then either click the **Special Character** icon on the Standard toolbar or go to **Insert > Special Character**. The toolbar icon drops down a quick grid of your favorites and recently used characters — just click one to pop it in. If the one you need isn't there, hit **More Characters** to open the full dialog.

See `fig01.png`.

In the Special Characters dialog, you can browse any font's character set, search by name, and preview a character by single-clicking it (its Unicode value and name appear on the right). Double-click a character to insert it directly, or select it and click **Insert**. Characters you use get saved to the Recent Characters list automatically. If a character doesn't appear in the current font, try switching the **Font** dropdown — different fonts carry different symbol sets.

Beyond individual symbols, Writer gives you a handful of handy formatting marks via **Insert > Formatting Mark**. A **non-breaking space** (Ctrl+Shift+Space) glues two words together so they never split across lines. A **non-breaking hyphen** (Shift+Ctrl+Hyphen) does the same for hyphenated terms like "123-4567". There's also a **soft hyphen** (Ctrl+Hyphen), which is invisible unless the word needs to break at a line ending — useful for helping Writer hyphenate long words gracefully. For a **narrow no-break space** (slightly thinner than a regular space), press Alt+Shift while you type the space.

See `fig02.png`.

For **en and em dashes**, you can let AutoCorrect handle them. Under **Tools > AutoCorrect > AutoCorrect Options**, the Replace dashes option converts typed hyphens on the fly: type a word, a space, a hyphen, another space, and a word to get an en dash; skip the spaces around two hyphens to get an em dash. You can also insert them manually through **Insert > Special Characters** by selecting U+2013 (en dash) or U+2014 (em dash) from the *General punctuation* subset. On macOS, Option+Hyphen gives you an en dash and Shift+Option+Hyphen gives you an em dash. On Windows, hold Alt and type 0150 or 0151 on the numeric keypad.

Other marks in the Formatting Mark submenu — **No-width Optional Break**, **Word Joiner**, **Left-to-right Mark**, and **Right-to-left Mark** — are mainly relevant for complex text layout (CTL) languages, so you can safely ignore them for everyday Western-language documents.
