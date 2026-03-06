
n = 5
order = 65
for i in range(1, n+1):
    row = ""
    
    for j in range(i):
        row += chr(order + j) + " "
    
    # Right side
    for j in range(i-2, -1, -1):
        row += chr(order + j) + " "
    
    print("  "*(n-i) + row)
    
    
#
n=5 
order=65 
for i in range(1, n+1):
    print("  "*(n-i), end="")
    for j in range(i):
        print(chr(order+j), end=" ")
    for j in range(i-2, -1, -1):
        print(chr(order+j), end=" ") 
    print()
    
#     
n=5 
i=1 
order=65
while i<=n:
    row=""
    j=0 
    while j<i:
        row+=chr(order+j) + " " 
        j+=1 
    
    j=i-2
    while j>=0:
        row+=chr(order+j) + " " 
        j-=1 
    print("  "*(n-i)+row)
    i+=1 








