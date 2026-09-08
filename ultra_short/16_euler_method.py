# Euler's Method (Ultra-Short)
def euler(f, x, y, xn, h=0.1):
    while x < xn - 1e-9:
        y += h * f(x, y)
        x += h
    return y

if __name__ == "__main__":
    print("y(0.2):", euler(lambda x, y: x + y, 0, 1, 0.2))
