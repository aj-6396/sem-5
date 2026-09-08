# Regula-Falsi Method (Ultra-Short)
def regula_falsi(f, a, b, steps=30):
    for _ in range(steps):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) == 0: return c
        a, b = (a, c) if f(a) * f(c) < 0 else (c, b)
    return c

if __name__ == "__main__":
    print("Root:", regula_falsi(lambda x: x**3 - 2*x - 5, 2, 3))
