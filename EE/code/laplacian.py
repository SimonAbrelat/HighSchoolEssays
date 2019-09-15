import numpy as np
import matplotlib.pyplot as plt

# Constants
s = 100
dx = s/2
a = 1
b = 2
c = 3

# Matrix Inits
M = np.empty((s, s))
M.fill(0)


def fn(x, y):
    return np.sqrt((x**2/a**2) + (y**2/b**2))


M = np.fromfunction(lambda x, y: fn(x, y), (s, s))


# Implementation of the decretized laplacian operator
def laplacian(Z):
    Ztop = Z[0:-2, 1:-1]
    Zleft = Z[1:-1, 0:-2]
    Zbottom = Z[2:, 1:-1]
    Zright = Z[1:-1, 2:]
    Zcenter = Z[1:-1, 1:-1]
    return (Ztop + Zleft + Zbottom + Zright - (4 * Zcenter)) / dx**2


L = laplacian(M)
# Graph Data
plt.subplot(121)
plt.imshow(M, cmap=plt.cm.coolwarm, label="Normal Function",
           interpolation='bilinear', extent=[-1, 1, -1, 1])
plt.subplot(122)
plt.imshow(L, cmap=plt.cm.coolwarm, label="Laplacian",
           interpolation='bilinear')
plt.show()
