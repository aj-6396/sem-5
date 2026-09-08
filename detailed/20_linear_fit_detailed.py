def linear_fit(x, y):
    n = len(x)
    sx, sy = sum(x), sum(y)
    sxy = sum(a * b for a, b in zip(x, y))
    sx2 = sum(a**2 for a in x)

    print(f"n = {n}, sum_x = {sx:.2f}, sum_y = {sy:.2f}, sum_xy = {sxy:.2f}, sum_x2 = {sx2:.2f}")
    m = (n * sxy - sx * sy) / (n * sx2 - sx**2)
    c = (sy - m * sx) / n
    return m, c

if __name__ == "__main__":
    m, c = linear_fit([1.0, 2.0, 3.0, 4.0, 5.0], [2.2, 2.8, 3.6, 4.5, 5.1])
    print(f"Fitted Line: y = {m:.4f}x + {c:.4f}")
