
n=5
order=65

for i in range(1, n+1):
    row=""
    for j in range(1, n-i+2):
        row+=chr(order + j-1) + " " 
    print(row)


# 
n=5
order=65 
i=1 
order=65
while i<=n:
    row=""
    j=0 
    while j<n-i+1:
        row+=chr(order + j) + " " 
        j+=1 
    print(row) 
    i+=1 
    
    
    
    
