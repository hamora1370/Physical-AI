# Current state — verified workstation setup

**Last updated:** 2026-10-23  
**Phase:** Y1 / Q1 / Ubuntu installed, ROS 2 pending  
**Source:** user-provided console transcripts. Physical testing, ROS installation and robotics skills have not yet been verified.

## Verified workstation environment

| Item | Observed status |
| --- | --- |
| Robotics WSL2 distro | `PhysicalAI` — Ubuntu 26.04.1 LTS (Resolute), x86_64 |
| Linux kernel | `6.18.54.1-microsoft-standard-WSL2` |
| Installation source | Ubuntu 26.04.1 official WSL AMD64 image; SHA256 matched the expected value |
| Install directory | `D:\WSL\PhysicalAI` — successful custom-location install |
| Existing development distro | `Ubuntu-24.04` preserved and still WSL default (*) |
| Docker integration | `docker-desktop` preserved; it was stopped during Linux setup |
| Memory inside new distro | ~15 GiB total, ~624 MiB used, ~15 GiB available at first boot |
| Swap | 4.0 GiB; 0 used on first boot |
| Linux root virtual filesystem | ~98 GiB capacity, ~1.3 GiB used, ~92 GiB available |
| ROS 2 | **not installed/verified** |
| RViz / Gazebo | **not installed/verified** |
| Physical robot | **none verified** |

**Important:** Linux root filesystem capacity is not the actual size occupied by the sparse VHDX on host D:. Previously measured Windows disk free-space values were C: 1.60 GB, D: 119.40 GB **before** image installation; current host free space has not been remeasured.

The transcript establishes that the new distro could be exited and restarted. A full, verified return to ERP mode after robotics mode has **not** been recorded yet. `wsl --list --verbose` showed a transitional `PhysicalAI Running` shortly after shell exit whereas `wsl --list --running` immediately reported none. This is not currently sufficient evidence of a fault.

## Work-mode agreement

- ERP/ToliHub and Physical AI will run **sequentially**, not as two simultaneous heavy workloads.
- Existing WSL2 global `.wslconfig` was `memory=16GB` and `defaultVhdSize=100GB`; no changes have been requested to it.
- During robotics work, stop development/CI and Docker workloads **gracefully**; never terminate a database during writes.
- Keep the development distro and Docker data unchanged; robotics code belongs in the new Linux filesystem, **under `~/` rather than `/mnt/c/`**.
- Public GitHub repository: no credentials, personal/local IPs, private company data or media.

See [WSL2 on-demand guide](docs/infrastructure/WSL2-ON-DEMAND.md).

## Verified background relevant to study

- CAD / mechanical engineering, full-stack software development, ERP architecture, production and 3D printing.
- Interest in robot control, ROS 2 and robot learning.
- No direct evidence of mastery in robotics yet; track with [skill matrix](docs/skills/SKILL_MATRIX.csv).

## Next checks

- [x] Download Ubuntu 26.04.1 official WSL image and verify SHA256
- [x] Install `PhysicalAI` WSL2 distro on D: without modifying original Ubuntu
- [x] Create an initial Unix account and verify Ubuntu release and Linux filesystem
- [ ] Confirm `locale`, package manager and start in `~/`
- [ ] Install ROS 2 Lyrical from official apt repository
- [ ] Test ROS 2 talker/listener and record evidence
- [ ] Verify WSLg and RViz before Gazebo
- [ ] Return to ERP development mode safely and verify the original environment remains functional
- [ ] Assess actual GPU, other hardware and available study time when relevant
