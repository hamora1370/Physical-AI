# Q1 scope triage and SCARA FK root regression preparation — 2026-11-28

## Why this change was made

Learner accepted the audit findings: existing iterative Jacobian IK was an educational one-target script and did not satisfy Q1's mandatory analytic elbow-branch and unreachable-target checks, root test discovery, or unambiguous non-convergence behavior. There are ~8 weeks until Q1 end (2027-01-24); protect time for mechanics, feedback, trajectory, ROS frame and simulation/kinematic fallback, and review. The learner authorized necessary repository preparation then a return to Issue #3.

## Changes committed

- [ADR-0003](../decisions/ADR-0003-Q1-scope-and-simulation-fallback.md): no Q1 physical hardware gate, J4 simulation optional, retain modelled yaw relation; prefer ROS 2/URDF RRP simulation if environment permits; documented reproducible kinematic fallback allowed but NOT credited as an unperformed simulator gate. ROS distro/RViz/Gazebo environment **has not yet been checked** during this work.
- [Q1 roadmap](../roadmap/Q1-2026-10.md) and [Milestone #5](https://github.com/hamora1370/Physical-AI/issues/5) point at the scope decision and current priority.
- [NEXT_SESSION.md](../../NEXT_SESSION.md) consolidated to **one active action**, complete analytic `ik_2r`; prior 20,500-character resume content preserved in [archive](2026-11-28-next-session-history.md) before updating the active file.
- [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3) rewritten with accurate verified baseline and explicit remaining acceptance criteria: 2 branches, radial boundaries, unreachable/invalid targets, joint limits assumptions, test discovery, and clear numerical solver status.
- [Root regression bridge](../../tests/test_scara_fk_practice.py) mirrors the learner's original four FK tests; the originals remain in [exercises/](../../exercises/01_robot_math/test_scara_fk_practice.py) as submitted evidence. [Exercise README](../../exercises/01_robot_math/README.md) states which is used by root test discovery.

## Local test execution and its limits

A temporary local directory was assembled using the **user-uploaded** `scara_fk_practice.py` and an exact copy of the new `tests/test_scara_fk_practice.py`. Ran `python3 -m unittest discover -s tests -v` in that isolated directory; **4/4 PASS**, 0 errors. This checks the new test file and original learner function together, **not the entire remote GitHub repository**. The repository's full root suite (including the pre-existing generic FK tests and any unrelated tests) has NOT been run in the learner's WSL or in a fresh checkout here; keep this unverified until actual commands from their environment are supplied.

No implementation of analytic `ik_2r` was inserted: learner should implement it independently as the next focused teaching task. No physical control, ROS runtime, RViz/Gazebo, simulation execution, or hardware test was performed.
