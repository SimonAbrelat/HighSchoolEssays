from numpy import linspace as lin  # linespace
from scipy.special import binom  # binomial coefficient
import matplotlib.pyplot as plt  # plotting
from math import pow # power function

x = lin(0, 1, 100)  # Input as 100 floats between 0 and 1
num: int = 10  # The degree

# returns the value from the Bernstein basis function at the point x
def bbf(i: int, n: int, x: float) -> float:
    return binom(n, i) * pow(x, i) * pow((1 - x), (n-i))

# Iterates through all of the functions for the degree
for c in range(num + 1):
    # Plots all of the functions 
    plt.plot(x, [bbf(c, num, i) for i in x])

plt.title("Bernstein Basis Functions")  # Title
plt.show()  # displays graphs
