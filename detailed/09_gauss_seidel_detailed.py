def gauss_seidel(A, b, tol=1e-5, max_iter=50):
    n = len(b)
    x = [0.0] * n
    print(f"{'Iter':<6}" + "".join(f"{'x' + str(i+1):<12}" for i in range(n)))
    print("-" * (6 + 12 * n))

    for step in range(1, max_iter + 1):
        x_old = list(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]

        print(f"{step:<6}" + "".join(f"{v:<12.5f}" for v in x))
        if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
            return x
    return x

if __name__ == "__main__":
    A = [[10.0, -1.0, 2.0], [-1.0, 11.0, -1.0], [2.0, -1.0, 10.0]]
    b = [6.0, 25.0, -11.0]
    sol = gauss_seidel(A, b)
    print("\nSolution:", [round(v, 4) for v in sol])
