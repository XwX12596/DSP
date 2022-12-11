from scipy.io.wavfile import read, write
import numpy as np
from numpy.fft import fft, fftfreq, ifft
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 18})

def loadWAV(fname):
    fs, w = read(fname)
    sec = len(w)/fs
    wt = fft(w)
    freq = fftfreq(wt.size, d=1/fs)
    """Simple High-Pass Filter"""
    fl = 400
    wt[int(-fl * sec):] = 0
    wt[:int(fl * sec)] = 0
    """Simple Low-Pass Filter"""
    fh = 500
    cfq = wt.size/2
    wt[int(cfq - (fs/2 - fh) * sec):int(cfq + (fs/2 - fh) * sec)] = 0
    return fs, w, wt, freq

def countFlip(w, fs, gate, intv):
    N = len(w)
    M = N//intv
    count = 0
    L = np.zeros(M)
    if w[0] > 0:
        flag = 1
    else:
        flag = -1
    for n in range(M):
        for m in range(intv):
            index = int(intv * n + m)
            if flag * w[index] > -gate:
                pass
            else:
                count += 1
                flag = w[index] / np.abs(w[index])
        L[n] = count/2
        count = 0
    return intv/fs, L

fs, w, wt, freq = loadWAV("/home/xmh/DSP/projF/code/mosquito-cut.wav")
iw = np.array(np.real(ifft(wt)), dtype=np.int16)
write('/home/xmh/DSP/projF/code/mosquito-out.wav', fs, iw)

dt, L = countFlip(iw, fs, gate=300, intv=400)
F = L/(dt)
gapTime = np.arange(0, 2, dt)

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(311)
ax.set_title("Spectrum")
ax.plot(freq, np.real(wt))

ax = fig.add_subplot(312)
ax.set_title("Wave Form")
ax.plot(iw)

ax = fig.add_subplot(313)
ax.set_title("Frequency vs Time")
ax.plot(gapTime, F)

plt.show()