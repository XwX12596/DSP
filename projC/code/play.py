import numpy as np
from scipy.io.wavfile import write
f = 130
fs = 96000 # sampling 
length = 2 # seconds it lasts
x = np.arange(fs*length)
y = np.sin(2 * np.pi * f / fs * x) # generate a sine wave
for i in range(2, 9):
    y += np.sin(2 * np.pi * i * f / fs * x)
write('sin.wav', fs, y)