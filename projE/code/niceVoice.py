import numpy as np
from scipy.io.wavfile import write
f = 440
fs = 96000 # sampling 
length = 2 # seconds it lasts
x = np.arange(fs*length)
y = np.sin(2 * np.pi * f / fs * x) # generate a sine wave

ctrl = [0, 1, 100, 2, 5, 0.1, 0.01]
for i in range(2, 7):
    y += ctrl[i] * np.sin(2 * np.pi * i * f / fs * x)
write('./projE/code/sin.wav', fs, y)