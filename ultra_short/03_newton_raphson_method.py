# Newton-Raphson Method (Ultra-Short)
def newton(f, df, x, steps=20):
    for _ in range(steps):
        x -= f(x) / df(x)
    return x

if __name__ == "__main__":
    print("Root:", newton(lambda x: x**2 - 2, lambda x: 2*x, 1.5))
