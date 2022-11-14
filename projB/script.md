$$
\widetilde{x}(k) = \sum_{n = 0}^{N - 1} x(n) \, w^{kn}, \quad k = 0, 1, \cdots, N - 1\\ 
= \begin{bmatrix}
 1 & 1 & 1 & \cdots & 1 \\
 1 & w^1 & w^2 & \cdots & w^{N - 1} \\
 1 & w^2 & w^4 & \cdots & w^{2(N - 1)}\\ 
 \vdots & \vdots & \vdots& \ddots & \vdots\\
 1 & w^{2(N - 1)} & w^{4(N - 1)} & \cdots & w^{(N - 1)^2}
 \end{bmatrix}
 \begin{bmatrix}
x(0) \\
x(1) \\
x(2) \\
\vdots \\
x(N - 1)
 \end{bmatrix} \\
 A = \begin{bmatrix}
w^{(i - 1)(j - 1)}
 \end{bmatrix} \\
$$

$$
w^a \cdot (w^b)^* = e^{-j \frac{2 \pi}{N} (a -b)} =  w^{\lambda}
$$
$$
\lambda = i - j \ne 0 \\
\alpha_i \cdot \alpha_j^H = \begin{bmatrix}
1 & w^a & w^{2i} & w^{3i} & \cdots & w^{(N - 1)i}
 \end{bmatrix}
 \cdot
 \begin{bmatrix}
1 \\ w^b \\ w^{2j} \\ w^{3j} \\ \vdots \\ w^{(N - 1)j}
 \end{bmatrix}\\
 
 = 1 + w^{\lambda} + w^{2 \lambda} + \cdots + w^{(N - 1) \lambda} \\
 
 = \frac{1 - w^{N \lambda}}{1 - w^{\lambda}}\\
 
 = \frac{1 - e^{j 2\pi\lambda}}{1 - e^{-j\frac{2\pi}{N}\lambda}}\\
 = 0
 \\
 so \\
 \alpha_i \cdot \alpha_i^H = N
$$

$$
A = 
\begin{bmatrix}
\alpha_0 \\ \alpha_1 \\ \alpha_2 \\ \vdots \\ \alpha_{N - 1}
 \end{bmatrix} \\
 A^H = 
 \begin{bmatrix}
\alpha_0^H & \alpha_1^H & \alpha_2^H & \cdots & \alpha_{N - 1}^H
 \end{bmatrix}
\\
A \cdot A^H = N \cdot 
\begin{bmatrix}
\alpha_i \cdot \alpha_j^H
 \end{bmatrix}
 = N \cdot I
 \\
 A^{-1} = \frac1N A^H
$$

$$
\tilde{x}(f) = \sum x(\frac n {f_s}) e^{-j 2 \pi \frac{n}{f_s} \cdot f} \\ 
\widetilde{x}(f) = \widetilde{x}_a(f) * \left[ f_s \sum_n \delta(f - nf_s) \right] \\
=f_s \cdot \widetilde{x}_a(f - nf_s) \\
= f_s \cdot \widetilde{x}_a[f_s\frac kN - f_s \cdot n] \\ 
= f_s \cdot \widetilde{x}_a[f_s(\frac kN - n)]
$$

Atacame in South America

- 鸬鹚 5万
- 陆地尘土肥沃大海
- 一场雨使沙漠焕发生机
- 干草甸 
- If anything happened to the ants or to the gentian, the alcon blue would become extinct
- protect the precious space that grasslands and deserts provide, and the animals will bounce back

从这次的视频中我们看到，生态系统是如何连系在一起的，从沙漠中的生物讲到草原上的生物，不管是鸬鹚还是野牛，不管是猎豹还是老虎，都同处于一个地球。就像A，ants，gentian这三者之间的关系一样，我们人类和动物之间也应该是相互依存的关系，我们人类当然也有保护这个地球的义务和责任，所以不论是盗猎，无尽扩张的农业，还是其他破坏野生动物栖息地的行为都应该得到控制，这确实是我们的责任。

我们从前学过地球上的水循环，水从地面上蒸发，被风带到世界各处，再通过雨水的形式降落到地球的各个角落，这样的空中水循环是依赖大气与其流动，也就是风来进行的，而在视频中特意提到，沙漠中的尘土通过风被传送到海上的提供养分这一细节。我认为这就是这部纪录片我很喜欢的原因

这周，我们领略了沙漠和草原的风光。然后，在第二节中，我从DFT推导出了IDFT的公式。在第三节中，我通过改写DTFT的公式，找到了能在DFT中找到模拟频谱分量的方式。最后，我统合了课堂上展示的代码，完成了这一部分比较代码运行速度的任务，此外，通过使用Matplotlib，我画了一张图用来比较不同代码实现DFT的运行速度。
