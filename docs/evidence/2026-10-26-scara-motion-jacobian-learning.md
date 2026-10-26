# SCARA-01 — motion, IK, velocity Jacobian and singularity (dialogue-based learning note)

**Date:** 2026-10-26 (Week 1; 2026-10-26 to 2026-11-01)
**Evidence source:** learner's conceptual answers in the Physical AI tutoring conversation on this date, plus tutor explanations. **No independently executed learner code, written derivation, test log, CAD, simulator or physical robot evidence is attached.**
**Assessment:** *conceptually discussed, multiple correct oral/chat responses, and learner explicitly reported understanding the Jacobian*. **Not an independent mastery/coding verification.**

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
| Jacobian | Tutor introduced partial derivatives of 2R FK, Jacobian as local mapping from joint velocities to Cartesian velocities, numerical example, inverse mapping, det/singularity, force/torque mapping. Learner later explicitly wrote: "این مفاهیم را متوجه شدم". | **Learner-reported understanding** after explanation; no independent derivation or worked numeric answer to certify M04 |
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

The symbolic determinant and examples are reference answers for subsequent independent exercises, not proof of learner's derivation or coding.

## Gaps deliberately still open

- No independently written/checked Jacobian derivation, numeric multiplication, determinant/singularity case or finite-difference comparison from the learner.
- No independently tested 2R FK/IK code or ROS robot-motion implementation, and no robot CAD/simulation.
- No confirmed initial tray dimensions, coordinates/clearances, actual component mass/size, joint travel, controller feedback hardware or gripper travel.
- No attempt to show direct force control, perception, RL, VLA, synchronized datasets or ROS 2 safety implementation.

## Rest-of-week learning plan (2026-10-26 to 2026-11-01)

**Goal:** consolidate understanding with a small independently checked calculation and an understandable goal-to-feedback architecture, *without rushing into robotics software infrastructure*. These are proposed blocks, not finished items; time spent earlier this week was not measured. Budget their total within the remaining share of the ~5 h/week.

| Order | Suggested focused time | Next activity | Independent evidence / stopping criterion |
|---|---:|---|---|
| 1 | 35–45 min | **One Jacobian exercise:** derive the four partial derivatives from SCARA 2R FK and calculate J at q1=0°, q2=90°; compute tool speed for (0.1, -0.1) rad/s. | Learner demonstrates J = [[-110,-110],[130,0]] mm/rad and v = (0,13) mm/s, explains columns. Allow guided correction; keep assessment as practiced until reproduced unaided. |
| 2 | 40–50 min | **Reachable configuration vs continuous safe movement:** inspect one SCARA pose with two IK elbows, compare joint limits; distinguish reaching a pose, checking whole path, and timing path. Discuss straight-arm singularity intuitively with det(J), no lengthy matrix inversion. | Learner explains why two IK branches may give different collision/joint-limit outcomes and why a geometric path alone lacks timing. |
| 3 | 45–60 min | **Control-loop architecture for future Physical AI:** sketch goal (x,y,z,yaw) → IK/motion plan/trajectory → low-level bounded execution → *measured* joint/gripper state → correction/logging; explain the future AI/camera entry point. | One labeled diagram and learner explanation distinguishing setpoint, command, sensor observation and independent safety; no ROS stack deployment required. |
| 4 | 20–30 min | **Weekly checkpoint / requirements carryover:** record unknown tray/part dimensions, safe Z clearance, tentative link/workcell geometry, selected next week's goal. Optionally run one tiny Python numeric Jacobian check **only if learner wants a practical coding exercise**. | Short note with known/assumed/open items and one next-action decision; do not overstate workshop requirements as validated. |

**Total remaining proposed content:** 140–185 minutes (~2 h 20 min–3 h 5 min), adaptable to availability and actual prior learning time. If time is tight, prioritize activities 1 and 3; carry activity 2/4 into Week 2. Do not interpret a suggested duration as a scheduled appointment.

## Status policy and links

- For skill matrix **M03** FK, **M04** Jacobians/singularity, **M05** IK, **P01** configuration/collision and **C02** trajectory concepts: set status only to `concept_discussed` (or a similarly explicitly non-mastery status) with current level **L0 (unassessed)** until learner independently demonstrates math/programmatic artifacts. A correct conceptual answer is evidence of *engagement and conceptual understanding*, not full L3 attainment.
- [Q1 roadmap](../roadmap/Q1-2026-10.md) · [Next session](../../NEXT_SESSION.md) · [SCARA requirements issue #6](https://github.com/hamora1370/Physical-AI/issues/6) · [FK tests issue #3](https://github.com/hamora1370/Physical-AI/issues/3)
