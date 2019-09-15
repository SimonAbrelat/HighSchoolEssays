from numpy import linspace as lin  # linespace
from scipy.special import binom # binomial coefficient
import matplotlib.pyplot as plt # Graphs 
from math import pow # power function

d: int = 3 # Degree of the polynomial
t = lin(0, 1, 100) # The time

# The cubic hermite basis functions 
def H(n: int, x: float) -> float:
    if  (n == 0): return (2 * pow(x, 3)) - (3 * pow(x, 2)) + 1 # H00
    elif(n == 1): return pow(x, 3) - (2 * pow(x, 2)) + x       # H01
    elif(n == 2): return (-2 * pow(x, 3)) + (3 * pow(x, 2))    # H10
    elif(n == 3): return pow(x, 3) - pow(x, 2) 		       # H11
    else: return 0

# returns the value from the Bernstein basis function at the point x
def bbf(i: int, n: int, x: float) -> float:
    return binom(n, i) * pow(x, i) * pow((1 - x), (n-i))

# The bernstein form of the cubic hermite basis function
def BH(n: int, x: float) -> float:
    B = lambda i: bbf(i, 3, x) # pythonic function curry
    if  (n == 0): return B(0) + B(1) # H00
    elif(n == 1): return B(1) / 3    # H01
    elif(n == 2): return B(3) + B(2) # H10
    elif(n == 3): return B(2) / -3   # H11
    else: return 0

# graph configs
plt.title("Cubic Hermite Basis Functions")
plt.axis('scaled') # equalize axes
plt.axhline(0, color='black', linewidth=.75) # y axis line

for n in range(d+1): plt.plot(t, [H(n, i) for i in t]) # plots all of the funcs
plt.show()
