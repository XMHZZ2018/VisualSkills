# Slideshow Configuration (LibreOffice Impress 7.3.7)

The heart of slideshow configuration lives in one dialog. Open it via **Slide Show > Slide Show Settings** on the Menu bar — but first, switch to **Slide Sorter** view (**View > Slide Sorter**) so you can see all your slides at a glance while you work.

See `fig01.png`.

In the **Range** section, decide which slides to include. *All slides* is the default; *From* lets you skip introductory slides by picking a starting point from the drop-down; and *Custom slide show* plays back a curated subset you've defined elsewhere via **Slide Show > Custom Slide Show**.

Under **Presentation Mode**, pick how the show runs. *Full screen* is the standard choice — it hides the Impress UI and ends after the last slide. *In a window* keeps the show inside the application frame, handy for demos where you need access to other apps. The real star for kiosk setups is *Loop and repeat after*: select it and enter a pause duration in the time box. The show will cycle continuously, displaying a pause slide between loops. Set the delay to zero and it restarts immediately with no pause. Check **Show logo** if you want the LibreOffice logo on that pause slide.

Before *Loop and repeat after* will actually work, you need automatic slide advancement configured. Open the **Slide Transition** deck in the Sidebar, make sure the *After* option is selected under **Advance Slide**, and set a time interval for each slide. Without that timing, looping has nothing to act on and the option silently does nothing.

The **Options** checkboxes fine-tune behavior. Uncheck *Change slides manually* if you want automatic transitions to drive everything — leaving it checked blocks auto-advance even when timings are set. *Animations allowed* controls whether animated GIFs play all frames. *Change slides by clicking on background* lets a click or spacebar press advance slides, which you'll probably want off for an unattended kiosk. *Presentation always on top* keeps other windows from covering your show.

For default timing across all slides, open the **Slide Transition** deck, set the transition to *None*, choose *After* in **Advance Slide** with your desired seconds, then click *Apply Transition to All Slides*. Preview the result with **Slide Show > Start from First Slide**. If you'd rather set per-slide timing by feel, use **Slide Show > Rehearse Timings** — Impress will run the show with a timer and record how long you spend on each slide.

To launch the finished show, press **F5** to start from the first slide, or **Shift+F5** to start from the current one. During playback, right-click for navigation options like **Go to Slide**, **Mouse Pointer as Pen**, or **Screen** (which lets you blank to black or white for a break). Press **Esc** at any time to bail out.

If you have a dual-monitor setup, the **Presenter Console** gives you a private control view on your laptop — showing the current slide, the next slide, your notes, and an elapsed timer — while the audience sees only the full-screen presentation.

See `fig02.png`.

---

## UI Reference  —  Slide Show Menu

_Scope: Slide Show Settings dialog (Range, Presentation Mode, Options), Rehearse Timings, Custom Slide Show_

The Slide Show menu controls presentation playback, rehearsal timings, custom shows, and presentation settings.

Read the screenshot `ui-slideshow-menu.png` in this directory.
Read the screenshot `ui-slideshow-settings-dialog.png` in this directory.

## Elements

- **Start from First Slide** (F5) — Launch full-screen presentation from slide 1
- **Start from Current Slide** (Shift+F5) — Launch from the currently selected slide
- **Rehearse Timings** — Run slideshow in rehearsal mode, recording per-slide timings
- **Custom Slide Show...** — Create, edit, copy, delete, or start named subsets of slides
- **Slide Show Settings...** — Opens the Slide Show Settings dialog (see below)

## Slide Show Settings Dialog

(see screenshot `ui-slideshow-settings-dialog.png`)

### Range
- All slides (default) / From: Slide N / Custom slide show

### Presentation Mode
- Full screen (default) / In a window / Loop and repeat after HH:MM:SS
- Show logo during pause (only with Loop mode)

### Presentation Options
- Disable automatic change of slides
- Change slides by clicking on background ✓
- Mouse pointer visible / Mouse pointer as pen
- Enable animated images ✓
- Keep Presentation always on top

### Display
- Presentation display dropdown
- Presenter console: Full screen
- Show navigation bar, Buttons size (Automatic)

### Remote Control
- Enable remote control, Download App link, Enable insecure WiFi connections

---

## UI Reference  —  Standard Toolbar

_Scope: Presentation button (F5) to start slideshow_

The first icon row below the menu bar. Provides quick access to common file and editing operations.

Read the screenshot `ui-standard-toolbar.png` in this directory.

## Elements

Row (left → right):

- **New** (dropdown ▾) — Create a new document (dropdown lists all document types)
- **Open** (dropdown ▾) — Open an existing file; dropdown shows recent documents
- **Save** (dropdown ▾) — Save the current document
- **Email Document** — Send document via email
- **Edit File** — Toggle read-only / edit mode
- **PDF** — Export directly as PDF
- **Print** — Print the document
- **Cut** / **Copy** / **Paste** — Clipboard operations
- **Paint Format** (Clone Formatting) — Copy formatting to other objects
- **Undo** / **Redo** — Step through undo/redo history
- **Find & Replace** — Open Find and Replace dialog
- **Spelling** — Run the spelling checker
- **Display Views** — Normal, Outline, Notes, Slide Sorter mode toggles
- **Presentation** — Start slideshow (F5)
- **Table** / **Insert Chart** / **Insert Text Box** — Quick insertion tools
- **Hyperlink** — Insert or edit hyperlinks
- **Sidebar** — Toggle the Properties sidebar
- **Start Center** — Return to the LibreOffice Start Center

