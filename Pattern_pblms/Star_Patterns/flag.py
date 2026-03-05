
n=5

for i in range(1, n*2-1):
    row="" 
    for j in range(1, n+1):
        if i<n:
            row+="* " 
        elif j==1:
            row+="* " 
        else:
            row+="  " 
    print(row) 

# 
n=5 

i=1 
while i<n*2-1:
    row="" 
    j=1 
    while j<=n:
        if i<n:
            row+="* " 
        elif j==1:
            row+="* " 
        else:
            row+="  " 
        j+=1 
    print(row)
    i+=1 


