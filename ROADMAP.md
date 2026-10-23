# Physical AI — Five-year roadmap

**Period:** 2026-10-23 to 2031-10-23. **Profile:** mechanical engineering + full-stack/industrial software + additive manufacturing.
**Primary focus:** robotic manipulation and reliable physical AI for manufacturing—not humanoid robotics as an end in itself.

## Strategy and time budget

| Year | Weekly guide | Objective | Evidence-based exit gate |
|---|---:|---|---|
| Y1 2026–27 | 5 h | Robotics fundamentals, ROS 2, classical manipulation | Independently derive/test FK & IK; simulated pick-and-place; initial low-power robot demo |
| Y2 2027–28 | 5 h | Perception & robot learning | Train/evaluate imitation policy on held-out scenes; compare against classical baseline |
| Y3 2028–29 | 8 h, if feasible | VLA, sim-to-real, industrial orchestration | End-to-end work order → safe cell action → verifiable result |
| Y4 2029–30 | 10 h, if feasible | Robust autonomy, contact-rich tasks, recovery | Controlled extended runs, intervention/failure analysis, recovery and uncertainty handling |
| Y5 2030–31 | 12 h, if feasible | Industrial productization and commercial validation | Repeatable demonstrator; cost/benefit model; real industrial discovery/pilot |

The schedule is **conditional**, not a guarantee. Protect the core businesses. Do not advance only because a date passed.

## Knowledge pillars

1. Robot math: coordinate frames, rotations, SE(3), Jacobians, FK/IK, numerical optimization.
2. Mechanics, dynamics and control: actuator limits, feedback, trajectories, PID, impedance, model-based control.
3. Middleware and integration: Linux, ROS 2, tf2, actions, URDF, ros2_control, MoveIt, diagnostics.
4. Perception: calibration, RGB-D, geometry, 6D poses, grasp perception and uncertainty.
5. Learning: supervised/deep learning, BC, offline RL, imitation, RL, VLA and evaluation.
6. Simulation: Gazebo, MuJoCo/Isaac, system identification, randomization, sim-to-real.
7. Systems: task planning, behavior trees, safety independence, recovery, observability, traceability.
8. Commercial: cycle time, integration costs, maintainability, TCO/ROI, adoption constraints.

See [skills matrix](docs/skills/SKILL_MATRIX.csv) for topic ownership, prerequisites and evidence.

## Decisions / gates

- **End of Y1**: can produce and debug deliberate motion, explain transformations, repeat a basic task.
- **End of Y2**: can collect a dataset, train a small policy, benchmark and diagnose failures.
- **End of Y3**: can separate a business-level job from deterministic robot execution and safety.
- **End of Y4**: can quantify reliability under varied initial conditions.
- **End of Y5**: can defend architecture, costs, risks and deployment decision to an engineering customer.

## Scope guardrails

- No expensive humanoid, industrial arm or GPU purchase in Y1 without a justified experiment.
- Never confuse public demo success with safety certification or robust generalization.
- Avoid committing confidential ERP internals or private business/customer data in this **public** repository.
- Future tools/models are reviewed each quarter, not hardcoded into five-year commitments.
- Important strategic change requires an ADR under `docs/decisions/` and updates to this document.

**Next:** [Y1 plan](docs/roadmap/Y1-2026-2027.md), [Q1 plan](docs/roadmap/Q1-2026-10.md).
