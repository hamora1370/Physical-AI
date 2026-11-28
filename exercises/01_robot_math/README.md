# Exercise 01: planar 2R forward kinematics

**Purpose:** create the first version-controlled, repeatable robotics math exercise before using ROS 2.

The planar example is intentionally simpler than a 6-DOF arm. It validates coordinate-frame reasoning and test discipline.

## Run

From repository root, with Python 3.11 or newer:

```sh
python -m unittest discover -s tests -v
python exercises/01_robot_math/fk_2r.py
```

There are no third-party Python dependencies for this starter exercise.

## Learner SCARA-01 practice (Q1)

The independently authored [`scara_fk_practice.py`](scara_fk_practice.py) is retained separately from the earlier generic starter `fk_2r.py`. Its first four unit checks are kept in [`test_scara_fk_practice.py`](test_scara_fk_practice.py) as the learner's original practice artifact, and are **mirrored** in the root suite at [`../../tests/test_scara_fk_practice.py`](../../tests/test_scara_fk_practice.py) for standard discovery.

From **repository root**, run:

```bash
python3 -m unittest discover -s tests -v
```

The analytic `ik_2r(x, y, elbow, l1, l2)` with both elbow branches and explicit geometric out-of-reach handling is the active next exercise; refer to [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3). Add its real tests in `tests/` once implemented. Keep the existing numeric Jacobian experiment as a learning reference, not an all-target solver.

## Expected next extension

- Draw the 2D manipulator with each joint's frame.
- Derive the equations on paper.
- Add tests for nontrivial angles and unreachable targets once IK is implemented.
- Cite your test commit SHA in the skill matrix before claiming mastery.
