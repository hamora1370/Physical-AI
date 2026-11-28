# ADR-0003 — Q1 deliverable scope and simulation fallback

- **Date:** 2026-11-28
- **Status:** Accepted for Q1 planning; runtime/environment decision remains conditional on verification
- **Scope:** Q1 2026-10-26 through 2027-01-24; SCARA-01 R-R-P-R teaching project
- **Related:** [ADR-0002](ADR-0002-scara-learning-platform.md) · [Q1 roadmap](../roadmap/Q1-2026-10.md) · [Milestone #5](https://github.com/hamora1370/Physical-AI/issues/5)

## Context

The program has a limited time budget (~5 focused hours/week) and eight weeks remain in Q1. An independently learner-authored 2R FK function has four passing tests; iterative Jacobian IK converges on one reachable target but does not yet expose a reusable API, robust failure status, joint-limited checks, or both branches. Basic ROS 2 Talker/Listener was previously checked, but the current RViz/Gazebo environment and runnable simulation have **not** been verified. Q1 must protect time for control/feedback, mechanical design, ROS model/frame consistency, repeatable simulation or bounded fallback, and an engineering report.

## Decision — achievable Q1 minimum

1. **First close the outstanding FK/IK verification gate (#3):** a reusable 2R analytic IK for explicit elbow branches, unreachable-target handling, boundary cases, a clear test interface through repository-root `unittest`, and documented joint limits or limits-assumption tests. Keep Jacobian solver as learning evidence; do not present it as production-grade.
2. **Keep the SCARA-01 concept and design intent unchanged:** four nominal R-R-P-R axes, independent J4 tool yaw as a **design requirement**, future real joint/gripper observation, timestamped command/feedback interface, independent safety provisions. Derive/document the yaw relation even if J4 is not simulated in Q1.
3. **Make a low-energy physical prototype explicitly OUT OF Q1 delivery scope.** Hardware prototype was already optional stretch; do not plan/purchase hardware to satisfy the gate.
4. **Do not make J4 dynamic simulation mandatory for Q1.** Baseline demonstration targets R-R-P position kinematics, a known, bounded tray transfer, and a documented J4 yaw relation. J4 visualization/actuation in the simulator remains optional if straightforward.
5. **Time-box an environment readiness check (~30 minutes)** before choosing a simulator. Record exact `ROS_DISTRO`, available `rviz2`, `gazebo`/`gz`, ROS packages, and actual command outcomes. No results are assumed in advance, and no uncontrolled installation is authorized.
6. **Preferred path if the environment permits:** minimal URDF/Xacro model with observed ROS 2 frames/state and repeatable R-R-P tray-to-tray sequence. **Fallback if tooling is blocked:** reproducible kinematic Python simulation with time-stamped commanded and simulated-observed joint states, tool pose, limits, failures and an explicit account of ROS/URDF/simulator gaps. A fallback **does not count as completion** of unperformed ROS 2/URDF/simulator exit criteria; carry those gaps to Q2.
7. **Retain light documentation deliverables:** preliminary parametric mechanical/actuator/encoder tradeoff, explicit assumptions and uncertainties, command/observation schema, and Q1 review. Do not fabricate motor sizing, hardware results, camera data or a trained policy.

## Alternatives

- Require a physical four-axis demonstrator and full simulator now: infeasible for the timebox, and risks unvalidated hardware/safety claims.
- Delete URDF and ROS 2 from Q1 immediately: reduces integration overhead but abandons the core project-to-middleware connection without evidence of a blocker.
- Keep all original gates with no fallback: creates artificial success pressure and unreported omissions.

## Consequences and review trigger

Q1 grades what was actually verified. The minimum fallback can be useful and reproducible, but simulator/URDF and real-state gates are explicitly NOT PASS when skipped. The next action is Issue #3, then environment check; revisit simulation scope immediately after real environment evidence. This ADR narrows *required delivery*, not the long-term SCARA-01 architecture or its robotic learning objectives.
