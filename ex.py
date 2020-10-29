import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

s=2
#设置坐标轴
plt.xlim((-5, 5))
plt.ylim((0, 10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴中心
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))

#图1
x1=np.linspace(-5,5,100)
y1=np.exp(s*x1)
plt.plot(x1,y1,c='r')
#plt.show()

#图2
x2=np.linspace(-5,5,100)
y2=1/np.exp(s*x2)
plt.plot(x2,y2,c='b')
#plt.show()

plt.title(r'x(t)=e^-2t   x(t)=e^2t') 




 
plt.show() 