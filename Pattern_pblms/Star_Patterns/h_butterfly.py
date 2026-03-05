
n=5

for i in range(1, n+1):
    row="" 
    for j in range(1, i+1):
        if j==1 or j==i:
            row+="* " 
        else:
            row+="  " 
    print(row + "  "*(n*2-2*i) + row) 

for i in range(1, n):
    row="" 
    for j in range(1, n-i+1):
        if j==1 or j==n-i:
            row+="* " 
        else:
            row+="  " 
    print(row + "  "*(2*i) + row) 


# 
n=5

i=1
while i<=n:
    row="" 
    j=1 
    while j<=i:
        if j==1 or j==i:
            row+="* " 
        else:
            row+="  "
        j+=1 
    print(row + "  "*(n*2 - 2*i) + row) 
    i+=1 


i=1 
while i<n:
    row="" 
    j=1 
    while j<=n-i:
        if j==1 or j==n-i:
            row+="* " 
        else:
            row+="  " 
        j+=1 
    print(row + "  "*(2*i) + row) 
    i+=1 
    


