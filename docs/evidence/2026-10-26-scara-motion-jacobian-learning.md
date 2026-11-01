# SCARA-01 — motion, IK, velocity Jacobian and singularity (dialogue-based learning note)

**Date:** initially 2026-10-26; **exercise completed 2026-11-01** (Week 1: 2026-10-26 to 2026-11-01)
**Evidence source:** learner's responses to four Jacobian exercise steps in the Physical AI tutoring conversation, supported by tutor explanations and checked arithmetic. **No learner-authored code, independent written artifact, unfamiliar-case test log, CAD, simulator or physical robot evidence is attached.**
**Assessment:** conceptual reasoning and **guided chat Jacobian derivation/velocity exercise PASS on 2026-11-01**. Not a validated independent software implementation or unfamiliar problem / full mastery benchmark.

## Scope and reference robot

- SCARA-01 is an approved compact **R-R-P-R** design concept: J1/J2 planar rotation, J3 Z translation, J4 independent tool yaw, and a separate printable parallel gripper (open/close).
- Tentative lengths **L1 = 130 mm, L2 = 110 mm**. Ideal unconstrained XY annulus **20–240 mm** radial reach; physical collision, joint travel, tool geometry, and actual workcell dimensions remain unvalidated.
- Learning preference: focus on mathematical/physical understanding, realistic robot control and future Physical AI. Defer detailed gripper gripping-force, servo torque, rack/pinion sizing and FFF mechanical detailing until actual design/sizing work in Weeks 5–6.
- Proposed baseline task: move small printed parts tray-to-tray and optionally rotate **yaw** in the horizontal plane. Earlier example **40×30×30 mm/100 g** is an illustrative assumption, not a confirmed payload requirement.

## Evidence: what learner answered correctly

| Concept | Learner response / direct exchange | Evidence status |
|---|---|---|
| IK multiple configurations | One endpoint target may be reachable with different mirrored arm configurations, one on each side of a symmetry line. | Correct conceptual explanation; joint-limit/IK branch solving untested |
| Motion planning vs IK | Learner correctly assigned collision-aware trajectory/route choice to Motion Planning. | Correct distinction; planning implementation untested |
| Joint-space vs Cartesian-space motion | Learner anticipated that joint-interpolated motion may create a curved tool path whereas a specified Cartesian line is straight. | Correct conceptual distinction; learner has not plotted trajectories |
| Constant tool speed, changing joint rates | Learner reasoned joint angular speeds generally change to maintain a constant tool Cartesian velocity; cited v = r·omega and geometry. | Correct outcome, with tutor clarification that *vector direction and contributions of both joints* are essential, not just a changing distance |
| Jacobian | Tutor introduced partial derivatives of 2R FK, Jacobian as local mapping from joint velocities to Cartesian velocities, numerical example, inverse mapping, det/singularity, force/torque mapping. Learner reported understanding, then solved all four guided chat exercise stages correctly on 2026-11-01. | **Guided calculation PASS**, with independent implementation and unseen-case assessment still open |
| Singular straight configuration | Tutor showed q1=q2=0 has instant x-velocity zero for any finite joint rates and explained nonlinear departure from singular posture. | Taught, not independently assessed |
| Engineering scope/prioritization | Learner challenged whether detailed grasp force was proportionate; agreed to prioritize robotics and Physical AI foundations. | Explicit curriculum preference |

## Reference math introduced (tutor material, not independently produced by learner)

2R planar FK, positive angles CCW viewed from above:

```text
x = L1 cos(q1) + L2 cos(q1 + q2)
y = L1 sin(q1) + L2 sin(q1 + q2)

J = [ -L1 sin(q1) - L2 sin(q1+q2), -L2 sin(q1+q2) ]
    [  L1 cos(q1) + L2 cos(q1+q2),  L2 cos(q1+q2) ]

[xdot,ydot]^T = J(q) [q1dot,q2dot]^T
det(J) = L1 L2 sin(q2)
```

At **q1 = 0°, q2 = 90°**, using mm and rad/s:

```text
J = [ -110, -110 ]
    [  130,    0 ]  mm/rad

(q1dot, q2dot) = (0.1, 0.0) rad/s  ->  (xdot,ydot) = (-11, 13) mm/s
(q1dot, q2dot) = (0.0, 0.1) rad/s  ->  (xdot,ydot) = (-11,  0) mm/s
(q1dot, q2dot) = (0.1,-0.1) rad/s  ->  (xdot,ydot) = (  0, 13) mm/s
```

At **q1 = q2 = 0°**:

```text
J = [   0,   0 ]
    [ 240, 110 ]  mm/rad
```

Here instantaneous **xdot = 0**, but the robot can depart the configuration and move inward on a suitable path starting with zero x-velocity; singularity is **not** a locked motor.

The determinant and the straight-arm singularity cases are still tutor reference explanations, not independently tested. **As of 2026-11-01, the learner has correctly derived the partial derivatives and solved the specific Jacobian numeric example in chat**, as detailed below.

## Gaps deliberately still open

- **Completed in guided chat:** all four symbolic Jacobian entries, one numeric Jacobian matrix, forward velocity multiplication, and one inverse-velocity linear solve, with correct answers. **Still open:** a new unseen numerical test, independent code/automated tests, determinant/singularity check and finite-difference comparison.
- No independently tested 2R FK/IK code or ROS robot-motion implementation, and no robot CAD/simulation.
- No confirmed initial tray dimensions, coordinates/clearances, actual component mass/size, joint travel, controller feedback hardware or gripper travel.
- No attempt to show direct force control, perception, RL, VLA, synchronized datasets or ROS 2 safety implementation.

## Rest-of-week learning plan (2026-10-26 to 2026-11-01)

**Goal:** consolidate understanding with a small independently checked calculation and an understandable goal-to-feedback architecture, *without rushing into robotics software infrastructure*. These are proposed blocks, not finished items; time spent earlier this week was not measured. Budget their total within the remaining share of the ~5 h/week.

| Order | Suggested focused time | Next activity | Independent evidence / stopping criterion |
|---|---:|---|---|
| 1 | 35–45 min | **COMPLETED 2026-11-01 (guided chat):** learner derived all four partial derivatives, computed J at q1=0°, q2=90°, tool speed for (0.1,-0.1) rad/s, and additionally solved desired v=(11,13) mm/s → qdot=(0.1,-0.2) rad/s. | All four stages checked correct. No code or unfamiliar-case test yet; full M04 mastery not claimed. |
| 2 | 40–50 min | **Reachable configuration vs continuous safe movement:** inspect one SCARA pose with two IK elbows, compare joint limits; distinguish reaching a pose, checking whole path, and timing path. Discuss straight-arm singularity intuitively with det(J), no lengthy matrix inversion. | Learner explains why two IK branches may give different collision/joint-limit outcomes and why a geometric path alone lacks timing. |
| 3 | 45–60 min | **Control-loop architecture for future Physical AI:** sketch goal (x,y,z,yaw) → IK/motion plan/trajectory → low-level bounded execution → *measured* joint/gripper state → correction/logging; explain the future AI/camera entry point. | One labeled diagram and learner explanation distinguishing setpoint, command, sensor observation and independent safety; no ROS stack deployment required. |
| 4 | 20–30 min | **Weekly checkpoint / requirements carryover:** record unknown tray/part dimensions, safe Z clearance, tentative link/workcell geometry, selected next week's goal. Optionally run one tiny Python numeric Jacobian check **only if learner wants a practical coding exercise**. | Short note with known/assumed/open items and one next-action decision; do not overstate workshop requirements as validated. |

**Original proposed content:** 140–185 minutes, of which the guided Jacobian exercise is **completed**. Other blocks are optional carryover; since 2026-11-01 is the final day of Week 1, prioritize an accessible closed-loop-control introduction today and continue as needed in Week 2. If time is tight, prioritize activities 1 and 3; carry activity 2/4 into Week 2. Do not interpret a suggested duration as a scheduled appointment.

## Status policy and links

- For skill matrix **M03** FK, **M04** Jacobians/singularity, **M05** IK, **P01** configuration/collision and **C02** trajectory concepts: set status only to `concept_discussed` (or a similarly explicitly non-mastery status) with current level **L0 (unassessed)** until learner independently demonstrates math/programmatic artifacts. A correct conceptual answer is evidence of *engagement and conceptual understanding*, not full L3 attainment.
- [Q1 roadmap](../roadmap/Q1-2026-10.md) · [Next session](../../NEXT_SESSION.md) · [SCARA requirements issue #6](https://github.com/hamora1370/Physical-AI/issues/6) · [FK tests issue #3](https://github.com/hamora1370/Physical-AI/issues/3)

## Guided Jacobian exercise — verified PASS (2026-11-01)

**Observed evidence in conversation:** user supplied every requested answer. Tutor provided the FK expressions, derivative rule and structured prompts, so this is a **guided problem**, not closed-book or independently tested implementation. The symbolic derivatives and numeric responses are the learner's own typed answers (notation normalized below), rather than merely learner agreeing with the solution.

- **Stage 1 (X partial derivatives):** learner gave `∂x/∂q1 = -L1*sin(q1)-L2*sin(q1+q2)`, `∂x/∂q2 = -L2*sin(q1+q2)`; evaluated both as **-110 mm/rad** at q1=0°, q2=90°. **PASS**.
- **Stage 2 (Y partial derivatives):** learner gave `∂y/∂q1 = L1*cos(q1)+L2*cos(q1+q2)`, `∂y/∂q2 = L2*cos(q1+q2)`; evaluated as **130** and **0 mm/rad**. **PASS**.
- **Stage 3 (forward velocity):** with `J=[[-110,-110],[130,0]] mm/rad` and `qdot=[0.1,-0.1] rad/s`, learner answered `[xdot,ydot]=[0,13] mm/s`, direction **+Y**. **PASS**.
- **Stage 4 (inverse velocity):** with desired `[xdot,ydot]=[11,13] mm/s`, learner solved `qdot=[0.1,-0.2] rad/s`. Independently checked: `xdot=-110(0.1)-110(-0.2)=11` and `ydot=130(0.1)+0(-0.2)=13` mm/s. **PASS**.

**Exercise conclusion:** the four-step **guided 2R Jacobian exercise is complete**. This is better evidence than a self-report but **does not complete full M04 / the Week 9–10 Jacobian gate**: still need closed-book explanation, an unfamiliar numeric configuration, programmatic check, limits and singularity diagnosis. Per [learning level policy](../LEARNING_SYSTEM.md), skill **M04 remains L0/unassessed for closed-book independent mastery**, while `status=guided_exercise_passed` reflects observed progress. `L1` requires explanation without reference and `L2` requires independently implemented/tested code.

**Immediate next topic (learner-requested):** Closed-Loop Control in SCARA-01: desired vs measured joint position, control error `e=q_target-q_measured`, a simple illustrative proportional correction, sensor feedback vs command, safety and where ROS 2/AI may interface. Present **one simple case and one question** before PI/PID, controller timing, advanced hardware or ROS implementation. 

## Guided Jacobian exercise: PASS (2026-11-01)

**Evidence:** Four-step learner-authored answers in the tutoring conversation, checked against the equations. The tutor supplied the SCARA FK equations and structured prompts. This is a completed **guided mathematical exercise**, not an independent code test or closed-book proficiency test.

| Stage | Answer entered by learner | Check |
|---|---|---|
| X derivatives | dx/dq1 = -L1 sin(q1) - L2 sin(q1+q2); dx/dq2 = -L2 sin(q1+q2). At 0°,90°: -110, -110. | PASS |
| Y derivatives | dy/dq1 = L1 cos(q1) + L2 cos(q1+q2); dy/dq2 = L2 cos(q1+q2). At 0°,90°: 130, 0. | PASS |
| Forward velocity | For qdot=(+0.1,-0.1) rad/s, tool velocity=(0,+13) mm/s, along +Y. | PASS |
| Inverse velocity | For requested tool velocity=(+11,+13) mm/s, learner calculated qdot=(+0.1,-0.2) rad/s. | PASS |

Reference: L1=130 mm, L2=110 mm, q1=0°, q2=90°, J=[[-110,-110],[130,0]] mm/rad.

**Verification of final step:** Vx=-110(0.1)-110(-0.2)=+11 mm/s; Vy=130(0.1)+0(-0.2)=+13 mm/s.

**Assessment boundary:** Four-stage guided Jacobian exercise is **complete**. User has demonstrated correct partial differentiation, evaluation, forward multiplication and inverse linear solve for this known case. No novel-case test, independent Python implementation, closed-book explanation, determinant calculation by learner or physical robot test was provided. Maintain a distinction between a passed exercise and full M04 proficiency under [learning level rules](../LEARNING_SYSTEM.md): L1 requires explanation without reference and L2 independently tested implementation.

**Next learner-requested topic:** SCARA-01 closed-loop control. Teach desired joint position versus independently measured position, error, local correction and bounded low-level control; then build from one illustrative J1 example. Full closed-loop hardware/simulation implementation is pending.
