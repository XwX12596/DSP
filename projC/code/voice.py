import numpy as np
from numpy.fft import fft, fftfreq, ifft
from matplotlib import pyplot as plt
from scipy.io.wavfile import write, read

"""Read Record File"""
fs, x = read('short.wav')
x = x[:, 0]
sec = x.size/fs
t = np.arange(0, sec, 1/fs)

"""Do FFT"""
xt = fft(x)
ap = np.abs(xt)
phase = np.angle(xt)
freq = fftfreq(x.size, d=(1/fs))

"""Simple High-Pass Filter"""
# fl = 750
# xt[int(-fl * sec):] = 0
# xt[:int(fl * sec)] = 0
"""Simple Low-Pass Filter"""
# fh = 810
# cfq = xt.size/2
# xt[int(cfq - (fs/2 - fh) * sec):int(cfq + (fs/2 - fh) * sec)] = 0

"""Do IFFT And Output"""
ix = np.array(np.real(ifft(xt)), dtype=np.int16)
write('out-voice.wav', fs, ix)

"""Draw Wave and Spectrum"""
ax0 = plt.subplot(311)
ax0.set_title("Original Wave")
ax0.plot(t, x)

ax1 = plt.subplot(312) 
ax1.set_title("Wave Through Filter")
ax1.plot(t, ix)

ax2 = plt.subplot(313)
ax2.set_title("Spectrum of Wave Through Filter")
ax2.plot(freq, np.abs(xt))

plt.show()
