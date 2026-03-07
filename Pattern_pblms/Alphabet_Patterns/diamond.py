n=5 
order=65 
for i in range(1, n+1):
    row=""
    for j in range(i):
        row+=chr(order+j) + " " 
    for j in range(i-2, -1, -1):
        row+=chr(order+j) + " " 
    print("  "*(n-i) + row)
    
for i in range(1, n):
    row=""
    for j in range(n-i):
        row+=chr(order+j)+" "
    for j in range(n-i-2, -1, -1):
        row+=chr(order+j) + " "
    print("  "*(i) + row)
    
    
# 
n=5 
order=65 
i=1 
while i<=n:
    row=""
    j=0 
    while j<i:
        row+=chr(order+j)+" "
        j+=1
    j=i-2 
    while j>=0:
        row+=chr(order+j) + " "
        j-=1 
    print("  "*(n-i)+row)
    i+=1 

i=1
while i<n:
    row=""
    j=0
    while j<n-i:
        row+=chr(order + j) + " "
        j+=1 
    j=n-i-2
    while j>=0:
        row+=chr(order+j)+" "
        j-=1 
    print("  "*(i)+row)
    i+=1
    



