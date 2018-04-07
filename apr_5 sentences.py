string=input("enter the sentences")
c1=0
c2=0

for i in string:
      if(i.isdigit()):
            c1=c1+1
      c2=c2+1
print("The number of digits is:")
print(c1)
print("The number of letters is:")
print(c2)