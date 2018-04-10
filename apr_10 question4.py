# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 01:01:38 2018

@author: Shyamala
"""

import pandas as pd

result={}
name=[]
score=[]
no_of_attempts=[]
qualify=[]
index=[]
number = int(input("Enter student number"))
for i in range(number):
    name.append(input("Enter a name : "))
    score.append(int(input("Enter the score : ")))
    no_of_attempts.append(int(input("Enter the no of attempts made : ")))
    qualify.append(input("Enter whether qualified or not : "))
    index.append(chr(ord('a')+i))
result['name']=name
result['score']=score
result['no_of_attempts']=no_of_attempts
result['qualify']=qualify

#dataframe: 
d=pd.DataFrame(result,index=index)
print("DataFrame : \n",d)
#print the first 4 rows of the data frame
print(d[:4])

#Print Name and qualify of dataframe:
print("Name : ",d['name']," Qualify : ",d['qualify'])

#printing number of score in between 20- 35":
for i in range(number):    
    if((d['score'][i]>=20 )and( d['score'][i]<35)):
        print("Score in between  20 and 35 : ",d['score'][i])
print("Sum  : ",sum(d['no_of_attempts']))