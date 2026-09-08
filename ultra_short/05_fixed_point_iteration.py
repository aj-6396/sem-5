# Fixed Point Iteration (Ultra-Short)
def fixed_point(g, x, steps=30):
    for _ in range(steps):
        x = g(x)
    return x

if __name__ == "__main__":
    print("Root:", fixed_point(lambda x: (x + 2 / x) / 2, 1.0))
