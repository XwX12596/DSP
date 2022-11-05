$$
x_a(t) = 2f_s T \sum_{n = -\infty}^{\infty} x(nT) ~ \mathrm{sinc} \left[ 2f_s(t - nT) \right]

\\

\widetilde{x}_a(f) = \int_{- \infty}^{\infty} \; x_a(t) \, e^{-j 2\pi n f} \; \mathrm{d}t = \mathcal{F} \left[ x_a(t) \right]
\\
x_s(t) = \sum_{n} \; x(nT) \, \delta(t - nT) = x_a(t) * s(t) =  x_a(t) * \sum_{n} \left[ \delta(t- nT) \right]
\\
	\widetilde{x}_s(f) = \int_{- \infty}^{\infty} \sum_{n} \; \left[  x(nT) \, \delta(t - nT) \right] \; e^{-j 2\pi ft}\; \mathrm{d} t \\
	= \int_{- \infty}^{\infty} \sum_{n} \; \left[  x(nT)  \, e^{-j 2\pi f nT} \, \delta(t - nT) \right] \; \mathrm{d} t \\
	= \sum_{n} \; x(nT)  \, e^{-j 2\pi f nT} \\ 
	=\sum_{n} \; x(n)  \, e^{-j 2\pi n f'}
$$

# Videos

## Log Brain

In this video we will explore log-normal distribution what it is and how it supports the computations carried out by networks of neurons 

- arises from summation of independent random variables
- Gaussian distribution
- bell curve
- central limited theorem
- summation of samples is always normal distribution

- log
  - multiply to sum

- logarithm of a product of many random variables is normally distributed
- synaptic weights are log normally distributed
- most of synapses are quite weak
- shape of the distribution can tell us some insights into the underlying mechanisms giving rise to the distribution 

这个视频首先介绍了一个叫做LND的类似于正态分布的概率分布。由中心极限定理，我们知道独立变量的大量样本和应该服从于正态分布。lnd则是独立变量的大量样本的乘积会服从的分布。

## Nuclear Energy

- why wind lose
- world economics
  - cost of construction
  - the fuel cost
  - construction time
- return on investment
- safety issues
- risk 
  - businessman
  - politician

- levelized cost of electricity or LCOE
- the cost a power plant will need to charge for a unit of energy in order to recoup its cost over the course of its lifetime
- wind and Natural Gas are both cheaper
- smaller, cheaper and safer

## DSP Platforms

1. 信号处理--如数字滤波、自适应滤波、快速傅里叶变换、相关运算、频谱分析、卷积等。
   1. microphone 
2. 通信--如调制解调器、自适应均衡、数据加密、数据压缩、回坡抵消、多路复用、传真、扩频通信、纠错编码、波形产生等。
   1. modem
3. 语音--如语音编码、语音合成、语音识别、语音增强、说话人辨认、说话人确认、语音邮件、语音储存等。
   1. smartphone
4. codec
   1. earphone
5. 图像/图形--如二维和三维图形处理、图像压缩与传输、图像增强、动画、机器人视觉等。 
6. 军事--如保密通信、雷达处理、声纳处理、导航等。
7. 仪器仪表--如频谱分析、函数发生、锁相环、地震处理等。
8. 自动控制--如引擎控制、深空、自动驾驶、机器人控制、磁盘控制。
   1. car
9. 医疗--如助听、超声设备、诊断工具、病人监护等。

- computer
- smart phone
- microphone and earphone
- car
- Electrocardiogram

