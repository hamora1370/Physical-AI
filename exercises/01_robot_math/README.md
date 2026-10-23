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

## Expected next extension

- Draw the 2D manipulator with each joint's frame.
- Derive the equations on paper.
- Add tests for nontrivial angles and unreachable targets once IK is implemented.
- Cite your test commit SHA in the skill matrix before claiming mastery.
