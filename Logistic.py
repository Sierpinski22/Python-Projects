import matplotlib.pyplot as plt
import numpy as np
from math import sin

rs = np.linspace(0, 4, 2000)
xs, ys = [], []
split_sites = []
n0 = 0.5
start, end = 500, 50


approx = lambda x: float(f"{x:.3f}")
f = lambda r, x: r*x*(1-x)
g = lambda r, x: r*sin(x)


for r in rs:
    n = n0
    ry = []
    for i in range(start + end):
        n = f(r, n)
        if i > start and not approx(n) in ry:
            ry.append(approx(n))
            xs.append(r)
    ys = ys + ry
    
    

plt.scatter(xs, ys, s=0.1)
# plt.axis('scaled')
plt.tight_layout()
plt.show()            
            
    
    
