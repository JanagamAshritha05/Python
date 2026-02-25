
n=5

for i in range(1, n+1):
    print("  "*(n-i) + "* "*(2*i-1)) 

val=n*2 - 3
for i in range(1, n):
    print("  "*i + "* "*(val)) 
    val-=2 


#
n=5 
i=1 
while i<=n:
    print("  "*(n-i) + "* "*(2*i-1)) 
    i+=1 

val=n*2-3 
i=1 
while i<n:
    print("  "*i + "* "*(val)) 
    i+=1 
    val-=2

# 

n=5

for i in range(1, n+1):
    row="" 
    left_spaces="  "*(n-i)
    for j in range(1, 2*i):
        row+="* " 
    print(left_spaces + row) 

for i in range(n-1, 0, -1):
    row="" 
    left_spaces="  "*(n-i) 
    for j in range(1, 2*i):
        row+="* " 
    print(left_spaces + row) 
    
   
# 

i=1 
while i<=n:
    row="" 
    left_spaces="  "*(n-i) 
    j=1 
    while j<2*i:
        row+="* " 
        j+=1 
    print(left_spaces + row) 
    i+=1 

i=n-1 
while i>=1:
    row="" 
    left_spaces="  "*(n-i)
    j=1
    while j<2*i:
        row+="* " 
        j+=1 
    print(left_spaces + row) 
    i-=1


