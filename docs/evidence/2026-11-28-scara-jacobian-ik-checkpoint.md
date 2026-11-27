# SCARA-01 2R Jacobian IK checkpoint — 2026-11-28

**Study track:** Y1 / Q1, Weeks 3–4 practical mathematics milestone carried into 2026-11-28. **Related Issue:** [#3](https://github.com/hamora1370/Physical-AI/issues/3). **Skills:** M03, M04, M05, C01 (earlier separate P-simulation evidence).

## Learner-submitted implementation

- [Independently coded planar FK](../../exercises/01_robot_math/scara_fk_practice.py), [four learner tests](../../exercises/01_robot_math/test_scara_fk_practice.py) previously checked with Python unittest (4/4 pass): extended, vertical, folded, nontrivial q1=30°,q2=60°.
- [Learner's iterative Jacobian IK script](../../exercises/01_robot_math/scara_jacobian_ik.py), as uploaded: uses the FK module, analytic 2x2 Jacobian, determinant check, inverse-J step, relaxation alpha=0.5, error tolerance 0.0001 m, max_iterations=100.
- Configuration: L1=0.13m, L2=0.11m, q1=0°, q2=90° initially; desired (x,y)=(0.12,0.14)m. All computations in SI units; ideal kinematics (no actual hardware, joint limits, feedback, collision or actuator dynamics).

## Verification

Learner reported and assistant independently executed a copy of the latest uploaded Python files with Python 3.13.5:

```
Converged after 8 iterations
New position: (0.120013, 0.139940) m
Remaining error: 0.0611 mm
```

Initial Cartesian position error = 31.6228mm. The final residual is lower than the stated 0.1mm tolerance for **one target starting from one initial joint configuration**. Earlier one-step tests checked alpha=0.2 -> 25.2741mm, alpha=0.5 -> 15.7018mm, alpha=1.0 -> 3.5071mm residual; outputs were supplied by learner, consistent with analytic FK.

**Minor diagnostic bug, not a convergence failure:** prints `Converged after 8 iterations`, but since Python's loop index starts at 0, **9 joint update steps** were performed before convergence. Script performs two condition checks per loop and does not safely handle a singularity/max-iteration exit before `x_new` was set. For a later refactor, use explicit updates count, a single stopping condition and a final FK evaluation. Do not silently rewrite learner code in the evidence snapshot.

## Conceptual checks

- Learner correctly differentiated IK **computational iterations** from physical motion time and real motor speed.
- Learner understood reducing controller sampling period Ts while holding Kp constant decreases alpha=Kp*Ts and typically increases the number of update steps in the ideal discrete proportional model.
- Jacobian IK step factor alpha is a numerical solver parameter; in an ideal discrete proportional velocity servo model the same algebraic form arises for Kp*Ts. The user requested to stop drilling this point and advance to the next roadmap block.

## Evidence-based skill assessment

- **M03 FK: L2**, learner-authored and independently executed numerical tests (not a full mastery gate).
- **M04 Jacobian: L1**, independently authored derivative implementation, demonstrated one operating point; singularity/conditioning and unfamiliar checks remain.
- **M05 IK: L1**, implemented convergent Jacobian method for one reachable example; multi-target, elbow branch, joint limits, failure tests remain.
- C01 discrete P explanation and Python simulation documented separately [2026-11-04](2026-11-04-scara-discrete-p-simulation.md); do not claim physical controller.

Issue #3 remains OPEN. This evidence does not satisfy full Q1 independent IK gate; preserve work for later assessment rather than forcing additional repetitive tests now.

## Roadmap handoff

Move to **Weeks 5–6 mechanical/actuator engineering** per [Q1 plan](../roadmap/Q1-2026-10.md) after learner's explicit request. Start with differentiating gravity-induced **bending moment in horizontal arm links/joints** from motor torque about **vertical J1/J2 axes**, then develop initial parametric load/inertia/torque estimates, servo/encoder and structural design tradeoffs. The compact printed SCARA and L1/L2 dimensions remain conceptual; no purchased hardware or physical motion.
