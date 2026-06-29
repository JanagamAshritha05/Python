m=2
n=3 
lcm_found=False  
for i in range(m,(m*n+1)):
    if not lcm_found:
        if i%m==0 and i%n==0:
            lcm_found=True
            lcm=i
print(lcm)
#2      //  6   #16     //  144
#3              #9  

# 

m = 16
n = 9
for i in range(m, m*n+1):
    if i%m == 0 and i%n == 0:
        lcm = i 
print(lcm)


 

