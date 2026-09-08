# Modified Euler's (Heun's) Method (Ultra-Short)
def modified_euler(f, x, y, xn, h=0.1):
    while x < xn - 1e-9:
        y += (h / 2) * (f(x, y) + f(x + h, y + h * f(x, y)))
        x += h
    return y

if __name__ == "__main__":
    print("y(0.2):", modified_euler(lambda x, y: x + y, 0, 1, 0.2))
