from typing import List

fo=open("foo.txt","w")
l=[]
n=int(input("enter the number"))
for i in range(n):
    fo.write("enter the name, population cities name %s ")
    fo.write('\n')
    fo.close()
    fo=open("foo.txt","r")
    value=fo.readlines()
for i in value:
    l.append(i.rstrip("\n"))
    l.sort()
    fo.close()
for i in range (0,len(l)):
    fo.write(l[i])
    fo.write("\n")
    fo.close()