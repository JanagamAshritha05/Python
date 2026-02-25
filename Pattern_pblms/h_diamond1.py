
n = 5

for i in range(1, n+1):
    row="" 
    left_spaces="  "*(n-i) 
    for j in range(1, 2*i):
        if i==1:
            row+="* "
        elif j==1 or j==2*i-1:
            row+="* "
        else:
            row+="  "
    print(left_spaces + row) 

for i in range(n-1, 0, -1):
    row=""
    left_spaces="  "*(n-i) 
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            row+="* " 
        else:
            row+="  " 
    print(left_spaces + row) 
    

#
n = 5

i=1 
while i<=n:
    row="" 
    left_spaces="  "*(n-i) 
    j=1
    while j<2*i:
        if j==1 or j==2*i-1:
            row+="* " 
        else:
            row+="  "
        j+=1 
    print(left_spaces + row) 
    i+=1 


i=n-1 
while i>=1:
    row="" 
    left_spaces="  "*(n-i) 
    j=1
    while j<2*i:
        if j==1 or j==2*i-1:
            row+="* " 
        else:
            row+="  " 
        j+=1 
    print(left_spaces + row) 
    i-=1


