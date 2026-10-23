# Physical AI — kickoff week checklist

**Period:** Mon 2026-10-19 to Sun 2026-10-25. **Snapshot:** Fri 2026-10-23.  
**Formal Q1 Week 1 starts:** Mon 2026-10-26 (per [Q1 roadmap](../roadmap/Q1-2026-10.md)).  
**Focus:** slow, concept-first education. A passing command is evidence of a working environment, **not evidence of conceptual mastery**. Do not push into Services, Actions, RViz or Gazebo until the ROS basics are understood.

## Completed — verified technical setup

- [x] GitHub repository, 5-year roadmap, quarterly sprint and learning support created
- [x] Ubuntu 26.04.1 LTS WSL2 distribution `PhysicalAI` installed on D: while original Ubuntu-24.04 remained intact
- [x] ROS 2 official apt source for Ubuntu resolute added; ROS 2 CLI and package discovery work (the ROS desktop/dev-tools meta-package identities are still awaiting direct dpkg confirmation)
- [x] C++ `demo_nodes_cpp talker` publishes and Python `demo_nodes_py listener` receives messages, verified numbers 24–34
- [x] Inspected `/talker`, `/chatter [example_interfaces/msg/String]`; received a live message using `ros2 topic echo --once`
- [x] Inspected publisher endpoint QoS `RELIABLE`, `KEEP_LAST (7)`, `VOLATILE`; displayed message interface `string data`
- [x] Recorded [observed evidence](../evidence/2026-10-23-ros2-talker-listener.md)

## Remaining — learning priorities before Sun 2026-10-25

- [ ] **~45 min** — Explain what a ROS 2 Node is; compare monolithic robot software with separate camera/perception/planning/control nodes
- [ ] **~45 min** — Explain Publisher, Subscriber, Topic, and typed message using the **already working** Talker → /chatter → Listener example
- [ ] **~30 min** — Independent pencil-and-paper exercise: divide a camera + robot-arm pick task into 3–4 nodes and propose data flow, then discuss tradeoffs
- [ ] **~10 min, optional** — Capture `echo "$ROS_DISTRO"` and `dpkg-query -W -f='${Package} ${Status} ${Version}\n' ros-lyrical-desktop ros-dev-tools` to finalize package evidence
- [ ] **~15 min, optional** — End-of-week learning recap: three ideas understood, two open questions, one next learning action

**Estimated remaining work:** ~2 h 25 m total (~2 h core + ~25 min optional). User determines pace; no additional commands/tests solely to make the checklist look complete.

## Not required this kickoff week

- Services and Actions; QoS configuration experiments; writing a production ROS node; RViz/Gazebo/MoveIt
- Independent robot-math FK tests (they are starter backlog and will be slotted into the formal plan)
- Full ERP/PhysicalAI shutdown/restart rehearsal can be done during the next natural work-mode transition, without interrupting running ERP jobs

## Handoff to formal Q1 Week 1 (2026-10-26 through 2026-11-01)

Review remaining conceptual gaps; learn first ROS 2 Service/Action **only after** Node/Topic concepts make sense. Then gradually approach the Q1 Week 1 items, including independently running the starter Python unittest suite. [Q1 roadmap](../roadmap/Q1-2026-10.md) is the overarching calendar; this kickoff checklist is an early progress snapshot.

**Reminder:** Do not claim `R01` proficiency from successful tutorial executions. Learning must be explained in the student's own words and applied to an unfamiliar scenario.
