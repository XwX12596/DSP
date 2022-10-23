import numpy as np
from matplotlib import pyplot as plt

N = 10
t = np.arange(0, 20, 0.1)
func = np.cos(t) * np.e**((-0.1)*t)

fig1 = plt.figure()
plt.plot(t, func)
plt.show()

maxs = []
intv = [i for i in range(N)]

for i in range(1, N + 1):
    df = np.diff(func, i)
    df.resize(len(t))
    df /= (t[1] - t[0])**i
    nl = 1
    for j in range(1, i + 1):
        nl *= j
    maxs.append((nl/np.max(df))**(1/i))

fig2 = plt.figure()
plt.scatter(intv, maxs)
plt.show()