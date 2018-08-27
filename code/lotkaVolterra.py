import matplotlib.pyplot as plt

# Model params
alpha = 2/3
beta = 4/3
gamma = 1
delta = 1

# Simulation constants: descrete time and space
dt = 0.001  # the change in time
n = 15000  # number of iterations

# Seed the space
U = 1  # Population of Pray
V = 0.1  # Population of Preditors
# output Arrays
Uy = []
Vy = []
X = []

# Simulate this ODE with Euler's method
for i in range(n):
    # Gets copies to prevent overwritting
    Uc = U
    Vc = V
    # Generate next time step
    U += (alpha*Uc - beta*Uc*Vc)*dt
    V += (gamma*Uc*Vc - delta*Vc)*dt
    # Record outputs
    Uy.append(U)
    Vy.append(V)
    X.append(i*dt)

# Graph Data
plt.title("Lotka-Volterra Model")
plt.plot(X, Uy, 'b', label="pray")
plt.plot(X, Vy, 'r', label="preditor")
plt.legend()
plt.show()
