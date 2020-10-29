import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#设置坐标轴
plt.xlim((-4*np.pi, np.pi))
plt.ylim(-100, 100)
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴中心
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))

#标题
plt.title(r'x(t)=e^(-1/2*t)*cos(4*t+π)') 

#幅度衰减正弦信号
x=np.linspace(-5*np.pi,5*np.pi,5000)
y=np.exp(-1/2*x)*np.cos(4*x+np.pi)
plt.plot(x,y,c='r')
plt.show()
