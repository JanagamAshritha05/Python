n = 5

for i in range(1, n+1):
    if i==n:
        print("  "*(n-1) + "*") 
    elif i==1:
        print("* "*n)
    else:
        print("  "*(i-1) + "* " + "  "*(n-i-1) + "*") 


# 
n = 5

i = 1
while i<=n:
    if i==1:
        print("* "*n) 
    elif i==n:
        print("  "*(n-1) + "*") 
    else:
        print("  "*(i-1) + "* " + "  "*(n-i-1) + "*")
    i+=1 
    


# 
n = 5

for i in range(1, n+1):
    row="" 
    left_spaces="  "*(i-1)
    for j in range(1, n-i+2):
        if i==1:
            row+="* " 
        elif j==1 or j==n-i+1:
            row+="* " 
        else:
            row+="  " 
    print(left_spaces + row) 


# 
n = 5

i = 1
while i<=n:
    row=""
    left_spaces="  "*(i-1) 
    j=1
    while j<=n-i+1:
        if i==1:
            row+="* " 
        elif j==1 or j==n-i+1:
            row+="* " 
        else:
            row+="  " 
        j+=1 
    print(left_spaces + row)
    i+=1 



