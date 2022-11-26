import numpy as np

def createMat(x):
    N = len(x)
    mat = np.zeros([N, N])
    for i in range(N):
        tmp = np.roll(x, i)
        mat[i] = tmp
    return np.transpose(mat)

def regulateVector(x, h):
    lx = len(x)
    lh = len(h)
    if (lx > lh):
        h = np.concatenate((h, np.zeros(lx -lh)))
    elif (lx < lh):
        x = np.concatenate((x, np.zeros(lh - lx)))
    return x, h

# x, h generation
N = 500
M = 400
x = np.random.randn(N)
h = np.random.randn(M)
x, h = regulateVector(x, h)

# create the H matrix and calculate the reverse of it
H = createMat(h)
H_r = np.linalg.inv(H)

# calculate the circular convolution and do the reverse work
y = np.matmul(H, x)
ix = np.matmul(H_r, y)

# test the algorithm
print(np.mean(x - ix))
