import numpy as np
import time
from matplotlib import pyplot as plt

def dft(x):
    N = len(x)
    xt = np.matmul(
        np.exp(-1j * 2 * np.pi * np.matmul(np.arange(N).reshape(N, 1), np.arange(N).reshape(1, N)/N)),
        x
        )
    return xt

def idft(xt):
    return np.conj(dft(np.conj(xt))) / N

def fft(x):
    N = len(x)
    if N == 1:
        return x
    else:
        x0, x1 = x[::2] , x[1::2]
        xt0 = fft(x0)
        xt1 = fft(x1)
        tmp = np.exp(-1j*2*np.pi*np.arange(N/2)/N) * xt1
        xt = np.concatenate([xt0 + tmp, xt0 - tmp])
    return xt

def ifft(xt):
    return np.conj(fft(np.conj(xt))) / N

def test(m):
    x = np.random.rand(2**m)

    # MyDFT
    st1 = time.time()
    y1 = dft(x)
    et1 = time.time()
    # xx1 = idft(y1)

    # MyFFT
    st2 = time.time()
    y2 = fft(x)
    et2 = time.time()
    # xx2 = idft(y2)

    # LibFFT
    st3 = time.time()
    y3 = np.fft.fft(x)
    et3 = time.time()
    # xx3 = idft(y3)

    # err1 = xx1 - x
    # err2 = xx2 - x
    # err3 = xx3 - x

    t1 = et1 - st1
    t2 = et2 - st2
    t3 = et3 - st3
    
    return t1, t2, t3


M = [i for i in range(6, 13)]
T1 = []
T2 = []
T3 = []
for m in M:
    tmp1, tmp2, tmp3 = test(m)
    T1.append(tmp1)
    T2.append(tmp2)
    T3.append(tmp3)

fig = plt.figure()
plt.xlabel('LogN')
plt.ylabel('Time')
plt.subplot(211)
plt.scatter(M, T1, label='MyDFT', c='r')
plt.scatter(M, T2, label='MyFFT', c='g')
plt.subplot(212)
plt.scatter(M, T2, c='g')
plt.scatter(M, T3, label='LibFFT', c='b')
fig.legend()
plt.show()


# print("MyDFT:\n\tError\tis\t", np.sum(np.absolute(err1)/N), "\n\tEnd\tin\t", et1 - st1)
# print("MyFFT:\n\tError\tis\t", np.sum(np.absolute(err2)/N), "\n\tEnd\tin\t", et2 - st2)
# print("LibFFT:\n\tError\tis\t", np.sum(np.absolute(err3)/N), "\n\tEnd\tin\t", et3 - st3)
