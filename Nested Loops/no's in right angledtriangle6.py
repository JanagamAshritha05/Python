n=int(input()) 
for i in range(1,n+1):
    new=""
    for j in range(1,i+1):
        new+=str(j)+" "
    for j in range(1,i):
        new+=str(j)+" "
    print(new)
    