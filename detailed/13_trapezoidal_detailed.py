def trapezoidal(f, a, b, n=6):
    h = (b - a) / n
    x_pts = [a + i * h for i in range(n + 1)]
    y_pts = [f(x) for x in x_pts]

    print(f"{'i':<6}{'x_i':<12}{'f(x_i)':<14}")
    print("-" * 32)
    for i, (xi, yi) in enumerate(zip(x_pts, y_pts)):
        print(f"{i:<6}{xi:<12.4f}{yi:<14.5f}")

    integral = (h / 2.0) * (y_pts[0] + 2 * sum(y_pts[1:n]) + y_pts[n])
    return integral

if __name__ == "__main__":
    ans = trapezoidal(lambda x: 1 / (1 + x**2), 0.0, 1.0, n=6)
    print(f"\nIntegral: {ans:.5f}")
