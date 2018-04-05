c1=0
c2=0
c3=0
c4=0
c5=0
s=input("Enter a string: ")
for i in s:
    if i.islower():
        c1=c1+1
    elif i.isupper():
        c2=c2+1
    elif i.isdigit():
        c3=c3+1
    elif i.isalnum():
        c4=c4+1
    else:
        c5=c5+1
c=c1+c2
print("Total letters :",c)
print("No. of lower cases:",c1)
print("No. of upper cases:",c2)
print("No. of digits:",c3)
print("No. of spl:",c5)
