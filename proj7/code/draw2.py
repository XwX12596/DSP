import numpy as np
from matplotlib import pyplot as plt

x = [0, 1, 0.5, 0.5]
xx = [0.5, 0.25, 0.75, 0.5]
y = [0, 0, 0.7, 0.35]
yy = [0.35, 0.175, 0.175, 0.525]
z = [0, 0, 0, 0.6]
zz = [0.6, 0.3, 0.3, 0.3]

plt.figure()
ax = plt.axes(projection = '3d')

for i in range(4):
    for j in range(4):
        ax.scatter((x[i]),(y[i]),(z[i]),color='r')
        ax.plot((x[i],x[j]),(y[i],y[j]),(z[i],z[j]),color='b', linewidth=1)
for i in range(4):
    for j in range(4):
        ax.scatter((xx[i]),(yy[i]),(zz[i]),color='r')
        ax.plot((xx[i],xx[j]),(yy[i],yy[j]),(zz[i],zz[j]),color='b',linewidth=1)
ax.scatter(0.5, 0.35, 0,color='r')
ax.scatter(0.5, 0.35, 0.3, color='r')
ax.plot((0.5,0.5,0.5),(0.35,0.35,0.35),(0,0.3,0.6))

plt.show()
