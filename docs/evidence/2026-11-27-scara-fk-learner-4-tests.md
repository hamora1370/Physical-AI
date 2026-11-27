# SCARA-01 planar forward kinematics — learner coding checkpoint (2026-11-27)

**Related issue:** [#3 — Independently derive and test planar 2R FK](https://github.com/hamora1370/Physical-AI/issues/3)  
**Skill:** M03, with M01 background.  
**Status:** Learner-coded 2R forward-kinematics function and **four functional unit tests pass**. This is a verified *checkpoint*, not completion of the full Issue #3 workspace/IK/singularity scope.

## Source and assumptions

Learner submitted `scara_fk_practice.py` and `test_scara_fk_practice.py` in chat. Saved snapshots:
- [Source](../../exercises/01_robot_math/scara_fk_practice.py)
- [Tests](../../exercises/01_robot_math/test_scara_fk_practice.py)

`fk_scara_2r(q1,q2,l1=0.13,l2=0.11)` works in **meters and radians**. q1 is relative to fixed base X; q2 is relative to link 1, so absolute orientation of link 2 is q1+q2. The function computes:
```
x = l1*cos(q1) + l2*cos(q1+q2)
y = l1*sin(q1) + l2*sin(q1+q2)
```
This is an ideal planar **2R model**, not a physical robot controller, and ignores joint limits/collisions.

## Tests and independently checked results

Learner reported from Linux terminal:
```
python3 -m unittest -v test_scara_fk_practice.py
test_folded ... ok
test_fully_extended ... ok
test_nontrivial_angles ... ok
test_vertical ... ok
Ran 4 tests in 0.000s
```
Assistant independently ran a copy of the two uploaded files using Python 3 and the same unittest command in a temporary directory. Result: **4 tests, OK**.

| q1 | q2 | Expected (x, y), m | Result |
| --- | --- | --- | --- |
| 0° | 0° | (0.2400000, 0) | PASS |
| 90° | 0° | (0, 0.2400000) | PASS |
| 0° | 180° | (0.0200000, 0) | PASS |
| 30° | 60° | (0.1125833, 0.1750000) | PASS |

Expected numbers were obtained from hand/trigonometric reasoning, especially the cumulative angle (30°+60°=90°). Four tests cover extended, vertical, folded and one mixed-angle case; no general correctness proof.

## Additional understanding check

Learner asked about `self` in Python classes and `unittest.TestCase`. In the two-object Motor illustration, learner answered `motor1.speed=150`, `motor2.speed=250`. Correction provided: **150 and 200**, since `motor1.accelerate(50)` mutates only `motor1`. Do not claim mastery of Python object/instance semantics without a follow-up check.

## What has NOT been verified / remains open

- This check was run from the learner's uploaded Python files, not from a clean repository checkout.
- Tests are currently stored alongside exercise code; they are invoked by changing to `exercises/01_robot_math/` and running `python3 -m unittest -v test_scara_fk_practice.py`. The repository's root `python -m unittest discover -s tests -v` was **not** run in this checkpoint.
- No physical robot or ROS 2 controller involved.
- Workspace annulus `|l1-l2| <= r <= l1+l2`, joint-limited reachable region, inverse kinematics elbow-up/down, singularities, and independently tested *unfamiliar* cases remain to be studied.
- Keep Issue #3 open; do not promote mastery level solely from these tests.

## Next teaching action

Explain the geometry of the ideal planar 2R workspace and show why the end effector radial distance is bounded by **20 mm to 240 mm** for L1=130 mm and L2=110 mm. Check the previously chosen target `Place=(120,140) mm` by computing its distance to origin; identify why radial reachability does not guarantee real physical reach. Then introduce IK by deriving `cos(q2)` from the law of cosines, one step at a time, without giving the complete implementation up front.
