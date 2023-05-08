import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np

n = 10
fig, axes = plt.subplots(n, n)
interval = 1000

angles = np.linspace(0, 2 * pi, interval)


def lissajous(w1, w2):
    x, y = [], []

    for i in angles:
        x.append(sin(w1 * i))
        y.append(sin(w2 * i + pi / 2))

    return x, y


for x1 in range(1, n + 1):
    for y1 in range(1, n + 1):
        x_, y_ = lissajous(y1, x1)
        axes[x1 - 1, y1 - 1].plot(x_, y_)


plt.show()
