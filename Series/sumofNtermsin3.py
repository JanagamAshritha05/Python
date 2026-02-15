x=int(input()) 
n=int(input()) 
power=2 
sum=0 
for i in range(1,n+1):
    if i%2!=0:
        sum+=x**power 
    else:
        sum-=x**power 
    power+=2  
print(sum)

#2      ex: 2**2 - 2**4 + 2**6 - 2**8 = -3276
#6


