n=int(input())
for i in range(1,n+1):
    factors=0  
    for j in range(1,i+1):
        if i%j==0:
            factors+=1  
    if factors==2:
        print(i)
        
#print primes from 1 to N
