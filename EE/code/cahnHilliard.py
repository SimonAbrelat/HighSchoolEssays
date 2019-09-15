from scipy.ndimage.filters import laplace  # Descrete Laplace
import matplotlib.pyplot as plt  # Graphing
import numpy.random as r  # Matrix Seeding

# Simulation constants
alpha = 0.04  # Diffusion constant
gamma = 0.125  # constant multiplier
n = 2000  # number of iterations
s = 200  # size of the matrix

# Matrix initialization
r.seed(100)
M = r.rand(s, s)

# iterating the Cahn-Hilliard Equation
for _ in range(n):
    G = gamma * laplace(M)  # inner laplace
    Mu = M**3 - M - G  # Mu: chemical potential
    M += laplace(Mu) * alpha  # outer laplace

# Graph Data
plt.imshow(M, cmap=plt.cm.coolwarm, interpolation='bicubic')
plt.axis('off')
plt.show()
