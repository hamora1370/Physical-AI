# 2026-11-21 — ROS 2 architecture/concurrency review; resume SCARA-01 FK

**Context:** Learner resumed after a gap and explicitly requested a slower, concept-first review. This note records **dialogue-based understanding only**; it is not evidence of independently executed concurrency labs or FK code. Linked learning task: [Issue #3](https://github.com/hamora1370/Physical-AI/issues/3), **M03** (pending implementation). ROS concepts relate to **R01**.

## Reviewed concepts
- ROS 2: Node vs OS process/thread; Publisher, Subscriber, Topic, DDS/RMW, QoS and discovery.
- QoS: learner calculated that a 100 Hz joint publisher generates ~20 updates during a 200 ms blocked callback, and identified that **latest state** is often preferable to replaying older state for live monitoring. Instructor qualified that lost vs buffered vs processed messages differ; KEEP_LAST depth alone does not guarantee an exact loss count, and VOLATILE concerns late subscribers.
- Timestamp/latency: a most-recently received sample can still be stale; message delivery and executing the subscriber callback are separate stages.
- Executors: learner correctly noted that QoS cannot fix a CPU-heavy callback blocking execution. Reviewed SingleThreaded vs MultiThreaded executors, callback groups, and what threads share within a process.
- Async vs thread: learner reasoned that a CPU-bound coroutine with no effective yield blocks an asyncio event loop, while another OS thread can advance independently (with GIL/runtime constraints). Compared with ERP-style async I/O and CPU-bound worker threads/processes.
- Shared state: explained inconsistent multi-joint snapshots, short-duration locks/snapshot copying, MutuallyExclusive callback groups, and deadlock. Learner chose separate callback groups + short lock for two callbacks and correctly explained why a consistent global A→B lock-acquisition order prevents the illustrated circular-wait deadlock. This does not prove deadlock freedom in general.

## Learning evidence and limitations
- Learner's answers were correct on: fresh state preference, callback-vs-transport distinction, CPU-bound event-loop blocking, separate callback groups plus short lock, consistent lock ordering.
- **Guided conceptual answers, not a closed-book or implementation assessment.** No executed ROS timing benchmark, thread-safety test, or independent Python FK implementation was supplied this session. Do **not** raise SKILL_MATRIX mastery levels on this evidence alone.
- Learner requested that review finish now and the session return to the previously planned coding exercise. Avoid further concurrency or ERP detours until needed by SCARA-01.

## Precise next task — Issue #3
1. Independently derive planar two-revolute FK with q2 **relative to link 1**: x=L1 cos(q1)+L2 cos(q1+q2), y=L1 sin(q1)+L2 sin(q1+q2).
2. Work with candidate SCARA links L1=130 mm, L2=110 mm (0.13 m and 0.11 m). Angles supplied in **radians**, output consistent with link-length units; test (0°,90°) -> (130,110) mm and (90°,0°) -> (0,240) mm.
3. **Existing repository starter is already implemented** at `exercises/01_robot_math/fk_2r.py` with signature `fk_2r(length_1, length_2, q1, q2)` and **meters**. `tests/test_fk_2r.py` contains existing tests with different generic lengths. Learner must not receive starter-code execution as proof of independent skill.
4. Have learner create/derive their own implementation or independently modify/add SCARA-specific tests; inspect and execute submitted work, then record actual results. Continue to Workspace/Reachability and IK only after FK understanding/code is checked.

## Teaching style
One concept and one meaningful coding check at a time. Teach geometric meaning, units, frame conventions and why the equation is structured this way *before* asking for code. Do not generate a completed independent solution and label it learner work.
