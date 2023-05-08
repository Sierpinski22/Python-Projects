import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

attractor = plt.figure("Strange attractor")
data = plt.figure("Graphs")
ax = Axes3D(attractor)
# dt = 0.07
iterations = 10000

rules = {'chen': {'a': 40, 'b': 3, 'c': 28, 'x1': -0.1, 'y1': 0.5, 'z1': -0.6, 'dt': 0.004},
         'chua': {'alpha': 10.82, 'beta': 14.286, 'a': 1.3, 'b': 0.11, 'c': 7, 'd': 0, 'x1': 1, 'y1': 1, 'z1': 0, 'dt': 0.03},
         'mod': {'a': 35, 'b': 3, 'c': 28, 'd0': 1, 'd1': 1, 'd2': -20, 'tau': .2, 'dt': 0.4, 'x1': 0, 'y1': 1, 'z1': 14}}


def mod():
    x1 = rules['mod']['x1']
    y1 = rules['mod']['y1']
    z1 = rules['mod']['z1']
    a = rules['mod']['a']
    b = rules['mod']['b']
    c = rules['mod']['c']
    d0 = rules['mod']['d0']
    d1 = rules['mod']['d1']
    d2 = rules['mod']['d2']
    t = rules['mod']['tau']
    dt = rules['chen']['dt']
    result = []

    for _ in range(iterations):
        f = d0 * z1 + d1*z1*(t*dt) - d2*np.sin(z1*(dt*t))
        dx = a * (y1-x1) * dt
        dy = ((c-a)*x1 - x1*f + c*y1) * dt
        dz = (x1*y1 - b*z1) * dt
        result.append([x1, y1, z1])
    return result


def chen():

    x1 = rules['chen']['x1']
    y1 = rules['chen']['y1']
    z1 = rules['chen']['z1']
    a = rules['chen']['a']
    b = rules['chen']['b']
    c = rules['chen']['c']
    dt = rules['chen']['dt']
    result = []

    for _ in range(iterations):
        dx = a * (y1 - x1) * dt
        dy = ((c - a) * x1 - x1 * z1 + c * y1) * dt
        dz = (x1 * y1 - b * z1) * dt
        x1 += dx
        y1 += dy
        z1 += dz
        result.append([x1, y1, z1])
    return result


def chua():
    x1 = rules['chua']['x1']
    y1 = rules['chua']['y1']
    z1 = rules['chua']['z1']
    al = rules['chua']['alpha']
    be = rules['chua']['beta']
    a = rules['chua']['a']
    b = rules['chua']['b']
    # c = rules['chua']['c']
    d = rules['chua']['d']
    dt = rules['chua']['dt']
    result = []

    for i in range(iterations):
        h = -b * np.sin((x1 * np.pi) / (2 * a) + d)
        dx = (al*(y1 - h)) * dt
        dy = (x1 - y1 + z1) * dt
        dz = (-be*y1) * dt
        x1 += dx
        y1 += dy
        z1 += dz
        result.append([x1, y1, z1])
    return result


def run(choice):
    r = chen()
    x_ = []
    y_ = []
    z_ = []
    n = []

    for i in range(iterations):
        x_.append(r[i][0])
        y_.append(r[i][1])
        z_.append(r[i][2])
        n.append(i)

    ax.plot(np.array(x_), np.array(y_), np.array(z_), c='b')
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


run('Chua')
plt.show()
