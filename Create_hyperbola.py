# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:40:13 2019

@author: 123
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,512)
x = np.arange(0,512)

f = 50;#双曲线顶部平滑程度
a = 1.5;#影响双曲线的开口 和介质波速有关系
sigma = 5;#控制双曲线深度 ricker-wavelet的标准差
x0 = 255;#顶点坐标
t0 = 255;#
alpha = 0.018;#双曲线能量衰减
A = np.zeros((len(t),len(x)))

for ii in range(0,len(t)):
    for jj in range(0,len(x)):
        A[ii,jj] = np.sqrt( (ii - t0)**2 + (jj - x0)**2 )
        
g = a * np.sqrt( f**2 + (x - x0)**2 )+ t0 - f*a
r = 2/(np.sqrt(3*sigma) * np.pi**(1/4) ) * (1 - t**2/sigma**2)*np.exp(-t**2/(2*sigma**2));#ricker-wavelet

R = np.zeros((len(t),len(x)))
for ii in range(0,len(x)):
    R[:,ii] = 2/(np.sqrt(3*sigma) * np.pi**(1/4) ) * (1 - (t - g[ii] )**2/sigma**2)*np.exp(-(t - g[ii] )**2/(2*sigma**2))

hyperbola = np.exp( -alpha * A ) * R;
plt.figure
plt.imshow(hyperbola)
plt.show()

