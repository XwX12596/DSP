import numpy as np
from numpy.fft import fft, fftfreq
from matplotlib import pyplot as plt
from scipy.io.wavfile import read

"""Read Record File"""
fs, x = read('./projE/code/2.wav')
x = x[:, 0]
sec = x.size/fs
t = np.arange(0, sec, 1/fs)

"""Do FFT"""
xt = fft(x)
ap = np.abs(xt)
phase = np.angle(xt)
freq = fftfreq(x.size, d=(1/fs))

"""Draw Wave and Spectrum"""
# ax0 = plt.subplot(311)
# ax0.set_title("Original Wave")
# ax0.plot(t, x)

plt.figure()
plt.title('Spectrum of Man')
plt.plot(freq, np.abs(xt))

plt.show()
