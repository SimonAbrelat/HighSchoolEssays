import matplotlib.pyplot as plt
import numpy as np
import math as ma

cx = []
cy = []
bx = []
by = []
px = []
py = []

xps = [1.0, 0.0, 1.0, 0.0]
yps = [1.0, 2.0, 3.0, 4.0]


class Cubic:
    a = 0
    b = 0
    c = 0
    d = 0

    def __init__(self, A, B, C, D):
        self.a = (-A/2.0 + (3.0*B)/2.0 - (3.0*C)/2.0 + D/2.0)
        self.b = (A - (5.0*B)/2.0 + 2.0*C - D / 2.0)
        self.c = (-A/2.0 + C/2.0)
        self.d = (B)

    def apply(self, t):
        return (self.a * pow(t, 3)) + (self.b * pow(t, 2)) + (self.c * t) + self.d


class Pose:
    x: int = 0
    y: int = 0
    r: float = 0

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

class Cubic254:
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

def polyApply(p: [int], t):
    x = p[0] * (1-t)**3  +  3 * p[1] * t * (1-t)**2  +  3 * p[2] * (1-t) * t**2  +  p[3] * t**3
    return x

if __name__ == "__main__":
    cX = Cubic(xps[0], xps[1], xps[2], xps[3])
    cY = Cubic(yps[0], yps[1], yps[2], yps[3])

    n = Cubic254(Pose(0,0,ma.pi/2), Pose(1.5,1,ma.pi/2))

    for i in np.linspace(0, 1, 100): 
        cx.append(cX.apply(i))
        cy.append(cY.apply(i))
        bx.append(polyApply(xps, i))
        by.append(polyApply(yps, i))
        (tx, ty) = n.apply(i)
        px.append(tx)
        py.append(ty)

    # for j in range(len(x)):
    #     print(x[j], y[j])

    # plt.plot(cx, cy, 'g')
    # plt.plot(bx, by, 'b')
    plt.plot(px, py, 'r')
    #plt.plot(xps, yps, 'ro')
    #plt.plot(xps, yps, 'r:')
    plt.show()

    # print("Y Cos:", Y.a, Y.b, Y.c, Y.d)
