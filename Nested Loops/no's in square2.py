n=int(input()) 

for i in range(n):
    new=""
    for j in range(n):
        new+=str(n-j)+" "
    print(new) 
    