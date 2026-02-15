m=int(input()) 
sum=0 
for i in range(1,m+1):
    sum+=i 
res=sum 
for i in range(m):
    new="  "*i
    for j in range(1,m-i+1):
        new+=str(res)+" "
        res-=1 
    print(new)



