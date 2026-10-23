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

## Verified preflight — 2026-10-23

This is user-provided observed system data; these are not projected allocations.

- WSL **2.3.26.0**, kernel 5.15.167.4-1, WSLg 1.0.65; Windows build 10.0.26200.7623.
- `wsl --list --online` reports only unnumbered `Ubuntu` plus other Linux distributions, **not** `Ubuntu-26.04`. Do **not** run `wsl --install -d Ubuntu-26.04` on this state.
- Drive **C: 1.60 GB free**; **D: 119.40 GB free**. Exact physical media type of D: not yet verified.
- Ubuntu's current WSL image format requires **WSL 2.4.10+** (see Canonical installation guide); WSL is older.
- Existing `Ubuntu-24.04` and `docker-desktop` must remain intact; Docker runtime consumption during ERP work is expected and **is not a blocker**.

**Decision:** update WSL first, after restoring Windows C: free-space headroom, and install the new distro + downloaded image entirely on **D:**. Do not modify existing Ubuntu, Docker images/volumes, or `.wslconfig`. WSL update is a **shared system-level change**, not a change confined to PhysicalAI; schedule it after active development work is saved/stopped. No work has yet been performed on the user's machine.

## Step 1 — prepare Windows and update WSL (not yet executed)

1. Reclaim enough C: space for reliable Windows/update activity: **8–10 GB free minimum planning target**, preferably more (not a documented WSL hard requirement). Use Settings → System → Storage → Temporary files or move ordinary personal files to D:. Review contents before deletion. Do **not** delete `docker_data.vhdx`, `ext4.vhdx`, Docker volumes, source repositories or unknown system files.
2. Complete/save running development, CI and databases gracefully; exit Docker Desktop and Ubuntu sessions.
3. From PowerShell, after adequate C: headroom:

```powershell
wsl --update
wsl --version
wsl --list --online
wsl --help
```

4. Verify WSL version **>= 2.4.10** and `--from-file` / `--name` / `--location` options in `wsl --help`; if update requests reboot, do it only after development workloads are stopped. Check original distros still exist and work before proceeding.
5. If update fails or WSL features are missing, stop and diagnose rather than trying an unversioned `Ubuntu` install on C:.

Note: installing WSL itself may use Windows system-drive space even though the new distro's rootfs will be stored on D:.

## Step 2 — download official Ubuntu 26.04.1 WSL image to D: (after WSL update)

The registered distro list need not show `Ubuntu-26.04` when installing directly from the **official** Canonical release image.

**Only for an AMD64 / x64 host** (check `$env:PROCESSOR_ARCHITECTURE`); different architecture requires the official corresponding image and checksum:

```powershell
New-Item -ItemType Directory -Force -Path 'D:\WSL\Downloads' | Out-Null
$wslImage = 'D:\WSL\Downloads\ubuntu-26.04.1-wsl-amd64.wsl'
Invoke-WebRequest -Uri 'https://releases.ubuntu.com/26.04.1/ubuntu-26.04.1-wsl-amd64.wsl' -OutFile $wslImage
Get-FileHash $wslImage -Algorithm SHA256
```

Compare the printed hash with the canonical AMD64 SHA256 (from Microsoft WSL's distro manifest, which uses Canonical's official image):

```text
48d56724b5c8e60f24893e83e73bbb58c60b3ca22fba3da977075420acd54104
```

**Do not install if hash differs.** The release location/hash are version-specific.

## Step 3 — install just the new distro on D: (after verified hash and WSL support)

```powershell
wsl --install --from-file 'D:\WSL\Downloads\ubuntu-26.04.1-wsl-amd64.wsl' --name PhysicalAI --location 'D:\WSL\PhysicalAI' --no-launch
wsl --list --verbose
```

Check that `PhysicalAI` is present, `Ubuntu-24.04` remains the default, and no action has changed the existing development distro. If WSL rejects the syntax, stop and inspect `wsl --help` for the actual installed version—do not fall back to default Ubuntu installation.

## Step 4 — first start and confirm release

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

## Step 5 — manual switching (safety first)

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

## Step 6 — follow-up checkpoints

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
- Canonical image-version requirement: https://ubuntu.com/wsl/docs/latest/howto/install-ubuntu-wsl2/
- Microsoft distro manifest (AMD64 image + SHA256): https://github.com/microsoft/WSL/blob/master/distributions/DistributionInfo.json
