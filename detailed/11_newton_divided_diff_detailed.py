def newton_divided_diff(x, y, target_x):
    n = len(x)
    table = [[0.0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    print("Divided Difference Table:")
    for i in range(n):
        print(f"{x[i]:<6.1f}" + "".join(f"{table[i][j]:<12.4f}" for j in range(n - i)))

    res, prod_term = table[0][0], 1.0
    for j in range(1, n):
        prod_term *= (target_x - x[j - 1])
        res += table[0][j] * prod_term
    return res

if __name__ == "__main__":
    ans = newton_divided_diff([4.0, 5.0, 7.0, 10.0, 11.0], [48.0, 100.0, 294.0, 900.0, 1210.0], 6.0)
    print(f"\nInterpolated Value: {ans:.5f}")
