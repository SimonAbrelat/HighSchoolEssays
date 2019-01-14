import matplotlib.pyplot as plt
from typing import List
import numpy as np
from math import sin, cos, hypot
from math import radians as rad

# Simulation Constants
dt: float = .001  # time between physics iterations

# Physics Constants
m: float = 69  # mass: kg
k: float = 7000  # spring constant: N/m
g: float = 9.81  # gravitational accel: m/s^2
theta: float = rad(45)  # the angle the robot luaches at
e: float = .5  # effiency

# Spring data recording
x: float = -0.3  # inital compression
v: float = 0  # initial velocity
a: float = 0  # initial accel
ta: List[float] = []  # time
xa: List[float] = []  # position
va: List[float] = []  # velocity
aa: List[float] = []  # acceleration


def hookesAcc(x: float) -> float:
    return (((-k * x) / m) - g) * e
    #v = ((-k * x) / m) - g
    #return hypot(v*sin(theta) - g, v*cos(theta))


i = 0
while(x < 0):
    i += 1
    a = hookesAcc(x)
    v += a * dt
    x += v * dt
    if(x > 0): break

    t = i * dt

    ta.append(t)
    xa.append(x)
    va.append(v)
    aa.append(a)
    print(x, v, a, t)

print("max vel: ", v)
print("height: ", ((v**2) / (2*g)))
plt.plot(ta, xa)
plt.plot(ta, va)
plt.plot(ta, aa)
plt.show()
