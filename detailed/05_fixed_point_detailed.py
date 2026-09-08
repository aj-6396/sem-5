import math

def fixed_point(g, x0, tol=1e-5, max_iter=50):
    print(f"{'Iter':<6}{'x0':<14}{'x1 = g(x0)':<14}")
    print("-" * 34)

    for i in range(1, max_iter + 1):
        x1 = g(x0)
        print(f"{i:<6}{x0:<14.5f}{x1:<14.5f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

    return x0

if __name__ == "__main__":
    root = fixed_point(lambda x: math.cos(x), 0.5)
    print(f"\nFixed Point: {root:.5f}")
