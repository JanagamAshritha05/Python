n=int(input())
num=1  
for i in range(1,n+1):
    new_num=""
    for j in range(1,i+1):
        new_num+=str(num)+" "
        num+=1  
    print(new_num)
 