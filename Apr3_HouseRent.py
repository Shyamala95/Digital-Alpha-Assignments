# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:11:06 2018

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

dataset = pd.read_csv('house_rent.csv')
X = dataset.iloc[:, 0].values

#mean,median,mode
mean = np.mean(X)
print("mean is", mean)
median = np.median(X)
print("median is", median)
modex = st.mode(X)
print("mode is", modex)


from collections import Counter
fd = Counter(X)
print(fd)
#cumulative frequency
from scipy.stats import cumfreq
cf = cumfreq(X)
print(cf)

#percentile
p1 = np.percentile(X, 25)
print("25th percentile is", p1)
p2 = np.percentile(X, 50)
print("50th percentile is", p2)
p3 = np.percentile(X, 75)
print("75th percentile is", p3)

#variance
vari = np.var(X)
print("Variance is", vari)
std_dev = np.std(X)
co_v = (std_dev/mean)*100
print("Co-eeficient of variance is", co_v)