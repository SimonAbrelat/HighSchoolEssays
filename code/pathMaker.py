import matplotlib.pyplot as plt
import numpy as np
import math as ma

class Pose:
    x: int = 0
    y: int = 0
    r: float = 0

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


class CubicHermite:
    def __init__(self, p0: Pose, p1: Pose):

        scale = 2 * ma.hypot(p0.x- p1.x, p0.y - p1.y);
        x0 = p0.x
        x1 = p1.x
        dx0 = ma.cos(p0.r) * scale
        dx1 = ma.cos(p1.r) * scale
        y0 = p0.y
        y1 = p1.y
        dy0 = ma.sin(p0.r) * scale
        dy1 = ma.sin(p1.r) * scale
        self.ax = dx0 + dx1 + 2 * x0 - 2 * x1
        self.bx = -2 * dx0 - dx1 - 3 * x0 + 3 * x1
        self.cx = dx0
        self.dx = x0
        self.ay = dy0 + dy1 + 2 * y0 - 2 * y1
        self.by = -2 * dy0 - dy1 - 3 * y0 + 3 * y1
        self.cy = dy0
        self.dy = y0


    def apply(self, t):
        x = (self.ax * pow(t, 3)) + (self.bx * pow(t, 2)) + (self.cx * t) + self.dx
        y = (self.ay * pow(t, 3)) + (self.by * pow(t, 2)) + (self.cy * t) + self.dy
        return (x, y)


def getClamped(arr, ind):
    if(ind < 0):
        ind = 0
    if(ind > len(arr) - 1):
        ind = len(arr) - 1
    return arr[ind]

if __name__ == "__main__":
    x: [float] = []
    y: [float] = []
    path: [CubicHermite] = []
    pos: [Pose] = [
            Pose(0, 0, ma.pi/2), 
            Pose(1, 1, ma.pi/2), 
            Pose(0, 2, ma.pi/2)
    ]

    for i in range(len(pos)):
        p0 = getClamped(pos, i)
        p1 = getClamped(pos, i+1)
        path.append(CubicHermite(p0, p1))

    for p in path:
        for t in np.linspace(0,1,50):
            xt, yt = p.apply(t)
            x.append(xt)
            y.append(yt)

plt.plot(x, y, 'r')
plt.show()
