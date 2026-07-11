The markdown doesn't contain any inline image references, so the text content is my sole source. I'll write the guide now.

# Using the Toonz Farm (OpenToonz 1.7)

The Toonz Farm lets you distribute rendering and cleanup tasks across multiple machines on the same network. Instead of one workstation grinding through frames, the farm's controller dispatches work to every available server node automatically — and if you split a render into chunks, each chunk lands on a different machine in parallel.

The farm has four parts: a **controller node** (runs `tfarmcontroller.exe` on Windows or `tfarmcontrollerd` on Mac) that dispatches work, one or more **server nodes** (running `tfarmserver.exe` / `tfarmserverd`) that do the actual rendering, a shared **FARMROOT** folder holding config files, and a **client** — which is just OpenToonz itself, running anywhere on the network. A single machine can act as both controller and server if needed.

On Windows, the installer creates Windows Services for each component. The critical step: both the **Toonz Farm Controller** and **Toonz Farm Server** services default to the Local System account, which can't reach network shares. Open **Control Panel > Administrative Tools > Services**, right-click the service, go to the **Log On** tab, switch to **This Account**, and provide credentials with admin rights on the farm network. On Mac, you instead edit `configfarmroot.txt` (buried inside the app bundle at `Contents/Resources`) to point at your shared FARMROOT path.

Configuration lives in `FARMROOT/config/`. Edit `controller.txt` with a single line — hostname, IP address, and port separated by spaces (e.g., `render1 10.10.0.130 10000`). Edit `servers.txt` the same way, one line per render node. Make sure the ports you pick aren't blocked by firewalls. If you add or remove a server later, restart the controller to pick up the change.

To connect OpenToonz as a client, open the **Farm** room, find the Batch Servers pane, and set **Process with:** to **Render Farm**. If prompted, provide the full path to your FARMROOT folder and click **OK**. Switch back to **Local** any time you want to render on just your own machine.

Once everything's running, the Batch Servers pane shows each node's name, IP, port, current task, and state (**Ready**, **Busy**, or **Down**). All server nodes must be up before the controller starts — a node that's offline at launch won't appear in the farm. All shared disks involved must grant full read/write permissions to everyone, or tasks will silently fail.

If something goes wrong, check the log files in `OpenToonz stuff/toonzfarm`: `server.log`, `controller.log`, `tcomposer.log` (render activity), and `tcleanup.log` (cleanup activity). Each machine writes its own logs locally, so look on the machine that had the problem.
