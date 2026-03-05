n = 5

for i in range(n, 0, -1):
    row="" 
    left_spaces="  "*(n-i)
    for j in range(1, 2*i):
        row+="* " 
    print(left_spaces + row) 

for i in range(2, n+1):
    row="" 
    left_spaces="  "*(n-i) 
    for j in range(2*i-1):
        row+="* " 
    print(left_spaces + row) 


#
n = 5

i = n
while i >= 1:
    row = ""
    left_spaces = "  " * (n-i)
    j = 1
    while j < 2*i:
        row += "* "
        j += 1
    print(left_spaces + row)
    i -= 1

i = 2
while i <= n:
    row = ""
    left_spaces = "  " * (n-i)
    j = 0
    while j < 2*i-1:
        row += "* "
        j += 1
    print(left_spaces + row)
    i += 1


