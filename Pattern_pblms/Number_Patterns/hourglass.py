
n=5 
for i in range(1, n+1):
    row=""
    for j in range(1, n-i+2):
        row+=str(j)+" "
    print("  "*(i-1)+row)
    
for i in range(2, n+1):
    row=""
    for j in range(1, i+1):
        row+=str(j)+" "
    print("  "*(n-i)+row)
    
#
n=5
i=1 
while i<=n:
    print("  "*(i-1), end="")
    j=1
    while j<n-i+2:
        print(str(j), end=" ")
        j+=1 
    print()
    i+=1 
    
# 
n=5 
i=2 
while i<=n:
    print("  "*(n-i), end="")
    j=1 
    while j<=i:
        print(str(j), end=" ")
        j+=1 
    print()
    i+=1 
    
"""
1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

"""
