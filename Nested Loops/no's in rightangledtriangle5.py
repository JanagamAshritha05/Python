s=int(input()) 
n=int(input()) 
k=0 
for i in range(1,n+1):
    k+=i 
num=k+s-1 
sum=num
for i in range(1,n+1):
    new=""
    for j in range(1,i+1):
        new+=str(sum)+" "
        sum-=1 
    print(new)
    
    
    
    