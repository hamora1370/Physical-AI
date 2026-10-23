"""Forward kinematics of a simple planar 2-revolute-link arm (meters, radians).

Educational example, not a physical robot command path.
"""
from math import cos, sin, pi


def fk_2r(length_1: float, length_2: float, q1: float, q2: float) -> tuple[float, float]:
    """Return planar end-effector (x, y) using cumulative joint angles.

    Raises ValueError for nonpositive link lengths.
    """
    if length_1 <= 0 or length_2 <= 0:
        raise ValueError("Link lengths must be positive")
    x = length_1 * cos(q1) + length_2 * cos(q1 + q2)
    y = length_1 * sin(q1) + length_2 * sin(q1 + q2)
    return x, y


if __name__ == "__main__":
    x, y = fk_2r(0.3, 0.2, pi / 4, -pi / 2)
    print(f"2R end effector: x={x:.4f} m, y={y:.4f} m")
