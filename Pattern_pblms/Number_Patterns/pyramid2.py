
n=5
for i in range(1, n+1):
    row=""
    for j in range(1, i+1):
        row+=str(j)+" "
    right=""
    for j in range(1, i):
        right=str(j)+" " + right
    print("  "*(n-i)+row + right)
    

# 
n=5 
i=1 
while i<=n:
    row=""
    j=1 
    while j<=i:
        row+=str(j)+" "
        j+=1 
    
    right=""
    j=1 
    while j<i:
        right=str(j)+" "+right 
        j+=1 
    print("  "*(n-i)+row+right)
    i+=1    
        
        



        

