from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

X, Y, Z = axes3d.get_test_data(0.2)

# Normalize to [0,1]
Z = (Z-Z.min())/(Z.max()-Z.min())

colors = cm.viridis(Z)
rcount, ccount, _ = colors.shape

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rcount=rcount, ccount=ccount,
                       facecolors=colors, shade=False)
surf.set_facecolor((0,0,0,0))
plt.show()
