# SCARA-01 — project concept and engineering brief

**Status:** educational design baseline; on 2026-10-26 the learner requested a compact **mostly FFF-printable** machine, an FFF-printable gripper and ability to rotate the part. **No dimensions, performance, CAD, parts or hardware have been validated.**

**Role in Physical AI:** one shared robot for teaching coordinate frames, kinematics, mechanisms, actuator sizing, sensing, feedback, motion planning, ROS 2, simulation and eventually reliable practical automation. Teach each concept when it solves a concrete SCARA-01 problem; do not reduce the course to either software tooling or pure theory.

## Intended first use case

Move small, lightweight, non-hazardous 3D-printed parts from a known pickup position in a tray to known destination positions. The first task uses manually entered coordinates; camera-based localization, sorting, and ERP integration are later expansions.

**Learning platform:** desktop / benchtop, low-voltage, slow and low-energy demonstration. No live production use and no physical motion before suitable guarding, limits, homing and independently effective stop mechanisms have been reviewed.

## Architecture choice

Proposed **four axis** SCARA form (**R-R-P-R**) for 3-D tool position plus in-plane tool orientation:
- **J1:** revolute joint about the vertical Z axis at the base.
- **J2:** revolute joint about a parallel vertical Z axis at the elbow.
- **J3:** vertical prismatic Z axis at the tool.
- **J4:** revolute wrist/tool axis around the vertical Z direction, to adjust the part's **yaw angle independently** while maintaining its intended X-Y-Z position. Check physical travel/cable constraints before specifying joint range.
- **End effector:** a compact, light, **3-D-printable, two-parallel-jaw gripper** is the preferred baseline. Gripper open/close is one additional actuator and is not another independently controlled pose degree of freedom. Explore servo-driven printed rack-and-pinion / linkage mechanisms; final selection requires gripping-force, jaw-travel and backlash review.

The first two rotary axes form a planar 2R subproblem; adding Z and wrist yaw produces a four-DOF R-R-P-R SCARA-like model. **Tool yaw is not tool roll/pitch**: this robot cannot flip a part over without a further wrist/fixture mechanism. **The learner confirmed that yaw about vertical Z is the only part-rotation capability required for the initial version**; part flipping/roll/pitch is out of scope. A compact printed-link robot does not imply industrial positioning accuracy.

### Geometric model — proposed frame convention

Define the planar base origin at J1, X-Y horizontal, positive Z up, positive joint angles counterclockwise as viewed from above. Define `L1` and `L2` along the links between the J1/J2/tool-center axes. For an ideal rigid 2R mechanism:

```text
x = L1*cos(q1) + L2*cos(q1+q2)
y = L1*sin(q1) + L2*sin(q1+q2)
z = z_ref + q3                 # sign, offsets and stroke to be finalized
yaw = q1 + q2 + q4             # commanded absolute tool yaw in base XY, subject to frame conventions
q4  = desired_yaw - q1 - q2   # wrist command, provided joint limits allow it
```

For inverse kinematics of the X-Y target, check reachability and joint limits before selecting an elbow branch. The ideal geometric radial envelope is `abs(L1-L2) <= r <= L1+L2`; mechanical stops, self-collision, end-effector offsets, cable routing and clearances reduce the usable workspace. With the *new smaller* candidate `L1=130 mm`, `L2=110 mm`, the ideal annulus is `20 mm <= r <= 240 mm`, **not guaranteed usable**. Previously discussed points `(200,0)` and `(160,200)` are no longer both inside this ideal envelope: the second has radius about `256.1 mm` and must be moved or the geometry revised.

tf2 and URDF frames will use one documented, tested joint/frame convention; measurements must carry the correct timestamps.

## Preliminary targets — values to validate, not approved specifications

| Parameter | Early hypothesis | Validation required |
|---|---|---|
| Link lengths (J1-J2 / J2-tool center) | approximately **130 / 110 mm** | actual tray placement, gripper offset, link strength and joint stops |
| Ideal maximum radial reach | approximately **240 mm** | real clearance and joint-limited workspace; tray placement must be reworked |
| Vertical travel | approximately **60–80 mm** | clearance above the tray, carried part and gripper geometry |
| Nominal payload candidate | approximately **0.05–0.10 kg** | realistic grasp mass plus grip/wrist mass; worst-case torque, inertia, bending and deflection |
| End effector | **printed two-parallel-jaw gripper**, initial jaw opening candidate **0–40 mm** | part gripping range, grip force, printed tooth durability, friction, backlash and drive selection |
| Structure | **print both links, housings, gripper and cosmetic covers if calculations permit; retain metal shafts, bearings, bolts, inserts and suitable guide elements** | print orientation, anisotropy, creep, stiffness, fatigue, backlash and cost |
| Actuation | candidates after calculation; **at least five driven functions** J1/J2/Z/J4/gripper | servo/stepper/encoder tradeoffs, gear reduction, cable twist at J4, mass distribution and control |
| Performance | accuracy, repeatability, speed, cycle time **TBD** | define test method and safe measured acceptance threshold |
| Control | independent low-level motor controller plus ROS 2 on host | responsibilities, loss-of-comms response and position feedback |

**No purchasing or definitive CAD dimensions** before workspace, payload, precision and actuator tradeoffs are documented. Vision camera and ERP connectivity are out of Q1 mandatory scope.

## Learner-driven compact/printable requirements (2026-10-26)

- **Confirmed preference:** a compact benchtop robot with **both arm covers and, preferably, both structural links 3-D printable**, plus a gripper that can be FFF printed. The learner has access to a Creality K2 Plus printer with nominal 320 x 320 x 320 mm build volume; fit each individual manufactured component within that envelope after orientation, support and tolerances are considered. **Do not confuse part fit with overall robot swept-envelope size.**
- **Confirmed manipulation requirement (2026-10-26):** independently rotate the held part in the **horizontal plane (yaw about vertical Z)** at a selected X-Y-Z location. J4 wrist rotation is a required axis of the chosen SCARA-01 concept, **not a hypothetical future feature**. No flip, tilt, roll or pitch capability is needed for version 1. The actual allowable wrist rotation range and repeatability remain to be engineered.
- **Print/assembly approach:** prioritize a printed two-parallel-jaw mechanism, potentially rack/pinion or linkage driven by a compact servo, with replaceable contact pads. Bearings, guide rods, shafts, heat-set inserts, metal bolts and appropriate transmissions remain nonprinted where required. The gripper's actual force and stroke must be tested with representative printed parts.
- **Design consequences:** smaller arm and lighter wrist reduce lever-arm loading but restrict tray positions. Add a wrist-yaw joint without routing cables through unlimited rotation; initial travel limits will be determined by wiring and mechanical stops. Relocating heavy actuators toward the base is a tradeoff to evaluate, not a predetermined design.
- **Printable structural parts:** start with engineering review of PETG/ASA, layer orientation, stiffness, creep and gear wear; do not state final material, wall count, infill or load rating without tests. Avoid using FFF plastic as an unverified substitute for shafts/bearings or high-wear slide rails.
- **Open requirements:** smallest/largest representative printed part dimensions, tray arrangement, required wrist-yaw travel and repeatability, required position repeatability and allowable assembly footprint. Accuracy, repeatability, payload and actual tool mass are still unmeasured.

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
- **Mechanical:** parametric CAD, printable J1/J2 links and covers sized for available K2 Plus printer, printable gripper with mechanical bearing/shaft hardware, possible printed rack/pinion, support/alignment, motor location, belt/reduction backlash, inserts, fasteners and iterative test coupons. Start with PETG/ASA candidate material trials; select structural polymer and wall/print orientation only after stiffness/load/temperature testing.
- **Embedded/control:** homing, soft/hard travel limits, local position/velocity control, trajectory execution, watchdog and fault handling; hardware-level stop independent of ROS 2.
- **ROS 2:** state reporting, high-level move requests, robot model, tf2, logging, simulation and orchestration. ROS 2 timer/Executor behavior is analyzed in the context of measured motion scheduling rather than as an isolated software goal.
- **Future:** camera calibration/vision, closed-loop pick verification, operation tracking/ERP integration. Part flipping/roll/pitch is explicitly out of the initial task scope; reconsider only if a future application demands it.

## Q1 learning/demo gates (2026-10-26 to 2027-01-24)

**Mandatory, evidence-based Q1 result:**
1. A documented use case and validated workspace/problem requirements.
2. Independently derived and tested 2R FK/IK; joint limits, two elbow branches, unreachable and singular cases demonstrated.
3. Preliminary torque, speed, acceleration, load and structural estimates, with assumptions and uncertainties.
4. A versioned **four-axis R-R-P-R model concept** with frame conventions and yaw relation; deliver a reproducible **R-R-P motion model** as mandatory, and simulate J4 yaw as part of Q1 when feasible. Report unsupported/missing model or simulation capabilities rather than claiming completion.
5. A reproducible simulated low-speed tray-to-tray pick/place sequence with logs, clear success/failure definition and measured outcomes. Include tool yaw in the scenario when J4 simulation is supported; if full physical collision simulation is unavailable, document limitations and maintain a reproducible kinematic sequence.
6. A concise Q1 review: observations, tests, safety assumptions, defects and Q2 build plan.

**Stretch, only if design gates/time permit:** physical two-axis low-voltage benchtop prototype with independent stop and conservative motion tests; then optional Z/gripper. A completed working **four-axis physical SCARA with gripper** is **not** a mandatory 65-hour Q1 promise. The physical integration path continues into Q2.

## Week-by-week integration

| Weeks | Robotics questions | Project output |
|---|---|---|
| 1–2 | What task, four SCARA axes, printable gripper and link structures, coordinate frames and safe compact envelope? | Requirements v0, tray/base sketch, candidate printable mechanism and actuator/feedback options |
| 3–4 | How do frames, 2R FK/IK and workspace limits predict reachable grasp poses? | Derivations, tests and reachable/unreachable plots |
| 5–6 | How do payload, link stiffness, inertia and transmission affect sizing? | CAD concept, basic torque/deflection estimates and motor-selection rationale |
| 7–8 | How will encoders, homing, feedback and soft/hard limits work? | Control block diagram, bench-oriented interface, optional guarded 2R hardware |
| 9–10 | How do Jacobian, velocity/acceleration, tool yaw and motion profiles limit commands? | Time-parameterized R-R-P-R path and error/limit tests (J4 simulation optional gate) |
| 11–12 | How do URDF, tf2, ROS 2 and simulation realize the same robot? | Model with J4 concept, joint states, frame tree and reproducible simulated pick/place |
| 13 | What actually works, what fails, and what is the safe Q2 next step? | Report, skill evaluation, issue/evidence links and Q2 build backlog |

Each session: **physical problem → theory → small calculation/code/experiment → learner explanation → evidence**. Keep to ~5 focused hours/week, roughly 2 h reasoning/theory, 2 h hands-on and 1 h review.

## Immediate first session: system requirements (no motor purchases)

1. Describe two **compact, repositioned** fixed tray positions that lie within the new *joint-limited* workspace; approximate part dimensions and 50–100 g tentative payload range.
2. Sketch base, 2R printable links, Z, wrist-yaw J4, printable two-jaw gripper and coordinate frames; distinguish 4 pose DOF from gripper actuation.
3. Derive the 20–240 mm ideal annular workspace for the tentative 130/110 mm links and identify why real reach is smaller; the earlier Place=(160,200) is now beyond even the ideal maximum.
4. Capture unknowns and decisions in an engineering requirements table.
5. Only then begin parametric CAD and actuator tradeoffs.

## Evidence/state policy

Already discussed: coordinate frames and conceptual FK; ROS 2 node/topic and Executor lab exercises were learner-reported completed. Do not label independent FK/IK implementation, ROS simulation or hardware as verified until numerical test logs and actual artifacts are reviewed. Preserve prior ROS 2 exercise outcomes; they become evidence to apply to this SCARA project rather than exercises to repeat.
