# Configuring FFmpeg (OpenToonz 1.7)

OpenToonz needs FFmpeg installed separately to export animations as **mp4**, **webm**, or **gif** (gif on Mac/Linux only). It's not bundled, so you'll grab it yourself and point OpenToonz to it.

**Windows:** Download a static build from ffmpeg.org — pick the Windows icon, grab the Windows builds link, and hit **Download Build**. The defaults are fine. Unzip the archive, find the **bin** folder inside, and copy its contents into a new folder at **C:\FFmpeg**. That's the path OpenToonz will need.

**Mac:** Same site, but click the Apple icon and grab **Static and Shared builds** (make sure **macOS 64-bit** is selected). Unzip and copy the **bin** contents into **/Applications/OpenToonz/FFmpeg**. On macOS 10.15+, you'll need to right-click each executable (ffmpeg, ffprobe, etc.) and choose **Open With > Terminal** once to clear the Gatekeeper warning — after that you can close Terminal.

**Linux:** Install via your package manager (`pacman -S extra/ffmpeg`, `apt install ffmpeg`, `emerge media-video/ffmpeg`, etc.). Run `which ffmpeg` in a shell to confirm the path — it's usually **/usr/bin**.

Once the binaries are in place, open OpenToonz and go to **File > Preferences…**, then navigate to the **Import/Export** category. You'll see an **FFmpeg Path** field at the top — enter the folder path where you put the executables (e.g., `C:\FFmpeg`, `/Applications/OpenToonz/FFmpeg`, or `/usr/bin`).

Restart OpenToonz, then check **Render > Output Settings…** — in the **File Settings** section, the format dropdown should now include **mp4** and **webm** (plus **gif** on Mac and Linux). You're all set to render video directly.
