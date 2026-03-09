
n=5
count=1
for i in range(1, n+1):
    row=""
    for j in range(1, i+1):
        row+=str(count)+" "
        count+=1 
    print(row)
    

# 
n=5 
count=1
i=1
while i<=n:
    row=""
    j=1 
    while j<=i:
        row+=str(count)+" "
        count+=1
        j+=1 
    print(row)
    i+=1 
    
    
