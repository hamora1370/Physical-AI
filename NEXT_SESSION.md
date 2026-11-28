# Next session — resume here

**Updated:** 2026-11-28  
**Track:** Y1 / Q1 / SCARA-01 Jacobian IK checkpoint complete; Weeks 5–6 mechanical design next  
**Current engineering project:** **SCARA-01**, a compact low-energy R-R-P-R SCARA concept (three positional coordinates plus wrist yaw), with a separate printable gripper intended first for tray-to-tray transport of small 3D-printed parts.

## Current resume point — 2026-11-28 mechanical lesson (active, supersedes earlier resume points)

**Learner requested progress registration before moving to next lesson.** Saved [2026-11-28 mechanical checkpoint](docs/evidence/2026-11-28-scara-gravity-bending-and-inertia.md), on gravity-induced bending versus zero ideal yaw-axis gravitational torque, single-axis inertial torque, inertia of a uniform link, and advantage/tradeoff from moving J2 motor mass near base. User independently answered gravity-yaw distinction and inertia arithmetic; in last motor relocation case gave I values when asked for torque, which was corrected. These are guided calculations and conceptual checks, **not validated motor, bearing, or printed part design**. ME02 in introductory guided state only; no mastery-level jump. [Issue #6](https://github.com/hamora1370/Physical-AI/issues/6) remains OPEN.

**Next ONE teaching action now:** SCARA-01 **J1 shaft/bearing load path**: gravity acting downward at an offset creates bending couple. Explain why supporting a rotating vertical spindle with two axially separated bearings distributes radial reaction forces and improves angular stiffness, while a single short bearing offers weak overturning moment restraint (bearing-specific capabilities vary). Use one concise schematic with directions: vertical shaft, bearings separation h, horizontal arm carrying force mg at offset r; bending M=F*r, radial reaction pair ~M/h, vertical thrust load requires axial-load capability. Compare what changes when h increases. End with one meaningful conceptual question about bearing spacing; do not start another sequence of repetitive numerical inertia questions. Later bearing selection, shaft/hub fit, print-link stiffness, drive backlash, actuators/encoder feedback per Q1 Weeks 5–6. No unverified hardware assumptions.

## Current resume point — 2026-11-28 (active)

**Learner asked to register progress and advance along the curriculum instead of repeating IK/P step-size drills.** Follow their request. **Current next stage:** [Q1 Weeks 5–6](docs/roadmap/Q1-2026-10.md) — SCARA-01 mechanical concepts, actuator/encoder feedback options, printable links, payload, stiffness, backlash and torque/speed estimates. Work through ONE concept/example at a time. Start by distinguishing **static gravity-induced bending moments** in horizontal SCARA printed links from **torque about vertical J1/J2 rotation axes** (gravity alone does not induce torque around a vertical yaw axis for a level arm). Example purely illustrative: payload 0.10 kg at 0.24 m creates bending moment ~0.235 N·m at base before link/gripper own masses, but ideal static motor torque about vertical yaw axis remains zero. Ask learner to reason why, then continue with inertial and friction torque, bearings, link sizing.

**Verified new learner artifact:** [scara_jacobian_ik.py](exercises/01_robot_math/scara_jacobian_ik.py), independently run from uploaded file with the existing [FK](exercises/01_robot_math/scara_fk_practice.py). Numerical inverse-J iterative method q0=(0°,90°), target=(120,140)mm, alpha=0.5, tolerance=0.1mm, converged to (120.013,139.940)mm, residual 0.0611mm; **9 joint correction steps**, although script says `after 8 iterations` due to zero-based loop index. Tests remain a single starting pose/target; no physical controller. [Full checkpoint](docs/evidence/2026-11-28-scara-jacobian-ik-checkpoint.md). Prior independent planar FK 4 tests passed. Skill levels M03 L2, M04 L1, M05 L1 conservatively assessed. Learner correctly explained IK iterations do not determine real motor motion speed. User wanted to move on.

**Open scope intentionally deferred:** [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3) still open for joint limits, multi-target IK, both elbow branches, singularity/robustness tests, root-suite check. [Issue #6](https://github.com/hamora1370/Physical-AI/issues/6) remains open for engineering brief and requirements. No fixed physical dimensions, validated link material, specific gripper/motor, or hardware evidence. Do not divert into repeated basic kinematics until an engineering design problem requires it.

## Current resume point — 2026-11-27 (supersedes 2026-11-21 below)

**Learner authored and uploaded Python FK and four tests.** Saved code at [SCARA FK practice](exercises/01_robot_math/scara_fk_practice.py), tests at [four checks](exercises/01_robot_math/test_scara_fk_practice.py). Assistant independently ran uploaded files via Python unittest: **4/4 PASS**. Geometric configurations: extended (240,0) mm; vertical (0,240) mm; folded (20,0) mm; mixed q=(30°,60°) -> (112.5833,175) mm. [Checkpoint evidence](docs/evidence/2026-11-27-scara-fk-learner-4-tests.md). This is an FK function-and-test checkpoint, not complete Issue #3, and root test discovery wasn't run. Do not overstate proficiency.

**Next ONE teaching action (active now):** Move to ideal planar 2R **workspace/reachability** before inverse kinematics. With L1=130 mm and L2=110 mm, show why the reachable radial interval is 20–240 mm. Check the provisional Place target (120,140) mm using r=sqrt(x²+y²); explain how joint limits/collisions may further restrict the usable workspace. Then introduce IK elbow-branch geometry via law of cosines, with one guided numerical question at a time. Learner explicitly requested to proceed with teaching rather than more ROS concurrency review or logging overhead.

**Recent Python semantics note:** learner discussed `self`, instance methods, and unittest; in a two-Motor example answered speed values 150 and 250, corrected to **150 and 200** (only motor1 accelerated). Do not mark instance-state concept as fully mastered without a later check.

## Current resume point — 2026-11-21 (supersedes older next-action text below)

Learner requested a slower, detailed conceptual ROS 2 concurrency review after a study gap. Review now **complete by learner request**: Node/Topic/DDS/QoS, timestamp and stale state, Executors/Threads, async vs CPU-bound work, mutually exclusive callback groups, short Mutex, race conditions and lock-order deadlocks. Learner correctly explained why global lock order A then B prevents the specific cycle. **Discussion only**, no independently executed concurrency/ROS benchmarks or code. [Review evidence](docs/evidence/2026-11-21-ros2-concurrency-review-and-fk-resume.md). Do not inflate mastery or reopen the review without a concrete SCARA need.

**Next ONE teaching action (active now):** Continue [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3), an **independently written and tested planar 2R FK** for SCARA-01. Teach joint-relative angle composition and units briefly, then have the learner write the Python function and verify one known numerical case before expanding to tests. Candidate L1=130 mm, L2=110 mm; q angles in radians. Cases: (q1=0°,q2=90°) → (130,110) mm; (90°,0°) → (0,240) mm. In repo, `exercises/01_robot_math/fk_2r.py` **already contains a generic solution in meters** and has function signature `fk_2r(length_1,length_2,q1,q2)` plus `tests/test_fk_2r.py` generic tests. This starter is not learner evidence. Avoid duplicating it without thinking, avoid changing its public interface unintentionally; invite learner to independently derive/code a SCARA-specific implementation or tests. After FK code and unfamiliar-case validation, proceed to Reachability/Workspace, IK elbow branches and singularities.

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

## Scope and geometry update — 2026-11-04 (learner confirmed)

**Teaching plan:** initial P velocity-output simulation completed; PD torque/inertia practice paused to rebalance project deliverables. Do **not** demand production workcell design details during foundational XY kinematics learning.

**Confirmed by learner for exercises:** revised **Place=(120,140) mm** is approved as a provisional **XY target for introductory FK/IK**; under L1=130 mm and L2=110 mm (still *candidate* link lengths) radial distance is 184.391 mm, within ideal 20–240 mm reach. Previous Place=(160,200) mm (r≈256.125 mm) is unreachable with the candidate links. **Pick=(200,0) mm** can remain an illustrative previous test point, *not* a learner-confirmed final physical tray coordinate. No collision, joint-range or physical workcell feasibility is claimed.

**Explicit learner preference:** postpone detailed **tray dimensions, part dimensions, payload, gripper sizing and Z/tray clearance** until relevant mechanical engineering or collision-aware design phases. Learner considers those unnecessary at this early educational stage. Never ask for them simply to satisfy a requirements checklist now.

- Updated [SCARA-01 Requirements v0 learning baseline](docs/projects/SCARA-01-REQUIREMENTS-v0.md), leaving full physical Requirements Issue #6 OPEN for later.
- Preserve W2 unfinished architecture review; then Weeks 3–4 (Nov 9–22), independently write and test the planar 2R FK/IK ([Issue #3](https://github.com/hamora1370/Physical-AI/issues/3)).
- Detailed PD/torque-based simulation returns when hardware dynamics and actuator choice justify it.

## Earlier single teaching action — historical (superseded 2026-11-21)

Present a **single compact conceptual architecture** for SCARA-01: ROS 2 host (goal/planning/monitoring) → bounded local controller (feedback/control/watchdog/limits) → motor/driver → joint, with **joint encoder observations fed back to local controller and ROS reporting measured state rather than echoing commands**. Explicitly distinguish proposed architecture from implemented hardware. Ask one conceptual comprehension question about which part must enforce safety if host ROS 2 commands cease. After this short checkpoint, begin 2R FK/IK with known illustrative XY targets; do not drift into PD or tray/part sizing.

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
