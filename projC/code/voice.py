import numpy as np
from numpy.fft import fft, fftfreq, ifft
from matplotlib import pyplot as plt
from scipy.io.wavfile import write, read

"""Read Record File"""
fs, x = read('song.wav')
x = x[:, 0]
sec = x.size/fs
t = np.arange(0, sec, 1/fs)

"""Do FFT"""
xt = fft(x)
ap = np.abs(xt)
phase = np.angle(xt)
freq = fftfreq(x.size, d=(1/fs))

"""Simple High-Pass Filter"""
fc = 1100
ap[int(-fc * sec):] = 0
ap[:int(fc * sec)] = 0
"""Simple Low-Pass Filter"""
# cfq = xt.size/2
# ap[int(cfq - (fs/2 - 2000) * seconds):int(cfq + (fs/2 - 2000) * seconds)] = 0

"""Do IFFT And Output"""
xt_f = ap * np.exp(1j * phase)
ix = np.real(ifft(xt_f))
write('out.wav', fs, ix)

"""Draw Wave and Spectrum"""
ax0 = plt.subplot(311)
ax0.set_title("Original Wave")
ax0.plot(t, x)

ax1 = plt.subplot(312) 
ax1.set_title("Wave Through Filter")
ax1.plot(t, ix)

ax2 = plt.subplot(313)
ax2.set_title("Spectrum of Wave Through Filter")
ax2.plot(freq, ap)

plt.show()
