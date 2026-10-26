# Next session — resume here

**Updated:** 2026-10-26  
**Track:** Y1 / Q1 / official Week 1 (2026-10-26 → 2026-11-01)  
**Status:** ROS 2 initial communication/CLI introspection are evidenced; learner reports completing the Executor/Concurrency/Process exercises. Their logs and learning mastery have **not yet been independently reviewed**.

## Last independently evidenced technical state

- WSL2 distro `PhysicalAI`: Ubuntu 26.04.1 LTS on D:; existing `Ubuntu-24.04` ERP distro preserved and default.
- ROS 2 Lyrical example communication PASS: C++ Talker publishes to `/chatter`; Python Listener receives matching numbered messages.
- CLI evidence: `ros2 node list`, `ros2 topic list -t`, `ros2 topic echo /chatter --once`, `ros2 topic info /chatter -v` and `ros2 interface show example_interfaces/msg/String`.
- Actual demo message type: **`example_interfaces/msg/String`**, not `std_msgs/msg/String`.
- Observed publisher QoS: `RELIABLE`, `KEEP_LAST(7)`, `VOLATILE`; subscription count was 0 **at the time of the inspection**, not a failure.
- [Saved evidence](docs/evidence/2026-10-23-ros2-talker-listener.md).

## New study progress — reported 2026-10-26, assessment pending

- Conceptual teaching delivered: Node/Process/Thread/Executor and Callback Groups; Concurrency vs Parallelism; Python client library vs C++, JavaScript and Rust; Topic names and introductory tf2 timestamp/latency.
- The learner said **all proposed practical exercises were done**, including `executor_lab.py` modes `single`, `multi-default`, `multi-groups`, `--work cpu` vs `--work sleep`, and `vision-only`/`control-only` in different processes.
- These are **self-reported completed exercises**. No measured intervals, saved terminal output or independent conceptual explanation has been provided and evaluated; do not mark a skill mastery level or timing benchmark as validated.

## Next single teaching action

**Debrief completed Executor labs, then introduce Scheduling/Jitter/Deadline.** Ask the learner to describe the most important observed difference between `multi-default` and `multi-groups` (or provide a few representative `CONTROL interval` lines, if available). Explain the cause in terms of Callback Group and Executor behavior. Separately distinguish event-loop concurrency from CPU parallelism. Do **not** request a rerun merely to tick a box.

Once the conceptual distinction is clear, run one *new* measured ROS 2 Timer experiment under an idle and blocked callback scenario. Capture mean/max/p95 interval where possible, then return to tf2 timestamp correctness and transform freshness.

## This week's plan and completion gates

See the live [official Week 1 adaptive schedule](docs/roadmap/Q1-2026-10.md#week-1-adaptive-study-plan-2026-10-26-to-2026-11-01-updated-2026-10-26) (five focused hours, no pressure to advance before understanding).

In order: results interpretation → Scheduling/Jitter/Deadline → measured Timer intervals → Topic discovery/QoS → tf2 timing diagnostic and short reflection. Defer deeper Services/Actions, independent authored ROS node and simulation until the present concepts are assessed.

## Outstanding verification (do not mislabel as PASS)

- `echo "$ROS_DISTRO"` and metapackage status of `ros-lyrical-desktop` / `ros-dev-tools`.
- Repo tests `python -m unittest discover -s tests -v`, an independently written ROS 2 Node, and Services/Actions work (tracked in [Issue #2](https://github.com/hamora1370/Physical-AI/issues/2)).
- Safe return from robotics to ERP workflow ([Issue #1](https://github.com/hamora1370/Physical-AI/issues/1)).
- RViz/Gazebo, physical robots, and stronger skill levels are not confirmed.

## Working rules

- Teach **concept → industrial use → implementation details → targeted experiment → comprehension assessment**.
- Maintain the roughly **5 hours/week** study budget and the two-active-work-item limit. Run ERP/ToliHub and robotics heavy workloads sequentially, not simultaneously.
- GitHub is a record of meaningful progress, not an interrupt for every command. Keep separate statuses for *taught*, *learner-reported run*, *observed/reproducible* and *demonstrated understanding*.
- Public repository: do not add private enterprise data, credentials, personal IPs or restricted recordings.
