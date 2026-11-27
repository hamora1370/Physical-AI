import math

from scara_fk_practice import fk_scara_2r

alpha = 0.5
tolerance = 0.0001  # 0.1 mm
max_iterations = 100

def jacobian_2r(q1, q2, l1=0.13, l2=0.11):

    j11 = -l1*math.sin(q1)-l2*math.sin(q1+q2)
    j12 = -l2*math.sin(q1+q2)
    j21 = l1*math.cos(q1)+l2*math.cos(q1+q2)
    j22 = l2*math.cos(q1+q2)

    return [
        [j11, j12],
        [j21, j22]
    ]


q1 = math.radians(0)
q2 = math.radians(90)



for i in range(max_iterations):

    # 1. Calculate current position using FK
    x_current, y_current = fk_scara_2r(q1, q2)

    # Target position
    x_target = 0.12
    y_target = 0.14

    # 2. Calculate ex, ey and error magnitude
    ex = x_target - x_current
    ey = y_target - y_current
    error = math.hypot(ex, ey)

    # 3. Stop if error < tolerance
    if error < tolerance:
        print(f"Converged after {i} iterations")
        break

    # 4. Recalculate Jacobian
    J = jacobian_2r(q1, q2)
    a, b = J[0]
    c, d = J[1]

    # 5. Calculate determinant and check singularity
    det = a*d-b*c

    if abs(det) < 1e-10:
        print("Jacobian is singular or nearly singular")
        break

    # 6. Calculate dq1 and dq2
    dq1 = (d*ex-b*ey)/det
    dq2 = (-c*ex+a*ey)/det

    # Apply joint corrections

    q1 = q1 + alpha * dq1
    q2 = q2 + alpha * dq2

    # Calculate the new end-effector position
    x_new, y_new = fk_scara_2r(q1, q2)

    # Calculate remaining position error
    error_x = x_target - x_new
    error_y = y_target - y_new

    error = math.hypot(error_x, error_y)
    if error < tolerance:
        print(f"Converged after {i} iterations")
        break

print(f"New position: ({x_new:.6f}, {y_new:.6f}) m")
print(f"Remaining error: {error * 1000:.4f} mm")
