m=int(input()) 
n=int(input()) 
num=m
for i in range(1,n+1):
    new=""
    for j in range(1,2*i+1):
        new+=str(num)+" "
        num+=1 
    print(new)
    
    