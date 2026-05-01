
n=7 
for i in range(1, n+1):
    row=""
    for j in range(n//2+2):
        if i==1 or i==n//2+1 or i==n:
            if j!=n//2+1:  #skip last star
                row+="* "
            else:
                row+="  " 

        elif j==0 or j==n//2+1:
            row+="* " 
        else:
            row+="  "
    
    print(row)


#
n=7 
i=1 
while i<=n:
    row=""
    j=0 
    while j<n//2+2:
        if i==1 or i==n//2+1 or i==n:
            if j!=n//2+1:
                row+="* " 
            else:
                row+="  "
        
        elif j==0 or j==n//2+1:
            row+="* "
        
        else:
            row+="  "
        j+=1 
    
    print(row)
    i+=1 



