import numpy as np
import matplotlib.pyplot as plt

# The base function
def fun(x, y):
    return x*(y**2) + y

def dy(x, y): return 2*x*y  # Partial derivative on Y
def dx(x, y): return 2*y+1  # Partial derivative on X

# gets input points
x = y = np.arange(-2.0, 2.0, 0.25)
X, Y = np.meshgrid(x, y)
# Derivatives for each point
Dx = np.array([dx(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Dy = np.array([dy(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Dx = Dx.reshape(X.shape)
Dy = Dy.reshape(Y.shape)
# Vectors given derivatives
Ax = np.array([x + dx for x, dx in zip(np.ravel(X), np.ravel(Dx))])
Ay = np.array([y + dy for y, dy in zip(np.ravel(Y), np.ravel(Dy))])
Ax = Ax.reshape(X.shape)
Ay = Ay.reshape(Y.shape)
# Graph
plt.quiver(X, Y, Ax, Ay, cmap=plt.cm.coolwarm)
plt.show()
