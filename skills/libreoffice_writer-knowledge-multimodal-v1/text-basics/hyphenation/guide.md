# Hyphenating Words (LibreOffice Writer 7.3.7)

Writer gives you two ways to hyphenate words at the end of a line: let it happen automatically through paragraph styles and hyphenation dictionaries, or insert soft hyphens manually right where you want them. You can also just skip hyphenation entirely — it's up to you.

## Automatic hyphenation

Automatic hyphenation is style-driven and overrides whatever you set under **Tools > Options**. To turn it on, click the **Styles** tab on the Sidebar to open the Styles deck. In the Paragraph Styles list, right-click **Default Paragraph Style** and choose **Modify**. In the dialog that opens, go to the **Text Flow** tab and look for the *Hyphenation* section — select or deselect **Automatically**. When it's on, you can also set criteria like how many characters to leave before or after a line break. Hit **OK** to save.

See `fig01.png`.

Keep in mind that turning on hyphenation for the *Default Style* affects all paragraph styles based on it. If you don't want headings hyphenated, for example, you can individually change those styles. Styles not based on Default Style won't be affected at all.

You can fine-tune hyphenation behavior globally under **Tools > Options > Language Settings > Writing Aids**. These settings only kick in when there's no specific setting in a paragraph style and automatic hyphenation is already enabled. Near the bottom of the Options area, you'll find controls for the minimum number of characters for hyphenation, characters before/after a line break, and more. Select an item and click **Edit** to change it.

See `fig02.png`.

Two handy options live here: **Hyphenate without inquiry** (Writer silently hyphenates words the dictionary doesn't recognize, instead of prompting you) and **Hyphenate special regions** (extends hyphenation into footnotes, headers, and footers).

## Manual hyphenation

When you need precise control, use a soft hyphen. Unlike a regular hyphen, a soft hyphen only appears when the word actually falls at the end of a line — if the text reflows, it vanishes. Place your cursor where you'd like the break and press **Ctrl+hyphen (minus sign)**, or go to **Insert > Formatting Mark > Insert Soft Hyphen**. The word will break at that spot when it lands at line's end, even if automatic hyphenation is off for that paragraph.
