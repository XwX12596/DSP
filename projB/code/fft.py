import numpy as np
import time
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

N = 2**10
x = np.random.rand(N) + 1j * np.random.rand(N)
st = time.time()
y = fft(x)
x1 = ifft(y)
et = time.time()
err = x1 - x
print("Error\tis\t", np.sum(np.absolute(err)/N), "\nEnd\tin\t", et - st)
