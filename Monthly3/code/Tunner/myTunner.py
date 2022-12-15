import pyaudio
import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt
from time import sleep

FORMAT = pyaudio.paInt16 # 位深，16位整型表示一个采样点的值大小，
CHANNELS = 1 # 声道数目，使用单声道
# SAMPLE_RATE = 44100  # 采样率 (Hz)，每秒收集的时刻点的数目
SAMPLE_RATE = 3000  # 采样率 (Hz)，每秒收集的时刻点的数目
SAMPLE_INTERVAL = 1/SAMPLE_RATE # 采样间隔 (s), 相邻两次采样间的时间间隔
END = False # 结束标志
T = 2 # 一小段音频持续的时间 (s)
RES = 1./T # 调音器的分辨率 (Hz)，傅立叶变换后两个相邻频率点之间的频率间隔
CHUNK = T*SAMPLE_RATE # 一小段音频的采样点的数目

lowcut, highcut = 75.0, 1250.0 # 带通滤波器保留的频率范围
freq_range = [75, 350] # 吉他空弦的频率范围
freq = np.fft.rfftfreq(CHUNK, d=SAMPLE_INTERVAL) # 傅立叶变换后的横坐标
mask = (freq < freq_range[0]) + (freq > freq_range[1]) # 通过它得到吉他空弦的频率范围外的范围

# Notes_guitar = ['E2','A2','D3','G3','B3','E4']
# 六条弦对应的音符和频率(Hz)
Notes_guitar = ['E2','A2','D3','G3','B3','E4']
freq_guitar = np.array([82.4069, 110.0000, 146.8324,
                        195.9977, 246.9417, 329.6276])

# 初始化麦克风输入
p = pyaudio.PyAudio()
in_stream = p.open(format=FORMAT, channels=CHANNELS, rate=SAMPLE_RATE,\
                input=True, frames_per_buffer=CHUNK)

for i in range(10):
    # 读取十六进制的数据到缓冲区;
    # False: 用来忽略 IOError exception    
    buffer = in_stream.read(CHUNK, exception_on_overflow = False)
    # 转化缓冲区的数据为16位的整型数据
    y = np.frombuffer(buffer, dtype = np.int16)
    # 对时域信号做傅立叶变换, 因为是输入是实数，我们使用rfft, 没有用fft。
    Y = np.fft.rfft(y)/CHUNK
    # 得到幅度谱
    Y_a = np.abs(Y)

    # 带通滤波器
    sos = signal.butter(10, [lowcut, highcut], 'bp', fs=SAMPLE_RATE, output='sos')
    filtered = signal.sosfilt(sos, y)
    FILTERED = np.fft.rfft(filtered)/CHUNK
    FILTERED_a = np.abs(FILTERED)
    
    S_a = FILTERED_a
    S_a[mask] = 0 # 强行让吉他音频范围以外的频率幅值归零
    freq_max = np.argmax(S_a)
    main_freq = freq[freq_max] # 找到幅值最大的频率
    # S_a[freq_max] = 0
    # freq_max = np.argmax(S_a)
    # second_freq = freq[freq_max]
    # base_freq = main_freq - second_freq
    # if (np.abs(main_freq - second_freq) > 75):
    #     main_freq = np.abs(base_freq)

    NoString = 0
    for i in range(6):
        if main_freq > freq_guitar[i]:
            NoString += 1
        else:
            break
    if NoString == 0:
        message = f"get {main_freq}Hz, lower than string 6 ({freq_guitar[NoString]}Hz, {Notes_guitar[NoString]})"
    elif NoString == 6:
        message = f"get {main_freq}Hz, higher than string 1 ({freq_guitar[NoString]}Hz, {Notes_guitar[NoString]})"
    else:
        message = f"get {main_freq}Hz, between string {NoString} ({freq_guitar[NoString-1]}Hz, {Notes_guitar[NoString-1]}) and string {NoString-1} ({freq_guitar[NoString]}Hz, {Notes_guitar[NoString]})"
    print(message)
    sleep(1)