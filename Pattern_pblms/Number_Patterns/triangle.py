
n=5 
row=""
for i in range(1, n+1):
    row+=str(i) + " " 
    print(row)
    
# 
n=5 
for i in range(1, n+1):
    row=""
    for j in range(1, i+1):
        row+=str(j) + " " 
    print(row)


# 
n=5 
i=1 
while i<=n:
    row=""
    j=1 
    while j<=i:
        row+=str(j) + " "
        j+=1 
    print(row)
    i+=1 






