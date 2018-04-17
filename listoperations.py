# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:56:14 2018

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
print("The 3rd and 6th element",l[length-2],l[length-5])
print("First 5 elements",l[:5])
print("From 7 elements",l[7:])
l[length-1]='x'
l[length-1]='y'
print("After Changing ",l[le])

