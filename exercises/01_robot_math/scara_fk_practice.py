import math


def fk_scara_2r(q1, q2, l1=0.13, l2=0.11):
    """
    q1, q2: joint angles in radians
    l1, l2: link lengths in meters

    Returns:
        x, y in meters
    """

    # Calculate x and y
    x = l1 * math.cos(q1) + l2 * math.cos(q1 + q2)
    y = l1 * math.sin(q1) + l2 * math.sin(q1 + q2)

    return x, y


if __name__ == "__main__":
   # First test
   tetha1 = 0
   tetha2 = 180

   q1 = math.radians(tetha1)
   q2 = math.radians(tetha2)

   x, y = fk_scara_2r(q1, q2)

   print(f"tetha1 = {tetha1: .4f} deg")
   print(f"x = {x:.4f} m")
   print(f"tetha2 = {tetha2: .4f} deg")
   print(f"y = {y:.4f} m")
