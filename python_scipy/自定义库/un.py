import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def u(n):
    bot=-20; top=20
    a = np.arange(bot, top)
    a[:] = 0; a[n+bot:] = 1
    return a

