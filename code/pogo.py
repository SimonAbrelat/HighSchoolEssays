import matplotlib.pyplot as plt
from typing import List
import numpy as np
from math import sin, cos, hypot, sqrt
from math import radians as rad

# Simulation Constants
dt: float = 1e-3  # time between physics iterations

# Physics Constants
m: float = 69   # mass: kg
k: float = 7000  # spring constant: N/m
g: float = 9.81  # gravitational accel: m/s^2
theta: float = rad(45)  # the angle the robot luaches at
z: float = 0.38 # step height

# Spring data recording
x: float = -0.3  # inital compression
v: float = 0  # placeholder
h: float = -1  # placeholder

def hookesAcc(x: float, k: float, m: float) -> float:
    return ((-k * x) / m) - g

def hookesAccAngle(x: float, k: float, m: float, t: float) -> float:
    return ((-k * x) / m) - (g * cos(t))

def spring(x: float, k: float, m: float) -> float:
    v: float = 0.0
    while(x < 0):
        a = hookesAccAngle(x, k, m, theta)
        v += a * dt
        x += v * dt
    return v

def height(): return (v ** 2 * sin(theta) ** 2) / (2 * g)
def distance(): return (v**2 * sin(2*theta)) / g
def stepDistance(v: float):
    det = (v**2 * sin(theta)**2) - (2 * g * z)
    if(det < 0): return -1
    return ((v * cos(theta)) / g) *\
           ((v * sin(theta)) + sqrt(det))

def isValid(x: float, k: float) -> float:
    return -1 if stepDistance(spring(x, k, m)) == -1 else 1

size: int = 2

P = np.zeros((size, size))
for i in range(size):
    for j in range(size):
        P[i][j] = isValid(i * -0.3, j * 15000)

plt.imshow(P, cmap=plt.cm.coolwarm, interpolation='bilinear')
plt.colorbar() # side colorbar for reference
plt.show()
