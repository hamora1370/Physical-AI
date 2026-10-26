# ADR-0002 — SCARA-01 as a Robot-Learning-Ready Teaching Platform

- **Date:** 2026-10-26
- **Status:** Accepted by learner for design planning; implementation unverified
- **Decision owner:** Physical AI project

## Context

The first Q1 curriculum was overly centered on ROS middleware/software. The learner elected an integrated, project-based path with a compact, mostly FFF-printable SCARA, printable parallel gripper and independently controllable horizontal tool yaw. The five-year goal is ultimately **Physical AI**, not only a deterministic pick-and-place demonstrator. The initial SCARA should therefore avoid hardware/software decisions that block later perception, demonstration learning and closed-loop evaluation.

## Decision

1. Use **SCARA-01 compact R-R-P-R**, with J1/J2 planar rotary joints, J3 vertical Z, J4 independent yaw and separate parallel-jaw-gripper actuation, as the shared engineering and ROS teaching vehicle.
2. Make it a **robot-learning-ready platform by design**. Require observed joint-state feedback; timestamped commands, observations and errors; a stable ROS 2/host interface; gripper state/feedback provision; CAD/URDF/simulator-to-hardware frame/limit consistency; and future camera/calibration mounting provisions.
3. Teach **problem → theory → calculation → measured implementation → learner explanation** on this robot. ROS 2 is an implementation tool, not the sole curriculum.
4. Preserve the five-year sequence: **Q1 specification/model/simulation**, **Q2 safe hardware integration and state logging**, **later vision/data collection**, **Y2 imitation learning**, and VLA/RL investigations only when validated prerequisites exist. Vision and model training are not Q1 mandatory gates.
5. Keep fault detection, drive limits, watchdog, safe motion/stop and risk controls independent of higher-level ROS/AI inference. Do not imply a machine is safe solely because ROS 2 runs.
6. Retain SCARA's limited 4-DOF manipulation envelope: yaw is achievable; arbitrary 3-D orientation and part-flipping are out of version-one scope. A higher-DOF arm may be a *subsequent distinct robot*, not an automatic retrofit.

## Alternatives considered

- **Only software/ROS 2:** quick middleware experience, inadequate mechanical/control learning and less direct physical AI transition.
- **Six-axis arm immediately:** richer 3-D manipulation, but higher cost, more difficult printable structure/actuator design and more complex first safety/learning experience.
- **Simple 2R teaching arm:** easiest to build and benchmark, but less directly suited to vertical pick/place and yaw manipulation; useful as a staged subsystem of SCARA-01.

## Consequences

- **Benefits:** one reusable robot across mechanics, math, control, middleware, perception and robot-learning experiments; clear test/evidence interfaces; less risky actuator purchasing.
- **Tradeoffs:** sensor quality, data time alignment, cable/weight allowance for camera/gripper and feedback-capable actuators may increase cost and complexity. These are reviewed before CAD/motor procurement.
- **Limitations:** required features are design intentions, not proof of implemented encoders, simulator, datasets, policy learning or robust safety.

## References and revisit

- [Engineering concept](../projects/SCARA-01-CONCEPT.md)
- [Learning-platform requirements](../projects/SCARA-01-LEARNING-PLATFORM.md)
- [Q1 project-based learning](../roadmap/Q1-2026-10.md)

Review at the Q1 exit gate (2027-01-24), or sooner if working-volume, cost, force, sensor or safety requirements invalidate the SCARA choice.
