# Next session — SCARA-01

**Updated:** 2026-11-28  
**Quarter:** Y1 / Q1 (ends 2027-01-24)  
**Active issue:** [#3 — independent planar 2R FK/IK validation](https://github.com/hamora1370/Physical-AI/issues/3)

## Next ONE action

**Complete analytic 2R inverse kinematics as an independently authored, reusable function** `ik_2r(x, y, elbow, l1=0.13, l2=0.11)`: choose both explicitly named branches; return `None` for geometrically unreachable targets. Start with law of cosines for `q2` and a sign-aware expression for `q1`; do **one step at a time**, not a pre-written complete solution. Then test both branches via `FK(IK(target))`, annular boundaries 20/240 mm, unreachable target (0.20,0.20)m, and report joint-limit assumptions. Add tests under `tests/` and run `python3 -m unittest discover -s tests -v`. Fix/refactor iterative Jacobian solver's success/failure reporting only as needed for #3, preserving the original learner-authored evidence version.

## Verified baseline and constraints

- Learner's 2R [FK](exercises/01_robot_math/scara_fk_practice.py) and [four local tests](exercises/01_robot_math/test_scara_fk_practice.py) passed (4/4); now mirrored in [root-discoverable regression tests](tests/test_scara_fk_practice.py). Root full suite has **not yet** been executed in the user's environment after the change.
- Learner's [Jacobian IK experiment](exercises/01_robot_math/scara_jacobian_ik.py) converged for one target (120,140) mm with 0.0611 mm numerical residual; 9 angle updates despite reporting 8. It is **not** yet a reusable general IK interface. [Evidence](docs/evidence/2026-11-28-scara-jacobian-ik-checkpoint.md).
- Q1 scope: [ADR-0003](docs/decisions/ADR-0003-Q1-scope-and-simulation-fallback.md) — hardware build not required, J4 dynamic simulation optional, ROS 2/URDF still preferred, reproducible kinematic fallback only with documented blockers. After #3, run time-boxed environment check (ROS_DISTRO, RViz, Gazebo/gz). No present simulator state is verified.
- Mechanical work (bearing layout, motor placement, stiffness, feedback) continues in [#6](https://github.com/hamora1370/Physical-AI/issues/6) after this focused #3 gate.
- [Q1 roadmap](docs/roadmap/Q1-2026-10.md) · [Skill matrix](docs/skills/SKILL_MATRIX.csv) · [Archived detailed history](docs/evidence/2026-11-28-next-session-history.md).
