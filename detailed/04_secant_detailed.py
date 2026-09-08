def secant(f, x0, x1, tol=1e-5, max_iter=50):
    print(f"{'Iter':<6}{'x0':<12}{'x1':<12}{'f(x1)':<14}{'x2':<12}")
    print("-" * 56)

    for i in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)
        if f1 - f0 == 0:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        print(f"{i:<6}{x0:<12.5f}{x1:<12.5f}{f1:<14.5f}{x2:<12.5f}")

        if abs(x2 - x1) < tol or abs(f(x2)) < tol:
            return x2
        x0, x1 = x1, x2

    return x1

if __name__ == "__main__":
    root = secant(lambda x: x**2 - 4, 1.0, 3.0)
    print(f"\nRoot: {root:.5f}")
