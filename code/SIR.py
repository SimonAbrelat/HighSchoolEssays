import matplotlib.pyplot as plt

# Model params
b = 1/2  # days of contact to spread
k = 1/4  # days to recover

# Simulation params
dt = 0.1  # change in time
n = 1400  # number of iterations

# Seeding
s = 1  # suseptible population
i = 1.27E-4  # Infected
r = 0  # Recovered
# To graph and record values
Sy = []
Iy = []
Ry = []
X = []

# Simulate ODE with Euler's method
for x in range(n):
    # Edge case
    if i <= 0:
        print("Done")
        break
    # copy to prevent overwritting
    Sc = s
    Ic = i
    Rc = r
    # Generate next timestep
    s += (-b * Sc * Ic) * dt
    i += ((b * Sc * Ic) - (k * Ic)) * dt
    r += (k * Ic) * dt
    # Record values
    Sy.append(s)
    Iy.append(i)
    Ry.append(r)
    X.append(x*dt)

# Graph Data
plt.title("SIR model")
plt.plot(X, Sy, 'g', label="Suseptible")
plt.plot(X, Iy, 'r', label="Infected")
plt.plot(X, Ry, 'b', label="Recovered")
plt.legend()
plt.show()
