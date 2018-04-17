# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:04:51 2018

@author: user
"""

l=[]
te=int(input("Enter the no.of.terms"))
for i in range(te):
    n=int(input("Enter the numbers:"))
    l.append(n)
    print("new list:",l)
length=len(l)
print(len(l))
l.sort()
# First Largest and Second Largest
print("First Largest Number in the list",l[length-1])
print("Second largest Number in the list ",l[length-2])
#swap
l[0],l[-1] = l[-1], l[0]
print("After swapping the first and last element in the list:",l[0],l[-1])
 
    