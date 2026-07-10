# Slide Dimensions (LibreOffice Impress 7.3.7)

To change your slide size, aspect ratio, or orientation, open the Slide Properties dialog. Go to **Slide > Slide Properties** on the Menu bar, or just right-click an empty area of the slide and choose **Slide Properties** from the context menu. Make sure you're in **Normal** view first.

In the dialog, click the **Slide** tab. The *Format* dropdown gives you predefined sizes — things like **Screen 16:9**, **Screen 4:3**, **Letter**, **A4**, and so on. Pick one and the *Width* and *Height* fields update automatically. If none of the presets fit, you can type custom dimensions directly into those fields.

See `fig01.png`.

Orientation is right there in the same dialog — just toggle between **Portrait** and **Landscape**. This affects the slide canvas itself, not the printed handout orientation. Hit **OK** when you're done and the change applies immediately.

There's also a quicker route if you just need to swap format or orientation without the full dialog. Open the **Properties** deck in the Sidebar, then expand the **Slide** panel. You'll find dropdowns for *Format* and *Orientation* that apply changes on the fly — no OK button needed.

See `fig02.png`.

One thing to keep in mind: changing the slide size affects every slide in your presentation, not just the current one. If you switch from 16:9 to 4:3 on a deck that already has content, objects may shift or get clipped. It's worth doing this early, ideally before you've laid out your content. If you do change it later, check each slide to make sure nothing looks off.

You can also tick **Fit object to paper format** in the Slide Properties dialog to have Impress attempt to scale objects when the slide size changes. The margins and layout settings in the same dialog mostly matter for printing — for on-screen presentations, the defaults (zero margins) are usually fine.

---

## UI Reference  —  Slide Menu

_Scope: Slide Properties... entry opening Slide Properties dialog_

The Slide menu manages slide creation, duplication, deletion, layout, master slides, visibility, and transitions.

Read the screenshot `ui-slide-menu.png` in this directory.

## Elements

- **New Slide** (Ctrl+M) — Insert a blank slide after the current one
- **Duplicate Slide** — Create an identical copy of the current slide
- **Insert Slide from File...** — Import slides from another presentation
- **Layout** `▸` — 16 layout options: Blank Slide, Title Only, Title Slide, Title Content, Centered Text, Title and 2 Content, Title Content and 2 Content, Title 2 Content and Content, Title Content over Content, Title 2 Content over Content, Title 4 Content, Title 6 Content, Vertical Title Vertical Text, Vertical Title Text Chart, Title Vertical Text, Title 2 Vertical Text Clipart
- **Delete Slide** — Remove the selected slide (only available with 2+ slides)
- **Save Background Image...** — Save slide background (greyed unless custom background set)
- **Set Background Image...** — Set a background image for the slide
- **Slide Properties...** — Opens Slide Properties dialog (Slide, Background, Transparency tabs)
- **Change Slide Master...** — Change the master slide template
- **New Master** / **Delete Master** — Create or remove master slides
- **Master Background** ✓ / **Master Objects** ✓ — Toggle master background/objects visibility
- **Master Elements...** — Edit master slide elements
- **Show Slide** / **Hide Slide** — Toggle slide visibility during slideshow
- **Rename Slide...** — Rename the slide (opens dialog with name field)
- **Jump to Last Edited Slide** (Shift+Alt+F5) — Navigate to last edited slide
- **Move** `▸` — Slide to Start, Slide Up, Slide Down, Slide to End (context-sensitive)
- **Navigate** `▸` — To First/Previous/Next/Last Slide (context-sensitive)
- **Summary Slide** / **Expand Slide** — (greyed in normal conditions)
- **Slide Transition** — Opens the Slide Transition sidebar panel

---

## UI Reference  —  Slide Properties Dialog

_Scope: Slide tab: Paper Format dropdown, Width/Height spinners, Orientation, Fit object to paper format_

A multi-tab dialog for configuring slide dimensions, background, and transparency. Opened via Slide > Slide Properties or right-click > Slide Properties on a slide thumbnail.

Read the screenshot `ui-slide-properties-dialog.png` in this directory.

## Tabs

### Slide Tab
- **Paper Format**: Format dropdown (e.g., "Screen 16:9"), Width/Height spinners
- **Orientation**: Portrait / Landscape radio buttons
- **Paper tray**: Dropdown ([From printer settings])
- **Margins**: Left, Right, Top, Bottom spinners (default 0.00")
- **Layout Settings**: Slide numbers dropdown (1, 2, 3, ...)
- **Fit object to paper format** ✓
- **Background covers margins** (unchecked)

### Background Tab
- **None** (default) / **Color** / **Gradient** / **Image** / **Pattern** / **Hatch** buttons
- Preview area on the right

### Transparency Tab
- **No transparency** (default) / **Transparency** (50% spinner) / **Gradient** (Type, Center X/Y, Angle, Start/End value)
- Preview area on the right

Buttons: Help, Reset, Cancel, OK

