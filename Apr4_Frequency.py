import re
d=dict()
s="#Python is is is is an interpreted high level programming language for general-purpose programming*."
print("\n",s)
output=re.sub('[^A-Za-z0-9 \-.]+','',s)
print(output)
s4=output
s3=str.split(output)
print(s3)
s4=s3[::-1]
for i in s3:
    if i==i[::-1]:
        print("palindrome :",i)
"""for i in s3:
    list(s3[i]==s3[i+1]):
        count=count+1"""

d={}
for i in s3:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
maxi=max(d.values())

for i in d:
    if d[i]>1:
        print(i,":",d[i])