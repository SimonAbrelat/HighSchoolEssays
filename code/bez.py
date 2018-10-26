from numpy import linspace as lin  # linespace
from scipy.special import binom  # binomial coefficient
import matplotlib.pyplot as plt  # plotting
from math import pow # power function

cpx: [float] = [1.0, 3.0, 6.0, 8.0]
cpy: [float] = [1.0, 9.0, 6.0, 1.0]

t = lin(0, 1, 100)  # Input as 100 floats between 0 and 1
num: int = 3  # The degree

# returns the value from the Bernstein basis function at the point x
def bbf(i: int, n: int, x: float) -> float:
    return binom(n, i) * pow(x, i) * pow((1 - x), (n-i))

# De Cas
def f(a: [float], t: float) -> float:
    ret = 0
    for i in range(num + 1):
        ret += a[i] * bbf(i, num, t)
    return ret

def x(t: float) -> float: return f(cpx, t)
def y(t: float) -> float: return f(cpy, t)

plt.plot([x(i) for i in t], [y(i) for i in t])
plt.plot(cpx, cpy, 'r--')
plt.plot(cpx, cpy, 'ro')
plt.show()
