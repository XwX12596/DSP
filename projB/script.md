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

