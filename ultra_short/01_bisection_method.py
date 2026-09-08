# Bisection Method (Ultra-Short)
def bisection(f, a, b, steps=30):
    for _ in range(steps):
        c = (a + b) / 2
        if f(c) == 0: return c
        a, b = (a, c) if f(a) * f(c) < 0 else (c, b)
    return (a + b) / 2

if __name__ == "__main__":
    print("Root:", bisection(lambda x: x**2 - 4, 1, 3))
