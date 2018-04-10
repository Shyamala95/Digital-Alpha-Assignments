# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading the file 
df=pd.read_csv('C:\\Users\\Shyamala\\.spyder-py3\\100 Sales Records.csv')

#printing  column names 
print(df.columns)
print("\n")
x=df['Total Profit']
y=df['Country']
plt.scatter(x,y)
plt.xlabel("Total Profit")
plt.ylabel("Country")
plt.xticks(Country,rotation=60)
plt.show()