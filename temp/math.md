
# 复数与复变函数

## 复平面

复数z的幅角记为 θ=argz(-π，π]

**欧拉公式**： $e^{±iθ}$=cosθ±isinθ

常用的两条共轭复数性质：
	1、z $\bar{z}$=$(Rez)^2$+$(Imz)^2$
	2、z+$\bar{z}$=2Rez, z-$\bar{z}$=2iImz.

复数的两点式直线方程：z=$z_1$+t($z_2$-$z_1$)

$\color{#FF0000}{乘方公式：}$
	<font size=4>$
z^n=|z|^n e^{inθ}=|z|^n（cosnθ+isinnθ）$</font>

$\color{#FF0000}{开方公式：}$
	<font size=4>$
ω= \sqrt[n]z =|z|^{1\over n}(cos{θ+2kπ \over n}+isin{θ+2kπ \over n})=|z|^{1\over n}e^{i{θ+2kπ \over n}} $       $ {(k=0,1,2,……,n-1)}$</font>

## 复变函数

极限存在的充分必要条件:

$ 
\lim \limits_{z\rightarrow z_0}f(z)=A $的充分必要条件是
$\lim \limits_{(x,y)\rightarrow (x_0,y_0)}u(x,y)=u_0   ,  \lim \limits_{(x,y)\rightarrow (x_0,y_0)}v(x,y)=v_0 $

```
Tip:求极限的时候，可以令y=kx判断极限存在与否，若极限随着k变化，则极限不存在。
```

## 初等函数

1.**指数函数**

$
ω=f(z)=e^z=e^{x+iy}=e^x(cosy+isiny)$
其中幅角Arg(expz)=y+2kπ  &#8195;  (k=0，±1，±2，……)

所以$e^z$是周期为2kπi的周期函数

2.*三角函数和双曲函数

3.**对数函数**

> 对数函数是多值函数、非周期函数

$ω=Ln|z|=ln|z|+iArgz$

​	其中当k=0时，称为主值，即$ω=ln|z|$

连续性：

​	模ln|z|:除原点外在其他点都连续。

​	幅角argz：在原点与负实轴上不连续。

4.幂函数

​	$ω=z^a=e^{alnz}$

# 解析函数

1.概念：

​	1)如果函数f(z)在$z_0$及$z_0$的邻域内处处可导，则称函数f(z)在$z_0$解析。

​	2)函数f(z)在区域D内每一点解析，则称函数f(z)在D内解析，或者说函数f(z)是D内一个解析函数。

​	3)如果f(z)在某一点$z_0$不解析，则称$z_0$为函数f(z)的奇点。

2.**$\color{#FF0000}{函数解析的充分必要条件}$**

​	<font size=4>$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}$ , $\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$</font>

3.**解析函数的导数公式**

​		<font size=4>$f'(z)=\frac{\partial u}{\partial x}+i\frac{\partial v}{\partial x}=\frac{\partial v}{\partial y}-i\frac{\partial u}{\partial y}=\frac{\partial u}{\partial x}-i\frac{\partial u}{\partial y}=\frac{\partial v}{\partial y}+i\frac{\partial v}{\partial x}$</font>

## 解析函数与调和函数的关系

1.解析函数是调和函数的充分不必要条件，即解析必调和，调和未必解析。

2.判断是否是调和函数，有

$$条件\left\{
\begin{matrix}
 存在二阶连续偏导 \\
 \frac{\partial^2 \varphi}{\partial x^2}+\frac{\partial^2 \varphi}{\partial y^2}=0
 \end{matrix}
 \right.
$$.

 其中<font size=4>$\frac{\partial^2 \varphi}{\partial x^2}+\frac{\partial^2 \varphi}{\partial y^2}$=0</font>称为二维拉普拉斯方程。

3.解解析函数与调和函数的关系问题有以下三种方法

​	a)**偏积分法**

​	b)**不定积分法**

​	c)曲线积分法

# 复变函数的积分

## 复变函数积分的定义

1.定义

​	1)**积分路径问题**：对第一类曲线积分，它的定义域是平面上的一条曲线，积分路径也是平面上的一条曲线；复变函数则不同，它的定义域是复平面上的区域，积分路径是这个区域内的一条曲线。

​	2)**被积函数问题：**对第一类曲线积分的被积函数实在曲线上有定义的二元函数f(x,y)；对于复变函数讨论的是在复平面某区域上有定义的复变函数$\omega$=f(z)沿着该区域内曲线C的积分。

2.**积分存在条件及计算方法**

> 当f(z)为解析函数时，积分值与积分路径无关	

​	积分式子①

​	<font size=4>$\int_{C}f(z)dz=\int_{C}u(x,y)dx-v(x,y)dy+i\int_{C}v(x,y)dx+u(x,y)dy$</font>

​	积分式子②

​	<font size=4>$\int_{C}f(z)dz=\int_{\alpha}^{\beta}f[z(t)]z'(t)dt$</font>

3.**常用积分结论**

​	<font size=4>$\oint_{C} \frac{dz}{(z-z_0)^{n+1}}=$$ \left\{
\begin{matrix}
 2πi，	n=0 \\
 0，	n≠0
 \end{matrix}
 \right.
$.</font>

> 其中C积分为圆。	

​	意思是，当且仅当原积分式分母为一次项时，且积分域C包含奇点，则为2πi，否则都为0.

​	*性质*：<font size=4>*$|\int_{C}dz| \le \int_{C}|f(z)|dz$*</font>

## 解析函数积分的基本定理

1.柯西积分定理

