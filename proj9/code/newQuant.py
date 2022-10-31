from cv2 import imread, imwrite
import numpy as np

img_ = imread("../../pic/picForQuantization.jpg")
X, Y, _ = img_.shape
M = 10

cx = np.zeros(256)
cy = np.zeros(256)
cz = np.zeros(256)
intv = np.arange(0, 256, 1)

X, Y, _ = img_.shape

img = np.zeros((X, Y, 3))
for x in range(X):
    for y in range(Y):
        for z in range(3):
            img[x, y, z] = int(round(img_[x, y, z]/8))

ppp = np.fromfile("P.bin")
P_  = np.reshape(ppp, (256, 256, 256))
P = np.zeros((33, 33, 33))
for i in range(32):
    for j in range(32):
        for k in range(32):
            P[i, j, k] = np.average(P_[8*i:8*i + 8, 8*j:8*j + 8, 8*k:8*k + 8])

def updateB(Q, B):
    for i in range(32):
        for j in range(32):
            for k in range(32):
                dis = [(i - q[0])**2 + (j - q[1])**2 + (k - q[2])**2 for q in Q]
                B[i, j, k] = np.argmin(dis)

def updateQ(P, B):
    num = np.zeros((2**M, 3))
    den = np.zeros((2**M, 3))
    for i in range(32):
        for j in range(32):
            for k in range(32):
                num[int(B[i][j][k])] += P[i][j][k] * np.array([i, j, k])
                den[int(B[i][j][k])] += P[i][j][k]
    Q = num/den

def quantiz(img, B, Q):
    qimg = np.zeros((X, Y, 3))
    for x in range(X):
        for y in range(Y):
            qimg[x][y] = (Q[int(B[int(img[x][y][0]), int(img[x][y][1]), int(img[x][y][2])])])
    return qimg

def judge(img, qimg):
    err = 0
    for x in range(X):
        for y in range(Y):
            err += (img[x, y, 0] - qimg[x, y, 0])**2 + (img[x, y, 1] - qimg[x, y, 1])**2 + (img[x, y, 2] - qimg[x, y, 2])**2
    return err

Q = np.random.randint(0, 32, size=(2**M, 3))
B = np.zeros((33, 33, 33))

flag = 0
err = 1
for it in range(100):
    updateB(Q, B)
    updateQ(P, B)
qimg = quantiz(img, B, Q)
err = judge(img, qimg)
print(err)

imwrite("new" + str(M) + ".jpg", qimg*8)
imwrite("img.jpg", img)