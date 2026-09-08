# Gauss-Jacobi Method (Ultra-Short)
def jacobi(A, b, steps=25):
    n, x = len(b), [0.0] * len(b)
    for _ in range(steps):
        x = [(b[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)) / A[i][i] for i in range(n)]
    return x

if __name__ == "__main__":
    print("Solution:", jacobi([[4, 1], [1, 3]], [5, 4]))
