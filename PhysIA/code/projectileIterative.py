import matplotlib.pyplot as plt
from typing import List
import numpy as np
from math import sin, cos
from math import radians as rad

# Simulation Constants
g: float = 9.81  # acceleration due to gravity
dt: float = 1e-06  # time between physics iterations

# Initial Values
v: float = 10  # the initial velocity
theta: float = rad(50)  # the initial angle
vv: float = sin(theta) * v  # verticle velocity
vh: float = cos(theta) * v  # horizontal velocity

# Data Recording
x: float = 0  # projectile x
y: float = 0  # projectile y
xa: List[float] = []  # projectile x
ya: List[float] = []  # projectile y
ym: float = 0  # max Y

def projectile():
    global x, y, vv
    x += vh * dt
    vv -= g * dt
    y += vv * dt


while(y >= 0):
    projectile()
    if(y > ym): ym = y
    xa.append(x)
    ya.append(y)

print(ym, x)
#plt.plot(xa, ya)
#plt.show()
