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

- 



# Videos

- military robotics technology
- Boston Dynamics
- 高抗干扰性，军事用途
- 高稳定性
- how the military can benefit form robotics and all the ancillary
- make soldiers obsolete
- The goal was to improve movement and rough terrain capabilities in robots
- keep balance
- 适应不同的环境
- convenience 
- fully automated industrial robots that is currently used for efficient warehouse operations
- Atlas bipedal humanoid robot designed for a variety of applications and tasks
- act as a force multiplier
- allow humans to step back and allow the robot to do its thing
- ethical programming 
- be honest and aware of their responsibility to protect human rights
- 特技动作
- synergy between mechanical parts and an ai-powered programmed brain that's why Atlas can potentially make soldiers totally obsolete in the future.
- automatic robots
  - need input in the control
- automated robots
  - carry out commands in a chronological and pre-programmed manner
  - programmed to identify enemy forces in a specific manner
- autonomous robot
  - be programmed to be able to make choices between different options even though they are still constrained by their programming they can exercise independent judgement using high-level artificial intelligence
  - eventually make soldiers obsolete
- advantages
  - 没有人员伤亡
  - 严酷的环境
- disadvantage
  - fully reliable on human programming and vulnerable to hacking
  - AI out of control
  - people who have access to the technology oppress those who don't
  - moral issues

## Bone

- bone density had decreased as much as 20% in some cases
- Exercise and physical activity plays a huge role in maintaining and even increasing bone density
- bone will also adapt by changing its shape and its internal architecture
- adaptations and changes
- compact bone tissue
-  spongy bone tissure
- deep to this compact bone
- not random architecture
- push and pull 
- both compressive and tensile
- 有机（胶原蛋白），无机（钙）
- consistently stimulate the bone tissue in order to gain and maintain these on these long-term adaptations
- running jumping pushing
- biceps curl
- bend the bone 
- those program would actually do a pretty good job at stimulating the bones in both ways
- exercise choosing
- lift a lot of weights 
- formation and resorption

# USB Hubs

- transmit: ==time division multiplexing==
- virtual address
  - the ==upstream port== can access all the ==downstream ports==
  - downstream ports cannot access any other ports except the upstream port
