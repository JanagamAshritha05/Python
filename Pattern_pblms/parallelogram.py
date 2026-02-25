n = 5

for i in range(1, n+1):
    print("  "*(i) + "* "*n)


#
n=5
for i in range(1, n+1):
    row="" 
    left_spaces="  "*i
    for j in range(1, n+1):
        row+="* "
    print(left_spaces + row) 


#
n=5 
i=1 
while i<=n:
    row=""
    left_spaces="  "*i 
    j=1
    while j<=n:
        row+="* " 
        j+=1 
    print(left_spaces + row)
    i+=1 
    

