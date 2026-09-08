# Gauss Elimination (Ultra-Short)
def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n): A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    return x

if __name__ == "__main__":
    print("Solution:", gauss_elimination([[2.0, 1.0], [1.0, 3.0]], [5.0, 5.0]))
