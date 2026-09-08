def gauss_jordan(A, b):
    n = len(b)
    for i in range(n):
        p = A[i][i]
        A[i] = [v / p for v in A[i]]
        b[i] /= p
        for k in range(n):
            if k != i:
                factor = A[k][i]
                A[k] = [A[k][j] - factor * A[i][j] for j in range(n)]
                b[k] -= factor * b[i]
    return b

if __name__ == "__main__":
    A = [[2.0, 3.0, 1.0], [1.0, 2.0, 3.0], [3.0, 1.0, 2.0]]
    b = [9.0, 6.0, 8.0]
    ans = gauss_jordan(A, b)
    for i, val in enumerate(ans):
        print(f"x{i+1} = {val:.4f}")
