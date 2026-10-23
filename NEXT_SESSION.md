# Next session — resume here

**Updated:** 2026-10-23  
**Track:** Y1 / Q1 / Week 1  
**Status:** Ubuntu verified; ROS 2 sample Publish/Subscribe **PASS** and CLI introspection **PASS**. Other ROS concepts and GUI tools pending.

## Last verified working state

- `PhysicalAI` WSL2 distro on D: is Ubuntu 26.04.1 LTS (`resolute`); original ERP `Ubuntu-24.04` remains installed and default.
- ROS 2 apt repository `ros2-apt-source 1.3.0~resolute` installed and package indexes loaded.
- `ros2 pkg list | head` showed multiple packages including `action_msgs`.
- **Smoke test PASS:** `demo_nodes_cpp talker` published numbered messages and `demo_nodes_py listener` received 24–34 in sequence. [Raw log excerpts / evidence](docs/evidence/2026-10-23-ros2-talker-listener.md).
- Confirmed via the user transcript: `source /opt/ros/lyrical/setup.bash` and both ROS 2 programs could execute.
- **CLI introspection PASS:** `/talker` visible, `/chatter [example_interfaces/msg/String]` shown by `ros2 topic list -t`, `ros2 topic echo /chatter --once` returned `data: 'Hello World: 23'`.
- **Correction:** message type is `example_interfaces/msg/String` in the observed Lyrical example, not `std_msgs/msg/String`.
- **Not yet independently verified:** `echo "$ROS_DISTRO"`, `dpkg-query` status of `ros-lyrical-desktop`/`ros-dev-tools`, Services/Actions exercise, independent node implementation, RViz/Gazebo.
- A full ERP-mode return test remains to be explicitly documented in [#1](https://github.com/hamora1370/Physical-AI/issues/1).

## Next single action

Inspect the observed Topic's contract while the example talker is running:

```bash
source /opt/ros/lyrical/setup.bash
ros2 topic info /chatter -v
ros2 interface show example_interfaces/msg/String
```

Verify `echo "$ROS_DISTRO"` (expected `lyrical`) and the metapackage installation with:

```bash
dpkg-query -W -f='${Package} ${Status} ${Version}\n' ros-lyrical-desktop ros-dev-tools
```

Next, explain Nodes, Topics, message types and QoS at a beginner level, then introduce Service/Action examples in [Issue #2](https://github.com/hamora1370/Physical-AI/issues/2). Work in the Linux home directory `~/` for actual project files.

## Next milestones

1. Confirm ROS metapackages and introspection output (Issue #2).
2. Basic Service and Action concepts, independent Node implementation.
3. Confirm safe return to ERP-mode after stopping robotics (Issue #1).
4. Check WSLg/RViz before adding Gazebo Jetty.

## Working rules

ERP/ToliHub and PhysicalAI are separate heavy-work modes; do not interrupt active database writes or agents. Never report experiments, CI, GUIs or skills as verified without evidence.
