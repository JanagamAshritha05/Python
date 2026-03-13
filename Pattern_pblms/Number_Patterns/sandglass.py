
n=5 
for i in range(1, n+1):
    row=""
    for j in range(i, n+1):
        row+=str(j)+" "
    print("  "*(i-1)+row)
    
for i in range(n-1, 0, -1):
    row=""
    for j in range(i, n+1):
        row+=str(j)+" "
    print("  "*(i-1)+row)
    
#
n=5 
for i in range(1, n+1):
    print("  "*(i-1), end="")
    for j in range(i, n+1):
        print(str(j), end=" ") 
    print()
   
for i in range(n-1, 0, -1):
    print("  "*(i-1), end="")
    for j in range(i, n+1):
        print(str(j), end=" ") 
    print()
    
    
# 
n=5 
i=1 
while i<=n:
    print("  "*(i-1), end="")
    j=i
    while j<=n:
        print(str(j), end=" ")
        j+=1 
    print()
    i+=1 
    
i=n-1
while i>0:
    print("  "*(i-1), end="")
    j=i 
    while j<=n:
        print(str(j), end=" ")
        j+=1 
    print()
    i-=1 

    
"""
1 2 3 4 5 
  2 3 4 5 
    3 4 5 
      4 5 
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5

"""
