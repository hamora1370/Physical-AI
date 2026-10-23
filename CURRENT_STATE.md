# Current state — initial assessment

**Last updated:** 2026-10-23
**Phase:** Y1 / Q1 / setup
**Assessment status:** baseline **not yet completed**. Do not claim mastery from prior experience alone.

## Confirmed relevant background

- Mechanical engineering and CAD design.
- Full-stack and industrial software engineering; experience with PostgreSQL, event-driven systems and ERP development.
- Practical 3D-printing/production experience.
- Interest in robot learning and ROS 2.

## Unknowns to assess (not assumed to be weak)

| Skill / equipment | Current verified level | How to assess |
|---|---|---|
| Linux & Python for robotics | unassessed | reproduce a ROS 2 workspace and scripted exercise |
| Linear algebra / SE(3) | unassessed | explain and implement coordinate transforms |
| FK & IK | unassessed | derive and independently test sample manipulator |
| Feedback control | unassessed | closed-loop control explanation and measured response |
| ROS 2 nodes/tf2/actions | unassessed | working example and logs |
| Robot hardware | unassessed | BOM/inventory and safe bench test |
| GPU and depth camera | unassessed | record actual available hardware before buying |

## Constraints

- **Planned capacity**: ~5 h/week in Y1 and Y2; adjust to protect ERP and manufacturing priorities.
- **Budget**: not assigned; prefer simulation and reusing existing hardware.
- **Infrastructure**: isolate robotics development from production ERP resources; do not assume Ubuntu / ROS is installed.
- **Observed host (2026-10-23, user-reported PowerShell):** Windows with 31.5 GB installed RAM, 4.2 GB Windows available RAM, WSL2 global `.wslconfig` `memory=16GB` and `defaultVhdSize=100GB`.
- **Running WSL:** `Ubuntu-24.04` (default) and `docker-desktop`, both running; `vmmemWSL` Windows process working set ≈8.31 GB at snapshot time.
- **Observed inside WSL:** total ≈15 GiB, Linux `MemAvailable` ≈8.5 GiB, swap used ≈0.5 GiB. This is *not* extra Windows-free RAM and does not split usage by distro.
- **Observed Docker (historical snapshot only):** six containers were running during a software development session. This workload is expected and **not** a blocker or optimization target for the Physical AI setup.
- **Operating decision:** ERP/ToliHub and Physical AI development will run **sequentially**, not as concurrent heavy workloads. No further Docker memory investigation required. **Install is gated on WSL runtime >=2.4.10 and safe Windows disk headroom**; gracefully complete workloads before shared WSL update. Only disk capacity and WSL CLI compatibility still need minimal installation checks.
- **Selected target (not installed):** isolated WSL2 distro named `PhysicalAI` with Ubuntu 26.04.1 LTS, ROS 2 Lyrical and Gazebo Jetty. [Installation and switching instructions](docs/infrastructure/WSL2-ON-DEMAND.md).
- **Measured WSL preflight (2026-10-23):** WSL **2.3.26.0** (kernel 5.15.167.4-1), WSLg **1.0.65**, Windows build **10.0.26200.7623**; `wsl --list --online` does not show `Ubuntu-26.04`. New .wsl image format requires **WSL >=2.4.10**.
- **Disk free space:** **C: 1.60 GB**, **D: 119.40 GB** (user-provided readings). C: needs more headroom before system-wide WSL update; target install location `D:\\WSL\\PhysicalAI`. Image download also to D:. D: media type unverified.
- **Public repository**: do not commit secrets, customer information or private operational data.

## Fill in before first sprint

- [ ] Actual OS / WSL / GPU / CPU / RAM and disk space
- [ ] Weekly available time block(s)
- [ ] Existing robotics knowledge and initial self-assessment
- [ ] Linux development environment choice and reason
- [ ] Date/time of first completed lab session
- [ ] Link to evidence of first running ROS 2 node

## Current open questions

1. Restore safe C: headroom (8–10 GB as a planning target), then update shared WSL to >=2.4.10 at a safe workload break and verify install flags.
2. Verify the official Ubuntu 26.04.1 WSL image/checksum before installing to D:.
2. What robotics hardware, if any, is already available?
3. What exercise can be independently tested before ROS hardware integration?
