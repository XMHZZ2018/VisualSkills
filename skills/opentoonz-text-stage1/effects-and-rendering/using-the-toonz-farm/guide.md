No images referenced in this page. The source is text-only. Here's the guide:

# Using the Toonz Farm (OpenToonz 1.7)

The Toonz Farm distributes cleanup and render tasks across networked machines via TCP/IP. A **controller node** dispatches work, **server nodes** execute it, and a shared **FARMROOT** folder holds configuration. OpenToonz itself acts as the client for submitting and monitoring jobs.

On Windows, install the Farm Controller component on your dispatch machine and the Farm Server component on each render node — both are registered as Windows Services. During install, provide the FARMROOT path in UNC format (`\\Host\Share\Folder`). On macOS, copy the `toonzfarm` folder from OpenToonz stuff to a shared location, then edit `configfarmroot.txt` (inside the app bundle at `Contents/Resources`) on every machine to point at it.

In `FARMROOT/config/controller.txt`, add one line: hostname, IP, and port separated by spaces (e.g., `render1 10.10.0.130 10000`). In `servers.txt`, add one line per render node in the same format. Restart the controller whenever you edit `servers.txt`.

Both Windows services default to Local System, which can't reach network shares. Open **Control Panel > Administrative Tools > Services**, right-click the service, go to the **Log On** tab, switch to **This Account**, and provide credentials with network admin rights.

If the OpenToonz client machine isn't itself a farm node, open the **Farm** room, set **Process with:** to **Render Farm** in the Batch Servers pane, and point it at your FARMROOT when prompted. Switch back to **Local** any time you want the local machine to handle tasks instead.

All disks involved must grant full read/write to everyone. Ensure the chosen ports aren't blocked by firewalls. If a server shows "Down," that's almost always a blocked port. Diagnostic logs land in `OpenToonz stuff/toonzfarm` on each machine — check `server.log`, `controller.log`, `tcomposer.log`, or `tcleanup.log` to trace issues.
