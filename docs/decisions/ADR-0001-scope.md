# ADR-0001 — Scope and learning architecture

- **Date:** 2026-10-23
- **Status:** Accepted for initial scaffolding
- **Decision owner:** project maintainer (review before treating assumptions as confirmed)

## Context
Five-year learning plan must coexist with existing ERP and manufacturing business responsibilities. Robotics tools change rapidly. Long-term skill claims need evidence and a resumable state.

## Decision
1. Focus on **robotic manipulation for industrial tasks**; avoid beginning with humanoid mechanics.
2. Use GitHub as canonical versioned repository for plans, decisions, code and experiment metadata.
3. Use GitHub Issues for near-term execution; detailed planning only one quarter ahead.
4. Favor low-cost simulation and small safe educational hardware before purchasing industrial equipment.
5. Separate high-level business commands and policy inference from deterministic robot control and independent safety functions.
6. Select **Ubuntu 26.04.1 LTS + ROS 2 Lyrical + Gazebo Jetty** as the *target stack* for an isolated robotics environment, pending a workstation/installation audit; treat later models and versions as replaceable. MoveIt 2 binaries are available for Lyrical. NVIDIA Isaac Sim 6.1 supports Ubuntu 22.04/24.04 on Linux, not 26.04, so its installation must remain a separately validated future decision.
7. Do not commit company-sensitive assets to this public repository.

## Consequences
+ Narrow, testable learning with real industrial transfer.
+ Can resume after long interruptions.
- Some broader Physical AI topics remain electives.
- Routine documentation and benchmark discipline required.

## Revisit
2027 Q1 review or earlier if operational needs fundamentally change.
