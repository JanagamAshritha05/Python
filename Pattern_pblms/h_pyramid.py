n = 5

for i in range(1, n+1):
    if i==1:
        print(" "*(n-i) + "*") 
    elif i==n:
        print("* "*n) 
    else:
        print(" "*(n-i) + "* " + "  "*(i-2) +"*")


#
n = 5

i = 1
while i<=n:
    if i==1:
        print(" "*(n-i) +"*") 
    elif i==n:
        print("* "*n) 
    else:
        print(" "*(n-i) + "* " + "  "*(i-2) + "*") 
    i+=1 
    

#
n = 5

for i in range(1, n+1):
    row="" 
    left_spaces=" "*(n-i) 
    for j in range(1, i+1):
        if i==n:
            row+="* " 
        elif j==1 or j==i:
            row+="* " 
        else:
            row+="  "
    print(left_spaces + row) 
    

# 
n = 5

i=1 
while i<=n:
    row=""
    left_spaces=" "*(n-i) 
    j=1 
    while j<=i:
        if i==n:
            row+="* " 
        elif j==1 or j==i:
            row+="* " 
        else:
            row+="  " 
        j+=1 
    print(left_spaces + row)
    i+=1 






