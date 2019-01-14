import matplotlib.pyplot as plt
from typing import List
import numpy as np
from math import sin, cos, hypot
from math import radians as rad

# Simulation Constants
dt: float = .001  # time between physics iterations

# Projectile data recording
xp: float = 0  # projectile x
yp: float = 0  # projectile y
vv: float = 0  # verticle velocity
vh: float = 10  # horizontal velocity
xpa: List[float] = []  # projectile x
ypa: List[float] = []  # projectile y

def projectile():
    global xp, yp, vv
    xp += vh * dt
    vv -= g * dt
    yp += vv * dt


while(yp >= 0):
    projectile()
    print(yp)
    xpa.append(xp)
    ypa.append(yp)

plt.plot(xpa, ypa)
plt.show()
