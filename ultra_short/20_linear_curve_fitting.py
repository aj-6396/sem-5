# Linear Curve Fitting (Ultra-Short)
def linear_fit(x, y):
    n, sx, sy = len(x), sum(x), sum(y)
    sxy, sx2 = sum(a * b for a, b in zip(x, y)), sum(a**2 for a in x)
    m = (n * sxy - sx * sy) / (n * sx2 - sx**2)
    return m, (sy - m * sx) / n

if __name__ == "__main__":
    m, c = linear_fit([1, 2, 3], [2, 4, 5])
    print(f"y = {m:.2f}x + {c:.2f}")
