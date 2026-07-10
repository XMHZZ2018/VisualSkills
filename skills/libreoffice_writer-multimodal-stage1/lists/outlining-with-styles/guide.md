# Outlining with Paragraph Styles (LibreOffice Writer 7.3.7)

LibreOffice gives you a couple of ways to outline using paragraph styles. The most direct route is **Tools > Chapter Numbering**, where you pick a numbering style for each paragraph style to pull it into the outline hierarchy. Alternatively, you can pair each Heading style with a separate list style right from the Styles deck on the Sidebar.

If you'd rather keep things simple, just create a single list style for all your outlining. Set up the different levels on the list style's **Customize** tab manually, or pick a pre-defined pattern from the style's **Outline** tab and let Writer handle it.

Once you're working with a paragraph style that's tied to a list, pressing **Enter+Tab** adds a sub-level paragraph. The sub-level automatically picks up the numbering pattern from the list style. To promote a paragraph back up a level, hit **Enter+Shift+Tab**.

**Setting up a single paragraph style for outlining** is straightforward. First, create a list style and link it to one of the pre-defined formats on the **Outline** tab. Then pick or create a paragraph style — just avoid Heading 1–10, since those are reserved for the standard outline and mixing them up causes confusion. On the **Organizer** tab of your paragraph style, set **Next Style** to itself so new paragraphs stay in the same style. Finally, assign the list style to the paragraph style using the **Numbering** field on the style's **Outline & List** tab.

**Outline levels** are how Writer connects paragraph styles to higher-level features like the Navigator and table of contents. By default, the Heading 1–10 styles map to Outline Levels 1–10 (Heading 1 is Level 1, and so on). You can reassign or add your own paragraph styles to any outline level through the **Outline level** field on the **Outline & List** tab of the Paragraph Style dialog.

See `fig01.png`.

This is especially handy when you want custom-named styles (like "Chapter Title" or "Appendix Header") to appear in the Navigator and be picked up by auto-generated tables of contents — just assign them the appropriate outline level and they'll behave just like the built-in headings.
