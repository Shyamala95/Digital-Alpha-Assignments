s_dict  = {1 : [50,60,80,90], 2: [40,60,80,90] , 3:[34,29,61,87], 4:[44,75,97,76]}
t= []
for j in s_dict:
   print("Student Highest Mark %d : %d"%(j,max(s_dict[j])))
   t.append(sum(s_dict[j]))
   s_dict[j].sort()

print("\n Topper Student %d "%(t.index(max(t))+1))

for j in s_dict:    
    print("\nStudent Mark  %d in  order:"%(j))
    print(s_dict[j])



s_dict[5]=[50,20,60,80]
s_dict[6]=[40,50,80,50]

for key,value in s_dict.items():    
   print("\n Student Marks %d"%(key))
   for v in value:
       print(v, end=" ")
print("\n")