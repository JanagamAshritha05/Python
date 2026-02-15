n=int(input())
num=1
for i in range(1,n+1):
    new_num=""
    for j in range(1,n+1):
        new_num+=str(num)+" "
        num+=1    
    print(new_num)

#i/p: 3     //      1 2 3
#                   4 5 6
#                   7 8 9 

