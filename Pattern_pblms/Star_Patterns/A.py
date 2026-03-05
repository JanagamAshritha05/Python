
n=6

for i in range(1, n+1):
    row="" 
    for j in range(1, i+1):
        if i<=2:
            row+="* " 
        elif i==n//2+1:
            row+="* " 
        elif j==1 or j==i:
            row+="* "
        else:
            row+="  "

    print(" "*(n-i) + row) 


# 
n=6
i=1 
while i<=n:
    row="" 
    j=1 
    while j<=i:
        if i<=2:
            row+="* " 
        elif i==n//2+1:
            row+="* "
        elif j==1 or j==i:
            row+="* " 
        else:
            row+="  " 
        j+=1 
    print(" "*(n-i) + row) 
    i+=1



