# SCARA-01 — closed-loop control, sensing, tracking and fault reasoning

**Logged:** 2026-11-02 · **Period covered:** 2026-11-01 to 2026-11-02 · **Learning week:** Week 2 starts 2026-11-02.
**Evidence type:** learner's answers and tutor feedback in the Physical AI tutoring conversation. This is **conceptual and guided arithmetic evidence**, not an independent controller implementation, actuator test or measured SCARA telemetry.

## Observed progress (be precise about evidence)

| Topic | What learner actually demonstrated | Assessment |
|---|---|---|
| Position feedback & error | Correctly identified 43° measured vs 40° target as a **3° negative correction**, i.e. e=-3°. | Correct guided reasoning |
| P proportional control | With target 60°, measured 55°, Kp=3 s^-1, learner answered **+15**, correct direction/magnitude; originally labeled it **rad/s**. Tutor corrected required units to **+15 deg/s** (≈0.262 rad/s). | Partial numeric pass; **unit correction was needed** |
| PD damping | Correctly reasoned: at e=0 with positive joint velocity, position-P torque is zero while PD demands a negative braking torque. | Correct conceptual explanation |
| PD numeric | At e=0, qdot=-2 rad/s and Kd=0.15 N·m·s/rad, learner calculated **+0.3 N·m**. | Correct guided arithmetic |
| Motion command abstraction | Asked whether real robots command position, velocity or torque; correctly noted servo drives often have internal PD/PID (sometimes cascaded) control. | Correct conceptual reasoning; no specific drive selected |
| Gear backlash/feedback | Correctly described reversal dead travel: motor encoder registers motion while the joint can remain stationary before gear lash is taken up. | Correct physical reasoning |
| Tracking error & monitoring | Correctly explained that a transient 3° tracking error is not automatically failure; evaluate time, movement, persistence and growth. Tutor clarified transient growth during acceleration may be normal if within tolerance. | Correct concept with caveat |
| Fault detection vs diagnosis | Correctly identified motor, encoder, cable and mechanical transmission as possible causes of a fixed encoder reading during commanded motion. | Correct multi-hypothesis reasoning |
| Fault isolation | For motor encoder moving, joint encoder stationary, current normal, learner favored joint encoder fault (and noted a hard jam may increase current). Tutor explained **transmission breakage / belt slip / coupling slip** also fits normal current and motor motion. | Learner hypothesis is plausible, **not a confirmed diagnosis**; independent corroboration needed |

## Tutor-provided content (not an independent learner result)

- Position, velocity and torque interface alternatives; low-level drive versus host ROS 2 planning; commanded/estimated versus independently measured **joint** position.
- P and PD joint-torque laws, static-friction and overshoot illustrations; distinctions between velocity-command versus torque-command P laws and drive saturation.
- Tutor showed a **P-vs-PD illustrative plot and model with hypothetical parameters** in conversation; the user interpreted the qualitative behavior correctly. **No code execution by learner, hardware measurements, or repository-backed simulation artifact has been verified here.**
- Tracking error vs final goal error; monitoring/tolerances; possible failure signatures and safe action before fault cause is known.
- Fault detection → fault isolation/diagnosis → fault handling. A stall is not inferred from a single unchanged sensor measurement.

## What this establishes, and what it does not

**Established:** elementary P/PD feedback reasoning, sign and braking-torque arithmetic, backlash/encoder limitations, error-trend interpretation, and need for multiple observations in diagnosis. All supported by actual dialogue responses.

**Not established:** a working servo/encoder, a measured motor current, automatic diagnosis, functional watchdog, implemented safety protection, closed-loop software/hardware, precise actuator timing, or completed Q1 control architecture. Full C01, SN01, C02 skill levels remain **unassessed**, although concepts were discussed and practiced.

## Next guided study: sampling period and loop frequency (2026-11-02)

**Starting definition:** `T_s` is the period between scheduled updates and `f_s = 1/T_s`; e.g., 1 ms → 1000 Hz, 10 ms → 100 Hz, 100 ms → 10 Hz. Distinguish **nominal loop period**, measured interval and **jitter**; distinguish controller update from encoder sampling, driver current control and ROS 2 high-level commands.

**Next numerical exercise (not completed yet):** for a simple *illustrative* discrete J1 proportional controller with position measured in degrees, `omega_cmd[k] = Kp*(q_target-q_measured[k])`, `Kp=2 s^-1`, `q_target=60°`, `q_measured=50°`, find command speed and **ideal one-period position change** for `T_s=0.01 s`. The 0.2° one-step ideal displacement is a tutor reference result, **not** a learner answer. Explain assumptions of exact velocity following and sample-hold.

**Follow-up:** time delay/jitter, discrete derivative definition (avoid naive D term without dt), why faster-than-necessary updates are not automatically better, and a small safe simulation or loop timing experiment if user chooses.

## Carryover / physical-robot caveats

- Robot concept remains R-R-P-R, separate observable gripper, possible future camera, independent safety; no real SCARA build or controller has been verified.
- Unknown: final encoder placement, driver interfaces, network transport, actual control bandwidth, measured plant parameters, joint/tray dimensions, limits and realistic sampling requirements.
- [Current quarter roadmap](../roadmap/Q1-2026-10.md) · [Next session](../../NEXT_SESSION.md) · [Learning-ready architecture](../projects/SCARA-01-LEARNING-PLATFORM.md) · [Original Jacobian exercise evidence](2026-10-26-scara-motion-jacobian-learning.md).
