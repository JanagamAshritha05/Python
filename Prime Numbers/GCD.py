m=int(input())
n=int(input())
  
for i in range(1,m+1):
    if m%i==0 and n%i==0:
        gcd=i  
print(gcd)
#4      //  2   #16     //  1
#6              #9

