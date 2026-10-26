# Next session — resume here

**Updated:** 2026-10-26  
**Track:** Y1 / Q1 / official Week 1 (2026-10-26 → 2026-11-01)  
**Current engineering project:** **SCARA-01**, a desktop low-energy 3-positioning-DOF R-R-P robot intended first for tray-to-tray transport of small 3D-printed parts.

## Decision made 2026-10-26

The learner approved switching Q1 to a **project-centered integrated robotics curriculum**, rather than separating ROS/software tools from mechanical, mathematical and control engineering. The single robot is the common thread: concept → requirements → 2R FK/IK → mechanical/actuator design → sensing/control → RRP path → ROS model/simulation → review.

- [SCARA-01 concept/requirements hypotheses](docs/projects/SCARA-01-CONCEPT.md)
- [Live Q1 13-week learning plan and updated Week 1](docs/roadmap/Q1-2026-10.md)
- [Active design requirements task #6](https://github.com/hamora1370/Physical-AI/issues/6)
- [Q1 milestone #5](https://github.com/hamora1370/Physical-AI/issues/5)

## Next **single** teaching action

**SCARA-01 requirements workshop (Issue #6), not another isolated ROS 2 tutorial.** Start with a simple fixed-tray pick/place task and teach why the mechanism needs J1, J2 and the prismatic Z joint, then distinguish gripper opening from positional DOF. Draw a labeled coordinate sketch and derive the ideal planar reach for provisional `L1=180 mm`, `L2=140 mm`. Ask for engineering justification of tray size/placement, part dimensions/mass, tool selection, Z clearance and repeatability vs accuracy. Mark unknowns; do not present tentative values as measured. Capture requirements v0.

**Teaching style:** explain one concept deeply, connect it to this SCARA task, then do a small calculation and comprehension check before another topic. Do not rush toward CAD purchase/Gazebo.

## Evidence carried from earlier sessions — avoid repetition

- **Verified via 2026-10-23 user logs:** `PhysicalAI` distro Ubuntu 26.04.1 WSL2, ROS 2 Lyrical initial communication; C++ Talker / Python Listener exchanged numbered `/chatter` messages of type `example_interfaces/msg/String`. `ros2 topic info -v` showed RELIABLE, KEEP_LAST(7), VOLATILE. [Saved log](docs/evidence/2026-10-23-ros2-talker-listener.md).
- **Introduced and conceptually practiced (2026-10-24):** Base/Wrist/Tool frames, translation/rotation, homogeneous transformations, introductory FK, 2D coordinate problems (correct learner answers). A new SCARA FK/IK derivation and code tests are still needed; do not re-teach the generic intro.
- **Learner-reported completed (2026-10-26):** `executor_lab.py` `single`, `multi-default`, `multi-groups`, CPU/sleep modes and separate Process experiments. **No output or timing distributions independently assessed**; discuss only when needed for SCARA timing.
- **Discussed/not yet mastery-assessed:** Node/Topic/Publisher/Subscriber, Process/Thread/Executor, Concurrency/Parallelism, language bindings (Python, C++, Rust, JavaScript), QoS, tf2 timestamp/latency basics.

## Q1 definition of done

Reliable conceptual and numerical understanding with evidence; a tested 2R FK/IK, initial sizing tradeoffs, documented RRP robot model and reproducible simulated pick/place sequence (or explicit simulator limitations/fallback). **Low-energy guarded physical 2R prototype is a stretch**, not an automatic requirement of ~65 study hours. Full 3-axis physical integration can extend to Q2.

## Remaining verification / limitations

- ROS 2 `ROS_DISTRO` and meta-package installation checks; WSLg/RViz/Gazebo not yet verified.
- No independent 2R FK/IK implementation or numeric tests verified; [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3) applies to SCARA 2R subchain.
- No SCARA CAD, purchased hardware, motion test, physical robot or production cell has been demonstrated.
- Safe return to ERP Linux workflow remains outstanding. Maintain sequential heavy-use of ERP/ToliHub and robotics environments.
- Learning mastery requires demonstration; `L0` in skill matrix is unassessed, not inability.

## Working rules

~5 focused hours/week, roughly 2h engineering theory, 2h calculation/build/code, 1h reflection. At most one theory and one implementation issue active. GitHub is an evidence register, not a source of excessive bookkeeping. No secret credentials or customer-specific material in this public repository.
