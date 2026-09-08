# Newton's Divided Difference (Ultra-Short)
def newton_divided_diff(x, y, target):
    n = len(x)
    t = [row[:] for row in [y]] + [[0.0] * n for _ in range(n - 1)]
    for j in range(1, n):
        for i in range(n - j):
            t[j][i] = (t[j - 1][i + 1] - t[j - 1][i]) / (x[i + j] - x[i])
    prod_term, res = 1.0, t[0][0]
    for i in range(1, n):
        prod_term *= (target - x[i - 1])
        res += t[i][0] * prod_term
    return res

if __name__ == "__main__":
    print("Value at 2.5:", newton_divided_diff([1, 2, 3], [1, 8, 27], 2.5))
