# SCARA-01 — project concept and engineering brief

**Status:** proposed educational design baseline, approved as the Q1 anchor project on 2026-10-26. **Not yet engineered, purchased, modeled, simulated, assembled, or validated.**

**Role in Physical AI:** one shared robot for teaching coordinate frames, kinematics, mechanisms, actuator sizing, sensing, feedback, motion planning, ROS 2, simulation and eventually reliable practical automation. Teach each concept when it solves a concrete SCARA-01 problem; do not reduce the course to either software tooling or pure theory.

## Intended first use case

Move small, lightweight, non-hazardous 3D-printed parts from a known pickup position in a tray to known destination positions. The first task uses manually entered coordinates; camera-based localization, sorting, and ERP integration are later expansions.

**Learning platform:** desktop / benchtop, low-voltage, slow and low-energy demonstration. No live production use and no physical motion before suitable guarding, limits, homing and independently effective stop mechanisms have been reviewed.

## Architecture choice

Three *positioning* degrees of freedom of SCARA form (R-R-P):
- **J1:** revolute joint about the vertical Z axis at the base.
- **J2:** revolute joint about a parallel vertical Z axis at the elbow.
- **J3:** vertical prismatic Z axis at the tool.
- **End effector:** a simple mechanical gripper or vacuum tool; its open/close actuation is an extra control function, not counted among the three positioning DOF.
- **Future J4 (optional):** rotation of the tool about the vertical axis, for independent in-plane yaw orientation; defer until needed.

The first two rotary axes form a planar 2R subproblem; adding Z creates the 3-DOF model. This is an educational SCARA-like RRP robot, not a promise of full 3D arbitrary orientation or industrial SCARA accuracy.

### Geometric model — proposed frame convention

Define the planar base origin at J1, X-Y horizontal, positive Z up, positive joint angles counterclockwise as viewed from above. Define `L1` and `L2` along the links between the J1/J2/tool-center axes. For an ideal rigid 2R mechanism:

```text
x = L1*cos(q1) + L2*cos(q1+q2)
y = L1*sin(q1) + L2*sin(q1+q2)
z = z_ref + q3                 # sign, offsets and stroke to be finalized
yaw = q1 + q2                 # if tool rigidly follows link 2; not an independent DOF
```

For inverse kinematics of the X-Y target, check reachability and joint limits before selecting an elbow branch. The ideal geometric radial envelope is `abs(L1-L2) <= r <= L1+L2`; mechanical stops, self-collision, end-effector offsets, cable routing and clearances reduce the usable workspace. At the planned lengths below, `40 mm <= r <= 320 mm` is only the unconstrained geometric annulus, **not a guaranteed usable workspace**.

tf2 and URDF frames will use one documented, tested joint/frame convention; measurements must carry the correct timestamps.

## Preliminary targets — values to validate, not approved specifications

| Parameter | Early hypothesis | Validation required |
|---|---|---|
| Link lengths (J1-J2 / J2-tool center) | approximately 180 / 140 mm | reachable tray layout, link strength, collision envelope |
| Ideal maximum radial reach | approximately 320 mm | workspace with hard joint limits and tool geometry |
| Vertical travel | approximately 80–120 mm | tray clearance, gripper dimensions and Z actuator load |
| Nominal payload candidate | 0.1–0.2 kg | worst-case static/dynamic torque, arm inertia, acceleration and deflection |
| End effector | light parallel-jaw gripper; vacuum alternative | actual part size/shape and retention requirements |
| Structure | 3D-printed housings/links, metal shafts/bearings as needed | stiffness, fatigue, backlash, tolerances and cost |
| Actuation | shortlisted only after torque/speed and feedback analysis | voltage, gear reduction, motor/driver, heating and control |
| Performance | accuracy, repeatability, speed, cycle time **TBD** | define test method and safe measured acceptance threshold |
| Control | independent low-level motor controller plus ROS 2 on host | responsibilities, loss-of-comms response and position feedback |

**No purchasing or definitive CAD dimensions** before workspace, payload, precision and actuator tradeoffs are documented. Vision camera and ERP connectivity are out of Q1 mandatory scope.

## Engineering questions to answer before CAD freeze

1. What are the pickup and destination tray dimensions, robot base placement, required Z clearance and the minimum accessible radial reach?
2. What are the largest/heaviest representative printable parts, grasp points and desired tool orientation?
3. What positioning **repeatability** and absolute **accuracy** are needed? How will each be measured separately?
4. What cycle time, smoothness and maximum speed are acceptable for the low-energy prototype?
5. What are the motion limits, collision cases, homing procedure, cable routing and loss-of-power behavior?
6. Which joints require encoders or closed-loop feedback, and how will joint zero/calibration be established?
7. How much do joint gear backlash and printed-link flexure contribute to total positioning error?

## Architecture boundaries

- **Math/robotics:** frame models, FK, IK with elbow branches/unreachable targets, Jacobian, link inertia, gravity on Z, torque/speed envelopes and motion profiles.
- **Mechanical:** parametric CAD, printed vs metal components, bearings, transmission choice, belt/reduction backlash, fasteners and printable assembly.
- **Embedded/control:** homing, soft/hard travel limits, local position/velocity control, trajectory execution, watchdog and fault handling; hardware-level stop independent of ROS 2.
- **ROS 2:** state reporting, high-level move requests, robot model, tf2, logging, simulation and orchestration. ROS 2 timer/Executor behavior is analyzed in the context of measured motion scheduling rather than as an isolated software goal.
- **Future:** tool yaw, camera calibration/vision, closed-loop pick verification, operation tracking/ERP integration.

## Q1 learning/demo gates (2026-10-26 to 2027-01-24)

**Mandatory, evidence-based Q1 result:**
1. A documented use case and validated workspace/problem requirements.
2. Independently derived and tested 2R FK/IK; joint limits, two elbow branches, unreachable and singular cases demonstrated.
3. Preliminary torque, speed, acceleration, load and structural estimates, with assumptions and uncertainties.
4. A versioned 3-DOF RRP URDF/Xacro model with correct frame convention, visualized and joint state/transform inspection confirmed (tooling availability permitting; document blockers).
5. A reproducible simulated low-speed tray-to-tray pick/place sequence with logs, clear success/failure definition and measured outcomes; if full physical collision simulation is unavailable, document limitations and maintain a reproducible kinematic sequence.
6. A concise Q1 review: observations, tests, safety assumptions, defects and Q2 build plan.

**Stretch, only if design gates/time permit:** physical two-axis low-voltage benchtop prototype with independent stop and conservative motion tests; then optional Z/gripper. A completed working three-axis physical SCARA is **not** a mandatory 65-hour Q1 promise. The physical integration path continues into Q2.

## Week-by-week integration

| Weeks | Robotics questions | Project output |
|---|---|---|
| 1–2 | What task, DoF, mechanisms, coordinates, acceptable safety envelope? What ROS basics are already evidenced? | Requirements v0, workcell sketch, actuator/feedback options, past lab debrief |
| 3–4 | How do frames, 2R FK/IK and workspace limits predict reachable grasp poses? | Derivations, tests and reachable/unreachable plots |
| 5–6 | How do payload, link stiffness, inertia and transmission affect sizing? | CAD concept, basic torque/deflection estimates and motor-selection rationale |
| 7–8 | How will encoders, homing, feedback and soft/hard limits work? | Control block diagram, bench-oriented interface, optional guarded 2R hardware |
| 9–10 | How do Jacobian, velocity/acceleration and motion profiles limit commands? | Time-parameterized 3-DOF path and error/limit tests |
| 11–12 | How do URDF, tf2, ROS 2 and simulation realize the same robot? | Model, joint states, frame tree and reproducible simulated pick/place |
| 13 | What actually works, what fails, and what is the safe Q2 next step? | Report, skill evaluation, issue/evidence links and Q2 build backlog |

Each session: **physical problem → theory → small calculation/code/experiment → learner explanation → evidence**. Keep to ~5 focused hours/week, roughly 2 h reasoning/theory, 2 h hands-on and 1 h review.

## Immediate first session: system requirements (no motor purchases)

1. Describe two fixed tray positions, plausible part dimensions and a target payload range.
2. Sketch base, 2R links, Z axis, gripper and coordinate frames; distinguish 3 positioning DOF from gripper actuation.
3. Derive the ideal annular workspace from candidate link lengths and identify why real reach is smaller.
4. Capture unknowns and decisions in an engineering requirements table.
5. Only then begin parametric CAD and actuator tradeoffs.

## Evidence/state policy

Already discussed: coordinate frames and conceptual FK; ROS 2 node/topic and Executor lab exercises were learner-reported completed. Do not label independent FK/IK implementation, ROS simulation or hardware as verified until numerical test logs and actual artifacts are reviewed. Preserve prior ROS 2 exercise outcomes; they become evidence to apply to this SCARA project rather than exercises to repeat.
