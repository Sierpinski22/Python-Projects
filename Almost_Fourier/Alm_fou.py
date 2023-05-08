import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, pi
from random import randint


def build_signal(nw=3):
    w = []
    while len(w) < nw:
        ra = randint(1, 7)
        if ra not in w:
            w.append(ra)
    return sorted(w)


def find_greatest(xax, yax, num):
    zipped = list(zip(xax, yax))
    zipped.sort(key=lambda e: e[1])
    values = [zipped[-1][0]]
    i = 0
    while len(values) < num:  # while !!!!!
        diff = [abs(v - zipped[len(zipped) - i - 1][0]) > 0.5 for v in values]
        if all(diff):
            values.append(zipped[len(zipped) - i - 1][0])
        i += 1

    return sorted(values)


waves = build_signal()
f = lambda x_: sum([sin(2 * pi * x_ * ran) for ran in waves])

fig, axs = plt.subplots(4, 1)

start, end = 0, 4
end_f = 10.0
accuracy = 500
n = 3

t_ax = np.linspace(start, end, accuracy)
f_ax = np.linspace(0.01, end_f, 5 * 100)
y_ax = [f(t) for t in t_ax]
x_mass, y_mass, r_mass = [], [], []

for f in f_ax:
    x, y, r = 0, 0, 0
    for vt, vy in zip(t_ax, y_ax):
        theta = vt % (1 / f) * 2 * pi * f

        x += vy * cos(theta)
        y += vy * sin(theta)
        r = (x ** 2 + y ** 2) ** 0.5

    x_mass.append(x)
    y_mass.append(y)
    r_mass.append(r)

x_found = find_greatest(f_ax, x_mass, len(waves))
y_found = find_greatest(f_ax, y_mass, len(waves))
r_found = find_greatest(f_ax, r_mass, len(waves))

print(f"Frequenze effettive delle sinusoidi: {waves}")
print(f"Frequenze trovate usando lo spostamento su x del 'centro di massa': {x_found}")
print(f"Frequenze trovate usando lo spostamento su y del 'centro di massa': {y_found}")
print(f"Frequenze trovate usando la distanza dall'origine del 'centro di massa': {r_found}")

axs[0].plot(t_ax, y_ax)
axs[0].grid()
axs[1].axvline(x=x_found[0], c='r', linestyle='-.')
axs[1].axvline(x=x_found[1], c='r', linestyle='-.')
axs[1].axvline(x=x_found[2], c='r', linestyle='-.')
axs[1].plot(f_ax, x_mass)
axs[1].grid()
axs[2].axvline(x=y_found[0], c='r', linestyle='-.')
axs[2].axvline(x=y_found[1], c='r', linestyle='-.')
axs[2].axvline(x=y_found[2], c='r', linestyle='-.')
axs[2].plot(f_ax, y_mass)
axs[2].grid()
axs[3].axvline(x=r_found[0], c='r', linestyle='-.')
axs[3].axvline(x=r_found[1], c='r', linestyle='-.')
axs[3].axvline(x=r_found[2], c='r', linestyle='-.')
axs[3].plot(f_ax, r_mass)
axs[3].grid()
plt.show()
