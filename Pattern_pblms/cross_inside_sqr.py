n=7
mid = n//2 

for i in range(n):
    row="" 
    for j in range(n):
        if i==0 or i==mid or i==n-1:
            row+="* " 
        elif j==0 or j==mid or j==n-1:
            row+="* " 
        else:
            row+="  "
    print(row) 


# 
n=7
mid=n//2

i=0 
while i<n:
    row="" 
    j=0 
    while j<n:
        if i==0 or i==mid or i==n-1:
            row+="* " 
        elif j==0 or j==mid or j==n-1:
            row+="* " 
        else:
            row+="  " 
        j+=1 
    print(row)
    i+=1 
    



