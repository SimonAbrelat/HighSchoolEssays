import numpy as np
import matplotlib.pyplot as plt

# Simulation constants
alpha = 0.00001  # Laplician multiplier
n = 8000  # number of iterations
s = 100  # size of the matrix
dx = 2/s  # Simulation speed/accuracy

# Matrix initialization
M = np.fill((s, s), 0.0)
# Hotspot Seeding
M[20:30, 45:50] = 90
M[70:80, 45:50] = 90

# Implementation of the decretized laplacian operator
def laplacian(Z):
    Ztop = Z[0:-2, 1:-1]
    Zleft = Z[1:-1, 0:-2]
    Zbottom = Z[2:, 1:-1]
    Zright = Z[1:-1, 2:]
    Zcenter = Z[1:-1, 1:-1]
    return (Ztop + Zleft + Zbottom + Zright - (4 * Zcenter)) / dx**2

# Iterations through PDE
for _ in range(n):
    Mn = M[1:-1, 1:-1]
    M[1:-1, 1:-1] = Mn + np.multiply(laplacian(M), alpha)

# Graph Data
plt.imshow(M, cmap=plt.cm.coolwarm,
           interpolation='bilinear', extent=[-1, 1, -1, 1])
plt.show()
