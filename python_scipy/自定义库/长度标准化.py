import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
from numpy.core.records import array
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def standardrize(x1,L):
    #把x1转换成标准长度
    xt1=np.arange(L)
    if len(x1)<L:
        for i in range (0, len(x1)):
            xt1[i]=x1[i]
        for i in range (len(x1),L):
            xt1[i]=0
    elif len(x1)>L:
        for i in range (0, L):
            xt1[i]=x1[i]
    return xt1
