# Simpson's 3/8 Rule (Ultra-Short)
def simpson_3_8(f, a, b, n=99):
    h = (b - a) / n
    return (3 * h / 8) * (f(a) + f(b) + sum((2 if i % 3 == 0 else 3) * f(a + i * h) for i in range(1, n)))

if __name__ == "__main__":
    print("Integral:", simpson_3_8(lambda x: x**2, 0, 1))
