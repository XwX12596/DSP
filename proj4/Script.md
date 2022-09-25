![image-20220925123554162](https://raw.githubusercontent.com/XwX12596/image/main/img/image-20220925123554162.png)

# Starlink

This is a video about how the satellite communicate with the antenna on earth, explaining the 3 questions below.

- How electrical signals become electromagnetic waves;
- How to realize automatic antenna tracking; 
- How to convert binary data into electrical signal 

电信号如何变为电磁波；如何实现天线自动跟踪；如何将二进制转变为便于传输的电信号

## Summary

### transmit and receive

为了将电信号通过无线信道传输至位于外太空的卫星上，我们需要将其转变为电磁波。在天线内有相距很近的一组馈电线和金属板，馈电线上会快速地流过电子，而在电子流动的过程中会产生变化的电场，从而使得金属板中的电子也开始几乎同时的振荡运动。通过电磁场知识我们知道，变化的电场会产生磁场，从而激发出电磁波，而在视频中这样的片状的天线会使得电磁场向四周传播。

方向性不好的单独天线不是我们想要的，所以在地面天线中有着1280个天线。由于电磁波传输时相位会随着空间变化，所以在空间中某些特定的位置会产生同相叠加和反相相消的情况。这就是电磁场束是如何产生的。

In order to transmit electrical signals to satellites through wireless channels, we need to convert them into electromagnetic waves. There is a feedline and a metal plate close to each other in the antenna. The electrons will flow quickly (13Ghz) on the feedline, and the changing electric field will be generated in the process of electron flow. We know that the changing electric field will produce magnetic field, which will finally generate electromagnetic waves. A slice antenna like this will make the electromagnetic wave propagates outwards in a balloon shape.

The single antenna with poor directivity is not what we want, so there are 1280 antennas in the antenna array. Because the phase of electromagnetic wave will change with the position when it is transmitted, there are always constructive interference and destructive interference happening at the same time, and while the little antennas get more, the zone of constructive interference becomes small. Therefore, the directivity gets better for the antenna array. This is how the beam of electromagnetic is generated.

### phase shift

由于电机的不可靠性，使用电机控制天线朝向是不可行的。我们可以通过每个天线发射时的信号相位以改变the zone of constructive interference，从而改变电磁波的朝向。

Due to the unreliability of the motor, it is not unrealistic to use the motor to control the antenna orientation. But, we can change the zone of constructive interference by changing the phase of signal when each antenna emits, so as to change the direction of the beam of electromagnetic wave.

### 64QAM

在幅度-相位的极坐标平面上，选取64个不同的点作为信号的载波，并给每一个点编码，表示不同的六位二进制，通过发送和接受这样的高频波形，我们可以通过电磁波传输我们的二进制数据。

QAM stands for Quadrature Amplitude Modulation. 64QAM means, on the polar coordinate plane of amplitude-phase, 64 different points are selected to stand for 64 different signals, and each point is encoded with six bit binary. By sending and receiving such high-frequency waves, the antenna can transmit the binary data to the satellites through electromagnetic waves.

## Further thoughts

这些人造卫星组成星链（ Starlink），这个项目的目的是从太空向地球上偏远地区提供高速互联网服务。

星链卫星也给天文学家带来新问题——在日出和日落时，它们可以被肉眼看到，卫星外翼反射太阳，闪闪发光，而这可能导致望远镜图像上出现条纹，模糊恒星和行星的视野。

The customer's monthly fee is \$99 (UK £ 89 per month). The cost of dish antennas and routers required to connect satellites is \$549 (£ 529).

Starlink is a satellite internet constellation operated by SpaceX, providing satellite Internet access coverage to 40 countries. It also aims for global mobile phone service after 2023.

 It looks like a  beautiful vision for the future, everyone on this planet can access the high-speed network. But the price is pretty expensive. The customer's monthly fee is \$99. The cost of dish antennas and routers required to connect satellites is \$549. Whether that vision could achieve success needs to be questioned.

Moreover, this project has brought more problems. Astronomers claim that the number of visible satellites will outnumber visible stars and that their brightness in both optical and radio wavelengths will severely impact scientific observations. 

# Proposal

## Why I want to do?

### Utilization of idle goods

I bought a Raspberry Pi 4B for fun when I was a freshman, but I don't really have the motivation to use this little thing as something functional. All I did was running a Minecraft server on this thing and broadcast the port where the server ran, in order to play with my friends in other universities.

It costs a lot these days to buy a Raspberry Pi, so I want to make it useful again!

### Inspiration From Others

But after I read the proposal of Su Rundong (*He again*), what came into my mind was to let the Raspberry Pi work as the hardware to realize the functions he mentioned in his proposal. Moreover, I want to use this thing as my remote monitor camera so that I can watch my seat and prevent someone from sitting in my chair! (Thankfully, in *LZU*, I have nice roommates who don't mess others' things up)

## What I want to do?

### The least things I will do

Raspberry Pi is a rich-functional micro computer, and it can drive camera to record videos or take a photo. What I should do in this project is to 

- Making a web camera watching my seat in dormitory
- Using python to control the camera to take a photo

> mjpg-streamer is a command line application that copies JPEG frames from one or more input plugins to multiple output plugins. It can be used to stream JPEG files over an IP-based network from a webcam to various types of viewers such as Chrome, VLC, and other software capable of receiving MJPG streams.

To achieve the first aim in the last subsection, I will try to use mjpg-streamer[x] to stream JPEG files over an IP-based network. This is a function already implemented by others, so I will follow the instructions in this repository.

Then, the second, it is easy if I use the python package of picamera.

### Other things I will try to do

A web page that can send http request what tell the camera to take a picture and return with a picture. Inspired by this blog.