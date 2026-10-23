# PhysicalAI — On-demand WSL2 workstation

**Decision date:** 2026-10-23  
**Decision:** create an isolated Ubuntu 26.04.1 LTS WSL2 distribution named `PhysicalAI`, using ROS 2 Lyrical and Gazebo Jetty after base verification.  
**Status:** planned; *not installed or tested*.

## Work-mode contract

The workstation has about 31.5 GB RAM and global WSL2 `memory=16GB`. The existing `Ubuntu-24.04` (default) and `docker-desktop` distributions support routine ERP/ToliHub work. The user has **explicitly chosen to run ERP/ToliHub and robotics sequentially**. Container resource use during software development is expected and **is not a blocker** for provisioning robotics.

- **Software mode:** existing Ubuntu and Docker Desktop as usual. PhysicalAI is stopped.
- **Robotics mode:** save/stop active development sessions, tests and database writes gracefully; quit Docker Desktop if its WSL backend is not needed; close old Ubuntu sessions; start `PhysicalAI` explicitly.
- Never auto-kill containers, databases, agents or other WSL distros. Do not edit ERP Docker Compose or other production settings.
- `.wslconfig` remains unchanged. A separate distro isolates packages and Linux files but **does not reserve an additional 16 GB**; active WSL2 distros share resources.
- **Do not configure PhysicalAI as WSL's default distro**; the existing `Ubuntu-24.04` remains default.
- Keep WSL distro storage on an SSD with ample free space; use a drive other than C: if C: is constrained.

## Step 1 — minimal, read-only preflight in PowerShell

```powershell
wsl --version
wsl --list --online
wsl --list --verbose
wsl --help | Select-String 'location|name|no-launch'
Get-PSDrive -PSProvider FileSystem |
    Select-Object Name,@{N='Free_GB';E={[math]::Round($_.Free/1GB,1)}}
```

Gate: WSL2 available, Ubuntu-26.04 listed, installer flags supported, a suitable SSD drive found (prefer around 60 GB or more *free* for initial tools and future expansion; this is a planning allowance, not an Ubuntu hard requirement). If no drive has suitable room, fix storage placement first instead of deleting ERP data.

## Step 2 — install only the new distro

**The following is an example assuming D: is an existing SSD with sufficient free space. Replace D: after verifying the actual drive. Do not run with a nonexisting drive.**

```powershell
$installPath = 'D:\WSL\PhysicalAI'
wsl --install -d Ubuntu-26.04 --name PhysicalAI --location $installPath --no-launch
wsl --list --verbose
```

If the installed WSL version does not support these arguments, **stop** and review the official WSL docs/version rather than falling back blindly to the system drive. WSL may need an update; coordinate any WSL update with existing dev workloads.

Ubuntu's documentation confirms `Ubuntu-26.04` in available distributions and supports installation under a custom name using `--name`. Microsoft's WSL documentation supports `--location` and `--no-launch`.

## Step 3 — first start and confirm release

At a natural break in ERP work (after saving and orderly stopping associated jobs), launch:

```powershell
wsl --distribution PhysicalAI
```

Complete the first-run Linux username and password setup if prompted. In the new Linux shell, verify:

```bash
cat /etc/os-release
uname -r
id -un
free -h
df -h /
```

Then from PowerShell:

```powershell
wsl --list --verbose
```

Gate: `PhysicalAI` reports Ubuntu 26.04 LTS and is WSL2; `Ubuntu-24.04` still exists and remains default. **Do not install ROS until this gate is met.**

## Step 4 — manual switching (safety first)

**ERP → robotics**: save ERP/ToliHub work; allow running tests/agents to finish; gracefully stop services and quit Docker Desktop; close interactive Ubuntu windows. Then:

```powershell
wsl --terminate Ubuntu-24.04
wsl --list --running
wsl --distribution PhysicalAI
```

Stopping Ubuntu alone does not automatically stop Docker Desktop; Docker may restart its backend if still open. Verify running distros. If there is still an active job, do not terminate it.

**Robotics → ERP**: save data, stop ROS/Gazebo processes, exit shell:

```powershell
wsl --terminate PhysicalAI
wsl --distribution Ubuntu-24.04
```

Launch Docker Desktop when required for normal development.

**`wsl --shutdown` stops *all* WSL2 distros, including Docker Desktop's backend.** Use it only after services have been stopped and when explicitly intending to stop WSL completely. If Windows retains Linux cache, memory release may be delayed.

## Step 5 — follow-up checkpoints

1. Verify base OS; record actual `wsl --version`, distro details and install drive in `CURRENT_STATE.md`.
2. Document and test Linux GUI/WSLg support before RViz/Gazebo.
3. Install ROS 2 Lyrical using its **official** Ubuntu 26.04 instructions; verify `ros2 --version` is *not* an appropriate universal check—use `ros2 doctor --report`, demo nodes and `ros2 pkg list`.
4. Integrate Gazebo Jetty and MoveIt 2 **only after** minimal ROS demos work.
5. For Isaac Sim 6.1 or demanding robot I/O, use a separately validated compatible native Linux environment when required.

## References

- Microsoft WSL commands: https://learn.microsoft.com/en-us/windows/wsl/basic-commands
- Microsoft WSL config: https://learn.microsoft.com/en-us/windows/wsl/wsl-config
- Canonical WSL installation: https://ubuntu.com/wsl/docs/latest/howto/install-ubuntu-wsl2/
- Canonical named instances: https://ubuntu.com/wsl/docs/latest/howto/manage-and-configure/
- Ubuntu WSL 26.04.1: https://ubuntu.com/download/wsl
