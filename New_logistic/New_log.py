import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

r_ = np.linspace(3, 4, 20000)
xy = []
acc = 60
plt.figure(figsize=(13, 9))


def stable(r1):
    x_ = [0.5]
    for i in range(acc):
        x_.append(r1 * x_[i] * (1 - x_[i]))
    x_ = x_[int(acc / 2):]
    result = []
    for x1 in x_:
        if (round(x1, 3), r1) not in result:
            result.append((round(x1, 3), r1))
    #  print(result)
    return result


def logistic():
    for r in r_:
        for c in stable(r):
            xy.append(c)
    # print(xy)


logistic()
x, y = zip(*xy)
# print(x, y)
plt.scatter(y, x, s=0.01)
plt.show()
