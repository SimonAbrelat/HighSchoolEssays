from scipy.ndimage.filters import laplace  # Descrete Laplace
import matplotlib.pyplot as plt  # graphing
from numpy import full  # matrix init

# Constants
s = 250  # size of the matrix
Du = 1  # U growth rate
Dv = 0.5  # V growth rate
f = .0545  # feed rate
k = .062  # kill rate


# Simulation Params
t = 5000  # 'time' simulated
dt = .1  # Iterations per time unit
n = int(t/dt)  # total iteration count

fig = plt.figure()

# Matrix Inits
U = full((s, s), 1.0)  # Starts U full of 1
V = full((s, s), 0.0)  # stats V full of 0
V[45:55, 45:55] = 1.0  # Adds a bit to V

# iterate though PDE
for _ in range(n):
    uvv = U * V * V  # prevents write error and clean
    U += ((Du*laplace(U) - uvv + (f * (1 - U))) * dt)  # U solve
    V += ((Dv*laplace(V) + uvv - (V * (f + k))) * dt)  # V solve

# Graph
plt.imshow(V, cmap=plt.cm.coolwarm)
plt.axis("off")
plt.show()
