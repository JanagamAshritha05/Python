n=int(input())
for i in range(1,n+1):
    len_i=len(str(i))
    sum=0
    for j in str(i):
        sum+=int(j)**len_i  
    if sum==i:
        print(i) 
        
# Print armstrong numbers from from 1 to n
