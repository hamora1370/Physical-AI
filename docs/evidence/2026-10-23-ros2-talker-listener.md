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

## Not yet independently verified

- `echo "$ROS_DISTRO"` returning `lyrical` (commands source Lyrical explicitly, but no echo was posted).
- Installed metapackages `ros-lyrical-desktop` and `ros-dev-tools` via `dpkg-query`.
- Explanations/skills for ROS 2 Services and Actions, or own publisher/subscriber implementations.
- Repeatability after a fresh WSL session, WSLg/RViz/Gazebo performance, robot device control.

## Next learning check

1. Confirm distro and installed metapackages if needed.
2. With talker running, inspect `ros2 node list` and `ros2 topic list -t`; use `ros2 topic echo /chatter --once`.
3. Independently explain publisher/subscriber/topic and message type, then learn Services and Actions.
4. Keep this evidence linked from Issue #2; assess skill matrix only after independent exercise.
