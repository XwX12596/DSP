import numpy as np
from sympy import sinc
from matplotlib import pyplot as plt

n = np.arange(0.7, 5, 0.01)
y = (np.sinc(n))**2
line = [0.01 for x in n]

fig = plt.figure()
plt.plot(n, y, linewidth=0.8, label="y = [sinc(n)]^2")
plt.plot(n, line, linewidth=0.8, label="y = 0.01")
plt.legend()
plt.show()