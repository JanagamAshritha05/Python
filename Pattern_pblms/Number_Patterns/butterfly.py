
n=4
for i in range(1, n+1):
    row=""
    for j in range(1, i+1):
        row+=str(j)+" "
        
    right=""
    for j in range(1, i+1):
        right=str(j)+" "+right 
    print(row + "  "*(n*2-2*i) + right) 
    
for i in range(1, n+1):
    row=""
    for j in range(1, n-i+2):
        row+=str(j)+" "
    
    right=""
    for j in range(1, n-i+2):
        right=str(j)+" "+right 
    print(row + "  "*(2*i-2) + right)
    
        
# 
n=4
i=1 
while i<=n:
    row=""
    j=1 
    while j<=i:
        row+=str(j)+" " 
        j+=1
        
    right="" 
    j=1 
    while j<=i:
        right=str(j)+" "+right 
        j+=1 
    print(row+"  "*(n*2-2*i) + right) 
    i+=1 
    
i=1 
while i<=n:
    row=""
    j=1 
    while j<n-i+2:
        row+=str(j)+" " 
        j+=1 
    
    right=""
    j=1 
    while j<n-i+2:
        right=str(j)+" "+right 
        j+=1 
    print(row + "  "*(2*i-2) + right)    
    i+=1 
    


'''
1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 
1 2 3 4 4 3 2 1 
1 2 3     3 2 1 
1 2         2 1 
1             1 

'''








        
        

        
        
