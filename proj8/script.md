## Comparison

### My Understanding of the Wan Sampling Method

#### Taylor's theorem

$$
f(x) = \sum_{i = 0}^{n} ~ \frac{f^{(i)}(x_0)}{i!} ~ (x - x_0)^i + R_n(x)
$$

Applying to our signal $x(t)$, we can make $t_0 = nT, n = 2$ here and get
$$
x(t) = x(nT) + x'(nT)(x - nT) + \frac{x''(t_0)}{2}(x - t_0)^2 + R_2(t)
$$
What exactly we get after sampling is only the values of $x(nT)$, but It is easy to do derivation. Therefore, using simple circuit, we know the values of $x'(nT),\,x''(nT),\,x'''(nT),\,\cdots$

So, the reconstructed signal $\hat{x}(t)$ can be expressed as
$$
\hat{x}(t) = x(nT) + x'(nT)(x - nT) + R_1(t)
$$
but also as
$$
\hat{x}(t) = x(nT) + R_0(t)
$$
The difference of the above two lies on the error of the reconstructed signal. It time to do the quantitative analysis, we assume that
$$
|\hat{x}(t) - x(t)| < \epsilon\\
|x^{(n)}(t)| < \eta_n
$$






