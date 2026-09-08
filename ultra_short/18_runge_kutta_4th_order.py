# Runge-Kutta 4th Order (RK4) (Ultra-Short)
def rk4(f, x, y, xn, h=0.1):
    while x < xn - 1e-9:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y

if __name__ == "__main__":
    print("y(0.2):", rk4(lambda x, y: x + y, 0, 1, 0.2))
