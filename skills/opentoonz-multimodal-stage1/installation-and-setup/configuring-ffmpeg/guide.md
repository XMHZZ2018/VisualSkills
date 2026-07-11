# Configuring FFmpeg (OpenToonz 1.7)

OpenToonz doesn't ship with video encoding built in. To render your animation as **mp4**, **webm**, or **gif** (Mac/Linux), you need to install FFmpeg separately and point OpenToonz to it.

**On Windows**, grab the latest build from ffmpeg.org — click the Windows icon, follow the **Windows builds** link, and hit the blue **Download Build** button (the defaults are fine). Unzip the archive, find the **bin** folder inside, and copy its contents (`ffmpeg.exe`, `ffplay.exe`, `ffprobe.exe`) into a new folder at **C:\FFmpeg**.

See `fig01.png`.

**On Mac**, same idea — grab the macOS 64-bit static build from the download page. Create an **FFmpeg** folder inside **/Applications/OpenToonz/** and drop the bin contents there. One extra wrinkle for macOS 10.15+: you need to right-click each executable in Finder, choose **Open With > Terminal**, and let it launch once. This clears the Gatekeeper quarantine so OpenToonz can actually call them later.

**On Linux**, just install from your package manager — `apt install ffmpeg`, `pacman -S extra/ffmpeg`, or equivalent. The binary usually lands at `/usr/bin/ffmpeg`; run `which ffmpeg` if you're unsure.

Once FFmpeg is in place, open OpenToonz and go to **File > Preferences…**, then navigate to the **Import/Export** category. You'll see an **FFmpeg Path** field at the top — enter the folder path where your FFmpeg executables live (e.g., `C:\FFmpeg` on Windows, `/Applications/OpenToonz/FFmpeg` on Mac, or `/usr/bin` on Linux).

See `fig02.png`.

Restart OpenToonz after setting the path. To confirm it worked, open **Render > Output Settings…** and check the format dropdown in the **File Settings** section — **mp4** and **webm** should now appear in the list (plus **gif** on Mac and Linux).

See `fig03.png`.
