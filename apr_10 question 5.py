# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 22:55:15 2018

@author: Shyamala
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode
from collections import Counter

#reading the file 
df=pd.read_excel('C:\\Users\\Shyamala\\.spyder-py3\\Book1.xlsx')
print(df.describe())
unit_price=df['Unit price']
meanx=np.mean(unit_price)
print("Mean of unit price : %d " % meanx)
print("Median of unit price : %d " % np.median(unit_price))
print("Mode of unit price : " ,Counter(unit_price))

print(type(df.values[0]))
print(df.dtypes)

customers =df[['Name','Ext price']]
print(customers)