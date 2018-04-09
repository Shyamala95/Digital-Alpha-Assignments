# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.





"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def cofficient(x,y):
    mean_x=sum(x)/len(x)
    mean_y=sum(y)/len(y)
    n=0
    s=0
    for i in range(len(x)):
         n = n + (x[i]-mean_x)*(y[i]-mean_y)
         s = s + (x[i]-mean_x)**2
        
    b2=n/s
    b1=mean_y - b2*mean_x
    y_calc=[]
    for j in range(len(x)):
       y_calc.append(b1+b2*x[j])
    p.plot(x,y,'ro')
    p.plot(x,y_calc)
    p.show()

names = ["week","PRICE_12PK","PRICE_18PK","PRICE_30PK","CASES_12PK","CASES_18PK","CASES_30PK"]
data = pd.read_csv("Regression_exampleS.csv")
data = data.dropna(axis = 0)
week=data['Week']

plt.plot(data['PRICE 12PK'],data['CASES 12PK'],'ro')
plt.show()
plt.plot(data['PRICE 18PK'],data['CASES 18PK'],'ro')
plt.show()
plt.plot(data['PRICE 30PK'],data['CASES 30PK'],'ro')
plt.show()
"""
plt.plot(week,data['PRICE 18PK'])
plt.show()
plt.plot(week,data['PRICE 30PK'])
plt.show()
plt.plot(week,data['CASES 12PK'])
plt.show()
plt.plot(week,data['CASES 18PK'])
plt.show()
plt.plot(week,data['CASES 30PK'])
plt.show()
"""
print(data.corr())
plt.matshow (data.corr())
