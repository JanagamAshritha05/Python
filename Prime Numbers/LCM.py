m=int(input())
n=int(input())
lcm_found=False  
for i in range(m,(m*n+1)):
    if not lcm_found:
        if i%m==0 and i%n==0:
            lcm_found=True
            lcm=i
print(lcm)
#2      //  6   #16     //  144
#3              #9  