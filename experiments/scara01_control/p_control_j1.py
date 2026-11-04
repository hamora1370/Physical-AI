# SCARA-01 - J1 Position Control Simulation
# Model: P position controller with ideal velocity tracking

import matplotlib.pyplot as plt

target = 60
cases = [
    ("Monotonic", 0.1, 72),
    ("Convergent Oscillation", 0.8, 9),
    ("Divergent Oscillation", 1.2, 6),
]


def simulate_p(theta_initial, theta_target, kp, dt, steps):

    theta = theta_initial

    times = [0.0]
    positions = [theta]

    for k in range(steps):

        # TODO 1: Calculate position error

        error_before = theta_target - theta

        # TODO 2: Calculate commanded velocity

        omega = kp * error_before

        # TODO 3: Update joint position

        theta = theta + omega * dt

        times.append((k + 1) * dt)
        positions.append(theta)

    return times, positions


plt.figure(figsize=(10, 6))

for label, dt, steps in cases:

    times, positions = simulate_p(
        theta_initial=50,
        theta_target=target,
        kp=2,
        dt=dt,
        steps=steps
    )

    plt.plot(times, positions, marker="o", label=label)

plt.axhline(
    y=target,
    linestyle="--",
    label="Target Position"
)

plt.xlabel("Time (s)")
plt.ylabel("Joint Position (deg)")
plt.title("SCARA-01 | J1 Position Control")

plt.grid(True)
plt.legend()

plt.savefig("j1_position_cases.png", dpi=150)
