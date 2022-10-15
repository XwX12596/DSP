from matplotlib import pyplot as plt
import numpy as np

inc = [(-1.3, -0.4, 180),
(-4, 0.1, 180),
(-1.25, 0.4, 180),
(0.3, 4.25, 180),
(-0.75, 6.5, 156),
(1, 2, 135),
(-4.75, 0.5, 144),
(-2.45, -4, 135),
(-6.5, 8.75, 104),
(1, 0, 228),
(0.25, 0.5, 264),
(1.5, -0.5, 264),
(7, 0, 270),
(3.75, 0, 270),
(-2.25, 12.25, 252),
(0.5, 2, 280),
(-1.25, -0.25, 264),
(-5.75, 1, 286),
(4.75, 0.75, 264),
(-1, -2, 84),
(8.5, -12.75, 75)]

point = [0, 0, 0]
x = []
y = []
z = []

for p in inc:
    point[0] = point[0] + p[0]
    point[1] = point[1] + p[1]
    point[2] = np.sqrt(p[2]) * 0.85
    x.append(point[0])
    y.append(point[1])
    z.append(point[2])

plt.figure()
ax = plt.axes(projection='3d')
ax.plot(x, y, z)
plt.show()