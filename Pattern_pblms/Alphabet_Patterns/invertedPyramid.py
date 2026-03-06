n=5 
order=65 
for i in range(1, n+1):
    row=""
    for j in range(n-i+1):
        row+=chr(order+j) + " " 
    for j in range(n-i-1, -1, -1):
        row+=chr(order+j)+" " 
    print("  "*(i-1) + row)
    
# 
n=5 
order=65
i=1 
while i<=n:
    row="" 
    j=0 
    while j<n-i+1:
        row+=chr(order+j) + " " 
        j+=1 
    
    j=n-i-1
    while j>=0:
        row+=chr(order+j) + " " 
        j-=1 
    print("  "*(i-1)+row)
    i+=1 
    
    
    
    
    
    
    
