# Working with Paragraph Styles (LibreOffice Writer 7.3.7)

Paragraph styles are where you control the overall shape and behavior of your text blocks — indentation, spacing, alignment, page breaks, and more. You'll find most of what you need by right-clicking a style in the **Styles** deck under the **Paragraph Styles** category and choosing **Modify**. You can also start from **Format > Paragraph...** for one-off tweaks, but styles are the way to go for consistency.

## Indents and Spacing

The **Indents & Spacing** tab is your go-to for controlling how a paragraph sits on the page. **Before text** sets the left indent, **After text** sets the right indent, and **First line** controls whether the opening line is indented (positive value) or hanging (negative value). Check **Automatic** if you want Writer to calculate the first-line indent based on font size automatically.

See `fig01.png`.

Below the indent fields you'll find **Spacing**, where you set the gap above and below the paragraph. A common trick is to add space above heading styles so they visually separate from the preceding body text without needing empty paragraphs. If two consecutive paragraphs share the same style, you can tick **Do not add space between paragraphs of the same style** to keep them snug.

For **Line Spacing**, the default is **Single**, but **1.15 lines** or **Proportional** at around 115% often reads better. If you're mixing font sizes in one paragraph, choose **Fixed** or **At least** to keep lines evenly spaced.

## Alignment

On the **Alignment** tab you pick between Left, Right, Center, and Justified. When using Justified, Writer lets you decide how to handle the last line — left-aligned is the default, but you can center or fully justify it too. There's also a **Text to Text** vertical alignment option here, handy when you mix font sizes on a single line; choose between Automatic, Base line, Top, Middle, or Bottom.

## Text Flow

The **Text Flow** tab handles hyphenation, page breaks, and widow/orphan control. Under **Hyphenation**, set the minimum characters before and after a break and the maximum consecutive hyphenated lines. In the **Breaks** section, you can force a paragraph to start on a new page — set *Type* to **Page**, *Position* to **Before**, and optionally pick a page style with **With Page Style**. This is the classic way to start each chapter on a fresh page.

See `fig02.png`.

Under **Options**, enable **Do not split paragraph** to prevent a paragraph from breaking across pages, or use **Orphan control** and **Widow control** (typically set to 2 or 3 lines) to avoid stranded lines at the top or bottom of a page.

## Outline Level and Lists

The **Outline & List** tab lets you assign an outline level to any paragraph style, which means it will appear in the Navigator and can be included in a table of contents generated via **Tools > Chapter Numbering**. You can also associate a list style here to get automatic numbering or bullets.

## A Few More Useful Tabs

The **Position** tab controls superscript/subscript settings and paragraph rotation — handy for rotated headings in narrow table columns (set rotation to 90 or 270 degrees). The **Drop Caps** tab on the Paragraph Style dialog lets you enable a large initial letter spanning multiple lines, great for a first-paragraph flourish. And on the **Area** tab, you can add a background color, gradient, or pattern to the entire paragraph area — a quick way to create callout blocks without resorting to frames.

See `fig03.png` for the Drop Caps settings.

---

## UI Reference  —  Styles Menu & Styles Panel

_Scope: Paragraph Styles category (default view) in Styles panel with hierarchical tree_

LibreOffice Writer uses a style-based formatting system. The Styles menu provides quick-apply shortcuts, while the Styles panel (F11) offers full management.

Read the screenshot `ui-styles-menu.png` in this directory.

## Styles Menu

The menu has three radio-button sections for quick style application:

**Paragraph styles:**
- Body Text (Ctrl+0), Title, Subtitle, Heading 1 (Ctrl+1), Heading 2 (Ctrl+2), Heading 3 (Ctrl+3), Block Quotation, Preformatted Text

**Character styles:**
- No Character Style (default), Emphasis, Strong Emphasis, Quotation, Source Text

**List styles:**
- No List (Shift+Ctrl+F12), Bullet • List Style, Numbering 123/ABC/abc/IVX/ivx List Styles

**Management commands:**
- Edit Style… (Alt+P), Update Selected Style (Shift+Ctrl+F11), New Style from Selection (Shift+F11), Load Styles from Template, Manage Styles (F11)

## Styles Panel (F11 / Alt+2)

The Styles panel in the right sidebar provides full style management:

- **Category toolbar:** Paragraph Styles, Character Styles, Frame Styles, Page Styles, List Styles, Table Styles, Fill Format Mode, Styles actions ▼
- **Style list:** Hierarchical tree of all styles (Default Paragraph Style, Body Text, Caption, Heading, Index, etc.)
- **Right-click on a style:** New…, Edit Style…, Hide, Show, Delete…
- **Show Previews** / **Spotlight** checkboxes
- **Filter dropdown:** Hierarchical, All Styles, Hidden Styles, Applied Styles, Custom Styles, Automatic, Text/Document/List/Index/Special/HTML/Conditional Styles
- **Styles actions dropdown:** New Style from Selection, Update Selected Style, Load Styles from Template

