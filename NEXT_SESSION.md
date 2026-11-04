# Next session — resume here

**Updated:** 2026-11-04  
**Track:** Y1 / Q1 / official Week 2 (2026-11-02 → 2026-11-08)  
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

## Completed learning checkpoint — 2026-11-01

**Four-stage SCARA-01 Jacobian exercise: PASS (guided chat).** Evidence: [motion/Jacobian learning note](docs/evidence/2026-10-26-scara-motion-jacobian-learning.md). The learner correctly derived all four partial derivatives of 2R FK, giving `J=[[-110,-110],[130,0]] mm/rad` at `q1=0°, q2=90°` with `L1=130 mm, L2=110 mm`. The learner then correctly calculated `(xdot,ydot)=(0,13) mm/s` from `qdot=(0.1,-0.1) rad/s`, and solved the inverse-velocity task `(xdot,ydot)=(11,13) mm/s` yielding **`qdot=(0.1,-0.2) rad/s`**, independently verified by substitution. **Mark the four-step chat exercise complete, not full Jacobian mastery.** No independently executed code, unseen test, closed-book mastery check or physical model; leave M04 skill level conservative per docs/LEARNING_SYSTEM.md.

## Learning checkpoint — 2026-11-02

**Conceptual Closed-Loop Control / P-PD / telemetry / fault reasoning:** learner accurately evaluated position-error direction, PD braking torque (at e=0, qdot=-2 rad/s and Kd=0.15 gives +0.3 N·m), P vs PD differences, motor-side versus joint-side encoder/backlash, the need to evaluate tracking error over time, and multiple fault hypotheses. **One unit mistake was corrected:** for e=5 degrees, Kp=3 s^-1, the P command was +15 **deg/s**, not +15 rad/s. When motor encoder moved but joint encoder was fixed and motor current normal, learner proposed faulty joint encoder; tutor noted broken/slipping transmission is another compatible hypothesis. None of these discussions establish independently functioning control or diagnosis.

[Detailed 2026-11-02 learning evidence](docs/evidence/2026-11-02-scara-feedback-and-fault-learning.md). Previously [guided Jacobian exercise PASS](docs/evidence/2026-10-26-scara-motion-jacobian-learning.md). The physical SCARA and controller do not exist as verified artifacts.

## Week 2 learning plan — November 2–8 (~5 focused hours; flexible)

| Order | Budget | Scope | Evidence |
|---|---:|---|---|
| 1 | 60 min | Sampling Time `Ts` vs update frequency `fs`; 1/10/100 ms examples, sample-and-hold, nominal versus measured update intervals and jitter. | Independent one-step J1 P controller calculation with units; explain why time interval matters. |
| 2 | 60 min | Discrete-time P/PD vs continuous-time; small hand calculation and optional small Python simulation with two `Ts` values, **no actual servo hardware**. | Verify numerical example; report dt, stability/tracking assumptions and observed effect if simulation runs. |
| 3 | 60 min | ROS 2 host vs local motor controller, encoder sample/timestamp, setpoint/actual, watchdog and fault event boundaries; connect to previous **learner-reported but not verified** Executor lab. | One clear architecture/signal-flow diagram with realistic timing and safe authority boundaries. |
| 4 | 75 min | Return to issue #6: base/tray/part workcell assumptions, safe XY pose and Z clearance; check elbow-branch/collision-path choices. | Requirements v0 known/assumed/unknown table and initial geometrical workcell sketch; **do not assume physical specifications confirmed**. |
| 5 | 45 min | Weekly review and one unfamiliar short exercise, set Week 3 FK/IK coding start. | Record one independently answered check, remaining environment/requirements gaps. |

**Time total: 300 min (5 h) only if actually available.** Adapt pace by comprehension, do not turn into checklist race. Existing Q1 syllabus continues: Weeks 3–4 independent 2R FK/IK and joint-limited tests; Weeks 5–6 mechanical/actuator design; Weeks 7–8 deeper feedback and fault design; Weeks 9–10 trajectories/Jacobian tests; Weeks 11–12 ROS model/simulation.

## Learning checkpoint — 2026-11-04: discrete P simulation **PASS**

Learner **implemented, executed and graphed** a discrete-time **position P → velocity command** controller for illustrative SCARA-01 J1 with ideal speed tracking. They calculated and explained the time-step effect, produced single-case plots, refactored `simulate_p(theta_initial,theta_target,kp,dt,steps)`, and made a three-curve plot across equal 7.2 s simulated durations. Learner predicted `[theta0,theta1,theta2]=[50,74,40.4]` degrees in the unstable case. Reviewer independently parsed/executed the supplied Python file and confirmed:

| Ts (s) | Steps | a=1-Kp Ts (Kp=2/s) | Behavior | Final position |
|---:|---:|---:|---|---:|
| 0.1 | 72 | +0.8 | monotonic stable | 59.9999989469° |
| 0.8 | 9 | -0.6 | alternating convergent | 60.10077696° |
| 1.2 | 6 | -1.4 | alternating divergent | -15.29536° |

**Complete this P *teaching exercise*, not the full feedback/mechatronics Q1 gate.** This is guided Python simulation only, not an independently validated physical controller. User-uploaded script and image were reviewed but **not committed to GitHub by this documentation update**. Minor code cleanup: move duplicate `plt.axhline` out of the loop and remove redundant pre-loop simulation call.

[Full evidence and reproducibility notes](docs/evidence/2026-11-04-scara-discrete-p-simulation.md).

## Next **single** teaching action — start now

**Learner explicitly requests ending introductory P exercises and moving to PD.** Honor the pace: introduce exactly one fundamental conceptual distinction before any new implementation. Previous P script commands **velocity** and assumes the motor follows it exactly; a PD simulation of derivative *damping* should instead start with a **torque-controlled inertial joint** `I*theta_ddot + b*theta_dot = torque`, and `torque_cmd=Kp*(theta_target-theta)-Kd*theta_dot` for a fixed target. Explain that in this second model `Kp` has units N·m/rad (not 1/s as in previous velocity P), `Kd` has N·m·s/rad, and `-Kd*theta_dot` damps motion. Clearly label the change in plant/command interface; do not imply dropping a D term into the old speed-output model is equivalent. Ask one short physical interpretation question (e.g. torque sign at zero position error and positive joint speed), only afterward scaffold a PD torque simulation with the learner. Maintain control practice to a bounded portion of week 2 and retain required FK/IK and workcell follow-ups.

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
