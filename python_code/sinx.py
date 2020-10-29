import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#设置坐标轴
plt.xlim((-4*np.pi, 4*np.pi))
plt.ylim((-4, 4))
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
plt.title(r'x(t)=3*cos(x+π)') 

x1=np.linspace(-4*np.pi,4*np.pi,200)
y1=3*np.cos(x1+np.pi)
plt.plot(x1,y1,c='r')
plt.show()

