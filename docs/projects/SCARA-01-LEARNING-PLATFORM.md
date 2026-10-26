# SCARA-01 — Robot-Learning-Ready Architecture and Data Contract (v0)

**Decision:** Approved concept on 2026-10-26. SCARA-01 is both a compact FFF-printable **four-axis R-R-P-R SCARA** (J1, J2, vertical Z, independent yaw J4) with a separate printable two-jaw gripper, **and a future robot-learning experimental platform**. This page defines **design requirements**, not built or validated capabilities.

**Immediate task:** slow tray-to-tray transfers of lightweight 3D-printed parts at known pick/place positions. **Future tasks:** camera-guided pose estimation, human demonstrations, imitation learning, controlled policy evaluation, and eventually selected VLA/RL experiments. The initial robot cannot tilt or flip parts; only yaw is independently controllable.

## Core non-negotiable design requirements (not yet achieved)

| ID | Capability to preserve in hardware/software design | Verification / evidence gate | Stage |
|---|---|---|---|
| RL-01 | Observable joint state J1/J2/J3/J4: measured position and calibration/zero state; velocity where measurable (otherwise mark as estimated). Read *actual state*, never treat command as feedback. | Document sensor selection, units and frame convention; check measured vs commanded states in bench tests, including homing/restart. | Select design in Q1; instrument/test during Q2 |
| RL-02 | Repeatable, timestamped logging of commanded actions, measured joints, gripper state, execution results, errors/faults, and future camera observations. | Reconstruct ordered motion episodes and distinguish timestamps/clock sources; inspect dropped samples and sync uncertainty. | Q1 event/schema design; recording with actual hardware from Q2 onward; images when vision added |
| RL-03 | A documented ROS 2/host command-and-observation interface separated from the **local actuator controller** and independent stop. | Simulated controller accepts valid requests, rejects out-of-range poses and reports execution result/fault; same interface can later be implemented on hardware. | Interface in Q1; hardware integration Q2 |
| RL-04 | Printed parallel-jaw gripper with observable open/closed or jaw aperture state; reserve design accommodation for grasp-detection feedback (position/current/contact sensing). | Test on representative parts: grasp/open/close behavior, slip and failed grasps; do not infer possession from an open/close command alone. | Packaging/sensor decision Q1; bench tests Q2 |
| RL-05 | Geometric and semantic alignment between CAD, URDF/Xacro, kinematics, simulator and physical robot (same joint order, axes, limits, units and tool frame). | Replay a common test pose/trajectory in numeric FK, model and hardware when available; record residuals and limitations. | Q1 model/calculation; calibrate physical correspondence Q2 |
| RL-06 | Accommodate a future fixed RGB camera, calibration target and safe cable routing, without requiring camera purchase now. | Camera mounting envelope and tool/wrist occlusion considered; later camera-to-base calibration, timestamp compatibility and perception tests. | Mechanical provision Q1; camera and vision follow later |
| RL-07 | Action limits, watchdog, safe state and a physical/low-level stop path that **cannot be bypassed by ROS 2, AI or an inferred policy**. | Document stop logic and fault response; hardware-level tests before autonomous physical trials. | Plan Q1, implement/verify before physical motion |

### Explicit distinctions

- **Design-ready ≠ implemented.** No encoder, camera, gripper feedback, simulation, dataset, control interface or AI policy is currently proven on SCARA-01.
- **Four pose DOF** (X, Y, Z and yaw) require four controlled joints; the gripper opening actuator is separate. J4 angle under the convention in the concept brief is `q4 = desired_yaw - q1 - q2`, subject to travel limits and calibration.
- Prefer feedback-capable joint actuation on J1/J2/Z/J4, but **do not choose a particular servo/stepper/encoder** until torque, backlash, speed, cost and measurable feedback have been evaluated. A hobby servo command is not inherently an independent measured-joint observation.
- Robot-learning algorithms issue **bounded, validated high-level goals or trajectories** through a command gateway; they do not directly drive raw motor current or replace limit enforcement, watchdog or independent stopping.

## Conceptual ROS 2 interface — proposed, not implemented

| Direction | Suggested concept | Responsibility |
|---|---|---|
| Robot → Host | `/joint_states` (e.g., sensor_msgs/JointState) | Actual observed state and units, with header timestamp; velocity optional when trustworthy |
| Robot → Host | Gripper state topic/message, exact type TBD | Actual aperture/status and any grasp-detection observation; unknown sensor values explicitly unknown |
| Robot → Host | Diagnostic/fault event stream | Controller mode, homed state, limit hits, fault reason and quality of state |
| Host → Robot | Validated trajectory/goal command (action/interface TBD) | Joint/pose command plus limits and bounded time; local controller enforces constraints |
| Camera → Host (later) | Image/depth observations and calibrated camera frame | Image sensor timestamps, frame IDs, exposure/capture metadata if available |
| Recorder | Episode/bag/structured log | Time-correlated observations, goals, outcomes and fault/safety events |

The exact ROS 2 message types, QoS, action interfaces, embedded protocol and recorder format are **deferred design decisions**, not installed packages or compatibility claims. When imaging arrives, compare ROS time, steady clock, and sensor/device clocks; never assume numerical timestamps from unrelated clocks are synchronized.

## Minimum proposed episode record (schema proposal, not software)

```text
episode_id; experiment_id; code_commit; model_urdf_version; calibration_id;
scene_or_task_id; payload_description; source/tray target;
t_observed with named clock + optional timestamp uncertainty;
joint_positions_measured=[q1,q2,z,q4] or explicit missing;
joint_velocities_measured_or_estimated + provenance;
gripper_opening_measured_or_unknown; grasp_detected_measured_or_unknown;
action_requested (pose/joints/yaw/gripper); action_applied_or_rejected;
controller_mode, homed, limits, fault_code, stop_event;
camera_frame_reference + capture_timestamp (future/optional);
outcome definition, success/failure, interventions, elapsed_duration.
```

Units convention proposed: radians for J1/J2/J4, meters for Z, seconds for durations, explicit base/tool frame IDs for poses. The logging implementation must include missing-data semantics and measured-vs-commanded provenance. Do not store passwords, secrets, customer parts or private workshop images in a public repository.

## Training and evaluation path (not a Q1 requirement)

1. **Classical baseline:** repeat deterministic pick/place with known positions, record success rate, cycle time, repeatability and failures.
2. **Instrumented robot:** stream independently observed joints and gripper, calibration, fault events and optional camera. Reconstruct episodes and time alignment.
3. **Demonstrations:** create a controlled human-guided/teleoperated demonstration method that respects the robot's accessible DOF and stop/limit behavior; a demonstration method is not assumed to exist merely because a gripper is controllable.
4. **Behavior cloning:** train a small policy on consenting, safely collected data. Hold out locations/lighting/part instances from training; compare results against the classical baseline with stated sample counts.
5. **Advanced Physical AI:** explore RL/VLA only after sensor, control, evaluation and physical safety gates are satisfied. A four-axis SCARA is a valid constrained manipulation benchmark, not a general 6-DOF wrist manipulator.

## Quarterly implementation boundaries

**Q1 (2026-10-26 to 2027-01-24, ~65h):** decide measurable state/feedback options before actuator selection; publish a draft command/observation/logging contract; reserve camera mounting/cable space in CAD; define gripper sensing path; validate FK/IK and simulated sequence. No camera, dataset, policy model, hardware sync or working AI required. A *synthetic* simulated episode log is an optional bonus, not a gate.

**Q2 (2027-01-25 to 2027-04-25):** implement supervised low-energy bench hardware in stages, verify encoders/homing/stop paths, connect ROS 2 state and logging. Do not move the physical arm autonomously until faults/limits are tested.

**Q3–Q4 of Y1:** integrate camera and calibration if the mechanism, time and safety prerequisites are satisfied; create a classical vision-guided baseline and a small quality-controlled dataset pilot. Defer training and benchmarking learned policies to Y2 as planned unless evidence supports a safe, contained exploration.

**Y2 and beyond:** data-driven control, imitation-learning baseline, held-out evaluation; later VLA/RL tasks and, if task demands true roll/pitch, a separate higher-DOF arm. Preserve the reusable logging, ROS interfaces and safety boundary rather than promising full SCARA-to-6DOF mechanical conversion.

## Open decisions (next requirements review)

- Which actuator/sensor alternatives can supply *observed* joint positions under the target payload and cost?
- What is a minimal gripper sensor that meaningfully distinguishes contact/failed grasp from a command?
- Where can we reserve a noncolliding fixed-camera field of view and mounting point?
- What data collection sample rate and timestamp tolerance are **necessary** for the first controlled task (determine experimentally, do not invent numerical targets)?
- What low-level transport, watchdog and command limits are needed before physical testing?

**Related:** [SCARA-01 concept](SCARA-01-CONCEPT.md) · [Q1 study plan](../roadmap/Q1-2026-10.md) · [ADR-0002](../decisions/ADR-0002-scara-learning-platform.md).
