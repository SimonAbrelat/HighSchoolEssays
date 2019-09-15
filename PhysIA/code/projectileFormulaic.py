import matplotlib.pyplot as plt
from typing import List
import numpy as np
from math import sin, cos, sqrt
from math import radians as rad

# Simulation Constants
g: float = 9.81  # acceleration due to gravity
dt: float = .001  # time between physics iterations

# Initial Values
v: float = 1  # the initial velocity
theta: float = rad(70)  # the initial angle
vv: float = sin(theta) * v  # verticle velocity
vh: float = cos(theta) * v  # horizontal velocity
z: float =  0.81 #0.6985 

# Data Recording
x: float = 0  # projectile x
y: float = 0  # projectile y
xa: List[float] = []  # projectile x
ya: List[float] = []  # projectile y
ym: float = 0  # max Y

def height(): return (v ** 2 * sin(theta) ** 2) / (2 * g)
def distance(): return (v**2 * sin(2*theta)) / g
def stepDistance():
    det = (v**2 * sin(theta)**2) - (2 * g * z)
    if(det < 0): return -1
    return ((v * cos(theta)) / g) *\
           ((v * sin(theta)) + sqrt(det))

h: float = -1 #distance
while(h == -1):
    v += .01
    h = stepDistance()

print(h, v)
#plt.plot(xa, ya)
#plt.show()
