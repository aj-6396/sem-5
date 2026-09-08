def simpson_1_3(f, a, b, n=6):
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x_pts = [a + i * h for i in range(n + 1)]
    y_pts = [f(x) for x in x_pts]

    print(f"{'i':<6}{'x_i':<12}{'f(x_i)':<14}{'Mult':<6}")
    print("-" * 38)
    for i, (xi, yi) in enumerate(zip(x_pts, y_pts)):
        mult = 1 if i in (0, n) else (4 if i % 2 != 0 else 2)
        print(f"{i:<6}{xi:<12.4f}{yi:<14.5f}{mult:<6}")

    integral = (h / 3.0) * (y_pts[0] + y_pts[n] + 4 * sum(y_pts[1:n:2]) + 2 * sum(y_pts[2:n:2]))
    return integral

if __name__ == "__main__":
    ans = simpson_1_3(lambda x: 1 / (1 + x**2), 0.0, 1.0, n=6)
    print(f"\nIntegral: {ans:.5f}")
