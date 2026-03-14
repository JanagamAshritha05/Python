
n = 5

for i in range(1, n+1):
    row=""
    for j in range(1, i+1):
        row+=str(j)+" " 
    
    right=""
    if i==n:
        for j in range(1, i):
            right=str(j)+" "+right 
    else:
        for j in range(1, i+1):
            right=str(j)+" "+right
    print(row + "  "*(n*2-2*i-1) + right)
    

#
n = 5
i = 1

while i <= n:

    # Left side
    row = ""
    j = 1
    while j <= i:
        row += str(j) + " "
        j += 1

    # Right side
    right = ""
    if i == n:
        j = 1
        while j <= i - 1:
            right = str(j) + " " + right
            j += 1
    else:
        j = 1
        while j <= i:
            right = str(j) + " " + right
            j += 1

    print(row + "  " * (n*2 - 2*i - 1) + right)

    i += 1

"""
1               1 
1 2           2 1 
1 2 3       3 2 1 
1 2 3 4   4 3 2 1 
1 2 3 4 5 4 3 2 1 

"""






