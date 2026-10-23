# Next session — resume here

**Updated:** 2026-10-23  
**Track:** Y1 / Q1 / Week 1  
**Status:** Ubuntu environment installed and verified; ROS 2 installation next.

## Last verified working state

- New `PhysicalAI` distro installed via official Ubuntu 26.04.1 WSL AMD64 image **on D:** and SHA256 verified.
- `PhysicalAI` is Ubuntu 26.04.1 LTS, kernel `6.18.54.1-microsoft-standard-WSL2`.
- Root Linux filesystem ~98 GB, ~1.3 GB used, ~92 GB available on first boot.
- About ~624 MiB RAM used when freshly booted; global WSL memory cap remains 16 GB.
- Original `Ubuntu-24.04` remains default and `docker-desktop` remains installed.
- ROS 2, RViz and Gazebo **not installed or tested**.
- A full switch back to ERP mode has not yet been explicitly tested after install; Issue #1 remains open for that final verification.

## ROS 2 apt source verified (2026-10-23)

The user installed `ros2-apt-source` **1.3.0~resolute** inside `PhysicalAI`. `sudo apt update` successfully fetched `packages.ros.org/ros2/ubuntu resolute` package indexes. Six Ubuntu packages were upgradable; this is informational. **ROS desktop itself has not been installed or tested yet.**

## Next single action

Inside **PhysicalAI**, run/review `sudo apt upgrade`, check `apt-cache policy ros-lyrical-desktop`, then install `sudo apt install ros-lyrical-desktop ros-dev-tools`. Verify `source /opt/ros/lyrical/setup.bash`, `echo "$ROS_DISTRO"`, and the two-terminal talker/listener exercise. Document actual outputs and any failed steps in [Issue #2](https://github.com/hamora1370/Physical-AI/issues/2).

**Execution issue:** [#2 ROS 2 installation & talker/listener verification](https://github.com/hamora1370/Physical-AI/issues/2)

## Follow-up

1. Two-terminal ROS talker/listener smoke test and command output.
2. Confirm clean return to original ERP distro and close [#1](https://github.com/hamora1370/Physical-AI/issues/1).
3. Test WSLg/RViz before planning Gazebo Jetty.
4. Update `docs/skills/SKILL_MATRIX.csv` only after evidence-based assessment.

## Safety / workflow

- Run ROS code under Linux `~/`, not `/mnt/c/Users/...`.
- Never stop active ERP tests, databases or CI runner mid-write to switch workloads.
- Continue treating Docker container RAM/CPU as normal during ERP development; use alternating work modes rather than optimizing it for robotics.
- Do not claim success for installations or tests that have not been shown.
