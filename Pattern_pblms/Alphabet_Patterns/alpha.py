
n=5 
order=65
for i in range(1,n+1):
    row="" 
    for j in range(1, i+1):
        row+=chr(order) + " "
    print(row) 
    order+=1 


#
n = 5

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(chr(64+i), end=" ")
        j += 1
    print()
    i += 1

