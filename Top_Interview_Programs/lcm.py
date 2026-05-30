m=16 
n=9 

lcm_found=False

for i in range(m, (m*n+1)):
    if not lcm_found:
        if i%m==0 and i%n==0:
            lcm=i 

print(lcm)


