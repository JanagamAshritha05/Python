a=int(input())
b=int(input())
power=-1 
sum=0
for i in range(1,b+1):
    power+=2  
    if i%2!=0:
        sum+=a**power  
    else:
        sum-=a**power   
print(sum)

# 2  
# 5     2**1 - 2**3 + 2**5 - 2**7 + 2**9 = 410


