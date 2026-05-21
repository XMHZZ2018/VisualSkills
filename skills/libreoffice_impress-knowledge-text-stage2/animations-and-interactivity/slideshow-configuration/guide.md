# Slideshow Configuration (LibreOffice Impress 7.3.7)

The heart of slideshow configuration lives in one dialog. Open it via **Slide Show > Slide Show Settings** on the Menu bar — but first, switch to **Slide Sorter** view (**View > Slide Sorter**) so you can see all your slides at a glance while you work.

The Slide Show Settings dialog is displayed over the Slide Sorter view, which shows a grid of slide thumbnails in the main area. The dialog is divided into several grouped sections: **Range** at the top-left with radio buttons for "All slides," "From:" (with a slide drop-down), and "Custom Slide Show"; **Presentation Mode** below it with radio buttons for "Full Screen," "In a window," and "Loop and repeat after" (with a time-entry spinner); and an **Options** area on the right containing a series of checkboxes that control slide advancement, animation, mouse pointer behavior, and window stacking. A **Display** section at the bottom offers a dropdown to select the presentation monitor and checkboxes for the Presenter Console and navigation bar.

In the **Range** section, decide which slides to include. *All slides* is the default; *From* lets you skip introductory slides by picking a starting point from the drop-down; and *Custom slide show* plays back a curated subset you've defined elsewhere via **Slide Show > Custom Slide Show**.

Under **Presentation Mode**, pick how the show runs. *Full screen* is the standard choice — it hides the Impress UI and ends after the last slide. *In a window* keeps the show inside the application frame, handy for demos where you need access to other apps. The real star for kiosk setups is *Loop and repeat after*: select it and enter a pause duration in the time box. The show will cycle continuously, displaying a pause slide between loops. Set the delay to zero and it restarts immediately with no pause. Check **Show logo** if you want the LibreOffice logo on that pause slide.

Before *Loop and repeat after* will actually work, you need automatic slide advancement configured. Open the **Slide Transition** deck in the Sidebar, make sure the *After* option is selected under **Advance Slide**, and set a time interval for each slide. Without that timing, looping has nothing to act on and the option silently does nothing.

The **Options** checkboxes fine-tune behavior. Uncheck *Change slides manually* if you want automatic transitions to drive everything — leaving it checked blocks auto-advance even when timings are set. *Animations allowed* controls whether animated GIFs play all frames. *Change slides by clicking on background* lets a click or spacebar press advance slides, which you'll probably want off for an unattended kiosk. *Presentation always on top* keeps other windows from covering your show.

For default timing across all slides, open the **Slide Transition** deck, set the transition to *None*, choose *After* in **Advance Slide** with your desired seconds, then click *Apply Transition to All Slides*. Preview the result with **Slide Show > Start from First Slide**. If you'd rather set per-slide timing by feel, use **Slide Show > Rehearse Timings** — Impress will run the show with a timer and record how long you spend on each slide.

To launch the finished show, press **F5** to start from the first slide, or **Shift+F5** to start from the current one. During playback, right-click for navigation options like **Go to Slide**, **Mouse Pointer as Pen**, or **Screen** (which lets you blank to black or white for a break). Press **Esc** at any time to bail out.

If you have a dual-monitor setup, the **Presenter Console** gives you a private control view on your laptop — showing the current slide, the next slide, your notes, and an elapsed timer — while the audience sees only the full-screen presentation.

The Presenter Console is shown as a dark-themed control window divided into distinct panels. The left side displays a large preview of the current slide being presented. To the upper-right is a smaller thumbnail of the next slide in the sequence. Below the next-slide preview is a notes area showing the speaker's notes for the current slide. Along the bottom of the console, an elapsed-time counter and navigation controls (previous/next buttons) are visible, giving the presenter full playback control without the audience seeing any of it.

---

## UI Reference  —  Slide Show Menu

_Scope: Slide Show Settings dialog: Range, Presentation Mode (loop/kiosk), Options; Rehearse Timings; Custom Slide Show_

The Slide Show menu controls presentation playback, rehearsal timings, custom shows, and presentation settings.

The Slide Show drop-down menu on the Menu bar is shown expanded, listing the following entries from top to bottom: **Start from First Slide** (with the keyboard shortcut F5), **Start from Current Slide** (Shift+F5), a separator, **Rehearse Timings**, **Custom Slide Show...**, and **Slide Show Settings...**. Each entry appears as a standard menu item in the LibreOffice menu style.

The Slide Show Settings dialog is displayed with all its configuration sections visible. At the top-left, the **Range** group provides three radio buttons: "All slides" (selected by default), "From:" with a slide-number drop-down, and "Custom Slide Show" with its own drop-down. Below that, the **Presentation Mode** group offers "Full Screen" (selected by default), "In a window," and "Loop and repeat after" with a time spinner and a "Show logo" checkbox. On the right side, the **Options** group lists checkboxes for disabling automatic slide changes, changing slides by clicking on background, mouse pointer visibility, mouse pointer as pen, enabling animated images, and keeping the presentation always on top. At the bottom, a **Display** section contains a monitor-selection drop-down and Presenter Console options, followed by a **Remote Control** section with an "Enable remote control" checkbox and related settings. Standard OK, Cancel, and Help buttons appear along the bottom edge.

## Elements

- **Start from First Slide** (F5) — Launch full-screen presentation from slide 1
- **Start from Current Slide** (Shift+F5) — Launch from the currently selected slide
- **Rehearse Timings** — Run slideshow in rehearsal mode, recording per-slide timings
- **Custom Slide Show...** — Create, edit, copy, delete, or start named subsets of slides
- **Slide Show Settings...** — Opens the Slide Show Settings dialog (see below)

## Slide Show Settings Dialog

The dialog is organized into clearly labeled group boxes. The **Range** group at the top-left contains radio buttons and associated drop-downs for selecting which slides to present. The **Presentation Mode** group beneath it contains radio buttons for full screen, windowed, and looping modes, with a time spinner for loop delay and a "Show logo" checkbox. The **Options** group on the right-hand side presents a column of checkboxes governing slide advancement, pointer behavior, animation, and window stacking. The **Display** group at the bottom offers a dropdown for choosing the output monitor, plus checkboxes and controls for the Presenter Console and an on-screen navigation bar. A **Remote Control** section at the very bottom provides options for enabling remote control of the slideshow, including a link to download the companion app.

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
