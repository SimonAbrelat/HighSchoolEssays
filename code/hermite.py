import matplotlib.pyplot as plt # Graphing Lib
from math import pow # Poewr function
import numpy as np # Arrays and matrices

p: [float] = [0, 3] # The control points
d: [float] = [0, 1] # the derivative at said control points
t = np.linspace(0, 1, 100) # an array of time values

# hermite spline interpolation between 2 points
def hermite(t1: float, t2: float, dt1: float, dt2: float, s: float) -> float:
    S = np.matrix([[pow(s, 3), pow(s, 2), s, 1]]) # horizontal matrix for x
    C = np.matrix([[t1, t2, dt1, dt2]]).T # verticle matrix for input values

    h = np.matrix([[ 2, -2,  1,  1], # weight matrix that represents 
                   [-3,  3, -2, -1], # the basis functions
                   [ 0,  0,  1,  0],
                   [ 1,  0,  0,  0]])
    # multiplies them all together and gets the scalar from it
    return np.asscalar(S * h * C)

# graph configs
plt.axes('equal')
plt.title("1D Hermite Interpolation")
# graphs the equation
plt.plot(t, [hermite(p[0], d[0], p[1], d[1], i) for i in t])
plt.show()
