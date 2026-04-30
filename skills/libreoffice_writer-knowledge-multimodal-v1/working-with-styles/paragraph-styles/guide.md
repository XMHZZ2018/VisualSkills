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
