
n = 5
triangle = []

for i in range(1, n+1):
    row = []
    for j in range(1, i+1):
        if j == 1 or j == i:
            row.append(1)           # first and last → 1
        else:
            # middle → sum of above two
            row.append(triangle[i-2][j-2] + triangle[i-2][j-1])
    
    triangle.append(row)
    
    # print row
    new=""
    for x in row:
        new+=str(x)+" "
    print(" "*(n-i) + new)


#
n = 5
triangle = []

for i in range(1, n+1):
    row = []
    for j in range(1, i+1):
        if j == 1 or j == i:
            row.append(1)           # first and last → 1
        else:
            # middle → sum of above two
            row.append(triangle[i-2][j-2] + triangle[i-2][j-1])
    
    triangle.append(row)
    
    # print row
    print(" "*(n-i) + " ".join(str(x) for x in row))  
    

# 
n = 5
triangle = []

for i in range(n):
    row = []
    for j in range(i+1):
        if j == 0 or j == i:
            row.append(1)          # first and last → 1
        else:
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # middle → sum of above two
    triangle.append(row)

for i in range(n):
    spaces = " " * (n-i-1)
    print(spaces + " ".join(str(x) for x in triangle[i]))  
    

# 
n = 5
triangle = []

i = 0
while i < n:
    row = []
    j = 0
    while j <= i:
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        j += 1
    triangle.append(row)
    i += 1

# print
i = 0
while i < n:
    spaces = " " * (n-i-1)
    print(spaces + " ".join(str(x) for x in triangle[i]))
    i += 1


"""
Row 1:         1
Row 2:        1 1
Row 3:       1 2 1
Row 4:      1 3 3 1
Row 5:     1 4 6 4 1

Rules of Pascal's Triangle:

Rule 1 → First and last element of every row is always 1
Rule 2 → Every middle element = sum of two elements above it

Row 3:      1  2  1
                ↑
            1+1 = 2 

Row 4:     1  3  3  1
              ↑  ↑
           1+2  2+1
            =3   =3 

Row 5:    1  4  6  4  1
             ↑  ↑  ↑
          1+3 3+3 3+1
           =4  =6  =4 
"""






