n = 5

for i in range(1, n+1):
    print("  "*(n-i) + "* "*n)


# 
n=5 

for i in range(1, n+1):
    row="" 
    left_spaces="  "*(n-i) 
    for j in range(n):
        row+="* " 
    print(left_spaces + row) 


#
n=5 

i=1 
while i<=n:
    row="" 
    left_spaces="  "*(n-i)  
    j=0
    while j<n:
        row+="* " 
        j+=1
    print(left_spaces + row) 
    i+=1 

