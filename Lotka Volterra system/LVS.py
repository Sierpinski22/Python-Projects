import matplotlib.pyplot as plt

alpha, beta, gamma, delta = .1, .02, .3, .02
x, y = 10., 10.
dt = 1
iterations = 150

dx = lambda x_, y_: x_*(alpha - beta*y_) * dt
dy = lambda x_, y_: y_*(delta*x_ - gamma) * dt

xs, ys, ts = [], [], []

for i in range(iterations):
    xs.append(x)
    ys.append(y)
    ts.append(i)

    x += dx(x, y)
    y += dy(x, y)


plt.subplot(1, 2, 1)
plt.grid()
plt.plot(ts, xs, linestyle='dashdot')
plt.plot(ts, ys, linestyle='dotted')
plt.title('Equazioni di Lotka Volterra')
plt.legend(['Prede', 'Predatori'])
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(xs, ys)
plt.title('Equazioni nello spazio delle fasi')
plt.show()
