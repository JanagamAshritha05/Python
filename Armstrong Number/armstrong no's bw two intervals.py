a=int(input())
b=int(input())
result=""
count=0
for i in range(a,b+1):
    str_i=str(i)
    l=len(str_i)
    sum=0
    for j in str_i:
        power=int(j)**l 
        sum=sum+power
    if sum==i:
        count=count+1
        if count> 0:
            result=result+(str(i))+" "
if result=="":
    print("-1")
else:
    print(result)
    
#150        //      153
#200