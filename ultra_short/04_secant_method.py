# Secant Method (Ultra-Short)
def secant(f, x0, x1, steps=20):
    for _ in range(steps):
        if abs(f(x1)) < 1e-6 or f(x1) == f(x0): break
        x0, x1 = x1, x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    return x1

if __name__ == "__main__":
    print("Root:", secant(lambda x: x**2 - 4, 1, 3))
