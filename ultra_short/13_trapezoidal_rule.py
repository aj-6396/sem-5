# Trapezoidal Rule (Ultra-Short)
def trapezoidal(f, a, b, n=100):
    h = (b - a) / n
    return h * (0.5 * f(a) + sum(f(a + i * h) for i in range(1, n)) + 0.5 * f(b))

if __name__ == "__main__":
    print("Integral:", trapezoidal(lambda x: x**2, 0, 1))
