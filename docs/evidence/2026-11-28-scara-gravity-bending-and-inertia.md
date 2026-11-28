# SCARA-01 mechanical foundations: gravity bending vs yaw torque and mass distribution

**Date:** 2026-11-28  
**Track:** Y1/Q1 Weeks 5–6, mechanical and actuator engineering  
**Associated requirements task:** [Issue #6](https://github.com/hamora1370/Physical-AI/issues/6)  
**Skill candidate:** ME02 — preliminary actuator/load sizing (guided introductory calculations, not a design qualification).

## Concepts and independently answered checks

The learner correctly explained: gravity acting on a horizontal SCARA arm does **not** produce idealized torque about the vertical J1 yaw axis. The offset vertical weight does generate a bending moment about a *horizontal* axis. The joint bearing and structure must carry it. Example point mass m=0.10 kg at r=0.24 m: M_bending = m*g*r = 0.23544 N·m. This does **not** imply that the yaw motor needs 0.23544 N·m to hold position (ignoring friction, external disturbance, actuator details).

For inertial yaw torque in a deliberately simplified **single-axis, rigid-rotation model**:
- A 0.10 kg point mass at r=0.24 m and angular acceleration 2 rad/s²: learner independently answered `tau = 0.01152 N·m`, correct. Its moment of inertia is `I=0.00576 kg·m²`.
- Uniform straight link L=0.13 m, m=0.15 kg, rotating about an end: learner independently answered `I=0.000845 kg·m²` and `tau=0.00169 N·m` at 2 rad/s²; both correct. This uses `I=mL²/3` and neglects realistic link section/mass distribution.
- Relocation of a *simplified point mass* representing a J2 motor, m=0.20 kg, from r_A=0.13 m to r_B=0.03 m: learner answered `0.00338` and `0.00018`, both correct as **moments of inertia (kg·m²)** rather than requested torque. The instructor corrected: at 2 rad/s², `tau_A=0.00676 N·m`, `tau_B=0.00036 N·m`. This is an ~18.78x reduction in *that component* of inertial torque, not a claim about total joint torque.

## Limitations and caveats

These are pencil-and-paper/conversational calculations. No independent CAD, measured mass, designed bearing, bearing load rating, joint backlash, output torque curve, motor selection, print material stiffness, or physical test has been validated. The planar 2R mechanism's full dynamics include configuration-dependent inertia, joint coupling, link and gripper masses, losses, reflected motor/gear inertia, accelerations, gravity loads on supports and possible torsional transmission stiffness. Transferring the J2 motor to the base needs a transmission and introduces its own masses, friction, backlash and deflection.

**Assessed now:** correct explanation of loading directions; correct introductory inertia/torque calculation and recognition of point-mass-distance sensitivity after feedback. Not sufficient to mark ME02 independent skill L2 or physical design ready.

## Next ONE teaching step

Per [Q1 Weeks 5–6 roadmap](../roadmap/Q1-2026-10.md), move to **J1 mechanical load path and bearing arrangement**. Explain that a radial/axial bearing arrangement must resist weight and the overturning bending couple while the drive provides yaw torque; compare a single unsupported bearing vs two axially spaced bearings, using one qualitative reasoning check before numerical bearing loads. Then address practical bearing arrangements, shaft/hub mounting, printable link stiffness, and backlash tradeoffs. The learner prefers focused conceptual progression and not repetitive arithmetic drills.
