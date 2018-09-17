import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def fun(x, y):
    return x*(y**2) + y


def dy(x, y):
    return 2*x*y


def dx(x, y):
    return 2*y+1


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-2.0, 2.0, 0.01)
X, Y = np.meshgrid(x, y)
zs = np.array([dx(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
