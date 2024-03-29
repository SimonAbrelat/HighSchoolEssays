import matplotlib.pyplot as plt
from typing import List
import numpy as np
from math import sin, cos, hypot
from math import radians as rad

# Simulation Constants
dt: float = 1e-3  # time between physics iterations

# Physics Constants
m: float = 69  # mass: kg
k: float = 1000  # spring constant: N/m
g: float = 9.81  # gravitational accel: m/s^2
theta: float = rad(90)  # the angle the robot luaches at

# Spring data recording
x: float = -0.05 # inital compression
v: float = 0  # initial velocity
ta: List[float] = []  # time
xa: List[float] = []  # position
va: List[float] = []  # velocity
aa: List[float] = []  # acceleration

def sign(x: float) -> float:
    return -1 if x < 0 else 1

def hookesAcc(x: float, k: float, m: float) -> float:
    return ((-k * x) / m) - g

def hookesAccAngle(x: float, k: float, m: float, t: float) -> float:
    a = ((-k * x) / m) - (g * cos(t))
    return a

def spring(x: float, k: float, m: float) -> float:
    global ta, xa, va, aa, v
    i = 0
    w:float = 0
    while(x < 0):
        i += 1
        a = hookesAccAngle(x, k, m, theta)
        v += a * dt
        x += v * dt
        w += m * a * (v*dt)
        t = i * dt

        ta.append(t)
        xa.append(x)
        va.append(v)
        aa.append(a)
    return (w)

#  print(ta[-1])
 plt.plot(ta, xa, label="Displacement")
plt.plot(ta, va, label="Velocity")
plt.plot(ta, aa, label="Acceleration")
plt.legend()
plt.show()
