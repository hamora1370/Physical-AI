# SCARA-01 — Requirements v0 (workcell and geometry)

**Draft started:** 2026-11-04  
**Status:** `DRAFT / awaiting learner confirmation of workspace and part requirements` — **not** a validated engineering specification.  
**Issue:** [#6 — SCARA-01 workcell, printable mechanism and requirements](https://github.com/hamora1370/Physical-AI/issues/6)  
**Source of existing constraints:** [SCARA-01 concept](SCARA-01-CONCEPT.md), [robot-learning architecture](SCARA-01-LEARNING-PLATFORM.md), [Q1 roadmap](../roadmap/Q1-2026-10.md). Do not confuse early examples or assistant proposals with user-approved dimensions.

## A. Intended task / scope

- **CONFIRMED design intent:** compact benchtop, low-energy, mostly FFF-printable SCARA for slow transfer of small non-hazardous 3-D-printed parts between two stationary tray locations, with initial manually entered pick/place positions.
- **CONFIRMED concept:** **R-R-P-R** (J1 base yaw, J2 elbow yaw, J3 vertical slide, J4 tool yaw around Z) with a **separate actuator** for a printable two-parallel-jaw gripper. The learner requires in-plane part rotation but **not** roll, pitch or flipping.
- **CONFIRMED direction:** design as a future Physical AI/robot-learning platform, preserving real joint observation, reproducible timestamps, observable gripper state and a safe local control authority independent of ROS 2/AI.
- **NOT CONFIRMED:** actual tray size/coordinates, representative part range, allowable robot footprint, cycle time, accuracy or repeatability requirements; any motor, encoder, Z mechanism, gripper gearing or final structural material.

## B. Coordinate convention / axes

Adopt the conceptual model, **not yet validated in CAD**:

- Base origin `O=(0,0)` at J1 vertical axis; X/Y horizontal, Z positive upwards, positive joint rotations CCW viewed from above.
- Link lengths between J1–J2 and J2–tool-center axes: `L1`, `L2`.
- For ideal rigid planar model, with angles in radians:
  - `x = L1*cos(q1) + L2*cos(q1+q2)`
  - `y = L1*sin(q1) + L2*sin(q1+q2)`
  - `yaw = q1 + q2 + q4`
  - `z = z_ref + q3` is provisional: direction, absolute reference and stroke to be established.
- Gripper jaw opening has independent actuation; it is **not** the fifth pose DOF.
- Mechanical travel of J1, J2, J4, collision geometry, joint zero and tool offsets: **TBD**.

## C. Workcell hypothesis (not an approved layout)

The earlier example `Place=(160,200) mm` lies outside the proposed compact 2R arm's ideal range; do **not** retain it as a reachable target.

| Quantity / point (base XY, mm) | Value | Status / verification |
|---|---|---|
| Link 1, L1 | 130 mm | Provisional candidate; not measured/approved |
| Link 2, L2 | 110 mm | Provisional candidate; not measured/approved |
| Ideal minimum radius | `abs(130-110)=20 mm` | **Geometric only**, before joints/collisions |
| Ideal maximum radius | `130+110=240 mm` | **Geometric only**, before joints/collisions |
| Previous example Pick `(200,0)` | `r=200 mm` | Geometrically reachable; **not** a confirmed physical tray coordinate |
| Previous example Place `(160,200)` | `r=sqrt(160^2+200^2)=256.125 mm` | **Unreachable** even ideally with these links |
| **New proposed comparison point** Place `(120,140)` | `r=sqrt(120^2+140^2)=184.391 mm` | **Geometrically reachable only**; candidate for learner approval |
| Proposed transfer | `(200,0) -> (120,140)` in XY | **Illustrative test case**, not validated safe approach/grasp/tray placement |

No workspace mask, full arm/gripper collision assessment, tray dimensions, intermediate transfer waypoints, singularity clearance, Z lift/return trajectory or joint-limited IK check has been established. The two targets should only be treated as candidates for forthcoming geometry tests; **radial reachability is necessary, not sufficient**.

### Top-down text sketch (not to scale)

```text
                      +Y
                       ^
                       |    Place?  (120,140)  [candidate]
                       |      o
                       |
            J1 O(0,0)  +------------------------> +X
                       |               o  Pick? (200,0)
                       |
              prior Place (160,200): OUTSIDE 240 mm ideal reach
```

The sketch describes **target centers**, not full tray rectangles. Real tray dimensions and collision zones must be supplied separately before approving a workcell.

## D. Part, grasp and mechanism hypotheses

| Requirement | Candidate hypothesis | Decision / test still needed |
|---|---|---|
| Typical printed part | Earlier **40×30×30 mm** illustration | User to provide min/max dimensions and grasp face; not approved |
| Payload | Early **50–100 g** working range | User confirmation; wrist/gripper mass and loading not yet calculated |
| Jaw opening | Concept note **0–40 mm** candidate (other early discussions mentioned ~50 mm) | Not reconciled nor confirmed; derive from actual part orientations + finger clearance |
| Vertical transfer | Approx **60–80 mm** travel candidate | Confirm tray rim height, part height, safe Z clearance, jaw/tool length and vertical axis convention |
| Construction | Prefer printable structural links/covers and gripper; metal shafts/bearings/fasteners as required | Evaluate PETG/ASA stiffness, creep, transmission, insert and mechanism design later |
| Orientation | User-confirmed **yaw-only** part rotation by independent J4 | Confirm actual yaw range, clearance, cable twist, tool/grasp orientations |
| Precision | TBD | Distinguish absolute accuracy vs repeatability; develop measurement procedure and acceptance targets |
| Speed/cycle time | Slow, low energy (qualitative only) | Specify max speed, acceleration, timing and supervised test acceptance after constraints known |

## E. Robot-learning readiness and safety checklist (architecture-level, NOT implemented)

- [ ] Proposed observable joint states J1/J2/J3/J4 with homing/zero and physical or explicitly justified estimated joint position; commands are never logged as if they were measurements.
- [ ] Gripper aperture/status feedback and optional grasp success sensor concept.
- [ ] Time-stamped requested action, applied command, actual position/velocity (velocity may be estimated), gripper state, fault/status, clock source and calibration ID in an event/episode draft.
- [ ] ROS 2 host handles goals/trajectory/coordinating; **local actuator controller** enforces bounded motion, timeouts/watchdog, limit response and fault state. Separate effective stop and physical protections.
- [ ] Design Z loss-of-power behavior; never assume unpowered vertical actuator safely holds a load.
- [ ] Preserve consistent frame/axis conventions in future CAD, 2R FK/IK, URDF and simulated task.
- [ ] Reserve physical space and wiring/cable routing for future camera, no camera required to pass Q1.

## F. Requirements v0 acceptance gate / next incremental decision

**Gate not complete:** physical workcell sketch and measured (or explicitly chosen design) coordinates, part envelopes, grip approach, Z clearance, angular limits, first-pass joint/feedback diagram and learner explanation are still missing. Keep issue #6 OPEN.

**Next SINGLE learner choice (Nov 4):** Are we retaining illustrative `Pick=(200,0)` mm and provisionally replacing the unreachable old Place with `Place=(120,140)` mm, using J1 at the base origin, *only for the first FK/IK/workspace test*? Or does the learner prefer a different tray layout? On confirmation, mark these as **accepted test-case geometry** (still not final CAD). Only then expand to physical tray footprint / obstacle clearance.

**Schedule boundary:** PD torque/second-order numerical work paused by agreement 2026-11-04. Brief ROS/local controller architecture review follows v0 workcell decision; Weeks 3–4 (Nov 9–22) independent 2R FK/IK in [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3) remains mandatory. Guided P exercise was completed and evidenced in [2026-11-04 control note](../evidence/2026-11-04-scara-discrete-p-simulation.md).
