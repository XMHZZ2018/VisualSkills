# Inserting Page Breaks (LibreOffice Writer 7.3.7)

Writer automatically flows text from one page to the next as you add or remove content. Most of the time that's exactly what you want — but sometimes you need to take control and force a break at a specific spot. Here's how.

## Controlling automatic page flow

Before inserting manual breaks, know that Writer gives you a few paragraph-level options to influence how text flows. Open the Paragraph dialog by right-clicking and choosing **Paragraph > Paragraph**, then head to the **Text Flow** tab.

Turn on **Keep with next paragraph** to glue a heading to the paragraph that follows it, preventing an awkward split across pages. **Do not split paragraph** does what it says — keeps an entire paragraph on one page. You can also use **Orphan control** and **Widow control** here to avoid stray single lines at the top or bottom of a page.

See `fig01.png`.

If you want a paragraph to *always* start on a new page — chapter titles are the classic case — set that up in a paragraph style rather than inserting manual breaks everywhere. See the paragraph style's Text Flow options for details.

## Inserting a break without changing the page style

Sometimes you just need a simple page break — say, to push a heading to the top of the next page. Click where you want the new page to begin and go to **Insert > More Breaks > Manual Break**. In the dialog, **Page break** is preselected by default, and **Style** is set to [None]. Just click **OK** and you're done.

## Inserting a break and switching to a new page style

If the new page needs a different page style — switching from a First Page style to Left Page, for instance — use the same **Insert > More Breaks > Manual Break** path. This time, open the **Style** drop-down in the *Type* section and pick the page style you want for the next page.

A word of caution: don't try to change a page style for a single page without inserting a page break. Doing so can unexpectedly change the style of other pages in your document.
