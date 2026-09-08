# Power Method (Ultra-Short)
def power_method(A, steps=25):
    n, x = len(A), [1.0] * len(A)
    for _ in range(steps):
        Ax = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
        val = max(Ax, key=abs)
        x = [v / val for v in Ax]
    return val, x

if __name__ == "__main__":
    val, vec = power_method([[4.0, 1.0], [2.0, 3.0]])
    print(f"Dominant Eigenvalue: {val:.4f}, Eigenvector: {[round(v, 4) for v in vec]}")
