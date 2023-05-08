import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from random import random

fig = plt.figure("Lorenz Attractor")
fig2 = plt.figure("Three axes", figsize=(7, 5))
ax = Axes3D(fig)

o = 10
p = 30
b = 8 / 3  # 10, 28

x_, y_, z_, n = [], [], [], []
x1 = 1
y1 = 1
z1 = 1


def generate(x, y, z):
    dt = 0.01
    dx = o * (y - x) * dt
    dy = (p*x - x*z - y) * dt
    dz = (x*y - b*z) * dt
    return x + dx, y + dy, z + dz


for i in range(3000):
    x_.append(x1)
    y_.append(y1)
    z_.append(z1)
    n.append(i)
    x1, y1, z1 = generate(x1, y1, z1)


x_ = np.array(x_)
y_ = np.array(y_)
z_ = np.array(z_)

# ax.plot(x_[i:i + 2], y_[i:i + 2], z_[i:i + 2], color=cols[i % 6])
ax.plot(x_, y_, z_, c='b')

plt.subplot(3, 1, 1)
plt.plot(n, x_)
plt.title("X")
plt.subplot(3, 1, 2)
plt.plot(n, y_)
plt.title("Y")
plt.subplot(3, 1, 3)
plt.plot(n, z_)
plt.title("Z")
plt.subplots_adjust(hspace=0.7)
plt.show()
