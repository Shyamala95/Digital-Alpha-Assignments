# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 22:14:55 2018

@author: Shyamala
"""


import pandas as pd
import matplotlib.pyplot as plt

plt.show()

dataset = pd.read_excel("ca_result.xlsx")
year = dataset.iloc[1:,0]
g1 = dataset.iloc[1:,3]
g2 = dataset.iloc[1:,6]
bg = dataset.iloc[1:,9]
plt.plot(year,g1,label="G1")
plt.plot(year,g2,label="G2")
plt.plot(year,bg,label="BG")
plt.xlabel("Year")
plt.ylabel("Pass percentage")
