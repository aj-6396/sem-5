def modified_euler(f, x0, y0, x_end, h=0.05):
    x, y, step = x0, y0, 0
    print(f"{'Step':<6}{'x':<10}{'y':<12}{'y_predict':<14}")
    print("-" * 42)

    while x < x_end - 1e-9:
        k1 = f(x, y)
        y_predict = y + h * k1
        print(f"{step:<6}{x:<10.3f}{y:<12.5f}{y_predict:<14.5f}")
        y += (h / 2.0) * (k1 + f(x + h, y_predict))
        x += h
        step += 1

    print(f"{step:<6}{x:<10.3f}{y:<12.5f}")
    return y

if __name__ == "__main__":
    ans = modified_euler(lambda x, y: x + y, 0.0, 1.0, 0.2, h=0.05)
    print(f"\ny(0.2): {ans:.5f}")
