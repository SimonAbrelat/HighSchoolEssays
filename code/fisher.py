import matplotlib.pyplot as plt
import numpy as np

# Model params
D = 0.01  # partial multiplier
r = 0.01  # rate

# Simulation params
t = 5000  # number of 'time units'
dt = 0.1  # iterations per time unit
n = int(t/dt)  # number of iterations
dx = 0.25  # spacial difference
s = 100

# Init Array
A = np.zeros(s)
A[0:10] = 1.0

# Wrapping index function
def get(a, i): return a[i % len(a)]

# d2u/dx2
def dx2(a):
    ret = np.empty(len(a))  # return array
    for i in range(len(a)-1):  # iterate through the array
        V = get(a, i)  # gets center
        L = get(a, i-1)  # Left value
        R = get(a, i+1)  # right value
        ret[i] = (L + R - (2*V)) / dx**2  # descrete laplace
    return ret

for _ in range(n):
    A += (((A*r)*(1-A)) + D*dx2(A)) * dt

plt.plot(A)
plt.show()
