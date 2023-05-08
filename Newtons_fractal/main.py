import matplotlib.pyplot as plt
import numpy as np

f = lambda z: z ** 3
h = 10 ** (-8.5)
d2 = lambda z: 3 * z ** 2


def d(func, z):
    delta_z = complex(h, h)
    w = func(z + delta_z) - func(z)
    return w / delta_z


def make_values(mini, maxi, accuracy):  # maxi excluded
    increment = (maxi - mini) / accuracy
    values = []
    for i in range(accuracy):
        for r in range(accuracy):
            values.append(complex(r * increment + mini, i * increment + mini))
    return values


def grid_to_axes(values):
    return [a.real for a in values], [a.imag for a in values]


z_ = make_values(-1, 1, 10)
z2 = list(map(f, z_))
z3 = list(map(lambda z: z + complex(h, h), z_))


def calculate_approximation():
    differences = []
    for j in range(len(z_)):
        try:
            differences.append(abs(d2(z_[j]) - d(f, z_[j])))
        except ZeroDivisionError:
            pass
    return differences


print(sum(calculate_approximation()))

r_, i_ = grid_to_axes(z_)
plt.scatter(r_, i_)
r_, i_ = grid_to_axes(z3)
plt.scatter(r_, i_)
plt.show()
