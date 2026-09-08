import math

def newton_forward(x, y, target_x):
    n = len(x)
    h, u = x[1] - x[0], (target_x - x[0]) / (x[1] - x[0])
    diff = [[0.0] * n for _ in range(n)]
    for i in range(n):
        diff[0][i] = y[i]

    for order in range(1, n):
        for i in range(n - order):
            diff[order][i] = diff[order - 1][i + 1] - diff[order - 1][i]

    print("Forward Difference Table:")
    for i in range(n):
        print(f"{x[i]:<6.1f}" + "".join(f"{diff[j][i]:<12.4f}" for j in range(n - i)))

    res, u_term = diff[0][0], 1.0
    for order in range(1, n):
        u_term *= (u - (order - 1))
        res += (u_term * diff[order][0]) / math.factorial(order)
    return res

if __name__ == "__main__":
    ans = newton_forward([10.0, 20.0, 30.0, 40.0, 50.0], [0.1736, 0.3420, 0.5000, 0.6428, 0.7660], 15.0)
    print(f"\nInterpolated Value: {ans:.5f}")
