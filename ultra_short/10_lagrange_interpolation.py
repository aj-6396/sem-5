# Lagrange Interpolation (Ultra-Short)
from math import prod

def lagrange(x, y, target):
    return sum(y[i] * prod((target - x[j]) / (x[i] - x[j]) for j in range(len(x)) if i != j) for i in range(len(x)))

if __name__ == "__main__":
    print("Value at 1.5:", lagrange([0, 1, 2], [1, 3, 7], 1.5))
