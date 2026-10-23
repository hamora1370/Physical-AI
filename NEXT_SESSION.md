# Next session — resume here

**Updated:** 2026-10-23
**Track:** Y1 / Q1 / Week 1 (starts 2026-10-26)
**Status:** Initial repository scaffolding complete; robotics environment and skills **not yet verified**.

## Last verified working state
- Five-year plan, quarterly plan, skill matrix, experiment and review templates committed on `main`.
- First educational FK exercise and GitHub Actions test configuration committed; **CI execution and test result not yet confirmed**.
- Starter Issues #1–#5 created.
- No ROS 2 installation, simulation, physical robot or mastery assessment has been verified.

## Chosen target stack (not yet installed)
Ubuntu 26.04.1 LTS + ROS 2 Lyrical + Gazebo Jetty + MoveIt 2 (Lyrical). Isaac Sim 6.1 lists only Ubuntu 22.04/24.04, so evaluate a secondary compatible environment later.

## Confirmed deployment decision (2026-10-23)

**Proceed** with an on-demand WSL2 `PhysicalAI` instance. ERP/ToliHub work and robotics work are **separate working modes**. No further container optimization or RAM-attribution study is needed for this installation decision. Existing WSL cap remains 16 GB globally. Existing Ubuntu-24.04 and Docker environments remain unchanged.

**Installation plan:** [WSL2-ON-DEMAND.md](docs/infrastructure/WSL2-ON-DEMAND.md). Base distro and ROS are **not installed yet**.

## Next single action
In PowerShell check `wsl --version`, `wsl --list --online`, WSL `--location`/`--name` support and available SSD drive space. Then install **only** Ubuntu 26.04 as a new `PhysicalAI` distribution on the selected drive. Do not modify or remove existing distributions.

## Next in sequence
1. [#1 Baseline / isolated environment](https://github.com/hamora1370/Physical-AI/issues/1) — start here.
2. [#2 ROS 2 first nodes](https://github.com/hamora1370/Physical-AI/issues/2) — after environment is reproducible.
3. [#3 Derive/test FK](https://github.com/hamora1370/Physical-AI/issues/3) — math track, can be independent of ROS.
4. [#5 Q1 milestone](https://github.com/hamora1370/Physical-AI/issues/5) — source of quarterly outcome.
5. [#4 GitHub Projects views](https://github.com/hamora1370/Physical-AI/issues/4) — optional board configuration.

## Current blockers
- New install drive capacity and supported WSL installation flags not yet verified; robotics distro and ROS not yet installed.
- Test workflow status not checked; do not report CI green without run evidence.

## End of every session
Record: date, last passing command/test, commit SHA, experiment ID (if any), blocker, and **one concrete next action**. Keep this file concise.
