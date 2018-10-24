from scipy.special import binom
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0, 1, 100)
num: int = 3

def bbf(i: int, n: int, x: float) -> float:  # Bernstein Basis Function
    return binom(n, i) * math.pow(x, i) * math.pow((1 - x), (n-i))

for c in range(num + 1):
    plt.plot(x, [bbf(c, num, i) for i in x])

plt.title("Bernstein Basis Functions")
plt.show()
