# Gauss-Jordan Method (Ultra-Short)
def gauss_jordan(A, b):
    n = len(b)
    for i in range(n):
        p = A[i][i]
        A[i] = [val / p for val in A[i]]
        b[i] /= p
        for k in range(n):
            if k != i:
                f = A[k][i]
                A[k] = [A[k][j] - f * A[i][j] for j in range(n)]
                b[k] -= f * b[i]
    return b

if __name__ == "__main__":
    print("Solution:", gauss_jordan([[2.0, 1.0], [1.0, 3.0]], [5.0, 5.0]))
