from cv2 import imread, imwrite
import numpy as np

img = imread("../../pic/picForQuantization.jpg")
X, Y, _ = img.shape
M = 3
cx = np.zeros(256)
cy = np.zeros(256)
cz = np.zeros(256)
for i in range(X):
    for j in range(Y):
        x, y, z = img[i, j]
        cx[x] += 1
        cy[y] += 1
        cz[z] += 1
px = cx / (X * Y)
py = cy / (X * Y)
pz = cz / (X * Y)

data = np.zeros((256, 256, 256))


for i in range(32):
    print(i)
    for j in range(32):
        for k in range(32):
            data[i][j][k] = px[i] * py[j] * pz[k]
data.tofile("P.bin")

ppp = np.fromfile("P.bin")
pp  = np.reshape(ppp, (256, 256, 256))
print(pp)