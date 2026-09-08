def bisection(f, a, b, tol=1e-5, max_iter=50):
    if f(a) * f(b) >= 0:
        return print("Error: f(a) and f(b) must have opposite signs.")

    print(f"{'Iter':<6}{'a':<12}{'b':<12}{'c (Mid)':<14}{'f(c)':<12}")
    print("-" * 56)

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        print(f"{i:<6}{a:<12.5f}{b:<12.5f}{c:<14.5f}{fc:<12.5f}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c
        a, b = (a, c) if f(a) * fc < 0 else (c, b)

    return (a + b) / 2

if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    root = bisection(f, 1.0, 2.0)
    print(f"\nRoot: {root:.5f}")
