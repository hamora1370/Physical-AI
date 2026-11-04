# SCARA-01 — discrete P position-control simulation (learning checkpoint)

**Date:** 2026-11-04 · **Q1 Week:** 2 (Nov 2–8) · **Status:** **PASS — guided educational P exercise completed**; next topic: PD.
**Source of evidence:** learner's Python script and plotted comparison uploaded in the Physical AI learning conversation. Script was also read and executed in an independent Python environment as part of the review. **It has not been committed to the GitHub repository by this documentation update.**

## Objective and scope

Implement and reason about a **position P controller whose output is an angular-velocity command**, assuming an ideal drive that follows commanded velocity instantly and holds it constant until the next controller update. **This is not a torque-controlled inertial joint, measured physical SCARA, ROS 2 hardware integration, or validated servo.**

- Target: 60 degrees; initial simulated joint position: 50 degrees.
- Gain: `Kp=2 s^-1`; use angle in degrees and commanded velocity in degrees per second.
- Per-cycle logic: `e[k]=target-theta[k]`; `omega[k]=Kp*e[k]`; `theta[k+1]=theta[k]+omega[k]*Ts` (zero-order-hold, ideal velocity tracking).
- Error recurrence: `e[k+1]=(1-Kp*Ts)e[k]`. **Asymptotic stability in this model:** `0<Kp*Ts<2`. This condition is **not transferable as-is** to a torque-output P/PD controller with inertia, friction and actuator lag.

## User work inspected

1. Completed TODOs for error, commanded velocity and position integration; ran a ten-cycle simulation (Ts=0.1 s). Correctly explained why the logged pre-update error differs from the post-update position, then separated error-before/error-after in output.
2. Saved time/position arrays, made the first user-generated position-versus-time PNG, and correctly explained decreasing slope as decreasing P velocity command with decreasing error.
3. Changed Ts to 0.8 s, correctly interpreted alternating overshoot with decreasing amplitude and reported a convergent oscillation.
4. Changed Ts to 1.2 s, independently predicted the first two positions **74° and 40.4°**, produced a plot of diverging oscillations.
5. Refactored the algorithm as `simulate_p(theta_initial, theta_target, kp, dt, steps)`, returning times and positions, then generated a **single three-case comparison plot** (`j1_position_cases.png`). Code syntax and output were independently checked for this report.

### Reproducible comparison, verified independently

| Case | Ts (s) | Steps | Total simulated time (s) | Multiplier `1-Kp*Ts` | Final position (degrees) | Expected / observed |
|---|---:|---:|---:|---:|---:|---|
| Monotonic | 0.1 | 72 | 7.2 | +0.8 | 59.9999989469 | Asymptotically convergent, no overshoot |
| Convergent oscillation | 0.8 | 9 | 7.2 | -0.6 | 60.10077696 | Alternating, decaying overshoot |
| Divergent oscillation | 1.2 | 6 | 7.2 | -1.4 | -15.29536 | Alternating, growing magnitude |

Numerical result for Ts=1.2 s: `theta[0:3] = [50, 74, 40.4]`. Note 6 steps versus 72 steps because all three cases cover **7.2 seconds of simulated time**.

Illustrative core algorithm (degrees and seconds):

```python
def simulate_p(theta_initial, theta_target, kp, dt, steps):
    theta = theta_initial
    times, positions = [0.0], [theta]
    for k in range(steps):
        error = theta_target - theta
        omega_cmd = kp * error
        theta += omega_cmd * dt
        times.append((k + 1) * dt)
        positions.append(theta)
    return times, positions
```

**Artifact provenance:** learner-supplied Python file `p_control_j1(2).py` (SHA-256 `f799aed22927bd4f3d151e17b45dc345771892ee139a12ddc73553d43d87ad8d`) and comparison image `j1_position_cases.png` (SHA-256 `21abb6ebec8a783c8edb36f2b407698527d68834f922da18a5bfca0d0606c026`). These are **conversation uploads**, not repository paths, as of this checkpoint. Local learner work was performed in their WSL PhysicalAI workflow; the exact state of their local Git tree was not verified.

## Review notes / improvements

- In the comparison script, `plt.axhline(..., label="Target Position")` is inside the cases loop and unnecessarily adds the same target line and legend entry three times. Move it **outside** the loop.
- A separate preliminary `simulate_p(...dt=1.2...)` call before the comparison loop is redundant; remove it.
- For future code review: prefer small checks/assertions for the first two steps, and keep `theta_target` used for plotting consistent with the simulation target.
- Simulated values outside mechanical joint limits are mathematical illustrations **not** feasible or safe real motion commands; no joint limits or motor saturation are modeled.
- P topic is **complete for this guided teaching unit**. Do not claim a fully tuned controller, verified joint sensor, numerical time-jitter experiment on actual hardware, complete C01 skill mastery, or closed Q1 mechatronics gates.

## Next teaching action: transition to PD with an appropriate plant

**Critical architecture choice:** the P experiment has a **velocity-command output** and ideal instantaneous speed tracking. To make the effect of D on real joint damping meaningful, first explicitly change to an **inertial torque-controlled joint model**, e.g. `I*theta_ddot + b*theta_dot = torque`, and then `torque_cmd=Kp*(target-theta)-Kd*theta_dot` for a fixed target. Derive units and interpret damping before any numerical code. Do not silently reuse the speed-P model for torque-PD; the gains have different units. Introduce **one concept and one exercise at a time**, then build the next simulation with the learner.

## Remaining Q1 tasks

- Requirements issue #6: confirmed workcell/trays/parts, joint limits and Z safe-clearance sketch remain open.
- Independent planar FK/IK code and tests issue #3 remain open. P exercise is not a substitute.
- Current simulator has no gravity/gearbox/backlash, friction, inertia, saturation, measured encoders, ROS 2 hardware, protection system or physical robot.

[Week 2 study plan](../roadmap/Q1-2026-10.md) · [Resume point](../../NEXT_SESSION.md) · [Earlier feedback and fault reasoning](2026-11-02-scara-feedback-and-fault-learning.md).
