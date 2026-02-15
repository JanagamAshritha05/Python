m=int(input()) 
n=int(input()) 
for i in range(n):
    new=" "*(n-i-1)
    for j in range(i+1):
        new+=str(m+j)+" "
    print(new) 
    