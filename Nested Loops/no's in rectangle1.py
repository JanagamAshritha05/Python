m=int(input()) 
n=int(input())
num=m*n
for i in range(1,m+1):
    new=""
    for j in range(1,n+1):
        new+=str(num)+" "
        num-=1 
    print(new)
    