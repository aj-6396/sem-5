def regula_falsi(f, a, b, tol=1e-5, max_iter=50):
    if f(a) * f(b) >= 0:
        return print("Error: f(a) and f(b) must have opposite signs.")

    print(f"{'Iter':<6}{'a':<12}{'b':<12}{'c':<14}{'f(c)':<12}")
    print("-" * 56)

    for i in range(1, max_iter + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)
        print(f"{i:<6}{a:<12.5f}{b:<12.5f}{c:<14.5f}{fc:<12.5f}")

        if abs(fc) < tol:
            return c
        a, b = (a, c) if f(a) * fc < 0 else (c, b)

    return c

if __name__ == "__main__":
    f = lambda x: x**3 - 2 * x - 5
    root = regula_falsi(f, 2.0, 3.0)
    print(f"\nRoot: {root:.5f}")
