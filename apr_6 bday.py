# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 22:31:06 2018

@author: Shyamala
"""

import matplotlib.pyplot as plt
from scipy import stats
V=[1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.22,1.75]
#frequency distribution
print(stats.itemfreq(V))
#histogram
plt.hist(V)
plt.xlabel("Birthdaycards Price ")
plt.ylabel("frequency")
plt.show()

