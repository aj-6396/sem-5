# Simpson's 1/3 Rule (Ultra-Short)
def simpson_1_3(f, a, b, n=100):
    h = (b - a) / n
    return (h / 3) * (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(f(a + i * h) for i in range(2, n, 2)))

if __name__ == "__main__":
    print("Integral:", simpson_1_3(lambda x: x**2, 0, 1))
