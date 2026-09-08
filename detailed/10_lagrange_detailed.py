import math

def lagrange(x_vals, y_vals, target_x):
    n = len(x_vals)
    print(f"{'i':<6}{'Basis L_i(x)':<16}{'y_i':<10}{'Term':<12}")
    print("-" * 44)

    total = 0.0
    for i in range(n):
        L_i = math.prod((target_x - x_vals[j]) / (x_vals[i] - x_vals[j]) for j in range(n) if i != j)
        term = y_vals[i] * L_i
        total += term
        print(f"{i:<6}{L_i:<16.5f}{y_vals[i]:<10.2f}{term:<12.5f}")

    return total

if __name__ == "__main__":
    ans = lagrange([5.0, 6.0, 9.0, 11.0], [12.0, 13.0, 14.0, 16.0], 10.0)
    print(f"\nInterpolated value: {ans:.5f}")
