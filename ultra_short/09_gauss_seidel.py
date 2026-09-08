# Gauss-Seidel Method (Ultra-Short)
def gauss_seidel(A, b, steps=25):
    n, x = len(b), [0.0] * len(b)
    for _ in range(steps):
        for i in range(n):
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)) / A[i][i]
    return x

if __name__ == "__main__":
    print("Solution:", gauss_seidel([[4, 1], [1, 3]], [5, 4]))
