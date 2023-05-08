import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))


def logistic(x, r, n):
    i = (4 - 2.4) / n
    r_list = []
    x_list = []
    for _ in range(n):
        x_list.append(x)
        r_list.append(r)
        x = r * x * (1 - x)
        r += i
    return x_list, r_list


xl, rl = logistic(0.1, 2.4, 10000)
plt.scatter(rl, xl, c='b', s=10)
plt.show()
