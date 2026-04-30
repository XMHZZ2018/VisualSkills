# Defining a Different First Page (LibreOffice Writer 7.3.7)

Many documents — letters, memos, reports — need a first page that looks different from the rest. A letterhead might have a unique header, or a report's first page might skip the header and footer entirely. Writer gives you a few ways to pull this off.

**The simplest approach: one page style.** If you just need different headers or footers on the first page, you can stick with the Default page style. Right-click anywhere on the page, choose **Page Style**, then go to the **Header** or **Footer** tab. Turn on **Header on** (or **Footer on**), and deselect **Same content on first page**. You can optionally deselect **Same content on left and right pages** too. Now just type your first-page header or footer content on page one, and different content on any subsequent page — Writer keeps them independent.

See `fig01.png`.

**The more flexible approach: separate page styles.** Writer ships with a built-in *First Page* style and a *Default* style that work as a pair. The idea is that the First Page style automatically flows into the Default style for every page after it. To set this up, open the Page Style dialog for the First Page style, go to the **Organizer** tab, and set the **Next style** dropdown to **Default Style**. Now your first page uses one style, and everything after it switches automatically.

See `fig02.png`.

**The quick route: title pages.** If you want to convert existing pages into title pages (or insert new ones), head to **Format > Title Page**. This dialog lets you choose how many title pages to add, where to place them, and whether to restart page numbering afterward. You can also pick which page style to apply. It's especially handy for books or long documents where you need title, copyright, and decorative pages up front before the main content begins.

See `fig03.png`.

Between these three methods — toggling first-page content within one style, chaining two page styles together, or using the Title Page feature — you can handle just about any first-page scenario Writer throws at you.
