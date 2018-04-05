#lower=900
#upper=1000
for num in range(900,1000):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
            if(num%10)==9:
                print(num," is a palindrome")