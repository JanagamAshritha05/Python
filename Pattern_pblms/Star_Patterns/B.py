
n = 7

for i in range(n):
    row = ""
    for j in range(n//2 + 2):
        if i == 0 or i == n//2 or i == n-1:
            if j < n//2 + 1:
                row += "* "
        elif j == 0:
            row += "* "
        elif j == n//2 and (0 < i < n//2 or n//2 < i < n-1):
            row += "* "
        else:
            row += "  "
    print(row)

    

