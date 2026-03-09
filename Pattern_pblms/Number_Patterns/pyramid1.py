
n=5 
for i in range(1, n+1):
    row=""
    for j in range(1, i+1):
        row+=str(i)+" "
    print(" "*(n-i)+row)

#
n=5 
i=1 
while i<=n:
    row=""
    j=1 
    while j<=i:
        row+=str(i)+" "
        j+=1 
    print(" "*(n-i)+row)
    i+=1 

