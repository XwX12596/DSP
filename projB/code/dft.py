import numpy as np
import time

def dft(x):
    N = len(x)
    xt = np.matmul(
            np.exp(-1j * 2 * np.pi * np.matmul(np.arange(N).reshape(N, 1), np.arange(N).reshape(1, N)/N)),
            x
            )
    return xt

def idft(xt):
    return np.conj(dft(np.conj(xt))) / N

N = 1024
x = np.random.rand(N)
st = time.time()
y = dft(x)
x1 = idft(y)
et = time.time()
err = x1 - x
print("Error\tis\t", np.sum(np.absolute(err)/N), "\nEnd\tin\t", et - st)
