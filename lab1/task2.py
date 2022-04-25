import matplotlib.pyplot as plt
import math
import numpy as np


u = np.linspace(0, 2 * math.pi, 50)
v = np.linspace(-1, 1, 50)

x = np.cos(u) * (1 + (v / 2) * np.cos(u / 2))
y = np.sin(u) * (1 + (v / 2) * np.cos(u / 2))
z = (v / 2) * np.sin(u / 2)

f = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title('x = cos(u)(1+(v/2)cos(u/2))\ny = sin(u)(1+(v/2)cos(u/2))\nz = (v/2)sin(u/2)')
plt.tight_layout()
ax.scatter(x, y, z)
plt.show()

n = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title('x = cos(u)(1+(v/2)cos(u/2))\ny = sin(u)(1+(v/2)cos(u/2))\nz = (v/2)sin(u/2)')
plt.tight_layout()
ax.plot(x, y, z, "orchid")
plt.show()



