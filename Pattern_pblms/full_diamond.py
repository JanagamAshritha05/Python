
n = 5 

for i in range(1, n+1):
    print(" "*(n-i) + "* "*i)

for i in range(1, n):
    print(" "*i + "* "*(n-i))  



#
n = 5 

i=1 
while i<=n:
    print(" "*(n-i) + "* "*i) 
    i+=1 
 
j=1
while j<n:
    print(" "*(j) + "* "*(n-j))  
    j+=1 


# 
n = 5 
for i in range(1, n+1):
    row=""
    left_spaces=" "*(n-i)
    for j in range(1, i+1):
        row+="* " 
    print(left_spaces + row) 

for i in range(1, n):
    row="" 
    left_spaces=" "*i
    for j in range(1, n-i+1):
        row+="* " 
    print(left_spaces + row) 
            


# 

n = 5 

i = 1 
while i<=n:
    row="" 
    left_spaces=" "*(n-i) 
    j=1 
    while j<=i:
        row+="* " 
        j+=1 
    print(left_spaces + row) 
    i+=1 

i = 1
while i<n:
    row=""
    left_spaces=" "*i 
    j=1 
    while j<=n-i:
        row+="* " 
        j+=1 
    print(left_spaces + row) 
    i+=1 






