import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import cmath
from math import *
import os
cls = lambda: os.system('cls')

values = []
mini, maxi = -1.7, 1.7
accuracy = 1000
h = 10 ** (-8.5)
n_ = 50
eq = input('Input function in z: ').replace('x', 'z')
f = eval('lambda z: ' + eq)
d = input("Input derivative of the function. Write 'none' to use automatic deriivation: ").replace("x", "z")

if d.lower() == 'none':
    automatic = True
else:
    d = eval('lambda z:' + d)
    automatic = False


def derivative(z, func=None):
    if not automatic:
        return d(z)
    else:
        delta_z = complex(h, h)
        w = func(z + delta_z) - func(z)
        return w / delta_z


for y in np.linspace(mini, maxi, accuracy):
    for x in np.linspace(mini, maxi, accuracy):
        values.append(complex(x, y))


def split_axes(z_):
    real = [r2.real for r2 in z_]
    imag = [i2.imag for i2 in z_]
    return real, imag


def draw_test(z_):
    r1, i1 = split_axes(z_)
    plt.scatter(r1, i1, 1, marker='s')


def purify(v, n):
    result = []
    for element in v:
        result.append(not abs(n - element) < 10 ** (-5))
    return result if len(result) != 0 else [True]


def progress_bar(n, max_):
    percentage = f'{n/max_ * 100:.2f}%'
    line = f"Loading {percentage:<10}|"
    for i in range(50):
        if i <= n/max_ * 50:
            line += '='
        else:
            line += ' '
    cls()
    print(line + '|')


def find_roots_plus_fractal(func, attem, n):
    roots_ = []
    colored = [[-1 for _ in range(accuracy)] for _ in range(accuracy)]
    for k in range(n):
        for j in range(len(attem)):
            try:
                attem[j] -= func(attem[j]) / derivative(attem[j], func)
            except ZeroDivisionError:
                pass
            if abs(func(attem[j])) < 10 ** (-9):
                if all(purify(roots_, attem[j])):
                    roots_.append(attem[j])
            if k + 1 == n:
                if k + 1 == n:
                    n_roots = len(roots_)
                    z = attem[j]
                    minval, c = abs(z - roots_[0]), 0
                    for indx, r0 in enumerate(roots_):
                        if abs(z - r0) < minval:  # è più vicino alla radice
                            minival = r0
                            c = indx

                    colored[j // accuracy][j % accuracy] = c
        progress_bar(k + 1, n)
    return roots_, attem, colored


# create colormap
fig, ax = plt.subplots()
fig.set_size_inches(10.5, 10.5)
fig.tight_layout()
roots, mapped, clrd = find_roots_plus_fractal(f, values, n_)
colormap = cm.get_cmap('viridis', len(roots))
colormap.set_under('k')
ax.imshow(clrd, cmap=colormap, vmin=0, vmax=len(roots))
plt.title(eq)
plt.show()
