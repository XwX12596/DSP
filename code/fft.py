# 画着玩儿的
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))

t = np.arange(-0.5, 0.5, 0.001)
y = np.cosh(t)
sp = np.fft.fft(y)
freq = np.fft.fftfreq(t.shape[-1])
plt.subplot(121)
plt.plot(freq, sp)
plt.subplot(122)
plt.plot(t, y)
plt.show()