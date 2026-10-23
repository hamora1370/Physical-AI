# ROS 2 Lyrical — cross-language talker/listener smoke test

- **Date:** 2026-10-23
- **Environment:** `PhysicalAI`, Ubuntu 26.04.1 LTS, WSL2 (as previously verified from user's shell)
- **Source of evidence:** user-provided terminal output pasted in conversation
- **Result:** **PASS** — publisher produced numbered messages and Python subscriber received matching message numbers in order
- **Scope:** ROS 2 command-line examples and inter-node topic communication only; not a claim of independent proficiency or working RViz/Gazebo

## Commands

Terminal A:

```bash
source /opt/ros/lyrical/setup.bash
ros2 run demo_nodes_cpp talker
```

Terminal B:

```bash
source /opt/ros/lyrical/setup.bash
ros2 run demo_nodes_py listener
```

## Representative observed logs

Publisher:

```text
[INFO] [1792746105.972556983] [talker]: Publishing: 'Hello World: 24'
[INFO] [1792746106.972536145] [talker]: Publishing: 'Hello World: 25'
[INFO] [1792746110.972518313] [talker]: Publishing: 'Hello World: 29'
[INFO] [1792746115.972489276] [talker]: Publishing: 'Hello World: 34'
```

Subscriber:

```text
[INFO] [1792746105.990216512] [listener]: I heard: [Hello World: 24]
[INFO] [1792746106.974214393] [listener]: I heard: [Hello World: 25]
[INFO] [1792746110.974206295] [listener]: I heard: [Hello World: 29]
[INFO] [1792746115.974159624] [listener]: I heard: [Hello World: 34]
```

The user shared Talker messages numbered 1–59 (with a truncated line for 60) and Listener messages 24–34. All 11 shown listener message numbers appear in the talker trace in the same order. Message intervals are approximately one second; no loss is apparent in **this limited observed span**. The subscriber started receiving after the publisher had already published initial messages, which is normal for this kind of test.

## CLI introspection — PASS (2026-10-23)

The user then ran the following in a second `PhysicalAI` shell while `/talker` was active:

```bash
source /opt/ros/lyrical/setup.bash
ros2 node list
ros2 topic list -t
ros2 topic echo /chatter --once
```

Actual user-observed output:

```text
/talker
/chatter [example_interfaces/msg/String]
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/rosout [rcl_interfaces/msg/Log]
data: 'Hello World: 23'
---
```

**Result: PASS.** CLI discovers `/talker`, shows `/chatter` with actual message type `example_interfaces/msg/String` and receives one `Hello World` sample. `--once` stops the temporary CLI subscriber after one message; it does not stop the talker. Some prior planning text incorrectly expected `std_msgs/msg/String`; the **actual** observed type is `example_interfaces/msg/String` and the docs should match reality.

## Not yet independently verified

- `echo "$ROS_DISTRO"` returning `lyrical` (commands source Lyrical explicitly, but no echo was posted).
- Installed metapackages `ros-lyrical-desktop` and `ros-dev-tools` via `dpkg-query`.
- Explanations/skills for ROS 2 Services and Actions, or own publisher/subscriber implementations.
- Repeatability after a fresh WSL session, WSLg/RViz/Gazebo performance, robot device control.

## Next learning check

1. Confirm distro and installed metapackages if needed.
2. **Completed:** with talker running, inspected `ros2 node list`, `ros2 topic list -t`, and echoed one `/chatter` message.
3. Independently explain publisher/subscriber/topic and message type, then learn Services and Actions.
4. Keep this evidence linked from Issue #2; assess skill matrix only after independent exercise.

## Topic endpoint QoS / interface inspection — PASS (2026-10-23)

The user ran:

```bash
ros2 topic info /chatter -v
ros2 interface show example_interfaces/msg/String
```

Important exact observed output (identifiers abbreviated; no personal system details):

```text
Type: example_interfaces/msg/String
Publisher count: 1
Node name: talker
Node namespace: /
Topic type: example_interfaces/msg/String
Topic type hash: RIHS01_5509d866a579951f2fc6c19577c32605ba16f308cae7b498341d79536d4eb06b
Endpoint type: PUBLISHER
QoS profile:
  Reliability: RELIABLE
  History (Depth): KEEP_LAST (7)
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite
Subscription count: 0
```

Interface:

```text
# This is an example message of using a primitive datatype, string.
# If you want to test with this that's fine, but if you are deploying
# it into a system you should create a semantically meaningful message type.
# If you want to embed it in another message, use the primitive data type instead.
string data
```

**Result: PASS.** This is the **publisher endpoint's** QoS profile, not a universal fixed policy for every entity on `/chatter`. `KEEP_LAST (7)` constrains history depth, `VOLATILE` does not persist past messages for late-joining subscribers. The subscriber count was 0 **at this moment** after the one-shot `ros2 topic echo --once` had exited (and the earlier listener was no longer running); it is not a failure. In this specific demo the message field is `string data`, and the package comment explicitly advises semantic messages for deployed systems.

### Next experiment

While publisher is running, launch `ros2 run demo_nodes_py listener` in a second terminal, then run `ros2 topic info /chatter -v` in a **third** terminal and verify `Subscription count` changes from 0 to >=1 after discovery. Stop listener with Ctrl+C and verify eventual return to 0. On that observation the student can explain endpoint discovery and QoS independently.

Still missing direct `echo "$ROS_DISTRO"` output and `dpkg-query` verification of installed `ros-lyrical-desktop` and `ros-dev-tools`. RViz/Gazebo have not been tested.
