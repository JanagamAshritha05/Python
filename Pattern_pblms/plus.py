
n=5
mid = n//2

for i in range(n):
    row=""
    for j in range(n):
        if i==mid or j==mid:
            row+="* " 
        else:
            row+="  " 
    print(row) 


# 
n=5
mid=n//2

i=0 
while i<n:
    row=""
    j=0 
    while j<n:
        if i==mid or j==mid:
            row+="* " 
        else:
            row+="  "
        j+=1 
    print(row) 
    i+=1 





