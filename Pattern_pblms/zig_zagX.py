
m=3 
n=9 

for i in range(1, m+1):
    row=""
    for j in range(1, n+1):
        if i%2!=0 and j%2!=0:
            row+="* " 
        elif i%2==0 and j%2==0:
            row+="* "
        else:
            row+="  " 
    print(row) 
    
        
# 
m=3 
n=9 

i=1 
while i<=m:
    row="" 
    j=1 
    while j<=n:
        if i%2!=0 and j%2!=0:
            row+="* " 
        elif i%2==0 and j%2==0:
            row+="* " 
        else:
            row+="  " 
        j+=1 
    print(row)
    i+=1 
    


