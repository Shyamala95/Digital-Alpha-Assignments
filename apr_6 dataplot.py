# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 00:02:57 2018

@author: Shyamala
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.array([14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1])
y=np.array([215,325,185,332,406,522,412,614])

plt.scatter(x,y)

meanx=np.mean(x)
meany=np.mean(y)
xi=x-meanx
yi=y-meany
xyi=xi*yi
xi=xi*xi

m=sum(xyi)/sum(xi)
print('Slope : ',m)
intercept=meany-m*meanx
print("Y-Intercept : ",intercept)
print("Equation of line : \n y = {}x+{}".format(round(m,1),round(intercept,1)))
new_y=m*np.array(x)+intercept
print("new y coordinates : \n",new_y)

plt.plot(x,new_y,color='red')
plt.show()