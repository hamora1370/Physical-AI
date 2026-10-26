# Next session — resume here

**Updated:** 2026-10-26  
**Track:** Y1 / Q1 / official Week 1 (2026-10-26 → 2026-11-01)  
**Current engineering project:** **SCARA-01**, a compact low-energy R-R-P-R SCARA concept (three positional coordinates plus wrist yaw), with a separate printable gripper intended first for tray-to-tray transport of small 3D-printed parts.

## Decision made 2026-10-26

The learner approved switching Q1 to a **project-centered integrated robotics curriculum**, rather than separating ROS/software tools from mechanical, mathematical and control engineering. They also approved using SCARA-01 as a **future Physical-AI/robot-learning platform**: actual joint feedback (not commands-as-observations), timestamped state/actions and later camera, stable ROS 2 interface, observable printed gripper, CAD/simulation/hardware alignment, and local independent safety. The single robot is the common thread: concept → requirements for a printable compact R-R-P-R and gripper → 2R FK/IK → mechanical/actuator design → sensing/control → RRP path → ROS model/simulation → review.

- [SCARA-01 concept/requirements hypotheses](docs/projects/SCARA-01-CONCEPT.md)
- [Learning-ready architecture and data schema proposal](docs/projects/SCARA-01-LEARNING-PLATFORM.md) · [ADR-0002](docs/decisions/ADR-0002-scara-learning-platform.md)
- [Live Q1 13-week learning plan and updated Week 1](docs/roadmap/Q1-2026-10.md)
- [Active design requirements task #6](https://github.com/hamora1370/Physical-AI/issues/6)
- [Q1 milestone #5](https://github.com/hamora1370/Physical-AI/issues/5)

## Teaching-pacing decision — confirmed 2026-10-26

The learner questioned over-investing class time in contact-friction and gripper-force equations before essential robot motion and Physical AI foundations. **Agreed:** mechanical sizing remains necessary for building the printed gripper, but move detailed gripper motor/rack/gear torque and material calculations to the **Week 5–6 hardware engineering stage**. For now teach task space, joint space, robot kinematics, trajectories, controller feedback and eventually robot-learning interfaces through SCARA-01. Avoid drifting into general software tutorials or multi-concept lectures; one concept, one meaningful check.

**Already discussed conceptually:** SCARA R-R-P-R and 4 pose DOF, independent horizontal yaw, compact printed two-jaw gripper, candidate 130/110 mm links (20–240 mm ideal unconstrained annulus), joint/link collision and Z transfer clearance; preliminary 40×30×30 mm / 100 g reference part and ~50 mm gripper opening are **not confirmed user requirements**; basic force/friction relation and `mu` halving implies required normal force doubling. Do not certify design or hardware mastery based on these conversations.

## Next **single** teaching action

**Begin SCARA-01's motion architecture: task space vs joint space.** Present a single conceptual goal, for instance tool center `(x=120 mm, y=60 mm, z=50 mm)`, tool `yaw=90°` relative to the base; coordinates are a *teaching example*, not validated workcell points. Explain the distinction between specifying a tool pose vs ordering motors to specific angles, and the need for inverse kinematics. Invite the learner to reason whether a pose has one or multiple joint configurations and what additional criteria choose a solution. Follow with goal → IK → feasible trajectory → local controller → measured feedback (not simply a direct motor command). Do **not** start by deriving the full analytic IK or writing a long ROS software stack. Formal tests in [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3) come as comprehension develops.

**Out-of-scope for this teaching step:** more friction/gripper sizing, motor purchase, rack torque, exact printed-wall parameters, independent policy/VLA training, simulator procurement. Actual tray geometry, part dimensions/mass, jaw force and achievable positioning precision remain unconfirmed requirements [Issue #6](https://github.com/hamora1370/Physical-AI/issues/6).

## Evidence carried from earlier sessions — avoid repetition

- **Verified via 2026-10-23 user logs:** `PhysicalAI` distro Ubuntu 26.04.1 WSL2, ROS 2 Lyrical initial communication; C++ Talker / Python Listener exchanged numbered `/chatter` messages of type `example_interfaces/msg/String`. `ros2 topic info -v` showed RELIABLE, KEEP_LAST(7), VOLATILE. [Saved log](docs/evidence/2026-10-23-ros2-talker-listener.md).
- **Introduced and conceptually practiced (2026-10-24):** Base/Wrist/Tool frames, translation/rotation, homogeneous transformations, introductory FK, 2D coordinate problems (correct learner answers). A new SCARA FK/IK derivation and code tests are still needed; do not re-teach the generic intro.
- **Learner-reported completed (2026-10-26):** `executor_lab.py` `single`, `multi-default`, `multi-groups`, CPU/sleep modes and separate Process experiments. **No output or timing distributions independently assessed**; discuss only when needed for SCARA timing.
- **Discussed/not yet mastery-assessed:** Node/Topic/Publisher/Subscriber, Process/Thread/Executor, Concurrency/Parallelism, language bindings (Python, C++, Rust, JavaScript), QoS, tf2 timestamp/latency basics.

## Q1 definition of done

Reliable conceptual and numerical understanding with evidence; a tested 2R FK/IK, initial sizing tradeoffs, documented R-R-P motion model plus wrist-yaw relation (J4 simulation when feasible), and reproducible simulated pick/place sequence (or explicit simulator limitations/fallback). **Low-energy guarded physical 2R prototype is a stretch**, not an automatic requirement of ~65 study hours. Full four-axis and gripper physical integration can extend to Q2. **Q1 learning-ready exit gate is a reviewed feedback/interface/logging design, not installed encoders/cameras, a dataset or a learned model.**

## Remaining verification / limitations

- ROS 2 `ROS_DISTRO` and meta-package installation checks; WSLg/RViz/Gazebo not yet verified.
- No independent 2R FK/IK implementation or numeric tests verified; [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3) applies to SCARA 2R subchain.
- No SCARA CAD, purchased hardware, motion test, physical robot or production cell has been demonstrated. Neither encoder telemetry nor synchronized camera/robot dataset nor AI policy has been verified.
- Safe return to ERP Linux workflow remains outstanding. Maintain sequential heavy-use of ERP/ToliHub and robotics environments.
- Learning mastery requires demonstration; `L0` in skill matrix is unassessed, not inability.

## Working rules

~5 focused hours/week, roughly 2h engineering theory, 2h calculation/build/code, 1h reflection. At most one theory and one implementation issue active. GitHub is an evidence register, not a source of excessive bookkeeping. No secret credentials or customer-specific material in this public repository.
