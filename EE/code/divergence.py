import matplotlib.pyplot as plt # graphing library
from numpy import fromfunction # generates matrix

size: int = 100 # size of the matrix

# The base function
def fun(x, y): return x*(y**2) + y

def dy(x, y): return 2*x*y # Partial derivative on Y
def dx(x, y): return 2*y+1 # Partial derivative on X

# Divergence function, sum of the partials
def div(x, y): return dx(x,y) + dy(x,y)

# transforms the coordinates to get the right domain
def t(x): return (x - (size/2))/10

# Generates a matrix from a functions that is given X and Y
# In this case, the x, y operate like a cartesian plane centered at 0
# we then plug in our modified coordients into our div function
P = fromfunction(lambda x, y: div(t(x), t(y)), (size, size))

# Graphs the matrix
plt.imshow(P, cmap=plt.cm.coolwarm, interpolation='bilinear')
plt.colorbar() # side colorbar for reference
plt.show()
