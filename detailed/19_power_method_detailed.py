def power_method(A, tol=1e-5, max_iter=50):
    n, x, lambda_old = len(A), [1.0] * len(A), 0.0
    print(f"{'Iter':<6}{'Eigenvalue':<14}{'Eigenvector':<20}")
    print("-" * 40)

    for step in range(1, max_iter + 1):
        y = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
        lambda_new = max(y, key=abs)
        x = [v / lambda_new for v in y]
        vec_str = "[" + ", ".join(f"{v:.3f}" for v in x) + "]"
        print(f"{step:<6}{lambda_new:<14.4f}{vec_str:<20}")

        if abs(lambda_new - lambda_old) < tol:
            return lambda_new, x
        lambda_old = lambda_new

    return lambda_new, x

if __name__ == "__main__":
    val, vec = power_method([[4.0, 1.0], [2.0, 3.0]])
    print(f"\nEigenvalue: {val:.4f}, Eigenvector: {[round(v, 4) for v in vec]}")
