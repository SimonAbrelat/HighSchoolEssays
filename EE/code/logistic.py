import matplotlib.pyplot as plt  # Graphing lib

# Model Params
r = 0.3  # growth rate
k = 100  # carrying capacity
p = 3  # init value

# Simulation params
t = 50  # total time units
dt = 0.01  # the resiprical of the iterations per time
n = int(t/dt)  # number of iterations

# Storing calculated values
y = []  # Output
t = []  # time for graphing

# Solve ODE using Euler's method
for i in range(n):
    p += ((r * p) * (1 - (p/k))) * dt  # logistic equation
    y.append(p)  # records output
    t.append(i*dt)  # records time

# graphs points
plt.plot(t, y)
plt.show()
