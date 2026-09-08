# Newton's Forward Difference (Ultra-Short)
from math import factorial

def newton_forward(x, y, target):
    n, h, u = len(x), x[1] - x[0], (target - x[0]) / (x[1] - x[0])
    d = [y[:]]
    for i in range(1, n):
        d.append([d[i - 1][j + 1] - d[i - 1][j] for j in range(n - i)])
    u_term, res = 1.0, d[0][0]
    for i in range(1, n):
        u_term *= (u - (i - 1))
        res += (u_term * d[i][0]) / factorial(i)
    return res

if __name__ == "__main__":
    print("Value at 0.5:", newton_forward([0, 1, 2], [1, 2, 5], 0.5))
