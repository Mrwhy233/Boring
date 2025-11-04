# 黑洞吸积系统的数学原理与可视化建模  


---

## 📜 目录
1. 系统概述  
2. 引力模型  
3. 能量与轨道稳定性  
4. 数值积分近似  
5. 亮度与光强分布  
6. 能量衰减  
7. 系统方程汇总  
8. 结论  

---

## 一、系统概述  
本文构建一个基于中心引力场的二维粒子系统，用以模拟黑洞吸积盘中粒子的动力学行为及其可视化表现。

---

## 二、引力模型  

在中心坐标为 $(x_c, y_c)$ 的黑洞引力场中，粒子 $i$ 的受力为：

$$
\vec{F}_i = -G \frac{M m_i}{r_i^2} \hat{r}_i
$$

其中：

$$
r_i = \sqrt{(x_i-x_c)^2 + (y_i-y_c)^2}
$$

拆分为分量形式：

$$
\begin{cases}
a_{x_i} = -G M \dfrac{(x_i - x_c)}{r_i^3}, \\[0.5em]
a_{y_i} = -G M \dfrac{(y_i - y_c)}{r_i^3}.
\end{cases}
$$

> **图示说明：**  
> 引力势能随距离变化递减的示意图（TikZ 形式）：
> ```tikz  
> \begin{tikzpicture}[scale=1.1]  
> \draw[->] (0,0)--(5,0) node[right]{$r$};  
> \draw[->] (0,-5)--(0,0.5) node[above]{$U(r)$};  
> \draw[smooth,domain=0.5:5,samples=100,blue,thick]  
> plot(\x,{-2*(1/\x)});  
> \node at (3.5,-0.7){\small $U(r)=-GM/r$};  
> \end{tikzpicture}  
> ```

---

## 三、能量与轨道稳定性  

势能与动能分别为：

$$
U(r) = - \frac{G M}{r}, \quad T = \frac{1}{2}v^2
$$

平衡条件：

$$
\dfrac{v^2}{r} = \dfrac{G M}{r^2} \Rightarrow v = \sqrt{\frac{G M}{r}}
$$

---

## 四、数值积分近似  

时间离散化欧拉法：

$$
\begin{cases}
\vec{v}_{t+1} = \vec{v}_t + \vec{a}_t \Delta t, \\[0.3em]
\vec{r}_{t+1} = \vec{r}_t + \vec{v}_{t+1} \Delta t.
\end{cases}
$$

极坐标形式近似：

$$
\begin{cases}
r_{t+1} = r_t - \delta r, \\[0.3em]
\theta_{t+1} = \theta_t + \sqrt{\dfrac{G M}{r_t^3}} \Delta t.
\end{cases}
$$

> **图示：吸积轨迹**  
> ```tikz  
> \begin{tikzpicture}[domain=0:6.28,samples=200,scale=0.8]  
> \draw[thick,->] (-4.2,0)--(4.2,0);  
> \draw[thick,->] (0,-4.2)--(0,4.2);  
> \foreach \r in {1,2,3}{  
>   \draw[cyan!30] (0,0) circle (\r);  
> }  
> \draw[thick,red,domain=0:6.28,smooth,samples=200,variable=\t]  
> plot ({3*cos(\t r)*(1-0.05*\t)}, {3*sin(\t r)*(1-0.05*\t)});  
> \node at (2.5,2.5){\small 吸积轨迹};  
> \end{tikzpicture}  
> ```

---

## 五、亮度与光强分布  

光强函数定义为：

$$
I(r) = I_0 e^{-r^2 / 2\sigma^2}
$$

> **图示：亮度分布函数**
> ```tikz  
> \begin{tikzpicture}[scale=1]  
> \draw[->] (0,0)--(4.5,0) node[right]{$r$};  
> \draw[->] (0,0)--(0,3) node[above]{$I(r)$};  
> \draw[thick,orange,domain=0:4,samples=100,smooth]  
> plot(\x,{3*exp(-\x*\x/4)});  
> \node at (2.3,1.4){\small $I(r)=I_0 e^{-r^2/2\sigma^2}$};  
> \end{tikzpicture}  
> ```

---

## 六、能量衰减  

由于吸积损耗能量：

$$
\frac{dE}{dt} = -\gamma E \Rightarrow E(t) = E_0 e^{-\gamma t}
$$

> **图示：能量随时间衰减**
> ```tikz  
> \begin{tikzpicture}[scale=1]  
> \draw[->] (0,0)--(5,0) node[right]{$t$};  
> \draw[->] (0,0)--(0,3) node[above]{$E(t)$};  
> \draw[thick,blue,domain=0:4.5,samples=100]  
> plot(\x,{3*exp(-0.5*\x)});  
> \node at (2.5,1){\small $E(t)=E_0 e^{-\gamma t}$};  
> \end{tikzpicture}  
> ```

---

## 七、系统方程汇总  

最终模型方程：

$$
\boxed{
\begin{aligned}
\ddot{\vec{r}} &= -G \frac{M}{r^3}\vec{r},\\
\dot{r} &= -k,\\
I(r,t) &= I_0 e^{-r^2/R^2} e^{-\lambda t}.
\end{aligned}
}
$$

离散更新公式：

$$
\vec{r}_{t+1} = \vec{r}_t + \dot{\vec{r}}_t \Delta t + \frac{1}{2}\vec{a}_t (\Delta t)^2
$$

---

## 八、结论  

本文通过中心势场的数学建模与函数示意，  
展示了黑洞吸积盘中粒子的引力运动、能量变化及亮度衰减机制。  

该模型结合了引力动力学和可视化参数化表达，可用于视觉特效、科研演示或教育展示等应用场景。

---

**完**