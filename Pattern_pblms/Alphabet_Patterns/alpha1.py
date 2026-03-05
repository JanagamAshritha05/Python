
n=5 

for i in range(1, n+1):
    row="" 
    for j in range(n):
        row+=chr(65 + j) + " " 
    print(row) 


# 
n=5 
i=1 

while i<=n:
    row=""
    j=0 
    while j<n:
        row+=chr(65 + j) + " " 
        j+=1 
    print(row) 
    i+=1

