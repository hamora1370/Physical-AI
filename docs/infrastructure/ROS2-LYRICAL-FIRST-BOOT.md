# ROS 2 Lyrical — first installation on PhysicalAI

**Date:** 2026-10-23  
**Target:** Ubuntu 26.04.1 LTS (`resolute`) on dedicated `PhysicalAI` WSL2 distro.  
**Status as of 2026-10-23:** Step 2 (official ROS apt source) was completed; the user has now shown `ros2 pkg list | head` listing `action_msgs`, `action_tutorials_cpp`, `ament_cmake` and other ROS packages. This **verifies the ROS CLI and package discovery work**, but does not by itself verify the `ros-lyrical-desktop` meta-package or the selected ROS distro, and the talker/listener test is still pending. **Next:** check `echo "$ROS_DISTRO"`, verify the desktop/dev-tools packages if needed, then perform Step 4.

## 0. Shell placement and preflight

Run these commands **inside `PhysicalAI` Ubuntu**, not PowerShell, not the ERP Ubuntu distro:

```bash
cd ~
pwd
cat /etc/os-release | grep -E '^(PRETTY_NAME|VERSION_CODENAME)='
locale
df -h /
```

Expected: home under `/home/<linux-user>`, Ubuntu 26.04 / `resolute`, and sufficient root filesystem free space. Avoid working under `/mnt/c/Users/...` for ROS projects and workspaces.

## 1. Prepare Ubuntu

The following steps update packages **only inside PhysicalAI**, not the existing Ubuntu 24.04 distro.

```bash
sudo apt update
sudo apt install -y locales software-properties-common curl ca-certificates
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
export LANG=en_US.UTF-8
sudo add-apt-repository -y universe
sudo apt update
sudo apt upgrade
```

Review apt prompts before proceeding. A reboot/restart of the distro may be needed if a tool reports it; coordinate shutdown with work sessions.

## 2. Add official ROS apt repository

Source: [ROS 2 installation documentation](https://docs.ros.org/en/lyrical/Installation/Ubuntu-Install-Debs.html) (GitHub documentation source: [Ubuntu install Debs](https://github.com/ros2/ros2_documentation/blob/rolling/source/Get-Started/Installation/Ubuntu-Install-Debs.rst)).

```bash
ROS_APT_SOURCE_VERSION=$(curl -fsSL https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F '"tag_name"' | cut -d '"' -f 4)
echo "$ROS_APT_SOURCE_VERSION"
curl -fL -o /tmp/ros2-apt-source.deb \
  "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.resolute_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
sudo apt update
```

If the release version is empty, download returns an error, or the Debian package is not for `resolute`, **stop and inspect** instead of manually adding an unsigned apt source.

## 3. Install ROS desktop and development tools — package discovery verified, package identity confirmation pending

```bash
sudo apt install -y ros-lyrical-desktop ros-dev-tools
source /opt/ros/lyrical/setup.bash
echo "$ROS_DISTRO"
ros2 pkg list | head
```

The distro should report `lyrical`; the package list should not be empty.

To confirm that the expected packages are actually installed (rather than inferring this solely from a populated ROS package list):

```bash
echo "$ROS_DISTRO"
dpkg-query -W -f='${Package} ${Status} ${Version}\n' ros-lyrical-desktop ros-dev-tools
```

If both show `install ok installed` and `ROS_DISTRO` is `lyrical`, proceed to Step 4. If a package is missing, resolve that first; don't mark the installation complete solely from `ros2 pkg list`.

**Do not automatically append the source line to .bashrc until installation and test pass.** After success, it can be added once with a guarded check.

## 4. Talker/listener smoke test

Two **different Linux terminals** in the same WSL distro:

Terminal A:
```bash
source /opt/ros/lyrical/setup.bash
ros2 run demo_nodes_cpp talker
```

Terminal B:
```bash
source /opt/ros/lyrical/setup.bash
ros2 run demo_nodes_py listener
```

Pass: talker publishes and listener receives numbered messages. Stop each with Ctrl+C.

## 5. Record evidence

In the GitHub Issue for ROS 2 first steps link:
- installed distro and `ROS_DISTRO`;
- both command lines and short excerpts of output;
- errors and how they were resolved;
- local workspace location and tested commit;
- next concrete task in `NEXT_SESSION.md`.

Once verified, check WSLg/RViz **before** installing Gazebo Jetty. Official recommended Gazebo pairing: `ros-lyrical-ros-gz`, to be installed in a later checkpoint.

## Safety and limits

- Ubuntu packages install under Linux root filesystem on **D:**, but Windows/WSL host operations may still use Windows storage; monitor C: headroom.
- Protect original `Ubuntu-24.04` default distro and Docker Desktop. Do not modify `.wslconfig` to follow this guide.
- A successful message demo verifies ROS communication, **not** RViz/Gazebo performance or physical robot safety.
