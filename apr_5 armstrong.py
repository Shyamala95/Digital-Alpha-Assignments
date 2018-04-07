# -*- coding: utf-8 -*-
""on Sat Apr  7 14:34:49 2018

@author: user
"""
l=1
U=1000
for n in range(l,U+1):
    order=len(str(n))
    s=0
    temp=n
    while temp > 0:
        d=temp%10
        s=s+d**order
        temp=temp/10
if n==s:
    print(n)
        
 
"
Created 